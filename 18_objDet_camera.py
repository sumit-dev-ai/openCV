import cv2
import numpy as np

cap=cv2.VideoCapture(0)
cv2.namedWindow('tracking')
def nothing(x):
    pass

cv2.createTrackbar('lH','tracking',0,255,nothing)   #lower hue
cv2.createTrackbar('LS','tracking',0,255,nothing)   #lower saturation
cv2.createTrackbar('LV','tracking',0,255,nothing)   #lower value
cv2.createTrackbar('HH','tracking',255,255,nothing)   #high hue
cv2.createTrackbar('HS','tracking',255,255,nothing)   #high sat
cv2.createTrackbar('HV','tracking',255,255,nothing)  #high val

while True:
    ret,frame = cap.read()
    # Get the dimensions of the image
    height, width, _ = frame.shape
    # # Create a resizable window
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', width, height)


    l_h=cv2.getTrackbarPos('lH','tracking')
    l_s=cv2.getTrackbarPos('LS','tracking')
    l_v=cv2.getTrackbarPos('LV','tracking')
    h_h=cv2.getTrackbarPos('HH','tracking')
    h_s=cv2.getTrackbarPos('HS','tracking')
    h_v=cv2.getTrackbarPos('HV','tracking')


    #main code starts here
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_color_bound = np.array([l_h, l_s, l_v])    #lower blue color range
    upper_color_bound = np.array([h_h, h_s, h_v])   #higher blue color range

    masking=cv2.inRange(hsv,lower_color_bound,upper_color_bound)
    res=cv2.bitwise_and(frame,frame,mask=masking)

    cv2.imshow('frame', frame)
    cv2.imshow('masking', masking)
    cv2.imshow('res', res)
    key = cv2.waitKey(1)
        
    if key == ord('q'):
        break
cap.release
cv2.destroyAllWindows()
