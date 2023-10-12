import cv2
import numpy as np
# img=cv2.imread('4018995.jpg',-1)
img=np.zeros([840,1580,3],np.uint8)

line=cv2.line(img,(0,0),(255,255),(255,0,0),3)

arrowedline=cv2.arrowedLine(img,(0,255),(300,300),(255,0,0),3)

rectangle=cv2.rectangle(img,(800,200),(200,800),(255,255,0),3)

circle=cv2.circle(img,(500,500),140,(255,255,0),-1)
font=cv2.FONT_HERSHEY_DUPLEX
text=cv2.putText(img,'DemonSlayer',(10,800),font,5,(255,0,0),5,cv2.LINE_4)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("demonslayer.png",img)