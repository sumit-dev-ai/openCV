import cv2
import numpy as np
def click_event(event, x, y, flags, param):
    if event==cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(img,(x,y),150,(0,0,255),1)
        points.append((x,y))
        if(len(points)>=2):
            cv2.line(img,points[-1],points[-2],(255,0,0),4)
        cv2.imshow("image",img)
 
    
    


img=np.zeros([612,612,3],np.uint8)
# img=cv2.imread("4018995.jpg",-1)
cv2.imshow("image",img)
points=[]
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()