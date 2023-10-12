import cv2
import numpy as np
img=np.zeros([600,600,3],np.uint8)
cv2.namedWindow('imageWindow')
def nothing(x):
    print(x)


cv2.createTrackbar('B','imageWindow',0,255,nothing)
cv2.createTrackbar('G','imageWindow',0,255,nothing)
cv2.createTrackbar('R','imageWindow',0,255,nothing)

while(1):
    cv2.imshow("imageWindow",img)
    k=cv2.waitKey(1) & 0xFF
    if k=='27':
        break;

    b=cv2.getTrackbarPos('B','imageWindow')
    g=cv2.getTrackbarPos('G','imageWindow')
    r=cv2.getTrackbarPos('R','imageWindow')

    img[:]=[b,g,r]

cv2.destroyAllWindows()
