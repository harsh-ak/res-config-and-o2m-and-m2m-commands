from odoo import fields, models,api,_
from datetime import date


class ExportSale(models.Model):
    _name = "export.sale" #This will be the table name.
    _description = "This is Sale export"
    