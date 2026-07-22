import cv2

img = cv2.imread("C:\\Users\\OTS\\Downloads\\microsoft-surface-5120x2880-26737.jpg", 0)

print(img)
height=len(img)
width=len(img[0])

print("Height:", height)
print("Width:", width)
print(img[0][0])
print(img[100][200])
print(img[50][50])

img[0][0] = 255
img[50][50] = 0
img[100][100] = 128

cv2.imshow("Updated Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()