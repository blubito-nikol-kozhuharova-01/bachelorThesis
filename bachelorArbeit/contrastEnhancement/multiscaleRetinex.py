import cv2
import numpy as np
from plotImages import plotImage

def multiscale_retinex(image, sigma_list):
    # Create a copy of the image
    img_msr = np.zeros_like(image, dtype=np.float16)

    for sigma in sigma_list:
        # Apply Gaussian smoothing to the image
        img_s = cv2.GaussianBlur(image, (0, 0), sigma)

        # Subtract the smoothed image from the original image
        img_msr += np.log10(image) - np.log10(img_s)

    # Normalize the image
    img_msr = img_msr / len(sigma_list)

    # Convert the image to uint8 data type
    img_msr = np.uint8(img_msr * 255)

    img_msr = cv2.normalize(img_msr, None, 0, 255, cv2.NORM_MINMAX)

    return img_msr


# Load an image
img = cv2.imread("../images/ctisus/ctisusTiff/adrenal_1-01.tiff")

# Apply Multiscale Retinex with a list of sigma values
img_msr = multiscale_retinex(img, [15, 80, 160])

# Display the original and enhanced images
plotImage(img, img_msr)
