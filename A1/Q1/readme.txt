First run a terminal in kali
Enter nc -v -l -p 5555 to set up the listener for connections to port 5555
You should get the message "listening on [any] 5555 ..." once the listener is set up

Ensure the kali_ip in backdoor.py is the correct IP address of your kali machine.
Open another terminal and run the backdoor script by entering "python3 backdoor.py"

In terminal 1, we should see this message if there is a successful connection

	"10.0.2.4: inverse host lookup failed: Unknown host
	connect to [10.0.2.4] from (UNKNOWN) [10.0.2.4] 41032
	Connected!"
	
We can now try typing commands in terminal 1. non-interactive commands like ls will list all items in the current folder. Interactive commands like cd will allow us to change directories. copying files works too

enter '&' to end the connection
