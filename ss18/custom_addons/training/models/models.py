# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta
from datetime import datetime

class TrainingSubject(models.Model):
    _name = 'training.subject'
    _description = 'Môn học'

    name = fields.Char(string="Tên môn học", required=True)
    code = fields.Char(string="Mã môn")
    description = fields.Text(string="Mô tả đề cương")
    
    # ========== SQL CONSTRAINT A.1 ==========
    _sql_constraints = [
        ('unique_code', 'UNIQUE(code)', 'Mã môn học [Code] đã tồn tại!'),
    ]

class TrainingTeacher(models.Model):
    _name = 'training.teacher'
    _description = 'Giảng viên'

    name = fields.Char(string="Tên giảng viên", required=True)
    phone = fields.Char(string="Số điện thoại")
    bio = fields.Text(string="Kỹ năng/Kinh nghiệm")

class TrainingStudent(models.Model):
    _name = 'training.student'
    _description = 'Sinh viên'

    name = fields.Char(string="Tên sinh viên", required=True)
    email = fields.Char(string="Email")
    student_id = fields.Char(string="Mã sinh viên")
    
    # ========== SQL CONSTRAINT A.3 ==========
    _sql_constraints = [
        ('unique_student_id', 'UNIQUE(student_id)', 'Mã sinh viên này đã tồn tại!'),
    ]

class TrainingSession(models.Model):
    _name = 'training.session'
    _description = 'Buổi học'

    name = fields.Char(string="Nội dung buổi học", required=True)
    
    # ========== SQL CONSTRAINT A.2 ==========
    _sql_constraints = [
        ('positive_duration', 'CHECK(duration > 0)', 'Thời lượng buổi học phải lớn hơn 0 phút!'),
    ]
    date = fields.Date(string="Ngày học", default=fields.Date.today)
    duration = fields.Integer(string="Thời lượng (phút)")
    
    # Many2one ngược về Lớp học
    class_id = fields.Many2one('training.class', string="Lớp học", required=True)


