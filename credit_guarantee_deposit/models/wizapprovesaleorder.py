# -*- coding: utf-8 -*-

from odoo import fields, models, api


class salewizdeposit(models.TransientModel):
    _inherit = 'sale.control.limit.wizard'
    partner_id=fields.Many2one(related='sale_order.partner_id')
    deposit_reason = fields.Many2one('credit.limit.mydeposit', string='Guarantee Deposit' )

