import csv, random, sys, math, os
from numpy import random as npr


NAME_DIR = 'Names/'
OUTPUT_DIR = 'Output/'

PRE_THRESH = 3
MID_THRESH = 12
SUF_THRESH = 24

VOWELS = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
RACES = ('altmer', 'argonian', 'bosmer', 'breton', 'dunmer', 'imperial', 'khajiit', 'nord', 'orsimer', 'redguard')
SEXES = ('female', 'male')


def calculate_mean_sd(names):
	mean = 0
	for name in names:
		mean += len(name)
	mean /= len(names)
	diff_mean = 0.0
	for name in names:
		diff_mean += (len(name) - mean) ** 2
	diff_mean /= len(names)
	return mean, math.sqrt(diff_mean)


def get_names(filename, organize, debug):
	names = []
	name_count = 0
	
	with open(filename) as file:
		reader = csv.reader(file)
		for row in reader:
			name_count += len(row)
			for name in row:
				if name not in names:
					names.append(name)
	
	if organize:
		names.sort()
		with open(filename, 'w') as file:
			writer = csv.writer(file)
			writer.writerow(names)
			
	if debug:
		if len(names) != name_count:
			print(f'Removed {name_count-len(names)} duplicates.')
		print(f'Found {len(names)} reference names in {filename}.')
		print('')
		
	return names


def get_pieces(names, debug):
	prefixes = dict()
	suffixes = dict()
	middles = dict()
	
	max_len = 0
	for name in names:
		if len(name) > max_len:
			max_len = len(name)
	
	piece_limit = max_len // 3
	piece_limit += max_len % 3
	
	for name in names:
		for size in range(1, min(piece_limit, len(name))):
			prefix = name[:size]
			suffix = name[len(name) - size:]
			
			if prefix in prefixes:
				prefixes[prefix] += 1
			else:
				prefixes[prefix] = 1
				
			if suffix in suffixes:
				suffixes[suffix] += 1
			else:
				suffixes[suffix] = 1
				
		start = 1
		end = len(name)-1
		while start != end:
			middle = name[start:end]
			if middle in middles:
				middles[middle] += 1
			else:
				middles[middle] = 1
			start += 1
			if start != end:
				middle = name[start:end]
				if middle in middles:
					middles[middle] += 1
				else:
					middles[middle] = 1
				end -= 1
	
	for prefix in prefixes:
		prefixes[prefix] *= 3 * len(prefix)
	for middle in middles:
		middles[middle] *= 3 * len(middle)
	for suffix in suffixes:
		suffixes[suffix] *= 3 * len(suffix)
	
	pieces = {
		'prefixes': {},
		'middles': {},
		'suffixes': {}
	}
	
	for piece, count in prefixes.items():
		if count >= PRE_THRESH:
			if random.choice([True, False]) and piece[-1] in VOWELS:
				continue
			pieces['prefixes'][piece] = count

	for piece, count in middles.items():
		if count >= MID_THRESH and piece[0] in VOWELS and piece[-1] in VOWELS:
			pieces['middles'][piece] = count

	f_suffixes = dict()
	for piece, count in suffixes.items():
		if count >= SUF_THRESH:
			if random.choice([True, False]) and piece[0] in VOWELS:
				continue
			pieces['suffixes'][piece] = count
			
	nd_data = dict()  # pieces to calculate a normnal distribution
	nd_data['mean'], nd_data['sd'] = calculate_mean_sd(names)
	
	''' 
	# Used to test and visualize threshold values
	avgs = {
		'prefixes': 0,
		'middles': 0,
		'suffixes': 0
	}
	maxes = {
		'prefixes': 0,
		'middles': 0,
		'suffixes': 0
	}
	mins = {
		'prefixes': float('inf'),
		'middles': float('inf'),
		'suffixes': float('inf')
	}
	for type in pieces:
		for piece in pieces[type]:
			avgs[type] += pieces[type][piece]
			
			if maxes[type] < pieces[type][piece]:
				maxes[type] = pieces[type][piece]
				
			if mins[type] > pieces[type][piece]:
				mins[type] = pieces[type][piece]
				
		avgs[type] /= len(pieces[type])
	
	print('Avgs: ',avgs)
	print('Maxes: ',maxes)
	print('Mins: ',mins)
	'''
	
	if debug:
		print(f"Found {len(pieces['prefixes'])} of {len(prefixes)} prefixes with threshold above {PRE_THRESH}.")
		print(f"Found {len(pieces['middles'])} of {len(middles)} middles with threshold above {MID_THRESH}.")
		print(f"Found {len(pieces['suffixes'])} of {len(suffixes)} suffixes with threshold above {SUF_THRESH}.")
		print(f"Able to generate {len(pieces['prefixes']) * len(pieces['middles']) * len(pieces['suffixes'])} names.")
		print(f"Mean name length: {nd_data['mean']:.4}, Standard deviation: {nd_data['sd']:.4}")
		print('')
		
	return pieces, nd_data


