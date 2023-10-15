import cv2
import numpy as np
img=cv2.imread("suduko-today-151019-tease.webp",0)  #a newspaper suduko image

th=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2);
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2);

cv2.imshow("IMAGE",img)
cv2.imshow("Thresh mean",th)
cv2.imshow("Thresh 2 Gausian ",th2)
cv2.waitKey(0)
cv2.destroyAllWindows()


# constant  :: 2
# It can be used to fine-tune the thresholding process.
# A larger constant will make the threshold more permissive, allowing more pixels to pass as foreground, 
# while a smaller constant will make the threshold more restrictive, resulting in a smaller region of interest.

# Block Size:
#  The block size defines the dimensions of this local neighborhood.
#  It is typically specified as a square or rectangular region. For example, 
# if you set the block size to 3x3, each pixel's threshold is calculated based on a 3x3 pixel region centered around that pixel. Similarly, 
# if you set it to 11x11, a larger area around each pixel is considered.