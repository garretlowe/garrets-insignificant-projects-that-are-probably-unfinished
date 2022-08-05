# Garret Lowe 2022

import json

DATA_DIR = '..\\data\\'

routes = {
	'road': {
	},
	'boat': {
	},
	'silt_strider': {
	},
	'mage_guild': {
	},
	'propylon': {
	},
	'special': {
	}
}


with open(DATA_DIR + 'routes.csv', 'r') as file:
	first = True
	for line in file:
		if first:
			first = False
			continue
		route = line.strip().split(',')
		if route[0] not in routes[route[2]]:
			routes[route[2]][route[0]] = dict()
		routes[route[2]][route[0]][route[1]] = {
			'travel_time': int(route[3]),
			'gold_cost': 0
		}

with open('out.json', 'w') as file:
	json.dump(routes, file, indent=2)