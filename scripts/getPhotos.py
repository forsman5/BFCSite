import os
import sys
import math

PHOTO_PATH = "resources/gallery_photos/"
IMAGE_PARTIAL = "./partials/gallery_image.html"
CAPTION_PATH = "resources/gallery_photos_dictionary.txt"
ROW_SIZE = 3

with open(sys.argv[1]) as f:
    row = f.read()

with open(IMAGE_PARTIAL) as f:
    image = f.read()

with open(CAPTION_PATH) as f:
    captions = f.read().splitlines()

#create a dictionary of captions
capDict = {}

for line in captions:
    pieces = line.split(":")
    capDict[pieces[0]] = pieces[1]

images = os.listdir(PHOTO_PATH)

rows = math.ceil(len(images) / float(ROW_SIZE))

for i in range(0, rows):
    row_images = ["", "", ""]

    for k in range(0, ROW_SIZE):
        index = 3 * i + k

        if (index < len(images)):
            #this is called at top level directory, so cannot have the .., but these files exist in a lower folder, so
            #manually adding the .. here is needed
            row_images[k] = image.format(imageName = "../" + PHOTO_PATH + images[index], description = capDict[images[index]])

    print(row.format(image1 = row_images[0], image2 = row_images[1], image3 = row_images[2]))
