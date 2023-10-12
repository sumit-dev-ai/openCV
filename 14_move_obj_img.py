import numpy as np
import cv2
img=cv2.imread("move.jpg")
if img is None:
    print("Image didnt load properly")
    exit()

ball=img[111:212,632:741]
source_height, source_width, _ = ball.shape
img[373:373 + source_height, 714:714 + source_width]=ball
print(_)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()