import cv2
img=cv2.imread(r"C:\Users\OTS\Downloads\microsoft-surface-5120x2880-26737.jpg");

height=len(img)
width=len(img[0])
numofchanels=len(img[0][0])
totalpixels=height*width

print("height=",height)
print("width=",width)
print("numofchanels=",numofchanels)
print("totalpixels=",totalpixels)

