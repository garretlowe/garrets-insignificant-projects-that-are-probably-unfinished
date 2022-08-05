import os

FILE_DIR = './pieces/'

NUM1_MIN = 0  # 2, 0
NUM1_MAX = 60 # 62, 60

NUM2_MIN = 0  # 4, 0
NUM2_MAX = 56 # 60, 56, 28, 14, 6, 2

STEP = 1

'''
index1 = 0
for num1 in range(2, 62):
	index2 = 0
	for num2 in range(4, 60):
		os.rename(f'./pieces/{num1}-{num2}.jpg', f'./pieces/{index1}-{index2}.jpg')
		index2 += 1
	index1 += 1
'''

index = 0
for num1 in range(NUM1_MIN, NUM1_MAX):
	for num2 in range(NUM2_MIN, NUM2_MAX, STEP):
		os.rename(FILE_DIR + f'{num1}-{num2}.jpg', FILE_DIR + f'{index}.jpg')
		index += 1
