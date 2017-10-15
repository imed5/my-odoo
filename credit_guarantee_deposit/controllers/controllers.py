# -*- coding: utf-8 -*-
from odoo import http

# class CreditGuaranteeDeposit(http.Controller):
#     @http.route('/credit_guarantee_deposit/credit_guarantee_deposit/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/credit_guarantee_deposit/credit_guarantee_deposit/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('credit_guarantee_deposit.listing', {
#             'root': '/credit_guarantee_deposit/credit_guarantee_deposit',
#             'objects': http.request.env['credit_guarantee_deposit.credit_guarantee_deposit'].search([]),
#         })

#     @http.route('/credit_guarantee_deposit/credit_guarantee_deposit/objects/<model("credit_guarantee_deposit.credit_guarantee_deposit"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('credit_guarantee_deposit.object', {
#             'object': obj
#         })