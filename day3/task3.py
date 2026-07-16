import cv2
import numpy as np
import matplotlib.pyplot as plt


img  = cv2.imread(r"C:\Users\OTS\Downloads\microsoft-surface-5120x2880-26737.jpg")

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


gray = np.zeros((height, width), dtype=np.uint8)

for i in range(height):
    for j in range(width):

        r = img_rgb[i][j][0]
        g = img_rgb[i][j][1]
        b = img_rgb[i][j][2]

        value = 0.299 * r + 0.587 * g + 0.114 * b

        gray[i][j] = int(value)

hsv = np.zeros((height, width, 3), dtype=np.uint8)

for i in range(height):
    for j in range(width):

        r = img_rgb[i][j][0] / 255.0
        g = img_rgb[i][j][1] / 255.0
        b = img_rgb[i][j][2] / 255.0

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


hsl = np.zeros((height, width, 3), dtype=np.uint8)

for i in range(height):
    for j in range(width):

        r = img_rgb[i][j][0] / 255.0
        g = img_rgb[i][j][1] / 255.0
        b = img_rgb[i][j][2] / 255.0

        maximum = max(r, g, b)
        minimum = min(r, g, b)

        delta = maximum - minimum

      
        l = (maximum + minimum) / 2

        
        if delta == 0:
            s = 0

        else:

            s = delta / (1 - abs(2 * l - 1))

        

        if delta == 0:

            h = 0

        elif maximum == r:

            h = 60 * (((g - b) / delta) % 6)

        elif maximum == g:

            h = 60 * (((b - r) / delta) + 2)

        else:

            h = 60 * (((r - g) / delta) + 4)

        hsl[i][j][0] = int(h / 2)
        hsl[i][j][1] = int(s * 255)
        hsl[i][j][2] = int(l * 255)



lab = np.zeros((height, width, 3), dtype=np.uint8)


Xn = 95.047
Yn = 100.000
Zn = 108.883

for i in range(height):
    for j in range(width):

        r = img_rgb[i][j][0] / 255.0
        g = img_rgb[i][j][1] / 255.0
        b = img_rgb[i][j][2] / 255.0

        # Gamma Correction
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
            fx = X ** (1 / 3)
        else:
            fx = (7.787 * X) + (16 / 116)

        if Y > 0.008856:
            fy = Y ** (1 / 3)
        else:
            fy = (7.787 * Y) + (16 / 116)

        if Z > 0.008856:
            fz = Z ** (1 / 3)
        else:
            fz = (7.787 * Z) + (16 / 116)

        L = (116 * fy) - 16
        A = 500 * (fx - fy)
        B = 200 * (fy - fz)

        # Scale to 0-255 for display
        L = np.clip(L * 255 / 100, 0, 255)
        A = np.clip(A + 128, 0, 255)
        B = np.clip(B + 128, 0, 255)

        lab[i][j][0] = int(L)
        lab[i][j][1] = int(A)
        lab[i][j][2] = int(B)


plt.figure(figsize=(18,10))

plt.subplot(2,3,1)
plt.imshow(img_rgb)
plt.title("RGB")
plt.axis("off")

plt.subplot(2,3,2)
plt.imshow(gray, cmap="gray")
plt.title("Grayscale")
plt.axis("off")

plt.subplot(2,3,3)
plt.imshow(hsv)
plt.title("HSV")
plt.axis("off")

plt.subplot(2,3,4)
plt.imshow(hsl)
plt.title("HSL")
plt.axis("off")

plt.subplot(2,3,5)
plt.imshow(lab)
plt.title("LAB")
plt.axis("off")

plt.tight_layout()
plt.show()