import cv2

def click_event(event, x, y, flags, param):
    if event==cv2.EVENT_FLAG_LBUTTON:
        print(x,",",y)
        font=cv2.FONT_HERSHEY_COMPLEX
        strXY=str(x)+","+str(y)
        cv2.putText(img,strXY,(x,y),font,0.6,(0,0,0),1)
        cv2.imshow("image",img)
    if event == cv2.EVENT_RBUTTONDBLCLK:
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        font=cv2.FONT_HERSHEY_COMPLEX
        strBGR="R:"+str(red)+","+"G:"+str(green)+","+"B:"+str(blue)
        cv2.putText(img,strBGR,(x,y),font,0.4,(0,255,255),1)
        cv2.imshow("image",img)
        
    
    



img=cv2.imread("move.jpg",-1)
cv2.imshow("image",img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()