# Copyright (c) 2023, ALYF GmbH and contributors
# For license information, please see license.txt

# import frappe

from frappe.model.document import Document
from qr_demo.qr_code import get_qr_code
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64
import os

def encrypt(data, key,iv):
		key = key[:16].encode('utf-8')
		iv = iv[:16].encode('utf-8')
		
		cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
		padder = padding.PKCS7(algorithms.AES.block_size).padder()

		padded_data = padder.update(data.encode('utf-8')) + padder.finalize()

		encryptor = cipher.encryptor()
		encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

		return base64.b64encode(encrypted_data).decode('utf-8')

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

	