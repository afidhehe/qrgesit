# Copyright (c) 2023, ALYF GmbH and contributors
# For license information, please see license.txt

# import frappe

from frappe.model.document import Document

from qr_demo.qr_code import get_qr_code

class JFDQR(Document):
	def after_save(self):
		self.qr_value = f'{self.sys_id}|{self.inv}|{self.ammount}+.00|{self.total}+00|{self.inv_tax}+00|{self.inv_tax_no}'

	def validate(self):
		data_to_encrypt = f'{self.sys_id}|{self.inv}|{self.ammount}+.00|{self.total}+00|{self.inv_tax}+00|{self.inv_tax_no}'
		#print('data yang bakal dienkripsi adalah : ',data_to_encrypt)
		secret_key = b'{self.key}'
		#print('konci rahasianya adalah : ',secret_key)
		iv = os.urandom(16).hex()

		encrypted_text = encrypt(data_to_encrypt, secret_key, iv)
		print('text yang telah dienkripsi jadinya :', encrypted_text)
		self.qr_code = get_qr_code(encrypted_text)

	