def extract_parent_directory(path):
#parent directory can be without '/'
#child directory needs to have parent directory + '/' + "name"
	
	#if it contains '/' i just want what is to the left of '/' because i dont care about the child name
	if '/' in path:
		sub_dirs = path.split('/')
		#parent directory will be the first one
		parent = sub_dirs[0]
		return parent
	else:
		return path
		
		
	


#open dirs.txt and append all the values into a list
with open('dirs.txt', 'r') as dirs_in:
	all_dir_list = []
	
	for line in dirs_in:
		all_dir_list.append(line.strip()) #remove any whitespaces


#using the function i can have only parent directories. if there are duplicates
#it means they must be from the same directory
parent_dir = []
for line in all_dir_list:
	parent_dir.append(extract_parent_directory(line))

duplicates = []
for line in parent_dir:
	if(parent_dir.count(line) > 1):
		duplicates.append(line)

#the subdirectories with this parent are matching
unique_dir = list(set(duplicates))

#search the original dir.txt for the lines that start with the parent directory
matches=[]
for line in unique_dir:
	for item in all_dir_list:
		if (item.startswith(line) and item != line and '/' in item): #so it doesnt print out the parent names and child directories must have '/' with the parent directory name
			matches.append(item)


for parent in unique_dir:
	print(f"Directory: {parent}")
	for children in matches:
		if(children.startswith(parent)):
			print(f"\tSubdirectory: {children}")
	print('\n')
		

	

