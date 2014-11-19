# -*- coding: utf-8 -*-
from openerp import http

# class Ca(http.Controller):
#     @http.route('/ca/ca/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ca/ca/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ca.listing', {
#             'root': '/ca/ca',
#             'objects': http.request.env['ca.ca'].search([]),
#         })

#     @http.route('/ca/ca/objects/<model("ca.ca"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ca.object', {
#             'object': obj
#         })