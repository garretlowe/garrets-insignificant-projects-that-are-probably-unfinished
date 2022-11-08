import json

WEAPON_TYPES = [
	'Fist', 'Hammer', 'Great Hammer', 'Axe', 'Greataxe', 'Dagger', 'Thrusting Sword',
	'Straight Sword', 'Greatsword', 'Ultra Greatsword', 'Katana', 'Curved Sword',
	'Curved Greatsword', 'Spear', 'Halberd', 'Bow', 'Crossbow', 'Greatbow', 'Whip',
	'Arrow', 'Bolt'
]
WEIGHTLESS = ['Arrow', 'Bolt']
UNBREAKABLE = ['Arrow', 'Bolt']
PARAM_BONUSES = ['S', 'A', 'B', 'C', 'D', 'E', '-']

with open('ds1_weapons.json') as file:
	weapons = json.load(file)
	
	print("Started.\n") 
	for wep in weapons:
		has_problem = False
		
		if not wep['name']:
			print('A weapon has no name.')
			continue
			
		if len(wep['attack_type']) < 1:
			print(f"{wep['name']} has no attack type.")
			has_problem = True
		for attack_type in wep["attack_type"]:
			if not attack_type in ['Regular', 'Strike', 'Thrust', 'Slash', 'None']:
				print(f"{wep['name']} contains invalid attack type: {attack_type}")
				has_problem = True
		
		if not wep['weapon_type'] in WEAPON_TYPES:
			print(f"{wep['name']} contains invalid weapon type: {wep['weapon_type']}")
			has_problem = True
			
		for dam_type in wep['attack_rating']:
			if type(wep['attack_rating'][dam_type]) != int or wep['attack_rating'][dam_type] < 0:
				print(f"{wep['name']} contains invalid {dam_type} rating: {wep['attack_rating'][dam_type]}")
				has_problem = True
			
		for dam_type in wep['damage_reduction']:
			if type(wep['damage_reduction'][dam_type]) != int or wep['damage_reduction'][dam_type] < 0 or wep['damage_reduction'][dam_type] > 100:
				print(f"{wep['name']} contains invalid {dam_type} reduction: {wep['damage_reduction'][dam_type]}")
				has_problem = True
				
		for param in wep['param_bonus']:
			if not wep['param_bonus'][param] in PARAM_BONUSES:
				print(f"{wep['name']} contains invalid {param} bonus: {wep['param_bonus'][param]}")
				has_problem = True
				
		for param in wep['req_param']:
			if type(wep['req_param'][param]) != int or wep['req_param'][param] < 0 or wep['req_param'][param] > 99:
				print(f"{wep['name']} contains invalid {param} bonus: {wep['req_param'][param]}")
				has_problem = True
				
		for effect in wep['aux_effects']:
			if type(wep['aux_effects'][effect]) != int or wep['aux_effects'][effect] < 0:
				print(f"{wep['name']} contains invalid {param} aux effect: {wep['aux_effect'][effect]}")
				has_problem = True
				
		if type(wep['durability']) != int or wep['durability'] < 0 or wep['durability'] > 999 or wep['weight'] < 0 or (wep['durability'] == 0 and wep['weapon_type'] not in UNBREAKABLE):
			print(f"{wep['name']} contains invalid durability: {wep['durability']}")
			has_problem = True
			
		if type(wep['weight']) != float or wep['weight'] < 0 or (wep['weight'] == 0 and wep['weapon_type'] not in WEIGHTLESS):
			print(f"{wep['name']} contains invalid weight: {wep['weight'], wep['weapon_type']}")
			has_problem = True
			
		has_upgrade = False
		multiple = False
		for upgrade in wep['upgrade_type']:
			if wep['upgrade_type'][upgrade]:
				if has_upgrade:
					multiple = True
					continue
				has_upgrade = True
		if not has_upgrade:
			print(f"{wep['name']} has no upgrade path")
			has_problem = True
		if multiple:
			print(f"{wep['name']} has multiple upgrade paths")
			has_problem = True
			
		if has_problem:
			print("\n=========================================================\n")
			
	print("Finished.")