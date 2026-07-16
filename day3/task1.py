import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread(r"C:\Users\OTS\Downloads\microsoft-surface-5120x2880-26737.jpg")

if img is None:
    print("Error: Image not found.")
    exit()


height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]


img_rgb = np.zeros((height, width, channels), dtype=np.uint8)


for i in range(height):
    for j in range(width):

        blue = img[i][j][0]
        green = img[i][j][1]
        red = img[i][j][2]

        img_rgb[i][j][0] = red
        img_rgb[i][j][1] = green
        img_rgb[i][j][2] = blue


plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.imshow(img)
plt.title("BGR Image (Displayed as RGB)")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(img_rgb)
plt.title("Manual RGB Image")
plt.axis("off")

plt.tight_layout()
plt.show()