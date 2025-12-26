{
    "name": "IT Support Ticket",
    "version": "1.0",
    "category": "Tools",
    "summary": "Quản lý sự cố IT",
    "depends": ["base"],
    'data': [
        'security/it_groups.xml',
        'security/it_rules.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    "installable": True,
    "application": True,
    "authors": ["Thieu"],
    "license": "LGPL-3",
}