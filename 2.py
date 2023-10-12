import cv2

img=cv2.imread('4018995.jpg',-1)
print(img) 
cv2.imshow("image",img)
key=cv2.waitKey(0)
if key==27:
    cv2.destroyAllWindows()
elif key==ord('s'):
    cv2.imwrite("demonslayer.png",img)