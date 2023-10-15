import cv2
from matplotlib import pyplot as plt
img=cv2.imread('image.jpg',-1)
resized_img=cv2.resize(img,(1280,820))
cv2.imshow("image OpenCV",resized_img)

# resized_img=cv2.cvtColor(resized_img,cv2.COLOR_BGR2RGB)

plt.imshow(resized_img)
# plt.xticks([]),plt.yticks([])       #it hides x and y scale
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

# obeservation
# you will see color difference in both images its because opencv prefers bgr format and matplotlib prefers rgb
# we use cvtcolor function to convert it to rgb format

#matplotlib provides extra features like scaling 