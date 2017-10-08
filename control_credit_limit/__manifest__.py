# -*- coding: utf-8 -*-
{
    'name': "Control the Credit Limit",
    'summary': "Allows a credit limit to be set for partners",
    'description': """
        This plugin can be used to limit the allowable credit for a partner can have. 
	All new credit transactions are checked against the credit limit and the accumulated owed credit to validate new sale
    """,
    'author': "ERPish.com",
    'website': "http://www.erpish.com",
    'category': 'Partner',
    'version': '10.0.10',   
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
