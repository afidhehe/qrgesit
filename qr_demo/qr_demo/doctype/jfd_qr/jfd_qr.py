# Copyright (c) 2023, ALYF GmbH and contributors
# For license information, please see license.txt

# import frappe

from frappe.model.document import Document

from qr_demo.qr_code import get_qr_code


class JFDQR(Document):
	def validate(self):
		self.qr_code = get_qr_code(self.plain)