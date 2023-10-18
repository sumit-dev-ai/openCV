# median filter is something that replaces each pixel value with the median of its neighboring pixels .
#  this is great when dealing with salt paper noise
# 
# Salt and pepper noise is a type of noise in digital images, 
# and it is characterized by the presence of random, isolated dark and bright pixels in an image.
#  These dark and bright pixels may resemble grains of salt and pepper, which is why it's referred to as such.
import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('salt_pepper.jpg',-1)
img =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

median_blur=cv2.medianBlur(img,5)  #kernel size should be an odd number except one
bilateralFilter=cv2.bilateralFilter(img,9,75,75)   #works for  borders and edges
titles=['image','median','bilateral filter']
images=[img,median_blur,bilateralFilter]
for i in range(3):
    plt.subplot(3,1,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([]) 
plt.show()