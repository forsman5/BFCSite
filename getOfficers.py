import os
import sys

#TODO: Ordering

#where the officer data is stored
DATA_DIR = "data"

#where the images are stored
IMAGE_PATH = "../resources/officer_photos/"

#THIS WILL NOT WORK IF THERE ARE ANY SPACES IN YOUR PATH TO THIS REPO!!
#Remove any spaces and try again if that is the case

# read the partial
with open(sys.argv[1]) as f:
    read_data = f.read()

#for each officer
for filename in os.listdir(DATA_DIR):
    #read each officer and fill their info in

    #name of the officer - taken from the name of the file
    nm = os.path.splitext(filename)[0]

    # open the file with the found fileanme for reading
    with open(DATA_DIR + "/" + filename) as f:
        lines = f.read().splitlines()

    #output the partial with the filled in data
    #this is captured by the html-partials-compiler, and placed directly into the html
    print(read_data.format(name = nm, position = lines[0], major = lines[1], hometown = lines[2], email = lines[3], bio = lines[4], image1 = IMAGE_PATH + lines[5], image2 = IMAGE_PATH + lines[6]))
