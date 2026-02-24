from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    old_bill_number = fields.Char(string="Refrence Bill Number", copy=False)