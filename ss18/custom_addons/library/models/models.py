# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from datetime import timedelta
from datetime import datetime

class LibraryCategory(models.Model):
    _name = 'library.category'
    _description = 'Thể loại sách'

    name = fields.Char(string="Tên thể loại", required=True)


class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Tác giả'

    name = fields.Char(string="Tên tác giả", required=True)
    bio = fields.Text(string="Tiểu sử")


class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Lịch sử mượn'

    borrower_name = fields.Char(string="Tên người mượn", required=True)
    borrow_date = fields.Date(string="Ngày mượn", default=fields.Date.today, required=True)
    return_date = fields.Date(string="Ngày trả")
    is_returned = fields.Boolean(string="Đã trả", default=False)
    
    # Computed field: Thời gian mượn (số ngày)
    duration = fields.Integer(string="Thời gian mượn (ngày)", compute='_compute_duration', store=True)
    
    # Many2one ngược về library.book
    book_id = fields.Many2one('library.book', string="Sách", required=True)

    @api.depends('borrow_date', 'return_date')
    def _compute_duration(self):
        """Tính số ngày mượn"""
        for record in self:
            if record.return_date and record.borrow_date:
                record.duration = (record.return_date - record.borrow_date).days
            else:
                record.duration = 0

    @api.onchange('borrow_date')
    def _onchange_borrow_date(self):
        """Tự động tính ngày trả (mượn 1 tuần = 7 ngày)"""
        if self.borrow_date:
            self.return_date = self.borrow_date + timedelta(days=7)

    @api.constrains('return_date', 'borrow_date')
    def _check_return_date(self):
        """Kiểm tra: Ngày trả không được nhỏ hơn ngày mượn"""
        for record in self:
            if record.return_date and record.borrow_date:
                if record.return_date < record.borrow_date:
                    raise ValidationError(
                        "Ngày trả sách không thể đứng trước ngày mượn!"
                    )

    @api.constrains('book_id')
    def _check_lost_book(self):
        """Chặn mượn sách đã mất"""
        for record in self:
            if record.book_id.state == 'lost':
                raise ValidationError(
                    "Cuốn sách này đã bị báo mất, không thể cho mượn!"
                )

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Sách'

    # Thông tin cơ bản
    name = fields.Char(string="Tên sách", required=True)
    isbn = fields.Char(string="Mã ISBN")
    year = fields.Integer(string="Năm xuất bản")
    
    # Trạng thái và tình trạng
    state = fields.Selection([
        ('draft', 'Mới nhập'),
        ('available', 'Có sẵn'),
        ('borrowed', 'Đang mượn'),
        ('lost', 'Đã mất')
    ], string="Tình trạng", default='draft')
    
    condition = fields.Selection([
        ('0', 'Kém'),
        ('1', 'Trung bình'),
        ('2', 'Tốt'),
        ('3', 'Mới')
    ], string="Tình trạng sách", default='3')
    
    # Thông tin tài chính (BẢO MẬT - Chỉ Librarian thấy)
    purchase_price = fields.Integer(
        string="Giá nhập sách",
        groups="library.group_librarian"
    )
    
    _sql_constraints = [
        ('unique_isbn', 'UNIQUE(isbn)', 'Mã ISBN này đã tồn tại trong hệ thống!'),
        ('positive_purchase_price', 'CHECK(purchase_price > 0)', 'Giá nhập sách phải là số dương!'),
    ]
    purchase_date = fields.Date(string="Ngày nhập sách", default=fields.Date.today)
    
    # Ghi chú
    notes = fields.Text(string="Ghi chú")
    
    # Relationships
    category_id = fields.Many2one('library.category', string="Thể loại", required=True)
    author_ids = fields.Many2many('library.author', string="Tác giả")
    loan_ids = fields.One2many('library.loan', 'book_id', string="Lịch sử mượn")
    
    # Computed fields
    short_description = fields.Char(
        string="Mô tả ngắn",
        compute='_compute_short_description',
        store=True
    )
    
    days_since_purchase = fields.Integer(
        string="Tuổi đời sách (ngày)",
        compute='_compute_days_since_purchase',
        store=True
    )
    
    total_loans = fields.Integer(
        string="Tổng số lần mượn",
        compute='_compute_total_loans',
        store=True
    )

    @api.depends('name', 'author_ids', 'isbn')
    def _compute_short_description(self):
        """Ghép chuỗi: [Tên Sách] - [Tác Giả] (ISBN)"""
        for record in self:
            authors = ', '.join([author.name for author in record.author_ids])
            if authors:
                record.short_description = f"{record.name} - {authors} ({record.isbn or 'N/A'})"
            else:
                record.short_description = f"{record.name} ({record.isbn or 'N/A'})"

    @api.depends('purchase_date')
    def _compute_days_since_purchase(self):
        """Tính số ngày từ ngày nhập đến hôm nay"""
        today = fields.Date.today()
        for record in self:
            if record.purchase_date:
                record.days_since_purchase = (today - record.purchase_date).days
            else:
                record.days_since_purchase = 0

    @api.depends('loan_ids')
    def _compute_total_loans(self):
        """Đếm số lần đã mượn"""
        for record in self:
            record.total_loans = len(record.loan_ids)

    @api.onchange('state')
    def _onchange_state_to_lost(self):
        """Khi state = lost, tự động set condition = '0' (Kém)"""
        if self.state == 'lost':
            self.condition = '0'

    @api.onchange('isbn')
    def _onchange_isbn(self):
        """Kiểm tra độ dài ISBN (tối đa 13 ký tự)"""
        if self.isbn and len(self.isbn) > 13:
            return {
                'warning': {
                    'title': 'Cảnh báo',
                    'message': 'Mã ISBN không chuẩn (thường tối đa 13 số)'
                }
            }

    @api.constrains('year')
    def _check_publication_year(self):
        """Kiểm tra: Năm xuất bản không được lớn hơn năm hiện tại"""
        current_year = datetime.now().year
        for record in self:
            if record.year and record.year > current_year:
                raise ValidationError(
                    f"Năm xuất bản không thể lớn hơn năm hiện tại ({current_year})!"
                )

    @api.constrains('purchase_price')
    def _check_purchase_price_positive(self):
        """Kiểm tra: Giá nhập phải dương (Python constraint)"""
        for record in self:
            if record.purchase_price and record.purchase_price <= 0:
                raise ValidationError(
                    "Giá nhập sách phải là số dương!"
                )

    @api.onchange('category_id')
    def _onchange_category_id(self):
        """Tự động điền ghi chú theo thể loại"""
        if self.category_id:
            self.notes = f"Sách thuộc thể loại {self.category_id.name} - Vui lòng xếp đúng kệ."

