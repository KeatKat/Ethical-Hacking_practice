from cryptography.fernet import Fernet
import base64
import os

#get the attacker key
with open('attacker_key.key', 'rb') as attacker_key_file:
	a_key = attacker_key_file.read()
	attacker_key_file.close()

#decrypt key.txt.asc with attacker key
with open('key.txt.asc', 'r') as key_file:
	enc_key = base64.b64decode(key_file.read())
	key_file.close()


attack_cipher_instance = Fernet(a_key)
dec_key = attack_cipher_instance.decrypt(enc_key)

#use dec key to decrypt the important.txt.asc file

cipher_instance = Fernet(dec_key)
with open('important.txt.asc','r') as data_file:
	enc_data = base64.b64decode(data_file.read())
	data_file.close()

#decrypt data
dec_data = cipher_instance.decrypt(enc_data)

#print in str
print(dec_data.decode('utf-8'))

	

