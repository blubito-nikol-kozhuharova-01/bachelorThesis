import cv2
import numpy as np

def sharpen_filter(img, alpha, beta):
    # Define the kernel for the sharpen filter
    # kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

    # Apply the filter to the input image
    output = cv2.filter2D(img, -1, alpha * kernel + beta)

    return output

# Read in an image
img = cv2.imread('../images/ctisus/ctisusBmp/adrenal_1-01.bmp')

# Apply the sharpen filter
alpha = 1.2
beta = 0
output = sharpen_filter(img, alpha, beta)

# Display the original and sharpened images
cv2.imshow('Original Image', img)
cv2.imshow('Sharpened Image', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
