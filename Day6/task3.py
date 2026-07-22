import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\OTS\Downloads\microsoft-surface-5120x2880-26737.jpg", 0)

height = len(img)
width = len(img[0])

minimum = 255
maximum = 0
total = 0

range1 = 0
range2 = 0
range3 = 0
range4 = 0
range5 = 0

histogram = [0] * 256

for i in range(height):
    for j in range(width):

        value = int(img[i][j])

        total += value

        histogram[value] += 1

        if value < minimum:
            minimum = value

        if value > maximum:
            maximum = value

        if 0 <= value <= 50:
            range1 += 1

        elif 51 <= value <= 100:
            range2 += 1

        elif 101 <= value <= 150:
            range3 += 1

        elif 151 <= value <= 200:
            range4 += 1

        else:
            range5 += 1

average = total / (height * width)

print("Minimum =", minimum)
print("Maximum =", maximum)
print("Average =", average)

print("\nIntensity Counts")

print("0-50     :", range1)
print("51-100   :", range2)
print("101-150  :", range3)
print("151-200  :", range4)
print("201-255  :", range5)

plt.bar(range(256), histogram)
plt.title("Pixel Intensity Distribution")
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.show()
#save the histogram as an image
plt.savefig("histogram.png", dpi=300, bbox_inches="tight")