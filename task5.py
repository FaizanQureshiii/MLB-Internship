import cv2
import numpy as np
img=cv2.imread(r"C:\Users\OTS\Downloads\microsoft-surface-5120x2880-26737.jpg");

if img is None:
    print("Error: Image not found or unable to load.")


height=len(img)
width=len(img[0])

blue=[]
green=[]
red=[]

for rows in range(height):
    bluearray=[]
    greenarray=[]
    redarray=[]
    for cols in range(width):
        b=img[rows,cols,0]
        g=img[rows,cols,1]
        r=img[rows,cols,2]
        bluearray.append(b)
        greenarray.append(g)
        redarray.append(r)
    
    blue.append(bluearray)
    green.append(greenarray)
    red.append(redarray)

blue = np.array(blue, dtype=np.uint8)
green = np.array(green, dtype=np.uint8)
red = np.array(red, dtype=np.uint8)

cv2.imwrite("blue.jpg",blue)
cv2.imwrite("green.jpg",green)
cv2.imwrite("red.jpg",red)


