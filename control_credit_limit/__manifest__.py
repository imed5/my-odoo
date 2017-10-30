# -*- coding: utf-8 -*-
{
    'name': "Control Sale Orders by Credit Limit",
    'summary': "Allows a credit limit to be set for partners to control sale orders",
    'description': """
	Approve Sale Orders Based on customers pre-set credit limit
    """, 
    'author': "ERPish.com",
    'website': "http://www.erpish.com",
    'category': 'Sales', 
    'version': '11.0.1.1',   
    'depends': ['sale','account'],
    'data': [
        'views/partner_credit_view.xml',
        'views/wizard.confirm.overcredit.xml',
        'views/wizard.confirm.overcredit.manager.xml',
        'views/mymenus.xml',
    ],
    'installable': True,
    'application': True,   
    'auto_install': False,
}
