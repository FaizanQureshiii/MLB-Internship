import cv2
import numpy as np

# Read grayscale image
img = cv2.imread(r"C:\Users\OTS\Downloads\microsoft-surface-5120x2880-26737.jpg", 0)

# Check if image is loaded
if img is None:
    print("Image not found!")
    exit()

# Get image dimensions
height = len(img)
width = len(img[0])


# Create a new image with 1-pixel border
padded = np.zeros((height + 2, width + 2), dtype=np.uint8)

# Copy original image into the center
for i in range(height):
    for j in range(width):
        padded[i + 1][j + 1] = img[i][j]


# Edge Detection Kernel
kernel = [
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
]


def convolution(image, stride):

    h = len(image)
    w = len(image[0])

    out_height = (h - 3) // stride + 1
    out_width = (w - 3) // stride + 1

    output = np.zeros((out_height, out_width), dtype=np.uint8)

    row = 0

    for i in range(0, h - 2, stride):

        col = 0

        for j in range(0, w - 2, stride):

            total = 0

            for ki in range(3):
                for kj in range(3):

                    pixel = int(image[i + ki][j + kj])
                    total += pixel * kernel[ki][kj]

            # Keep values between 0 and 255
            if total < 0:
                total = 0
            elif total > 255:
                total = 255

            output[row][col] = total
            col += 1

        row += 1

    return output

# Apply convolution with different strides
stride1 = convolution(padded, 1)
stride2 = convolution(padded, 2)


print("Original Image Size :", img.shape)
print("Padded Image Size   :", padded.shape)
print("Stride 1 Size       :", stride1.shape)
print("Stride 2 Size       :", stride2.shape)



cv2.imshow("Original Image", img)
cv2.imshow("Padded Image", padded)
cv2.imshow("Convolution (Stride = 1)", stride1)
cv2.imshow("Convolution (Stride = 2)", stride2)

# Save results
cv2.imwrite("padded_image.png", padded)
cv2.imwrite("stride1_output.png", stride1)
cv2.imwrite("stride2_output.png", stride2)

cv2.waitKey(0)
cv2.destroyAllWindows()