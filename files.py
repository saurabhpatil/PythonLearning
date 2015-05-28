import os, time, re
from operator import itemgetter

path = r"C:\Users\saurabh\Documents"
	
PS_course = open(os.path.join(path, 'filelist.txt'))
PS_courselist = ('').join(PS_course.readlines())
PS_files = re.findall('[a-z][a-z: ]+', PS_courselist, re.I | re.M | re.X)
PS_folders = re.findall('(^(?!\s)[a-z][a-z ]*)', PS_courselist, re.I | re.M | re.X)

for root, dirs, files in os.walk(path):
	for dir in dirs:
		
	break

# for directories in os.listdir(path):
	# directory_path = os.path.join(path,directories)
	# file_list = list()
	# for files in os.listdir(directory_path):
		# file_path = os.path.join(directory_path,files)
		# file_list.append((files,time.ctime(os.stat(file_path).st_ctime)))
	# sorted_list = sorted(file_list, key=itemgetter(1))
	# count = 1
	# for item in sorted_list:
		# file_name = os.path.join(directory_path, item[0])
		# os.rename(file_name, os.path.join(directory_path,
                       # str(count)+". "+item[0]))
		# count+=1
	# print('-'*50)
	# print('File renaming completed: '+directories)

# print(PS_files)