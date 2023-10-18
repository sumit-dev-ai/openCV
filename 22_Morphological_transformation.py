import cv2 
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("421.jpg",0)
_,mask=cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)
# In the context of image processing, a "kernel" typically refers to a small matrix or filter
#  that is used to perform various operations on an image, 
# such as convolution. Kernels are fundamental to many image processing techniques,
#  including blurring, sharpening, edge detection, and more.

# 1.Place the kernel over a portion of the image.
# 2.Multiply each element in the kernel by the corresponding pixel value in the image.
# 3.Sum up all the products.
# 4.Replace the central pixel in the kernel's position in the output image with the sum.
# 5.Move the kernel to the next position and repeat the process until you cover the entire image.

kernal =np.ones((5,5),np.uint8)         #kernal=1/(height*width)
dilation=cv2.dilate(mask,kernal,iterations=3)
erosion=cv2.erode(mask,kernal,iterations=3)
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal,iterations=3)
closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal,iterations=3)
grad=cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal,iterations=3)
tophat=cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernal,iterations=3)

titles=['image','mask','dilate','Erosion','open','close','gradiant','tophat']
images=[img,mask,dilation,erosion,opening,closing,grad,tophat]

for i in range(8):
    plt.subplot(2,4,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([]) 
    
plt.show()