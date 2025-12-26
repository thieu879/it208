# -*- coding: utf-8 -*-
{
    'name': "Hệ thống Quản Lý Đào Tạo",

    'summary': "Module quản lý khóa học, lớp học, giảng viên và sinh viên",

    'description': """
Hệ thống Quản Lý Đào Tạo cho Trung tâm
- Quản lý Môn học, Giảng viên, Sinh viên
- Mở các Lớp học với lịch học chi tiết
- Phân công sinh viên vào lớp
- Báo cáo sĩ số và thời lượng khóa học
    """,

    'author': "IT Training Center",
    'website': "https://www.training.edu",

    'category': 'Training',
    'version': '1.0',

    'depends': ['base'],

    'data': [
        'security/training_groups.xml',
        'security/ir.model.access.csv',
        'security/training_record_rules.xml',
        'views/views.xml',
        'views/training_menus.xml',
        'demo/demo.xml',
    ],
    
    'demo': [],
    
    'installable': True,
    'auto_install': False,
}

