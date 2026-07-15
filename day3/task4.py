import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_blue = (100,50,50)
upper_blue = (140,255,255)

mask = cv2.inRange(hsv, lower_blue, upper_blue)

result = cv2.bitwise_and(img,img,mask=mask)

plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.title("Original")

plt.subplot(1,3,2)
plt.imshow(mask,cmap="gray")
plt.title("Mask")

plt.subplot(1,3,3)
plt.imshow(cv2.cvtColor(result,cv2.COLOR_BGR2RGB))
plt.title("Segmented")

plt.show()