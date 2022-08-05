import requests

BASE_URL = 'https://eldenring.wiki.fextralife.com/file/Elden-Ring/map-d8dc59f2-67df-452e-a9ea-d2c00ddc3a2b/map-tiles.1/6/'
IMG_DIR = './pieces/'

name1 = 0
for num1 in range(2,62):
	name2 = 0
	for num2 in range(4,60):
		img_data = requests.get(BASE_URL + f'{num1}/{num2}' +'.jpg').content
		with open(IMG_DIR + f'{name1}-{name2}.jpg', 'wb') as img_file:
			img_file.write(img_data)
		name2 += 1
	name1 += 1