import cv2
video= cv2.VideoCapture(0)
print("Previous Height : ",video.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("Previous Width : ",video.get(cv2.CAP_PROP_FRAME_WIDTH))
video.set(3,1280)
video.set(4,680)
while(True):
     ret,frame=video.read()
     cv2.imshow("DekhFace",frame)
     if cv2.waitKey(1) & 0xFF == ord('q'):
        break;

video.release()
cv2.destroyAllWindows()