# -*- coding: utf-8 -*-
{
    'name': "Guarantee Deposits for Credit Limit",
    'summary': "Guarantee Deposits for Credit Limit",
    'description': """
	Guarantee Items for Credit Limit
    """, 
    'author': "ERPish.com",
    'website': "http://www.erpish.com",
    'category': 'Sales',
    'version': '10.0.1.1',   
    'depends': ['control_credit_limit','account','sale'],
    'data': [
	'security/ir.model.access.csv',
        'views/mymenus.xml',
        'views/deposit.xml',
    ],
    'installable': True,
    'application': True,   
    'auto_install': False,
}
