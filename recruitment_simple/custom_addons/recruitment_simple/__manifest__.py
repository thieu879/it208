{
    'name': 'Recruitment Simple',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Quản lý hồ sơ ứng viên',
    'description': """
        Module quản lý danh sách ứng viên xin việc
        - Quản lý thông tin cơ bản ứng viên
        - Phân quyền Recruiter, Manager, Customer
    """,
    'author': 'Tên của bạn',
    'depends': ['base'],
    'data': [
        'security/hr_groups.xml',
        'security/ir.model.access.csv',
        'security/hr_rules.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
