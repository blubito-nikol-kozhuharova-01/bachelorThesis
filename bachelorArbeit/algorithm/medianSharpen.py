# import cv2
# import numpy as np
# from scipy.ndimage import median_filter
# from PIL import Image
# from skimage import io, exposure
#
# def sharpen_filter(img, alpha, beta):
#     # Define the kernel for the sharpen filter
#     # kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
#     kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
#
#     # Apply the filter to the input image
#     output = cv2.filter2D(img, -1, alpha * kernel + beta)
#
#     return output
#
# # Load the image
# img = cv2.imread("../images/ctisus/ctisusBmp/adrenal_1-01.bmp")
#
# # Convert the image to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# # Apply the median filter
# size = 4
# gray_filtered = median_filter(gray, size=size)
#
# # Apply the sharpen filter
# alpha = 1.7
# beta = 0
# output = sharpen_filter(gray_filtered, alpha, beta)
#
# # Display the original and median-filtered images
# cv2.imshow('Original Image', img)
# cv2.imshow('Filtered Image', output)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#



# import cv2
# import numpy as np
# from scipy.ndimage import median_filter
# from skimage import io, exposure
# from PIL import Image, ImageOps, ImageTk, ImageFilter
#
#
# def sharpen_filter(img, alpha, beta):
#     # Define the kernel for the sharpen filter
#     # kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
#     kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
#
#     # Apply the filter to the input image
#     output = cv2.filter2D(img, -1, alpha * kernel + beta)
#
#     return output
#
# # Load the image
# img = cv2.imread("../images/ctisus/ctisusBmp/adrenal_1-01.bmp")
#
# # cv2.medianBlur(img, ksize=5)
# cv2.medianBlur(img, ksize=5)
#
# # Apply the sharpen filter
# # alpha = 1.7
# # beta = 0
# # output = sharpen_filter(img, alpha, beta)
#
#
# output = img.filter(ImageFilter.SHARPEN)
#
# # Display the original and median-filtered images
# cv2.imshow('Original Image', img)
# cv2.imshow('Filtered Image', output)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np
from scipy.ndimage import median_filter
from skimage import io, exposure
from PIL import Image, ImageOps, ImageTk, ImageFilter

# Load the image
img = cv2.imread("../images/ctisus/ctisusBmp/adrenal_1-01.bmp")

# Apply the median filter
img = cv2.medianBlur(img, ksize=7)

# Convert the NumPy array to a PIL image
pil_img = Image.fromarray(img)

# Apply the sharpen filter
output = pil_img.filter(ImageFilter.SHARPEN)

# Display the original and filtered images
cv2.imshow('Original Image', img)
cv2.imshow('Median Filtered Image', np.array(pil_img))
cv2.imshow('Sharpen Filtered Image', np.array(output))
cv2.waitKey(0)
cv2.destroyAllWindows()