class TrainingClass(models.Model):
    _name = 'training.class'
    _description = 'Lớp học'

    # Thông tin cơ bản
    name = fields.Char(string="Tên lớp", required=True)
    start_date = fields.Date(string="Ngày khai giảng")
    end_date = fields.Date(string="Ngày bế giảng")
    
    # Trạng thái
    state = fields.Selection([
        ('draft', 'Dự thảo'),
        ('open', 'Đang mở'),
        ('closed', 'Đã đóng')
    ], string="Trạng thái", default='draft')
    
    # Sĩ số
    max_student = fields.Integer(string="Sĩ số tối đa", default=40)
    
    # Thông tin giảng viên
    teacher_phone = fields.Char(string="SĐT Giảng viên", readonly=True, help="Tự động lấy từ Giảng viên")
    
    # Relationships
    subject_id = fields.Many2one('training.subject', string="Môn học", required=True)
    teacher_id = fields.Many2one('training.teacher', string="Giảng viên", required=True)
    student_ids = fields.Many2many('training.student', string="Danh sách sinh viên")
    session_ids = fields.One2many('training.session', 'class_id', string="Lịch học chi tiết")
    
    # Computed fields
    student_count = fields.Integer(
        string="Sĩ số hiện tại",
        compute='_compute_student_count',
        store=True
    )
    
    total_duration = fields.Float(
        string="Tổng thời lượng (giờ)",
        compute='_compute_total_duration',
        store=True
    )
    
    occupancy_rate = fields.Float(
        string="Tỷ lệ lấp đầy (%)",
        compute='_compute_occupancy_rate',
        store=True
    )
    
    color_status = fields.Integer(
        string="Color Status",
        compute='_compute_color_status',
        store=True
    )

    @api.depends('student_ids')
    def _compute_student_count(self):
        """Đếm số sinh viên hiện tại"""
        for record in self:
            record.student_count = len(record.student_ids)

    @api.depends('session_ids')
    def _compute_total_duration(self):
        """Cộng tổng thời lượng của tất cả sessions (tính ra giờ)"""
        for record in self:
            total_minutes = sum(session.duration for session in record.session_ids if session.duration)
            record.total_duration = total_minutes / 60.0 if total_minutes else 0.0

    @api.depends('student_count', 'max_student')
    def _compute_occupancy_rate(self):
        """Tính tỷ lệ lấp đầy (%)"""
        for record in self:
            if record.max_student > 0:
                record.occupancy_rate = (record.student_count / record.max_student) * 100
            else:
                record.occupancy_rate = 0

    @api.depends('occupancy_rate')
    def _compute_color_status(self):
        """Trả về màu sắc: 10 (Đỏ) nếu > 80%, 0 (Bình thường) nếu không"""
        for record in self:
            record.color_status = 10 if record.occupancy_rate > 80 else 0

    @api.onchange('subject_id')
    def _onchange_subject_id(self):
        """Tự động điền tên lớp: Lớp [Tên Môn] - [Năm hiện tại]"""
        if self.subject_id:
            current_year = datetime.now().year
            self.name = f"Lớp {self.subject_id.name} - {current_year}"

    @api.onchange('student_ids')
    def _onchange_student_ids(self):
        """Cảnh báo nếu số sinh viên vượt quá sĩ số tối đa"""
        if len(self.student_ids) > self.max_student:
            return {
                'warning': {
                    'title': 'Cảnh báo',
                    'message': 'Lớp đã quá sĩ số quy định! Vui lòng cân nhắc mở lớp mới.'
                }
            }

    @api.onchange('teacher_id')
    def _onchange_teacher_id(self):
        """Tự động lấy SĐT giảng viên"""
        if self.teacher_id:
            self.teacher_phone = self.teacher_id.phone or "" 
        else:
            self.teacher_phone = ""

    @api.onchange('start_date')
    def _onchange_start_date(self):
        """Tự động tính end_date = start_date + 30 ngày"""
        if self.start_date:
            self.end_date = self.start_date + timedelta(days=30)

    # ========== PYTHON CONSTRAINT B.1 ==========
    @api.constrains('end_date', 'start_date')
    def _check_end_date(self):
        """
        Kiểm tra: Ngày bế giảng không được trước ngày khai giảng
        
        CONSTRAINT: end_date >= start_date
        ERROR MESSAGE: "Ngày bế giảng không thể trước ngày khai giảng!"
        TYPE: Python Constraint (Application Level)
        """
        for record in self:
            if record.end_date and record.start_date:
                if record.end_date < record.start_date:
                    raise ValidationError(
                        "Ngày bế giảng không thể trước ngày khai giảng!"
                    )

    # ========== PYTHON CONSTRAINT B.2 ==========
    @api.constrains('teacher_id', 'start_date')
    def _check_teacher_schedule_conflict(self):
        """
        Chặn trùng lịch Giảng viên
        
        CONSTRAINT: Một giảng viên không thể dạy 2 lớp cùng ngày
        LOGIC: Tìm các lớp khác (state != 'closed') cùng teacher_id và cùng start_date
        ERROR MESSAGE: "Giảng viên đã dạy lớp khác vào ngày này!"
        TYPE: Python Constraint (Application Level)
        """
        for record in self:
            if record.teacher_id and record.start_date:
                # Tìm lớp khác cùng teacher_id, cùng start_date, và state != 'closed'
                conflicting_classes = self.search([
                    ('teacher_id', '=', record.teacher_id.id),
                    ('start_date', '=', record.start_date),
                    ('state', '!=', 'closed'),
                    ('id', '!=', record.id)  # Không tính lớp hiện tại
                ])
                
                if conflicting_classes:
                    raise ValidationError(
                        "Giảng viên đã dạy lớp khác vào ngày này!"
                    )

    # ========== PYTHON CONSTRAINT B.3 ==========
    @api.constrains('state', 'teacher_id')
    def _check_teacher_required_when_opening(self):
        """
        Bắt buộc có Giảng viên khi Mở lớp
        
        TRIGGER: Khi state chuyển thành 'open'
        CONSTRAINT: teacher_id không được rỗng
        ERROR MESSAGE: "Vui lòng chọn Giảng viên trước khi Mở lớp!"
        TYPE: Python Constraint (Application Level)
        """
        for record in self:
            # Kiểm tra nếu state = 'open' và teacher_id trống
            if record.state == 'open' and not record.teacher_id:
                raise ValidationError(
                    "Vui lòng chọn Giảng viên trước khi Mở lớp!"
                )
