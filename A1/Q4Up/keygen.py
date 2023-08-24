from cryptography.fernet import Fernet

#generate random synmmetric key for attacker
key = Fernet.generate_key()

with open('attacker_key.key', 'wb') as w :
	w.write(key)
	w.close()

print("Attacker key generated")

