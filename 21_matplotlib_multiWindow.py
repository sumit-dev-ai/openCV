#the code is for showing multiwindows using matplotlib
import cv2 
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('koa4.jpg',0)  #Load image as a gray image

resized_image = cv2.resize(img, (400, 400))

_,th1=cv2.threshold(resized_image,50,255,cv2.THRESH_BINARY)     
_,th2=cv2.threshold(resized_image,200,255,cv2.THRESH_BINARY_INV)  
_,th3=cv2.threshold(resized_image,127,255,cv2.THRESH_TRUNC) 
_,th4=cv2.threshold(resized_image,127,255,cv2.THRESH_TOZERO)  


        # Normally we do this

# cv2.imshow("Original",resized_image)
# cv2.imshow("Binary ",th1)
# cv2.imshow("Binary inv",th2)
# cv2.imshow("trunc",th3)
# cv2.imshow("tozero",th4)


titles=['original','binary','binary_inv','trunc','tozero']
images=[resized_image,th1,th2,th3,th4]

for i in range(5):
    plt.subplot(2,3,i+1)       #no of rows and columns (2,3)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])


plt.show()

# cv2.waitKey(0)
# cv2.destroyAllWindows()