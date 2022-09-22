from odoo import fields, models,api,_
from datetime import date
import csv 


class AddProduct(models.TransientModel):
	_name="add.product"

	quotation_id=fields.Many2one(comodel_name="sale.order",string="Quotations",domain=[('state','=','draft')])
	product_ids=fields.One2many(comodel_name="add.products",string="Add Products",inverse_name="quotation_id")
	partner_ids=fields.Many2many(comodel_name="res.partner",string="Partner Names")

	def add_product(self):
		print("____________",self.quotation_id)
		insert_products=[]
		for records in self.product_ids:
			print("____________",records)
			insert_products.append((
			0,0,{'product_id':records.product_id.id,'product_uom_qty':records.quantity,'price_unit':records.unit_price})
			)
			print("__________________",insert_products)
		self.quotation_id.write(
			{'order_line':insert_products,
			'partner_ids':[(6,0,self.partner_ids.ids)]

			})

	

class Products(models.TransientModel):
	_name="add.products"


	quotation_id=fields.Many2one(comodel_name="add.product")
	product_id=fields.Many2one(string="Product Name",comodel_name="product.product")
	quantity=fields.Float(string="Quantity")
	unit_price=fields.Float(string="Unit Price")



