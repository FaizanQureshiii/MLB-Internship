import cv2
import numpy as np

img = cv2.imread(r"C:\Users\OTS\Downloads\microsoft-surface-5120x2880-26737.jpg", 0)

if img is None:
    print("Image not found!")
    exit()

height = len(img)
width = len(img[0])
kernel = [
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
]


output = np.zeros((height, width), dtype=np.uint8)


for i in range(1, height - 1):
    for j in range(1, width - 1):

        total = 0

        for ki in range(3):
            for kj in range(3):

          
                pixel = int(img[i + ki - 1][j + kj - 1])

                total += pixel * kernel[ki][kj]

        if total < 0:
            total = 0
        elif total > 255:
            total = 255

        output[i][j] = total


cv2.imshow("Original Image", img)
cv2.imshow("Convolution Output", output)


cv2.imwrite("convolution_output.png", output)

cv2.waitKey(0)
cv2.destroyAllWindows()