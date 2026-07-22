import cv2
import numpy as np

# Read grayscale image
img = cv2.imread(r"C:\Users\OTS\Downloads\microsoft-surface-5120x2880-26737.jpg", 0)

# Check if image loaded successfully
if img is None:
    print("Image not found!")
    exit()

# 3×3 Edge Detection Kernel
kernel = [
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
]

# Get image dimensions
height = len(img)
width = len(img[0])

# Function to perform manual convolution with a given stride
def convolution(stride):

    # Calculate output image size
    out_height = (height - 3) // stride + 1
    out_width = (width - 3) // stride + 1

    # Create empty output image
    output = np.zeros((out_height, out_width), dtype=np.uint8)

    row = 0

    # Move kernel over image according to stride
    for i in range(0, height - 2, stride):

        col = 0

        for j in range(0, width - 2, stride):

            total = 0

            # Apply 3×3 kernel
            for ki in range(3):
                for kj in range(3):

                    pixel = int(img[i + ki][j + kj])
                    total += pixel * kernel[ki][kj]

            # Keep pixel value between 0 and 255
            if total < 0:
                total = 0
            elif total > 255:
                total = 255

            output[row][col] = total
            col += 1

        row += 1

    return output

# Apply convolution with stride 1
stride1 = convolution(1)

# Apply convolution with stride 2
stride2 = convolution(2)

# Print output sizes
print("Original Size :", img.shape)
print("Stride 1 Size :", stride1.shape)
print("Stride 2 Size :", stride2.shape)

# Display images
cv2.imshow("Original", img)
cv2.imshow("Stride 1", stride1)
cv2.imshow("Stride 2", stride2)

cv2.waitKey(0)
cv2.destroyAllWindows()