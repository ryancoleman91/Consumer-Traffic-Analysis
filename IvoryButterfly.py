# -*- coding: utf-8 
"""
Ivory Butterfly
October 12th 2018
Challenge # 3
Sources: Paul, Lecture 9 Slides, and my previous challenge #2
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as mplot
import glob
from PIL import Image

image = sorted(glob.glob('star*.jpg'))

images=[]
for i in image:
    i = Image.open(i)
    images.append(np.float64(i))

avg_image = images[0]
for index in range(1, len(images)): 
    avg_image += images[index]
avg_image /= len(images)

dev_image = [0, 0, 0]
for index in range(1, len(images)):
    dev_image += ((images[index] - avg_image) ** 2)
dev_image /= len(images)
dev_image = np.sqrt(dev_image)


uinput = float(input("please input a deviation value you " + 
                     "wish to be displayed (0-255): "))


if -1 < uinput < 256:
    for row in range(0, len(dev_image)):
        for col in range(0, len(dev_image[row])):
            if (dev_image[row][col] > [uinput, uinput, uinput]).any():
                avg_image[row][col]=[255, 0, 0]
            
    avg_image=np.clip(avg_image, 0, 255)
    dev_images=np.clip(dev_image, 0, 255)
    #converts the image from a 32-bit float to an
    #unsigned 8-bit integer (the format needed to
    #display the image)
    dev_images=np.uint8(dev_image)
    avg_image=np.uint8(avg_image)
    #displays the image!
    #mplot.imshow(dev_images)
    #mplot.show()
    mplot.imshow(avg_image)
    mplot.show()
                       
else:
    print("You have entered an invalid entry for deviation.")


