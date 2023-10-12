import cv2 
img=cv2.imread("image.jpg")
img2=cv2.imread("4018995.jpg")

img=cv2.resize(img,[1800,820])
img2=cv2.resize(img2,[1800,820])

mergeImage=cv2.addWeighted(img,0.5,img2,0.5,0)
# mergeImage=cv2.add(img,img2)
cv2.imshow("image",mergeImage)
cv2.waitKey(0)
cv2.destroyAllWindows()