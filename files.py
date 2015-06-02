import os, time, re ,sys
from operator import itemgetter

file_count = 1
path = sys.argv[1]
os.chdir(path)

PS_course = open('filelist.txt')
PS_courselist = ('').join(PS_course.readlines())
PS_files = re.findall('[a-z.][a-z: \d,/?]+', PS_courselist, re.I | re.M | re.X)
PS_folders = re.findall('(^(?!\s)[a-z.][a-z \d,]*)', PS_courselist, re.I | re.M | re.X)

for root, dirs, files in os.walk("."):
	for dir_idx, dir in enumerate(dirs):
		new_dir_name = str(dir_idx+1)+". "+PS_folders[dir_idx] 
		print(dir+' --> '+new_dir_name+"\n")
		#os.rename(dir, new_dir_name)
		
		directory_path = os.path.join(path,new_dir_name)
		file_list = list()
		for files in os.listdir(directory_path):
			file_path = os.path.join(directory_path,files)
			file_list.append((files,time.ctime(os.stat(file_path).st_ctime)))
		sorted_list = sorted(file_list, key=itemgetter(1))
		for idx, item in enumerate(sorted_list):
			file_name = os.path.join(directory_path, item[0])
			new_file_name = PS_files[file_count].replace(':', ' -').replace('/', '&')+".mp4"
			print(item[0]+' --> '+(str(idx+1)+". "+new_file_name))
			# os.rename(file_name, os.path.join(directory_path,
						   # str(idx+1)+". "+new_file_name))
			file_count+=1
		print("\n"+'File renaming completed: '+new_dir_name)
		print('-'*50)
		file_count += 1
	break