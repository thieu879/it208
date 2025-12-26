# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HrCandidate(models.Model):
    _name = "hr.candidate"
    _description = "Hồ sơ ứng viên"
    
    # --- CÁC TRƯỜNG CƠ BẢN ---
    name = fields.Char(string='Họ và tên', required=True)
    
    gender = fields.Selection(
        string='Giới tính',
        selection=[
            ('male', 'Nam'),
            ('female', 'Nữ'),
            ('other', 'Khác')
        ],
        required=True
    )
    
    birth_date = fields.Date(string='Ngày sinh', required=True)
    
    phone = fields.Char(string='Số điện thoại')
    
    email = fields.Char(string='Email')
    
    address = fields.Text(string='Địa chỉ')
    
    position_applied = fields.Char(string='Vị trí ứng tuyển', required=True)
    
    expected_salary = fields.Float(string='Mức lương mong muốn', required=True)
    
    cv_file = fields.Binary(string='File CV')
    
    application_date = fields.Date(
        string='Ngày nộp đơn',
        default=fields.Date.today(),
        required=True
    )
    
    # --- TRƯỜNG BẢO MẬT ---
    # Chỉ Manager mới nhìn thấy trường này
    manager_note = fields.Text(
        string='Đánh giá nội bộ',
        groups='recruitment_simple.group_hr_manager'
    )
