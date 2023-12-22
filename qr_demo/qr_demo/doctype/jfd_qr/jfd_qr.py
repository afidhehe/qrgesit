# Copyright (c) 2023, ALYF GmbH and contributors
# For license information, please see license.txt

# import frappe

from frappe.model.document import Document

from qr_demo.qr_code import get_qr_code
from qr_demo.encrypt import encrypt_text

class JFDQR(Document):
	def validate(self):
		konci = self.key
		secret_key = konci.encode('utf-8')
		iv = bytes([0] * 16)  # 16 bytes IV
		input_mentah = self.plain
		input_text = input_mentah.encode('utf-8')
		encrypted_text = encrypt_text(input_text, secret_key, iv)
		#generate and display QR
		self.qr_code = get_qr_code(encrypted_text)