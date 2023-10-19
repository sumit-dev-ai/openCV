import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('vk_gradient.jpg',0)

lap= cv2.Laplacian(img,cv2.CV_64F,ksize=3)     #CV2.CV_64F is justdatabyte of flot type  #it supports negative numbers while dealing with laplase
lap=np.uint8(np.absolute(lap))

sobelx=cv2.Sobel(img,cv2.CV_64F,1,0)
sobelY=cv2.Sobel(img,cv2.CV_64F,0,1)

sobelx=np.uint8(np.absolute(sobelx))
sobelY=np.uint8(np.absolute(sobelY))

#we can combine sobel x and y 
sobelXY=cv2.bitwise_or(sobelx,sobelY)




titles=['image','laplacian','sobelX','sobelY','SobelXY']
images=[img,lap,sobelx,sobelY,sobelXY]
for i in range(5):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([]) 
plt.show()