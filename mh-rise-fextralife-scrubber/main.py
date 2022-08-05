import io, re

data = {
	'weaknesses': {
		'weapon_type': {},
		'elemental': {}
	},
	'ailment_effectiveness': {
		'poison': None,
		'stun': None,
		'paralysis': None,
		'sleep': None,
		'blast': None,
		'exhaust': None,
		'fireblight': None,
		'waterblight': None,
		'thunderblight': None,
		'iceblight': None
	},
	'low_rank_materials': {},
	'high_rank_materials': {}
}

high_rank = True
with open('input.txt', encoding='utf-8') as file:
	for line in file:
		exp = re.match(r'(\w+)\s*(\d+)\s*(\d+)\s*(\d+)', line)
		if exp:
			data['weaknesses']['weapon_type'][exp.group(1)] = [exp.group(2), exp.group(3), exp.group(4)]
			
		exp = re.match(r'(\w+)\s*(\d+)\s*(\d+)\s*(\d+)\s*(\d+)\s*(\d+)', line)
		if exp:
			data['weaknesses']['elemental'][exp.group(1)] = [exp.group(2), exp.group(3), exp.group(4), exp.group(5), exp.group(6)]
			
		exp = re.match(r'Poison (⭐*) Stun (⭐*) Paralysis (⭐*) Sleep (⭐*) Blast (⭐*) Exhaust (⭐*) Fireblight (⭐*) Waterblight (⭐*) Thunderblight (⭐*) Iceblight (⭐*)', line)
		if exp:
			data['ailment_effectiveness']['poison'] = exp.group(1)
			data['ailment_effectiveness']['stun'] = exp.group(2)
			data['ailment_effectiveness']['paralysis'] = exp.group(3)
			data['ailment_effectiveness']['sleep'] = exp.group(4)
			data['ailment_effectiveness']['blast'] = exp.group(5)
			data['ailment_effectiveness']['exhaust'] = exp.group(6)
			data['ailment_effectiveness']['fireblight'] = exp.group(7)
			data['ailment_effectiveness']['waterblight'] = exp.group(8)
			data['ailment_effectiveness']['thunderblight'] = exp.group(9)
			data['ailment_effectiveness']['iceblight'] = exp.group(10)
			
		exp = re.match(r".*monster hunter rise wiki guide(.*)	(\d+%.*|-+)	(\d+%.*|-+)	(\d+%.*|-+)	(\d+%.*|-+)	(\d+%.*|-+)", line)
		if exp and high_rank:
			data['high_rank_materials'][exp.group(1)] = [exp.group(2), exp.group(3), exp.group(4), exp.group(5), exp.group(6)]
			
		exp = re.match(r'Low Rank .*', line)
		if exp:
			high_rank = False
			
		exp = re.match(r".*monster hunter rise wiki guide(.*)	(\d+%.*|-+)	(\d+%.*|-+)	(\d+%.*|-+)	(\d+%.*|-+)	(\d+%.*|-+)", line)
		if exp and not high_rank:
			data['low_rank_materials'][exp.group(1)] = [exp.group(2), exp.group(3), exp.group(4), exp.group(5), exp.group(6)]
with open('output.txt', 'w', encoding='utf-8') as file:
	file.write('''
[h1]Weaknesses[/h1]
[b]Weapon Type[/b]
[table]
  [tr]
    [th]Body Part[/th]
    [th][previewimg=26276201;sizeOriginal,floatLeft;severing.png]Severing Damage[/previewimg][/th]
    [th][previewimg=26276197;sizeOriginal,floatLeft;blunt.png]Blunt Damage[/previewimg][/th]
    [th][previewimg=26276199;sizeOriginal,floatLeft;projectile.png]Projectile Damage[/previewimg][/th]
  [/tr]''')
	for name, contents in data['weaknesses']['weapon_type'].items():
		file.write(f'''  [tr]
    [th]{name}[/th]
    [td]{contents[0]}[/td]
    [td]{contents[1]}[/td]
    [td]{contents[2]}[/td]
  [/tr]''')
  
	file.write('''[/table]

[b]Elemental[/b]
[table]
  [tr]
    [th]Body Part[/th]
    [th][previewimg=26276209;sizeOriginal,floatLeft;fire.png]Fire[/previewimg][/th]
    [th][previewimg=26276210;sizeOriginal,floatLeft;water.png]Water[/previewimg][/th]
    [th][previewimg=26276212;sizeOriginal,floatLeft;thunder.png]Thunder[/previewimg][/th]
    [th][previewimg=26276213;sizeOriginal,floatLeft;ice.png]Ice[/previewimg][/th]
    [th][previewimg=26276215;sizeOriginal,floatLeft;dragon.png]Dragon[/previewimg][/th]
  [/tr]''')

	for name, contents in data['weaknesses']['elemental'].items():
		file.write(f'''  [tr]
    [th]{name}[/th]
    [td]{contents[0]}[/td]
    [td]{contents[1]}[/td]
    [td]{contents[2]}[/td]
    [td]{contents[3]}[/td]
    [td]{contents[4]}[/td]
  [/tr]''')
  
	file.write('''[/table]

[h1]Ailment Effectiveness[/h1]
[table]
  [tr]
    [th]Ailment[/th]
    [th]Rating[/th]
  [/tr]''')
  
	for type, rating in data['ailment_effectiveness'].items():
		file.write(f'''  [tr]
    [th]{type}[/th]
    [td]{rating}[/td]
  [/tr]''')

	file.write('''[/table]

[h1]Low Rank Materials[/h1]
[table]
  [tr]
    [th]Material[/th]
    [th]Target[/th]
    [th]Capture[/th]
    [th]Part Break[/th]
    [th]Carve[/th]
    [th]Dropped[/th]
  [/tr]''')
  
	for name, mats in data['low_rank_materials'].items():
		file.write(f'''  [tr]
    [th]{name}[/th]
    [td]{mats[0]}[/td]
    [td]{mats[1]}[/td]
    [td]{mats[2]}[/td]
    [td]{mats[3]}[/td]
    [td]{mats[4]}[/td]
  [/tr]''')

	file.write('''[/table]

[h1]High Rank Materials[/h1]
[table]
  [tr]
    [th]Material[/th]
    [th]Target[/th]
    [th]Capture[/th]
    [th]Part Break[/th]
    [th]Carve[/th]
    [th]Dropped[/th]
  [/tr]''')
  
	for name, mats in data['high_rank_materials'].items():
		file.write(f'''  [tr]
    [th]{name}[/th]
    [td]{mats[0]}[/td]
    [td]{mats[1]}[/td]
    [td]{mats[2]}[/td]
    [td]{mats[3]}[/td]
    [td]{mats[4]}[/td]
  [/tr]
''')
	file.write('[/table]')