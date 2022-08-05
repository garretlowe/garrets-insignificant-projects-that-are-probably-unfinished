import random

'''
# Male
PREFIXES = ('B', 'Ba', 'Bl', 'Br', 'C', 'Ca', 'Ch', 'Cr', 'D', 'Dh', 'F', 'Fh', 'Fl', 'Fr', 'G', 'Gh', 'Gl', 'Gr', 'K', 'Kh', 'Kl', 'Kr', 'L', 'Lh', 'M', 'Ma', 'Mh', 'N', 'Nh', 'R', 'Rh', 'Rl', 'S', 'Sa', 'Sh', 'Shr', 'Sl', 'St', 'T', 'Th', 'Tl', 'V', 'Vl')
VOWELS = ('a', 'e', 'i', 'o', 'u')
CONSONANTS = ('b', 'c', 'd', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'z')
SUFFIXES_1 = ('am', 'an', 'ar', 'e,' 'em', 'en', 'er', 'im', 'in', 'ir', 'ke', "'kern", 'om', 'on', 'rn', 't', 'ta', 'te', 'ten', 'um', 'un', 'ur', '')
SUFFIXES_2 = ('')
'''
'''
# Female
PREFIXES = ('B', 'Ba', 'Bl', 'Br', 'C', 'Ca', 'Ch', 'Cr', 'D', 'Dh', 'F', 'Fh', 'Fl', 'Fr', 'G', 'Gh', 'Gl', 'Gr', 'K', 'Kh', 'Kl', 'Kr', 'L', 'Lh', 'M', 'Ma', 'Mh', 'N', 'Nh', 'R', 'Rh', 'Rl', 'S', 'Sa', 'Sh', 'Shr', 'Sl', 'St', 'T', 'Th', 'Tl', 'V', 'Vl')
VOWELS = ('a', 'e', 'i', 'o', 'u')
CONSONANTS = ('b', 'c', 'd', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'z')
SUFFIXES_1 = ('am', 'an', 'ar', 'e', 'em', 'en', 'er', 'im', 'in', 'ir', 'ke', "'kern", 'om', 'on', 'rn', 't', 'ta', 'te', 'ten', 'um', 'un', 'ur', '')
SUFFIXES_2 = ('-e', 'i', '-i', 'ka', 'ki', '-si', 'ti')
'''

names = []
for prefix in PREFIXES:
	for vowel in VOWELS:
		for consonant in CONSONANTS:
			for suffix_1 in SUFFIXES_1:
				for suffix_2 in SUFFIXES_2:
					names.append(f'{prefix}{consonant}{vowel}{suffix_1}{suffix_2}')

with open('output.txt', 'w') as file:
	for name in names:
		file.write(name + ',')