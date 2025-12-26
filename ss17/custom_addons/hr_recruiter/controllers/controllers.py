# -*- coding: utf-8 -*-
# from odoo import http


# class HrRecruiter(http.Controller):
#     @http.route('/hr_recruiter/hr_recruiter', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_recruiter/hr_recruiter/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_recruiter.listing', {
#             'root': '/hr_recruiter/hr_recruiter',
#             'objects': http.request.env['hr_recruiter.hr_recruiter'].search([]),
#         })

#     @http.route('/hr_recruiter/hr_recruiter/objects/<model("hr_recruiter.hr_recruiter"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_recruiter.object', {
#             'object': obj
#         })

