# -*- coding: utf-8 -*-

from odoo import fields, models, api

class CreditPartner(models.Model):
	_inherit = 'res.partner'
	check_credit_limit = fields.Boolean('Enforce the Credit Limit for Sale orders', default=True)
	my_credit_limit = fields.Float('The Credit Limit :') 
	my_credit_agent_change = fields.Boolean('Allow Sale Managers to modify this limit ?', default=True)
	my_credit_is_over = fields.Boolean('is over credit ?', compute='_check_if_over_limit', store=True)

#	@api.onchange('my_credit_limit', 'credit')
#	def check_credit_over(self):
#		if self.my_credit_limit<self.credit:
#			self.my_credit_is_over=True
#		else:
#			self.my_credit_is_over=False


	@api.depends('credit', 'my_credit_limit')
	def _check_if_over_limit(self):
		for item in self:
			if item.my_credit_limit<item.credit:
				item.my_credit_is_over=True
			else:
				item.my_credit_is_over=False
		
	
