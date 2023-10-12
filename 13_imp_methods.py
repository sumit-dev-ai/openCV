import numpy as np
import cv2
img=cv2.imread("image.jpg")

print(img.size)
print(img.shape)
print(img.dtype)
# cv2.imshow("image",img)
# cv2.waitkey(0)
# cv2.destroyAllWindows()