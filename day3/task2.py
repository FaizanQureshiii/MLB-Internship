import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread(r"C:\Users\OTS\Downloads\microsoft-surface-5120x2880-26737.jpg")

if img is None:
    print("Error: Image not found.")
    exit()

height, width, channels = img.shape

img_rgb = np.zeros((height, width, channels), dtype=np.uint8)

for i in range(height):
    for j in range(width):
        img_rgb[i][j][0] = img[i][j][2]  
        img_rgb[i][j][1] = img[i][j][1]   
        img_rgb[i][j][2] = img[i][j][0]   

red_channel = np.zeros((height, width, 3), dtype=np.uint8)
green_channel = np.zeros((height, width, 3), dtype=np.uint8)
blue_channel = np.zeros((height, width, 3), dtype=np.uint8)


for i in range(height):
    for j in range(width):

        red = img_rgb[i][j][0]
        green = img_rgb[i][j][1]
        blue = img_rgb[i][j][2]

        
        red_channel[i][j][0] = red
        red_channel[i][j][1] = 0
        red_channel[i][j][2] = 0

        
        green_channel[i][j][0] = 0
        green_channel[i][j][1] = green
        green_channel[i][j][2] = 0

        
        blue_channel[i][j][0] = 0
        blue_channel[i][j][1] = 0
        blue_channel[i][j][2] = blue


merged_image = np.zeros((height, width, 3), dtype=np.uint8)

for i in range(height):
    for j in range(width):

        merged_image[i][j][0] = red_channel[i][j][0]
        merged_image[i][j][1] = green_channel[i][j][1]
        merged_image[i][j][2] = blue_channel[i][j][2]


plt.figure(figsize=(15,10))

plt.subplot(2,3,1)
plt.imshow(img_rgb)
plt.title("Original RGB")
plt.axis("off")

plt.subplot(2,3,2)
plt.imshow(red_channel)
plt.title("Red Channel")
plt.axis("off")

plt.subplot(2,3,3)
plt.imshow(green_channel)
plt.title("Green Channel")
plt.axis("off")

plt.subplot(2,3,4)
plt.imshow(blue_channel)
plt.title("Blue Channel")
plt.axis("off")

plt.subplot(2,3,5)
plt.imshow(merged_image)
plt.title("Merged Image")
plt.axis("off")

plt.tight_layout()
plt.show()