import cv2
video= cv2.VideoCapture(0)
video.set(3,1280)
video.set(4,720)
while(True):
     ret,frame=video.read()
     text='Height :'+str(video.get(4))+' Width'+str(video.get(3))
     font=cv2.FONT_HERSHEY_COMPLEX
     frame=cv2.putText(frame,text,(10,50),font,1,(0,0,255),2,cv2.LINE_AA)
     cv2.imshow("DekhFace",frame)
     if cv2.waitKey(1) & 0xFF == ord('q'):
        break;

video.release()
cv2.destroyAllWindows()