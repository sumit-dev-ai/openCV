import cv2
video= cv2.VideoCapture(0)
while(video.isOpened()):
     ret,frame=video.read()
     a=video.get(cv2.CAP_PROP_FRAME_HEIGHT)
     b=video.get(cv2.CAP_PROP_FRAME_WIDTH)
     cv2.imshow("DekhFace",frame)
     if cv2.waitKey(1) & 0xFF == ord('q'):
        break;

video.release()
print(a,"-",b)
cv2.destroyAllWindows()