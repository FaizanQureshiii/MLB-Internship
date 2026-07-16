import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread(r"C:\Users\OTS\Downloads\microsoft-surface-5120x2880-26737.jpg")

if img is None:
    print("Image not found!")
    exit()

height, width, channels = img.shape



img_rgb = np.zeros((height, width, 3), dtype=np.uint8)

for i in range(height):
    for j in range(width):

        blue = img[i][j][0]
        green = img[i][j][1]
        red = img[i][j][2]

        img_rgb[i][j][0] = red
        img_rgb[i][j][1] = green
        img_rgb[i][j][2] = blue


lab = np.zeros((height, width, 3), dtype=np.uint8)

Xn = 95.047
Yn = 100.000
Zn = 108.883

for i in range(height):
    for j in range(width):

        r = img_rgb[i][j][0] / 255.0
        g = img_rgb[i][j][1] / 255.0
        b = img_rgb[i][j][2] / 255.0

        
        if r > 0.04045:
            r = ((r + 0.055) / 1.055) ** 2.4
        else:
            r = r / 12.92

        if g > 0.04045:
            g = ((g + 0.055) / 1.055) ** 2.4
        else:
            g = g / 12.92

        if b > 0.04045:
            b = ((b + 0.055) / 1.055) ** 2.4
        else:
            b = b / 12.92

        r *= 100
        g *= 100
        b *= 100
        
        X = r * 0.4124 + g * 0.3576 + b * 0.1805

        Y = r * 0.2126 + g * 0.7152 + b * 0.0722

        Z = r * 0.0193 + g * 0.1192 + b * 0.9505
        X /= Xn
        Y /= Yn
        Z /= Zn
        if X > 0.008856:
            fx = X ** (1/3)
        else:
            fx = (7.787 * X) + (16 / 116)

        if Y > 0.008856:
            fy = Y ** (1/3)
        else:
            fy = (7.787 * Y) + (16 / 116)

        if Z > 0.008856:
            fz = Z ** (1/3)
        else:
            fz = (7.787 * Z) + (16 / 116)

        L = (116 * fy) - 16
        A = 500 * (fx - fy)
        B = 200 * (fy - fz)
        L = np.clip(L * 255 / 100, 0, 255)
        A = np.clip(A + 128, 0, 255)
        B = np.clip(B + 128, 0, 255)

        lab[i][j][0] = int(L)
        lab[i][j][1] = int(A)
        lab[i][j][2] = int(B)

L_channel = np.zeros((height, width), dtype=np.uint8)
A_channel = np.zeros((height, width), dtype=np.uint8)

B_channel = np.zeros((height, width), dtype=np.uint8)

for i in range(height):

    for j in range(width):

        L_channel[i][j] = lab[i][j][0]
        A_channel[i][j] = lab[i][j][1]
        B_channel[i][j] = lab[i][j][2]

plt.figure(figsize=(14,8))

plt.subplot(2,2,1)
plt.imshow(img_rgb)
plt.title("Original RGB")
plt.axis("off")

plt.subplot(2,2,2)
plt.imshow(L_channel, cmap="gray")
plt.title("L Channel (Lightness)")
plt.axis("off")

plt.subplot(2,2,3)
plt.imshow(A_channel, cmap="gray")
plt.title("A Channel (Green ↔ Red)")
plt.axis("off")

plt.subplot(2,2,4)
plt.imshow(B_channel, cmap="gray")
plt.title("B Channel (Blue ↔ Yellow)")
plt.axis("off")

plt.tight_layout()
plt.show()