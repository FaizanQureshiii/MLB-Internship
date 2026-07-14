import cv2

img=cv2.imread("C:\\Users\\OTS\\Downloads\\microsoft-surface-5120x2880-26737.jpg")

if img is None:
    print("Error: Image not found or unable to load.")

height=len(img)
width=len(img[0])
channels=len(img[0][0])
total=0
count=0
minimum=img[0,0,0]
maximum=img[0,0,0]

for rows in range(height):
    for cols in range(width):
        for ch in range(channels):
            pixel=img[rows,cols,ch]
            total=total+pixel
            count=count+1;

            if pixel<minimum:
                minimum=pixel
            if pixel>maximum:
                maximum=pixel

mean=total/count;

print("mean=",mean)

print("minimum=",minimum)

print("maximum=",maximum)





