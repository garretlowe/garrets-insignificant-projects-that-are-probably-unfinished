import json

types = dict()
with open('../types.json') as file:
	types = json.load(file)
	
triads = []
perfect_triads = []

for option1, option1_data in types.items():
	for option2, option2_data in types.items():
		if option2 in option1_data['super_effective']:
			for option3, option3_data in types.items():
				if option3 in option2_data['super_effective'] and option1 in option3_data['super_effective']:
					if f"{option2} {option3} {option1}" not in triads and f"{option3} {option2} {option1}" not in triads and f"{option3} {option1} {option2}" not in triads and f"{option1} {option3} {option2}" not in triads:
							triads.append(f"{option1} {option2} {option3}")
					if option3 in option1_data['not_very_effective'] and option1 in option2_data['not_very_effective'] and option2 in option3_data['not_very_effective']:
						if f"{option2} {option3} {option1}" not in perfect_triads and f"{option3} {option2} {option1}" not in perfect_triads and f"{option3} {option1} {option2}" not in perfect_triads and f"{option1} {option3} {option2}" not in perfect_triads:
							perfect_triads.append(f"{option1} {option2} {option3}")
print('Triads:')
for triad in triads:
	print(triad)
print('\nPerfect Triads:')
for triad in perfect_triads:
	print(triad)