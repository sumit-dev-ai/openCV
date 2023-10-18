# as in 1-D singnals images also can be filtered with various low pass filters (LPF),high pass filters(HPF)etc 
#LPF helps in removing noises ,blurring images   .filter@D()
# HPf filters help in finding edges in the images
#  
#gausian filter is nothing but using diff weight kernel in both x and y direction,
# Gaussian blur is a widely used image processing technique for reducing noise and smoothing images.
# sigmaX: The standard deviation in the X direction, which controls the spread or width of the Gaussian kernel
#  in the horizontal direction. If you set sigmaX to 0, OpenCV will automatically calculate it based on the kernel size.
import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('noise_2.jpg',-1)
img =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
kernal=np.ones((5,5),np.float32)/25
dst=cv2.filter2D(img,-1,kernal)
blur=cv2.blur(img,(5,5));
gau_blur=cv2.GaussianBlur(img,(5,5),0)
titles=['image','filter1','blur','gblur']
images=[img,dst,blur,gau_blur]
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([]) 
plt.show()
# cv2.imshow('gblur',gau_blur)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


