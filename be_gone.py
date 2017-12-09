
"""
    By: Jonathan Cabrera
    Project Description: Creates a new image from the 9 images without the pesky tourist.
"""
from PIL import Image
import glob

# Creates a list of all png files in a given directory
image_list = map(Image.open, glob.glob('Images/*.png'))

# Demensions of the first image in the list
width = image_list[0].size[0]
height = image_list[0].size[1]

# Middle value
mid = len(image_list)/2

# Creates blank canvas to later populate with new pixels
final_image = Image.new("RGB",(width, height), "black")

# Iterates image pixels (coordinates (x,y))
for x in range(width):
    for y in range(height):
        
        # Creates empty lists for each coordinate
        reds, blues, greens = [],[],[]
        
        # Adds RBG values to to list
        for image in image_list:
            r, g, b = image.getpixel((x,y))
            reds.append(r)
            greens.append(g)
            blues.append(b)
        
        # Sorts collection of each images r, b, g values and creates tuple using each values median
        median = (sorted(reds)[mid], sorted(greens)[mid], sorted(blues)[mid])
        
        # Allows to reassign pixels using dict
        pixels = final_image.load()
        
        # Re-assigns pixel with median
        pixels[x, y] = median

# Create picture name
filename = raw_input("What do you want to call the file? \n") + ".png"

# Saves picture
final_image.save(filename ,"PNG")
