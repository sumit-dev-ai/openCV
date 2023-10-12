import cv2
video= cv2.VideoCapture('Hataraku Maou-sama - S02E11.mkv')
while(video.isOpened()):
     ret,frame=video.read()
     cv2.imshow("DekhFace",frame)
     if cv2.waitKey(1) & 0xFF == ord('q'):
        break;

video.release()
cv2.destroyAllWindows()