import cv2
import numpy as np
def nothing(x):
    pass

while True:
    frame = cv2.imread('1112.jpg', -1)
    # Get the dimensions of the image
    height, width, _ = frame.shape
    # # Create a resizable window
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', width, height)




#main code starts here
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_blue = np.array([100, 50, 50])    #lower blue color range
    upper_blue = np.array([130, 255, 255])   #higher blue color range

    masking=cv2.inRange(hsv,lower_blue,upper_blue)
    res=cv2.bitwise_and(frame,frame,mask=masking)

    cv2.imshow('frame', frame)
    cv2.imshow('masking', masking)
    cv2.imshow('res', res)

    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break

cv2.destroyAllWindows()
