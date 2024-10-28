# -*- coding: utf-8 -*-
# from odoo import http


# class Filmotecaalvaro(http.Controller):
#     @http.route('/filmotecaalvaro/filmotecaalvaro', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/filmotecaalvaro/filmotecaalvaro/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('filmotecaalvaro.listing', {
#             'root': '/filmotecaalvaro/filmotecaalvaro',
#             'objects': http.request.env['filmotecaalvaro.filmotecaalvaro'].search([]),
#         })

#     @http.route('/filmotecaalvaro/filmotecaalvaro/objects/<model("filmotecaalvaro.filmotecaalvaro"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('filmotecaalvaro.object', {
#             'object': obj
#         })
