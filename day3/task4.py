import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread(r"C:\Users\OTS\Downloads\microsoft-surface-5120x2880-26737.jpg")

if img is None:
    print("Image not found!")
    exit()

height, width, channels = img.shape


img = np.zeros((height, width, 3), dtype=np.uint8)

for i in range(height):
    for j in range(width):

        blue = img[i][j][0]
        green = img[i][j][1]
        red = img[i][j][2]

        img[i][j][0] = red
        img[i][j][1] = green
        img[i][j][2] = blue


hsv = np.zeros((height, width, 3), dtype=np.uint8)

for i in range(height):
    for j in range(width):

        r = img[i][j][0] / 255.0
        g = img[i][j][1] / 255.0
        b = img[i][j][2] / 255.0

        maximum = max(r, g, b)
        minimum = min(r, g, b)
        delta = maximum - minimum

        
        if delta == 0:
            h = 0

        elif maximum == r:
            h = 60 * (((g - b) / delta) % 6)

        elif maximum == g:
            h = 60 * (((b - r) / delta) + 2)

        else:
            h = 60 * (((r - g) / delta) + 4)

        
        if maximum == 0:
            s = 0
        else:
            s = delta / maximum

        
        v = maximum

        hsv[i][j][0] = int(h / 2)
        hsv[i][j][1] = int(s * 255)
        hsv[i][j][2] = int(v * 255)



mask = np.zeros((height, width), dtype=np.uint8)
segmented = np.zeros((height, width, 3), dtype=np.uint8)


lower_h = 100
upper_h = 140

lower_s = 100
upper_s = 255

lower_v = 50
upper_v = 255

for i in range(height):
    for j in range(width):

        h = hsv[i][j][0]
        s = hsv[i][j][1]
        v = hsv[i][j][2]

        if (lower_h <= h <= upper_h and
            lower_s <= s <= upper_s and
            lower_v <= v <= upper_v):

            mask[i][j] = 255

            segmented[i][j][0] = img[i][j][0]
            segmented[i][j][1] = img[i][j][1]
            segmented[i][j][2] = img[i][j][2]

        else:

            mask[i][j] = 0

            segmented[i][j][0] = 0
            segmented[i][j][1] = 0
            segmented[i][j][2] = 0


plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.imshow(img)
plt.title("Original RGB")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(mask, cmap="gray")
plt.title("Mask")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(segmented)
plt.title("Segmented Output")
plt.axis("off")

plt.tight_layout()
plt.show()  