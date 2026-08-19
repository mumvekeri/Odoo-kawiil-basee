{
    'name': 'Kawiil Financing',
    'summary': 'Streamlines the loan application process for dealerships.',
    'category': 'Kawiil/Custom Modules',
    'version': '1.0.0',
    'author': 'ODOP Trainee',
    'maintainer': 'Your Name',
    'depends': ['product'],
    'license': 'OPL-1',
    'application': True,

    'data': [
        'security/kawiil_financing_groups.xml',
        'security/ir.model.access.csv',
        'security/kawiil_financing_security.xml',
        'views/loan_application_views.xml',
        'views/kawiil_financing_menu.xml',
    ],

    'demo': [
        'demo/loan_demo.xml',
    ],
}