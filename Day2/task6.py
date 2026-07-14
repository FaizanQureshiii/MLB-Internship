import cv2
import numpy as np

img=cv2.imread(r"C:\Users\OTS\Downloads\microsoft-surface-5120x2880-26737.jpg");
if img is None:
    print("Error Image not found")

height=len(img)
width=len(img[0])
grey = np.zeros((height, width), dtype=np.uint8)

for row in range(height):
    for col in range(width):
        b=img[row,col,0]
        g=img[row,col,1]
        r=img[row,col,2]
        grey[row,col] = int((b+g+r)/3)

cv2.imwrite("grey.jpg",grey)

