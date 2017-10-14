from odoo import api, models,fields
from odoo.exceptions import UserError
from odoo import exceptions
import logging 
_logger = logging.getLogger(__name__)


PARAMS = [
    ("include_not_invoiced", "credit.limit.include.not.invoiced"),
    ("force_limit_fresh_orders", "credit.limit.force_limit_fresh_orders"),
]


class CreditLimitConfig(models.TransientModel):
    _inherit = 'res.config.settings'
    _name = 'credit.limit.config'

    default_my_credit_limit = fields.Float(default_model='res.partner')
    include_not_invoiced    = fields.Boolean(string='Consider including Sale Orders not invoiced yet')
    force_limit_fresh_orders    = fields.Boolean(string='Apply the Credit limit even for customers without Unpaid Invoices')

    @api.multi
    def set_params(self):
        self.ensure_one()

        for field_name, key_name in PARAMS:
            value = getattr(self, field_name)
            self.env['ir.config_parameter'].set_param(key_name, value)


    def get_default_params(self, fields):
        res = {}
        for field_name, key_name in PARAMS:
            res[field_name] = self.env['ir.config_parameter'].get_param(key_name)
        return res

