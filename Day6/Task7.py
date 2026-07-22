import cv2
import numpy as np


img = cv2.imread(r"C:\Users\OTS\Downloads\microsoft-surface-5120x2880-26737.jpg", 0)

if img is None:
    print("Image not found!")
    exit()

height = len(img)
width = len(img[0])


def apply_kernel(kernel):

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

    return output


identity = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

blur = [
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]
]

sharpen = [
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
]


edge = [
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]
]

identity_img = apply_kernel(identity)
blur_img = apply_kernel(blur)
sharpen_img = apply_kernel(sharpen)
edge_img = apply_kernel(edge)

cv2.imshow("Original", img)
cv2.imshow("Identity", identity_img)
cv2.imshow("Blur", blur_img)
cv2.imshow("Sharpen", sharpen_img)
cv2.imshow("Edge Detection", edge_img)

cv2.imwrite("identity.png", identity_img)
cv2.imwrite("blur.png", blur_img)
cv2.imwrite("sharpen.png", sharpen_img)
cv2.imwrite("edge_detection.png", edge_img)

cv2.waitKey(0)
cv2.destroyAllWindows()