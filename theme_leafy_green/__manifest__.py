# -*- coding: utf-8 -*-
{
    'name': 'Leafy Green Backend Theme',
    'version': '19.0.1.0.1',
    'summary': 'Modern backend theme for Odoo Community Edition',
    'description': """
Leafy Green is a modern backend theme designed to enhance the user interface
of Odoo Community Edition with a clean and professional look.
""",
    'sequence': 3,
    'category': 'Themes/Backend',
    'depends': ['base', 'web'],
    'author': 'Wyn Interactive Ltd.',

    'assets': {
        'web.assets_backend': [
            'theme_leafy_green/static/src/scss/custom_variables.scss',
            'theme_leafy_green/static/src/scss/style.scss',
            'theme_leafy_green/static/src/css/odoo_icons.css',
            'theme_leafy_green/static/src/xml/navbar.xml',
            'theme_leafy_green/static/src/js/navbar.js',
        ],
        'web._assets_primary_variables': [
            'theme_leafy_green/static/src/scss/primary_variables.scss',
        ]
    },

    "images": [
        "static/description/banner.jpg",
        "static/description/theme_screenshot.jpg",
    ],

    'license': 'OPL-1',
    'application': False,
    'installable': True,
    'price': 1.99,
    'currency': 'USD',
}
