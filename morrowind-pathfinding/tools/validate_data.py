# Garret Lowe 2022

DATA_DIR = '..\\data\\'

locations = dict()
routes = []
LOCATION_TYPES = [
	'city', 'town', 'house_stronghold', 'imperial_fort',
	'major_camp', 'dunmer_stronghold', 'temple'
]
TRAVEL_METHODS = {
	'road': 'has_road',
	'boat': 'has_boat',
	'silt_strider': 'has_strider',
	'mage_guild': 'has_guild',
	'propylon': 'has_propylon',
	'special': 'special'
}

with open(DATA_DIR + 'locations.csv', 'r') as file:
	first = True
	for line in file:
		if first:
			first = False
			continue
		data = line.strip().split(',')
		locations[data[0]] = {
			'location_type': data[1],
			'has_road': data[2] == 'true',
			'has_boat': data[3] == 'true',
			'has_strider': data[4] == 'true',
			'has_guild': data[5] == 'true',
			'has_propylon': data[6] == 'true',
			'special': data[7] == 'true'
		}

for location in locations:
	if locations[location]['location_type'] not in LOCATION_TYPES:
		print(f"Invalid location type at Location: {location}")

print("Locations Validated.")

with open(DATA_DIR + 'routes.csv', 'r') as file:
	first = True
	for line in file:
		if first:
			first = False
			continue
		route = line.strip().split(',')
		route_dict = {
			'source': route[0],
			'destination': route[1],
			'travel_method': route[2],
			'travel_time': int(route[3])
		}
		routes.append(route_dict)

for route in routes:
	tm_source_error = False
	if route['destination'] not in locations:
		print(f"Invalid destination at Route: {route}")
		
	if route['source'] not in locations:
		tm_source_error = True
		print(f"Invalid source at Route: {route}")
		
	if route['travel_method'] not in TRAVEL_METHODS:
		tm_source_error = True
		print(f"Invalid travel method at Route: {route}")
		
	if not tm_source_error and not locations[route['source']][TRAVEL_METHODS[route['travel_method']]]:
		print(f"Invalid travel method at Route: {route} from Location: {locations[route['source']]}")
	
	if route['travel_time'] < 0:
		print(f"Invalid travel time at Route: {route}")
	
print("Routes Validated.")
