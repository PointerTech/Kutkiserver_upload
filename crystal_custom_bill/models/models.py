# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class crystal_custom_bill(models.Model):
#     _name = 'crystal_custom_bill.crystal_custom_bill'
#     _description = 'crystal_custom_bill.crystal_custom_bill'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

