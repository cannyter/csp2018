# -*- coding: utf-8 -*-
'''
JDoe_JSmith_1_4_2: Read and show an image.
'''
import matplotlib.pyplot as plt
import os.path
import numpy as np # “as” lets us use standard abbreviations
import PIL

   
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'man.jpg')
# Read the image data into an array
img = plt.imread(filename)
  
'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 2)
# Show the image data in a subplot
ax[0].imshow(img, interpolation='none')
ax[0].set_title('I sleep on them')
ax[1].set_title('Real stuff?')
ax[1].set_ylim(260, 0)
ax[1].plot(605,121,'ro')
ax[1].plot(654,118,'ro')

img2 = img
height = len(img)
width = len(img[0])
for r in range(height):
    for c in range(width):
        if sum(img[r][c])<50: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,255,255] # R + B = magenta

''' img2 = PIL.Image.fromarray(img)
box = (100,100,300,300)'''
ax[1].imshow(img2, interpolation='none')

# Show the figure on the screen
fig.show()
