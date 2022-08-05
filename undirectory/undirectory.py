import os, sys, re


HOME_DIR = sys.argv[1] if len(sys.argv) > 1 else './'
if HOME_DIR[-1] != '/' and HOME_DIR[-1] != '\\':
	HOME_DIR += '/'
print(f'Home Directory: {HOME_DIR}')

def handle_file(file):
	filename = os.path.basename(file)
	
	if os.path.isfile(HOME_DIR + filename):
		extension = re.search(r'.*(\..*)', filename).group(1)
		new_filename = filename.replace(extension, '')
		count = 1
		
		while os.path.isfile(HOME_DIR + new_filename + f' ({count})' + extension):
			count += 1
			
		os.rename(file, HOME_DIR + new_filename + f' ({count})' + extension)
		print(f'Moved {filename} & renamed to {new_filename + f" ({count})" + extension}')
		
	else:
		os.rename(file, HOME_DIR + filename)
		print(f'Moved {filename}')

def handle_dir(dir):
	for filename in os.listdir(dir):
		path = os.path.join(dir, filename)
		
		if os.path.isdir(path):
			handle_dir(path)
			os.rmdir(path)
			print(f'Deleted folder {path}')
			
		elif dir != HOME_DIR:
			handle_file(path)

handle_dir(HOME_DIR)
		
