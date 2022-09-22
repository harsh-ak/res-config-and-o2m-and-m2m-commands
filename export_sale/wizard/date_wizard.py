from odoo import fields, models,api,_
from datetime import date
import csv 


class Date(models.TransientModel):
    _name = "date.check" #This will be the table name.
    _description = "This is Sale export"
    

    start_date=fields.Date(string="Start Date",required=True)
    end_date=fields.Date(string="End Date",required=True)


    def check_date(self):
            print("wizard button clicked")
            #self.env.user.company_id
            li=self.env.user.company_id.record_status.split(",")
            res=self.env['sale.order'].search([('state','=',li)])
            header = ['Sr.no','Customer Name','Quotation Date','Sales Person','total']
            
            
            f = open('/home/odoo/Desktop/Export_Sale/export_sale/my.csv', 'w')
            writer = csv.writer(f)
            writer.writerow(header)
            srno=0
            
            for records in res:
                
                if records.date_order.date() < self.end_date and records.date_order.date() > self.start_date:
                    my_list=[]
                    srno+=1
                    my_list.append(srno)
                    my_list.append(records.partner_id.name) 
                    my_list.append(records.date_order) 
                    my_list.append(records.user_id.name)
                    my_list.append(records.amount_total)
                writer.writerow(my_list)
                          

            f.close()
            