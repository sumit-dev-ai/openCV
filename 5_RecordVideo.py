import cv2
video= cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter("Output.avi",fourcc,25.0,(640,480))
while(video.isOpened()):
     ret,frame=video.read()
     if ret==True:
        out.write(frame)
        cv2.imshow("DekhFace",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break;

video.release()
out.release()
cv2.destroyAllWindows()