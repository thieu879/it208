{
    "name": "finance_expense",
    "version": "1.0",
    "category": "unknown",
    "summary": "Short (1 phrase/line) summary of the module's purpose",
    "depends": ["base"],
    'data': [
        'security/finance_groups.xml',
        'security/ir.model.access.csv',
        'security/finance_rules.xml',
        'views/views.xml',
    ],
    "installable": True,
    "application": True,
    "authors": ["Thieu"],
    "license": "LGPL-3",
}