# # canny edge detector is an edge detection operator that uses a multi-stage algorithm to 
# # to detect a wide range of edges in images
# #5 steps 
# Noise Reduction: The first step involves reducing noise in the image. 
# This is typically done using a Gaussian filter to smooth the image and remove high-frequency noise.

# Gradient Calculation: In this step, the algorithm calculates the gradient of the image intensity.
#  It involves computing the derivative of the image in both the horizontal and vertical directions 
# to determine the magnitude and direction of the gradient at each pixel.

# Non-Maximum Suppression: After gradient calculation, the algorithm performs non-maximum suppression.
#  This step helps thin out the edges by keeping only the local maxima in the gradient magnitude.
#  It ensures that only the most significant edges are retained.

# Double Thresholding In this step, the edges are classified into two categories: strong edges and weak edges. 
# Pixels with gradient magnitudes above a high threshold are considered strong edges, 
# and those below a low threshold are considered non-edges.
#  Pixels with gradient magnitudes between the high and low thresholds are classified as weak edges.

# Edge Tracking by Hysteresis: This final step aims to connect weak edges to strong edges to form continuous edge contours.
#  It works by starting from strong edge pixels and following the weak edges in their vicinity as long as they form
# a connected path of strong edges. 
# This helps in detecting continuous edges in the image.

import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('vk_gradient.jpg',0)
#in laplacian and sobel method our model also shows to much noise wgile canny methode minimizes those noise
canny=cv2.Canny(img,100,200,)



titles=['image','canny']
images=[img,canny]
for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([]) 
plt.show()