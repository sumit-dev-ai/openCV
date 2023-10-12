import cv2

import numpy as np
img=np.zeros([250,500,3])
img=cv2.rectangle(img,(200,0),(300,100),(255,255,255),-1)





#bitwise And
Not_img=cv2.bitwise_not(img)
cv2.imshow("Original image",img)
cv2.imshow("bitwise not 1",Not_img)



cv2.waitKey(0)
cv2.destroyAllWindows()
