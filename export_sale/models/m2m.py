from odoo import fields, models,api,_
from datetime import date
import csv 


class MyClass(models.Model):
    _inherit="sale.order"

    partner_ids=fields.Many2many(comodel_name="res.partner",string="Partner Names")
    product_id=fields.Many2one(comodel_name="product.product",string="Product Name")
    qty=fields.Float(string="Quantity")
    quotation_id=fields.Many2one(comodel_name="sale.order",string="Quotations")
   


    @api.onchange('product_id','qty')
    def add_product(self):
        #print("____________",self.quotation_id)
        # print("_____________________",self.product_id)
        # print("________________________________",self.order_line.product_id)
        if self.product_id in self.order_line.product_id:
        #     # print("_________________",self.order_line.product_id.ids)
        #     # print("_________________",self.product_id)
        #     # print("_____order line id",self.order_line.ids)
        #     # rec=self.order_line.ids
            for records in self.order_line:
                if records.product_id==self.product_id:
                    line=records.id
                    print("__________lineid",line)
        #     a=self.env['sale.order.line'].search([('product_id.id','=',self.product_id.id)]).id
        #     print("_________________________________aaaaaaa",a)
            insert_existing_product=[(1,line,{'product_uom_qty':self.qty})]
            print("_______________insert_list",insert_existing_product)
            self.write(
            {'order_line':insert_existing_product,
            })

        else:

            insert_products=[(
            0,0,{'product_id':self.product_id.id,'product_uom_qty':self.qty})
            ]
            print("_____________insert",insert_products)
                #print("__________________",insert_products)
            self.write(
                {'order_line':insert_products,
                })


        # print("_______________________Method Called")
        # print("_________Customer Name is",self.partner_id.name)
        # for records in self.order_line:
        #     print(records.product_id.name," is ",records.product_uom_qty," Quantity and line ID is ",records.id)
    