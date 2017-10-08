# -*- coding: utf-8 -*-

from odoo import api, models,fields
from . import mysale
from odoo.exceptions import UserError
from odoo import exceptions
import logging
_logger = logging.getLogger(__name__) 

class SaleConfirmLimit(models.TransientModel):
	_name='sale.control.limit.wizard'
	sale_order = fields.Many2one('sale.order')
	invoice_amount = fields.Float('Invoice Amount',readonly=1)
	new_balance = fields.Float('Total Balance',readonly=1)
	my_credit_limit = fields.Float('Partner Credit Limit',readonly=1)

	@api.multi
	def agent_exceed_limit(self):
		self.sale_order.need_approval=True
		_logger.debug(' \n\n \t Adding USers\n\n\n')
		group = self.env.ref('sales_team.group_sale_manager')
		for myu in group.users:
			self.sale_order.message_subscribe([myu.partner_id.id])            		
                self.sale_order.message_post('Order Approval is requested for a customer with Credit Limit issue', subject='Order Approval is requested for a customer with Credit Limit issue',subtype='mail.mt_comment',type='comment')

	@api.multi
	def exceed_limit_approve(self):
		_logger.debug(' \n\n \t Trying to approve a Sale\n\n\n')
		context = {'can_exceed_limit': 1}
		self.sale_order.with_context(context).action_confirm()
