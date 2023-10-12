import cv2 
img=cv2.imread("image.jpg")
img2=cv2.imread("move.jpg")

img2_height,img2_weight,_=img2.shape

img[180:180+img2_height,320:320+img2_weight]=img2

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()