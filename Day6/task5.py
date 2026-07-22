import cv2

img = cv2.imread(r"C:\Users\OTS\Downloads\microsoft-surface-5120x2880-26737.jpg")

points = [
    ((50, 60), (200, 180)),
    ((100, 50), (300, 250)),
    ((20, 200), (400, 100))
]

for p1, p2 in points:

    x1, y1 = p1
    x2, y2 = p2


    cv2.circle(img, (x1, y1), 5, (0, 0, 255), -1)
    cv2.circle(img, (x2, y2), 5, (255, 0, 0), -1)

    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    euclidean = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    manhattan = abs(x2 - x1) + abs(y2 - y1)

    print("Point 1:", p1)
    print("Point 2:", p2)
    print("Euclidean Distance:", round(euclidean, 2))
    print("Manhattan Distance:", manhattan)
    print()

cv2.imshow("Distance Comparison", img)
cv2.imwrite("distance_comparison.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()