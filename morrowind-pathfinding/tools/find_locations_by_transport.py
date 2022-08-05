# Garret Lowe 2022

DATA_DIR = '..\\data\\'

in_str = input('Enter transport method (r,b,s,g,p,x): ')
while in_str != '':
	if in_str == 'r':
		index = 2
	elif in_str == 'b':
		index = 3
	elif in_str == 's':
		index = 4
	elif in_str == 'g':
		index = 5
	elif in_str == 'p':
		index = 6
	elif in_str == 'x':
		index = 7
	else:
		print('invalid entry')
		break
		
	results = []
	first = True
		
	with open(DATA_DIR + 'locations.csv', 'r') as file:
		for line in file:
			if first:
				first = False
				continue
				
			location = line.strip().split(',')
			if location[index] == "true":
				results.append(location)
	
	for result in sorted(results):
		print(result[0])
	
	print('')
	in_str = input('Enter transport method (r,b,s,g,p,x): ')