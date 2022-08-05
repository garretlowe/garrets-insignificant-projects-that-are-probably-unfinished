import json

ratings = dict()
with open('../types.json') as file:
	ratings = json.load(file)
types = dict()
for rating in ratings:
	types[rating] = {"super_effective": 0, "not_very_effective": 0, "not_effective": 0}
	
def build_team(chosen, teams):
	if len(chosen) == 6:
		return [chosen]
		
	for type in types.keys()-chosen:
		new_chosen = chosen + [type]
		#teams += build_team(new_chosen, teams)
	return teams
	

def rate_types():
	for rating in ratings:
		for type in ratings[rating]["super_effective"]:
			types[type]["super_effective"] += 1
		for type in ratings[rating]["not_very_effective"]:
			types[type]["not_very_effective"] += 1
		for type in ratings[rating]["not_effective"]:
			types[type]["not_effective"] += 1
			
	for type in types:
		for effect in types[type]:
			if types[type][effect] == 0:
				ratings[type][effect] = 0
			else:
				ratings[type][effect] = 1.0/types[type][effect]
	print(ratings)

rate_types()
	