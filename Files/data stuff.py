import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os.path

average = [0,0,0,0,0,0,0,0,0,0,0]
year = [1978, 1982, 1986, 1990, 1992, 1994, 1996, 1999, 2004, 2008, 2012]
black = [81.46, 86.31, 90.03, 90.94, 88.97, 90.01, 90.20, 89.06, 89.56, 90.45, 91.14]
hispanic = [86.92, 88.34, 90.35, 91.25, 92.56, 90.63, 91.36, 92.57, 90.53, 92.30, 93.60]
white = [100.00, 99.99, 100.75, 101.60, 102.32, 102.07, 102.19, 102.43, 101.69, 102.29, 102.28]
asian = [100.89,99.98,101.73,100.70,102.67,101.60,100.11, 102.87,102.06, 103.92, 105.05]

for x in range (0,11):
    average[x] = (black[x]+hispanic[x]+white[x]+asian[x])/4
    
        
plt.plot(year, average, color = 'black')
plt.plot(year, black, color='g', marker = '.')
plt.plot(year, hispanic, color='orange', marker = '.')
plt.plot(year, white, color='blue', marker = '.')
plt.plot(year, asian, color ='purple', marker = '.')

plt.xlabel('Years')
plt.ylabel('NAEP based IQ scores')
plt.title('NAEP based IQ scores by race through the years')


purple_patch = mpatches.Patch(color='purple', label='Asian')

average_patch = mpatches.Patch(color='black', label='Average')

orange_patch = mpatches.Patch(color='orange', label='Hispanic')


green_patch = mpatches.Patch(color='green', label='Black')


blue_patch = mpatches.Patch(color='blue', label='White')

plt.legend(handles=[blue_patch, purple_patch,orange_patch,green_patch, average_patch])

plt.axhline(y=85, color = 'black', linestyle = 'dotted', linewidth = .5)
plt.axhline(y=90, color = 'black', linestyle = 'dotted', linewidth = .5)
plt.axhline(y=95, color = 'black', linestyle = 'dotted', linewidth = .5)

plt.axhline(y=100, color = 'black', linestyle = 'dotted', linewidth = .5)

plt.axhline(y=105, color = 'black', linestyle = 'dotted', linewidth = .5)

directory = os.path.dirname(os.path.abspath(__file__)) 
imageFile = os.path.join(directory, 'dunlea.PNG')
image = plt.imread(imageFile) 
plt.imshow(image, extent = (1976,2013,80,106)) 


plt.show()