def invalid(name):
	prev_char = None
	prev_prev_char = None
	for char in name:
		if char in VOWELS and prev_char in VOWELS and prev_prev_char in VOWELS:
			return False
		prev_prev_char = prev_char
		prev_char = char
	return True


def find_pieces(pieces, length):
	found_pieces = []
	for piece in pieces:
		if len(piece) == length:
			found_pieces.append(piece)
	return found_pieces
	
	
def get_valid_pieces(pieces, length):
	options = []
	options += find_pieces(pieces, length)
	mod = 1
	while length != 0 and len(options) == 0:
		options += find_pieces(pieces, length + mod)
		options += find_pieces(pieces, length - mod)
		mod += 1
	return options
	

def generate_names(n, pieces, nd_data, debug):
	names = []
	
	for _ in range(n):
		name_len = max(2, int(npr.normal(nd_data['mean'], nd_data['sd'])))
		pre_len = name_len // 3
		mid_len = name_len // 3
		suf_len = name_len // 3

		if name_len%3 == 1:
			if random.choice([True, False]):
				pre_len += 1
			else:
				suf_len += 1
				
		elif name_len%3 == 2:
			if random.choice([True, False]):
				if random.choice([True, False]):
					pre_len += 2
				else:
					suf_len += 2
			else:
				pre_len += 1
				suf_len += 1

		pre_options = get_valid_pieces(pieces['prefixes'], pre_len)
		mid_options = get_valid_pieces(pieces['middles'], mid_len)
		suf_options = get_valid_pieces(pieces['suffixes'], suf_len)
		
		first = True
		name = ''
		while first or not invalid(name):
			first = False
			pre = '' if len(pre_options) == 0 else random.choice(pre_options)
			mid = '' if len(mid_options) == 0 else random.choice(mid_options)
			suf = '' if len(suf_options) == 0 else random.choice(suf_options)
			name = f'{pre}{mid}{suf}'
			name = f'{name[0].upper()}{name[1:].lower()}'
			
	
		if debug:
			print(f'Length: {name_len}')
			print(f'Name: {name}')
			print(f'Piece lengths: {pre_len}|{mid_len}|{suf_len}')
			print('')
			
		names.append(name)
		
	return names


def concat_names(given_names, *other_names):
	full_names = []
	for n in range(len(given_names)):
		full_name = given_names[n]
		for names in other_names:
			full_name += ' ' + names[n]
		full_names.append(full_name)
	full_names.sort()
	return full_names


def validate_filepath(path):
	path = os.path.join(os.getcwd(), OUTPUT_DIR)
	if not os.path.isdir(path):
		os.mkdir(path)


def output_names(filename, names):
	validate_filepath(OUTPUT_DIR)
	with open(filename, 'w') as file:
		for name in names:
			file.write(name + '\n')


def main():
	if len(sys.argv) < 3 or len(sys.argv) > 6:
		print(f'Invalid number of params. Expected: <int:count> <str:race> (<str:sex> <bool:organize> <bool:debug>)')
		return
		
	elif not sys.argv[1].isdigit():
		print(f'Expected param <count> of type int. Recieved: {sys.argv[3]}')
		return
		
	elif sys.argv[2].lower() not in RACES:
		print(f'Invalid race: {race}')
		return
		
	organize = False
	debug = False
	sex = None
	n = int(sys.argv[1])
	race = sys.argv[2].lower()
	if len(sys.argv) > 3:
		sex = sys.argv[3].lower()
		if sex not in SEXES:
			sex = None
		if len(sys.argv) > 4:
			organize = bool(sys.argv[4])
			if len(sys.argv) > 5:
				debug = bool(sys.argv[5])
	
	if sex is not None:
		given_names = get_names(NAME_DIR + f'{race}_{sex}.csv', organize, debug)
		output_filename = OUTPUT_DIR + f'{race}_{sex}.txt'
	else:
		given_names = get_names(NAME_DIR + f'{race}_male.csv', organize, debug)
		given_names += get_names(NAME_DIR + f'{race}_female.csv', organize, debug)
		output_filename = OUTPUT_DIR + f'{race}.txt'
		
	family_names = get_names(NAME_DIR + f'{race}_family.csv', organize, debug)
	
	given_pieces, given_nd_data = get_pieces(given_names, debug)
	family_pieces, family_nd_data = get_pieces(family_names, debug)
	
	gen_given_names = generate_names(n, given_pieces, given_nd_data, debug)
	gen_family_names = generate_names(n, family_pieces, family_nd_data, debug)
	
	full_names = concat_names(gen_given_names, gen_family_names)
	
	output_names(output_filename, full_names)
	return


main()