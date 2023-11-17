# import cv2
# import numpy as np
# from scipy.ndimage import median_filter
# from PIL import Image
# from plotImages import plotImage
#
# # Load the image
# img = np.array(Image.open("../images/ctisus/ctisusBmp/adrenal_1-01.bmp"))
#
# # Apply the median filter
# size = 3
# img_filtered = median_filter(img, size=size)
#
# # Display the original and median-filtered images
# cv2.imshow('Original Image', img)
# cv2.imshow('Filtered Image', img_filtered)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
import numpy as np
from scipy.ndimage import median_filter
from PIL import Image
from plotImages import plotImage

# Load the image
img = cv2.imread("../images/ctisus/ctisusBmp/adrenal_1-01.bmp")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply the median filter
size = 5
gray_filtered = median_filter(gray, size=size)

# Display the original and median-filtered images
cv2.imshow('Original Image', gray)
cv2.imshow('Filtered Image', gray_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
