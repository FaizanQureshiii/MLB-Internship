import cv2

img=cv2.imread(r"C:\Users\OTS\Downloads\microsoft-surface-5120x2880-26737.jpg");

if img is None:
    print("Error: Image not found or unable to load.")
    

img[20][20]=[0,0,255]
img[10][10]=[0,255,0]
img[100][100]=[255,0,0]
img[40][40]=[0,0,0]
img[30][30]=[255,255,255]

cv2.imwrite("modifyimage.jpg",img)
print("image modified.jpg")
