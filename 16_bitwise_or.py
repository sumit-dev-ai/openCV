import cv2

import numpy as np
img2=np.zeros([250,500,3])
img2=cv2.rectangle(img2,(200,0),(300,100),(255,255,255),-1)

img=np.zeros([250,500,3])
img=cv2.rectangle(img,(250,0),(500,250),(255,255,255),-1)




#bitwise And
bit_or=cv2.bitwise_or(img2,img)
cv2.imshow("bitwise image ",bit_or)





cv2.imshow("image",img)
cv2.imshow("image2",img2)



cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("demonslayer.png",img)