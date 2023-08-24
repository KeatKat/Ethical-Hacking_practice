import requests
meta_ip ="10.0.2.4" #Your Metasploitable’s IP can be different
target_website = "http://"+meta_ip+"/mutillidae"


#open dirs.txt and append all the values into a list
with open('dirs.txt', 'r') as dirs_in:
	all_dir_list = []
	
	for line in dirs_in:
		all_dir_list.append(line.strip()) #remove any whitespaces


for line in all_dir_list:
	url = target_website+"/"+line
	response = requests.get(url)
	
	if str(response.status_code).startswith('2'):
		print(f"Subdirectory exists: {url}")




