import cv2
import matplotlib.pyplot as plt

low_contrast = cv2.imread(r"C:\Users\OTS\Downloads\low_contrast.jpg", cv2.IMREAD_GRAYSCALE)
bright = cv2.imread(r"C:\Users\OTS\Downloads\bright.jpg", cv2.IMREAD_GRAYSCALE)
dark = cv2.imread(r"C:\Users\OTS\Downloads\dark.jpg", cv2.IMREAD_GRAYSCALE)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

images = [
    ("Low Contrast", low_contrast),
    ("Bright", bright),
    ("Dark", dark)
]

plt.figure(figsize=(15,12))

position = 1

for title, image in images:

    equalized = cv2.equalizeHist(image)
    clahe_image = clahe.apply(image)

    plt.subplot(3,3,position)
    plt.imshow(image, cmap="gray")
    plt.title(title)
    plt.axis("off")

    plt.subplot(3,3,position+1)
    plt.imshow(equalized, cmap="gray")
    plt.title("Histogram Equalization")
    plt.axis("off")

    plt.subplot(3,3,position+2)
    plt.imshow(clahe_image, cmap="gray")
    plt.title("CLAHE")
    plt.axis("off")

    cv2.imwrite(title.replace(" ","_")+"_equalized.jpg", equalized)
    cv2.imwrite(title.replace(" ","_")+"_clahe.jpg", clahe_image)

    position += 3

plt.tight_layout()
plt.show()