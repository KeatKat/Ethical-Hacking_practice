Ensure we have a file called important.txt with whatever content that you want inside.


First we run keygen.py using "python3 keygen.py" to simulate the generation of
	1. Key for encrypting the victims file (ransom key) (ransomkey.key)
	2. Key for encrypting key 1 (attacker's key) (attackerkey.key)

if successful, we will get a key generated message in the terminal and we can see in our folder the 2 files
that are generated

Next we are ready to run our ransomware
we run the ransom.py script in our terminal using "python3 ransom.py"
	1. it will prompt us to enter the ransom key. open the ransomkey.key file, copy and paste the key into the terminal and press enter.
	2. Once you press enter, we can see from the console that the original important.txt file and key.txt file has been deleted. You will also see the ransom message.
	3. The file important.txt.asc and key.txt.asc has also been generated, with the original messages encoded.
	
	
	
	
	
Optional:
	you can run decrypt.py to decrypt the important.txt.asc file to see the message
	
	1. the decryption file, decrypts the key.txt.asc file to get back the ransom key
	2. with the ransom key it decrypts the important.txt.asc file
