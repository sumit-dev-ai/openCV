# The code is for image thresholding using OpenCV.
#  Image thresholding is a process of converting a grayscale image into a binary image, 
# where pixels are either set to one of two values (typically 0 and 255) 
# based on a specified threshold value. Here's how the code works:
import cv2 
import numpy as np
img=cv2.imread('koa4.jpg',0)  #Load image as a gray image

resized_image = cv2.resize(img, (400, 400))

 #The threshold value. Pixels with values greater than or equal 
# to 50 will be set to 255, and those below 50 will be set to 0.
_,th1=cv2.threshold(resized_image,50,255,cv2.THRESH_BINARY)     

#perofrms inverse of above threash hold
_,th2=cv2.threshold(resized_image,200,255,cv2.THRESH_BINARY_INV)  


# 127: The threshold value. In this case, pixels with values less than or equal to 127
#  will be kept as they are, and pixels with values greater than 127 will be set to 127.
#  This is the behavior of the cv2.THRESH_TRUNC thresholding method.
# 255: The maximum value to which pixels can be set.
_,th3=cv2.threshold(resized_image,127,255,cv2.THRESH_TRUNC) 

# 127: The threshold value. In this case, pixels with values less than or equal to 127 are set to 0,
#  and pixels with values greater than 127 remain unchanged. This is the behavior of the cv2.THRESH_TOZERO thresholding method.

# 255: The maximum value to which pixels can be set.

_,th4=cv2.threshold(resized_image,127,255,cv2.THRESH_TOZERO)  


cv2.imshow("frame",resized_image)
cv2.imshow("threashhold1",th1)
cv2.imshow("threashhold2",th2)
cv2.imshow("threashhold3",th3)
cv2.imshow("threashhold4",th4)

cv2.waitKey(0)
cv2.destroyAllWindows()