# -*- coding: utf-8 -*-
# from odoo import http


# class RhEnsao(http.Controller):
#     @http.route('/rh_ensao/rh_ensao', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rh_ensao/rh_ensao/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rh_ensao.listing', {
#             'root': '/rh_ensao/rh_ensao',
#             'objects': http.request.env['rh_ensao.rh_ensao'].search([]),
#         })

#     @http.route('/rh_ensao/rh_ensao/objects/<model("rh_ensao.rh_ensao"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rh_ensao.object', {
#             'object': obj
#         })

