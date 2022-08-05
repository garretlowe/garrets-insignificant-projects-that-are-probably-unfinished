from PIL import Image
import os

PIECES_DIR = './output6/'
OUT_DIR = './output7/'

INDEX_LIMIT = 26

def merge_image_vert(file1, file2):
    image1 = Image.open(file1)
    image2 = Image.open(file2)

    (width1, height1) = image1.size
    (width2, height2) = image2.size

    result_width = max(width1, width2)  # width1 + width2
    result_height = height1 + height2  # max(height1, height2)

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(0, height1))
    return result

def merge_image_hori(file1, file2):
    image1 = Image.open(file1)
    image2 = Image.open(file2)

    (width1, height1) = image1.size
    (width2, height2) = image2.size

    result_width = width1 + width2
    result_height = max(height1, height2)

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(width1, 0))
    return result

count = 0
os.mkdir(OUT_DIR)
for index in range(0, INDEX_LIMIT, 2):
		merged = merge_image_vert(PIECES_DIR + f'{index}.jpg', PIECES_DIR + f'{index+1}.jpg')
		merged.save(OUT_DIR + f'{count}.jpg')
		count += 1

'''
count = 0
for num1 in range(0, 2, 2):
	merged = merge_image_hori(PIECES_DIR + f'{num1}.jpg', PIECES_DIR + f'{num1 + 1}.jpg')
	merged.save(OUT_DIR + f'{count}.jpg')
	count += 1
'''