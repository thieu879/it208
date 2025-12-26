# -*- coding: utf-8 -*-
{
    'name': "Quản Lý Thư Viện",

    'summary': "Module quản lý sách, tác giả, thể loại và lịch sử mượn trả",

    'description': """
Module Quản Lý Thư Viện cho trường học
- Quản lý sách, tác giả, thể loại
- Lịch sử mượn trả sách
- Phân quyền: Sinh viên (chỉ xem) và Thủ thư (quản lý toàn bộ)
    """,

    'author': "IT Students",
    'website': "https://www.school.edu",

    'category': 'Library',
    'version': '1.0',

    'depends': ['base'],

    'data': [
        'security/library_groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/library_menus.xml',
        'demo/demo.xml',
    ],
    
    'demo': [],
    
    'installable': True,
    'auto_install': False,
}

