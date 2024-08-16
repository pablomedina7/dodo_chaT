# -*- coding: utf-8 -*-
# from odoo import http


# class Chat(http.Controller):
#     @http.route('/chat/chat', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/chat/chat/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('chat.listing', {
#             'root': '/chat/chat',
#             'objects': http.request.env['chat.chat'].search([]),
#         })

#     @http.route('/chat/chat/objects/<model("chat.chat"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('chat.object', {
#             'object': obj
#         })
