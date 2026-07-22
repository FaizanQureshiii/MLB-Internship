import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread(r"C:\Users\OTS\Downloads\microsoft-surface-5120x2880-26737.jpg")

if img is None:
    print("Error: Image not found!")
    exit()


coordinates = [
    (50, 50),
    (150, 100),
    (300, 200),
    (500, 400)
]

print("Selected Pixel Values:\n")

for x, y in coordinates:

    if 0 <= x < img.shape[1] and 0 <= y < img.shape[0]:

        pixel = img[y][x]   

        print(f"Coordinate (x={x}, y={y})")
        print(f"Pixel Value (B, G, R): {pixel}\n")

    
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

    
        cv2.putText(
            img,
            f"({x},{y})",
            (x + 10, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 0, 0),
            1
        )

    else:
        print(f"Coordinate ({x}, {y}) is outside the image.\n")


cv2.imshow("Coordinate System", img)
plt.savefig("marked_coordinates.png", dpi=300, bbox_inches="tight")
cv2.waitKey(0)
cv2.destroyAllWindows()
