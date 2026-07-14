import cv2

img=cv2.imread(r"C:\Users\OTS\Downloads\microsoft-surface-5120x2880-26737.jpg");

height=len(img)
width=len(img[0])
numofchanels=len(img[0][0])
totalpixels=height*width

pixelcount1=0
pixelcount2=0
pixelcount3=0

for rows in range(height):
    for cols in range(width):
        for ch in range(numofchanels):
           
            pixel=img[rows,cols,ch]

            if pixel==0:
                pixelcount1=pixelcount1+1
            if pixel==255:
                pixelcount2=pixelcount2+1
            if pixel > 200:
                pixelcount3=pixelcount3+1



print("Total Pixels",totalpixels)
print("Black Pixels",pixelcount1)
print("White Pixels",pixelcount2)
print("More than 200 Pixels",pixelcount3)