# -*- coding: utf-8 -*-

from odoo import models, fields


class ITTicket(models.Model):
    _name = 'it.ticket'
    _description = 'IT Support Ticket'

    name = fields.Char(
        string='Tiêu đề sự cố',
        required=True,
        help='Tiêu đề cơ bản để mô tả sự cố'
    )

    user_name = fields.Char(
        string='Tên người báo cáo',
        required=True,
        help='Tên nhân viên báo cáo sự cố'
    )

    email = fields.Char(
        string='Email liên hệ',
        help='Email của người báo cáo'
    )

    description = fields.Text(
        string='Mô tả chi tiết',
        help='Mô tả chi tiết về sự cố'
    )

    priority = fields.Selection(
        [('low', 'Thấp'), ('medium', 'Trung bình'), ('high', 'Cao'), ('critical', 'Khẩn cấp')],
        string='Độ ưu tiên',
        default='medium',
        help='Mức độ ưu tiên của sự cố'
    )

    category = fields.Selection(
        [('hardware', 'Phần cứng'), ('software', 'Phần mềm'), ('network', 'Mạng'), ('other', 'Khác')],
        string='Phân loại sự cố',
        help='Loại sự cố'
    )

    date_created = fields.Date(
        string='Ngày báo cáo',
        default=fields.Date.today,
        help='Ngày báo cáo sự cố',
        required=True
    )

    deadline = fields.Date(
        string='Hạn xử lý',
        help='Hạn chót xử lý sự cố'
    )

    is_solved = fields.Boolean(
        string='Đã xong chưa',
        default=False,
        help='Đánh dấu sự cố đã được giải quyết'
    )

    tech_note = fields.Text(
        string='Ghi chú kỹ thuật',
        help='Ghi chú từ kỹ thuật viên về cách sửa chữa, nguyên nhân...',
        groups='it_support_ticket.group_it_technician,it_support_ticket.group_it_manager'
    )

    repair_cost = fields.Integer(
        string='Chi phí sửa chữa',
        help='Chi phí để sửa chữa',
        groups='it_support_ticket.group_it_manager'
    )