import cv2
import numpy as np
def click_event(event, x, y, flags, param):
    if event==cv2.EVENT_FLAG_LBUTTON:
        red=img[y,x,2]
        green=img[y,x,1]
        blue=img[y,x,0]
        mycolorImage=np.zeros([512,512,3],np.uint8)
        mycolorImage[:]=[blue,green,red]
        font=cv2.FONT_HERSHEY_COMPLEX
        strBGR="R:{},G:{},B:{}".format(red,green,blue)
        cv2.putText(mycolorImage,strBGR,(10,30),font,0.4,(255,255,255),1)
        cv2.imshow("colorpicker",mycolorImage)


# img=np.zeros([612,612,3],np.uint8)
img=cv2.imread("image.jpg",-1)
cv2.imshow("image",img)
points=[]
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()