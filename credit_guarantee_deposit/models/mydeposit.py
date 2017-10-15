# -*- coding: utf-8 -*-

from odoo import api, models,fields
from odoo.exceptions import UserError 
from odoo import exceptions
import logging
_logger = logging.getLogger(__name__)

class MyDeposit(models.Model):
	_name='credit.limit.mydeposit'
	_inherit=['mail.thread']
	_description='Deposit Class for Credit Guarantee'

	deposit_state = fields.Selection([
	('handed', 'Handed by Client'),
	('returned', 'Returned to Client'),
	('seized', 'Seized')], Required=True)
 
	deposit_type = fields.Selection([
	('cheque', 'Cheque'),
	('other', 'Other')], Required=True)

	deposit_value     =fields.Float(string='Deposit Value', Required=True)
	deposit_desc      =fields.Text(string='Description or Cheque number/Bank' , Required=True)
	partner_id	      =fields.Many2one('res.partner',string='Customer or Company', Required=True)
	display_name = fields.Char(string='Name', compute='_compute_display_name')
	name = fields.Char(string='Name', compute='_compute_name')

        @api.one
       # @api.depends('id')
        def _compute_display_name(self):
		if self.id<10:
	        	self.display_name = 'GD00'+str(self.id)
		elif self.id<100:
	        	self.display_name = 'GD0'+str(self.id)
		else:
	        	self.display_name = 'GD'+str(self.id)

        @api.one      
        def _compute_name(self):
		if self.id<10:
	        	self.name = 'GD00'+str(self.id)+' - '+self.deposit_type
		elif self.id<100:
	        	self.name = 'GD0'+str(self.id)+' - '+self.deposit_type
		else:
	        	self.name = 'GD'+str(self.id)+' - '+self.deposit_type
   
