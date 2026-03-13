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

    'price': 1.00,
    'currency': 'EUR',

    'author': 'Wyn Interactive Ltd.',
    'license': 'OPL-1',

    'application': False,
    'installable': True,

    "images": [
        "static/description/theme_screenshot.png",  # square preview
        "static/description/banner.jpg",            # wide banner
    ],

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
}
