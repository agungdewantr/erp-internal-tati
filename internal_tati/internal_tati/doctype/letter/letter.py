# Copyright (c) 2024, tati and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname
from datetime import datetime

def int_to_roman(num): 
    val = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ] 
    syb = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ] 
    roman_num = '' 
    for i in range(len(val)): 
        count = int(num / val[i]) 
        roman_num += syb[i] * count 
        num -= val[i] * count 
    return roman_num 
    
def get_current_month_in_roman(date): 
    month = datetime.strptime(date, '%Y-%m-%d').month 
    return int_to_roman(month)

class Letter(Document):
	def autoname(self):
		current_month_roman = get_current_month_in_roman(self.date) 
		prefix=".code_legal_type./.###./PTTATI/.to./{}/{}".format(current_month_roman, datetime.strptime(self.date, '%Y-%m-%d').year)
		self.name = make_autoname(prefix, doc=self)