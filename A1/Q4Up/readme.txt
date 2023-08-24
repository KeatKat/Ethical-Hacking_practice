Ensure we have a file called important.txt with whatever content that you want inside.


First we run keygen.py using "python3 keygen.py" to simulate the generation of
	1. Key for encrypting key 1 (attacker's key) (attackerkey.key)

if successful, we will get a key generated message in the terminal and we can see in our folder the file that is generated

Next we are ready to run our ransomware
we run the ransom.py script in our terminal using "python3 ransom.py"
	1. it will prompt us to enter the ransom key. Enter whatever string you would like (eg."bananas")
	2. Once you press enter, we can see from the console that the original important.txt file and key.txt file has been deleted. You will also see the ransom message.
	3. The file important.txt.asc and key.txt.asc has also been generated, with the original messages encoded.
	
	
	

