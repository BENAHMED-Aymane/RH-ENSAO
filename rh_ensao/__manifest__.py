# -*- coding: utf-8 -*-
{
    'name': "RH ENSAO",

    'summary': "Gestion des RH de l'ENSAO",

    'description': """
Le module de gestion des ressources humaines (RH) de l'ENSAO est une solution complète et intuitive développée sous Odoo pour répondre aux besoins spécifiques de l'établissement en matière de gestion du personnel administratif et enseignant. Il permet d'automatiser et de centraliser les processus RH, garantissant une gestion efficace et conforme aux réglementations en vigueur.
    """,

    'author': "Les Aymane et Les Aya",
    'website': "https://ensao.ump.ma/",

    'application':True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/rh_security.xml',
        'security/ir.model.access.csv',
        'views/employe.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

