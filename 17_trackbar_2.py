import cv2


def nothing(x):
    pass

cv2.namedWindow("imageWindow")

switch='Color/Gray'
cv2.createTrackbar(switch,'imageWindow',0,1,nothing)

while True:
    img=cv2.imread("image.jpg")
    k=cv2.waitKey(1) & 0xFF
    if k=='27':
        break;
    s=cv2.getTrackbarPos(switch,'imageWindow')
    if s==0:
        pass
    else:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img=cv2.imshow('imageWindow',img)


cv2.destroyAllWindows()
