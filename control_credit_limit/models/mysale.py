# -*- coding: utf-8 -*-

from odoo import api, models,fields
from odoo.exceptions import UserError 
from odoo import exceptions
import logging
_logger = logging.getLogger(__name__)

class MySale(models.Model):
	_inherit = "sale.order"
	need_approval=fields.Boolean(string='Pending Manager\'s Approval',default=False)
	credit_limit =fields.Float(string='Customer Credit Limit',related='partner_id.my_credit_limit')
	customer_balance =fields.Monetary(string='Customer Total Balance',related='partner_id.credit')

	@api.one
	def check_credit_limit(self):
		partner=self.partner_id

		## check if this is a customer who doesn't need to be enforced
		if not partner.check_credit_limit:
			return 1

		## Find not invoiced sale orders
		all_so_notinv=self.env['sale.order'].search([
				('partner_id', '=', partner.id),
				('company_id', '=', self.company_id.id),
				('invoice_status', 'in', ['to invoice']),
			])
		due_notinv=0
		for so in all_so_notinv:			
			due=so.amount_total
			due_notinv+=due


		all_invoices=self.env['account.invoice'].search([
				('partner_id', '=', partner.id),
				('type', '=', 'out_invoice'),
				('company_id', '=', self.company_id.id),
				('state', 'in', ['open']),
			])
		all_open=0
		all_due=0.0	
		for inv in all_invoices:			
			due=inv.residual
			all_due+=due
			all_open+=1
			aa='\n\nInvoice %s Due %s \n\n' % (inv.display_name, due)

		

		new_balance=self.amount_total+partner.credit

		##get some parameters
		includenot=self.env['ir.config_parameter'].get_param('credit.limit.include.not.invoiced')
		fresh_orders=self.env['ir.config_parameter'].get_param('credit.limit.force_limit_fresh_orders')

		if includenot:
			new_balance=new_balance+due_notinv

		msg='Credit Limit Error !! You need to increase the limit of this customer to proceed \n New Balance %s \n Current Customer Balance %s \n  Limit %s \n Open Invoices %s \n Due Invoices %s ' % (new_balance, (partner.credit*(-1)), partner.my_credit_limit, all_open, all_due)
		_logger.debug(msg)
		
		v_fresh=True
		if all_open==0 and not fresh_orders:
			v_fresh=False

		if v_fresh and new_balance>partner.my_credit_limit:
			params = {'sale_order':self.id,'invoice_amount':self.amount_total,'new_balance': new_balance,'debt':partner.credit,'my_credit_limit': partner.my_credit_limit,'due_not_invoiced':due_notinv}
		        return params		
		else:
			return 1



	@api.multi
	def action_confirm(self):
		_logger.debug(' \n\n \t Calling Action Confirm for a child\n\n\n')		
		for order in self:
			b=order._context.get('can_exceed_limit')
			_logger.debug(' \n\n \n My Context \n\n\n')
			_logger.debug(b)
			if b==1:
				_logger.debug(' \n\n \n Exceeding is confirmed\n\n\n')
				return super(MySale, self).action_confirm()
			else:
				params=order.check_credit_limit()
				_logger.debug(params)
				if params[0]==1:
					_logger.debug(' \n\n \t No Limit issue : Order can be Confirmed\n\n\n')
					return super(MySale, self).action_confirm()
				else:		
					view_id=self.env['sale.control.limit.wizard']
					new = view_id.create(params[0])
					if self.env.user.has_group('sales_team.group_sale_manager') :
						_logger.debug('Here is a manager !')
						return {
							'type': 'ir.actions.act_window',
							'name': 'Warning : Confirm Sale Order with Credit over Limit',
							'res_model': 'sale.control.limit.wizard',
							'view_type': 'form',
							'view_mode': 'form',
							'res_id'    : new.id,
							'view_id': self.env.ref('control_credit_limit.my_credit_limit_confirm_wizard',False).id,
							'target': 'new',
						}
				
					else:
						return {
							'type': 'ir.actions.act_window',
							'name': 'Request Approval for Sale Order with Credit over Limit',
							'res_model': 'sale.control.limit.wizard',
							'view_type': 'form',
							'view_mode': 'form',
							'res_id'    : new.id,
							'view_id': self.env.ref('control_credit_limit.my_credit_limit_wizard',False).id,
							'target': 'new',
						}
		#res = super(MySale, self).action_confirm()
		#return res
