import frappe
from frappe.model.document import Document

class DesignEvaluation(Document):
    pass

@frappe.whitelist()
def get_design_requests():
    return frappe.get_all('Design Request', fields=['requester'])
