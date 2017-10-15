# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    credit_deposit_count = fields.Integer(compute='_compute_credit_deposit_count', string='# of Guarantee Deposits')
    credit_deposit_ids = fields.One2many('credit.limit.mydeposit', 'partner_id', 'Guarantee Deposits')

    def _compute_sale_order_count(self):
        deposit_data = self.env['credit.limit.mydeposit'].read_group(domain=[('partner_id', 'child_of', self.ids)],
                                                      fields=['partner_id'], groupby=['partner_id'])

        # read to keep the child/parent relation while aggregating the read_group result in the loop
        partner_child_ids = self.read(['child_ids'])
        mapped_data = dict([(m['partner_id'][0], m['partner_id_count']) for m in deposit_data])
        for partner in self:
            # let's obtain the partner id and all its child ids from the read up there
            partner_ids = filter(lambda r: r['id'] == partner.id, partner_child_ids)[0]
            partner_ids = [partner_ids.get('id')] + partner_ids.get('child_ids')
            # then we can sum for all the partner's child
            partner.credit_deposit_count = sum(mapped_data.get(child, 0) for child in partner_ids)
