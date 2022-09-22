from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'res.company'

    record_status=fields.Char(string="Enter Status")