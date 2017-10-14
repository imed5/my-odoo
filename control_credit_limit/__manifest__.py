# -*- coding: utf-8 -*-
{
    'name': "Control the Credit Limit",
    'summary': "Allows a credit limit to be set for partners",
    'description': """
	Approve Sale Orders Based on customers pre-set credit limit
    """,
    'author': "ERPish.com",
    'website': "http://www.erpish.com",
    'category': 'Partner',
    'version': '10.0.2.0',   
    'depends': ['account','sale'],
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
