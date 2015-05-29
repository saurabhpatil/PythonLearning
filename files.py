import os, time, re, locale
from operator import itemgetter
from functools import cmp_to_key

file_count = 0
path = r"C:\Users\saurabh\Desktop\Big Data - The Big Picture"
os.chdir(path)

PS_course = open('filelist.txt')
PS_courselist = ('').join(PS_course.readlines())
PS_files = re.findall('[a-z][a-z: \d]+', PS_courselist, re.I | re.M | re.X)
PS_folders = re.findall('(^(?!\s)[a-z][a-z \d]*)', PS_courselist, re.I | re.M | re.X)

print(PS_folders)
for root, dirs, files in os.walk("."):
	for dir_idx, dir in enumerate(dirs):
		print(dir_idx , dir, PS_folders[dir_idx])
		new_dir_name = str(dir_idx+1)+". "+PS_folders[dir_idx] 
		os.rename(dir, new_dir_name)
		
		directory_path = os.path.join(path,new_dir_name)
		file_list = list()
		for files in os.listdir(directory_path):
			file_path = os.path.join(directory_path,files)
			file_list.append((files,time.ctime(os.stat(file_path).st_ctime)))
		sorted_list = sorted(file_list, key=itemgetter(1))
		for idx, item in enumerate(sorted_list):
			file_name = os.path.join(directory_path, item[0])
			os.rename(file_name, os.path.join(directory_path,
						   str(idx+1)+". "+PS_files[file_count]))
			file_count+=1
		print('-'*50)
		print('File renaming completed: '+new_dir_name)
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