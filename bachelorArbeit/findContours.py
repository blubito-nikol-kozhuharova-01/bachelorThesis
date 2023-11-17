import cv2
import numpy as np
from skimage.measure import regionprops

# Load the image and perform k-means clustering
img = cv2.imread('./images/ctisus/ctisusBmp/adrenal_1-01.bmp')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
Z = img.reshape((-1,1)).astype(np.float32)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 6
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Extract the pixels belonging to the region of interest
binary_image = np.zeros_like(img)
binary_image[label.reshape(img.shape) == 1] = 255
# Clean up the binary image
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
binary_image = cv2.erode(binary_image, kernel, iterations=1)
binary_image = cv2.dilate(binary_image, kernel, iterations=1)

# Find the contour of the region
contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Compute the diameter of the region
props = regionprops(binary_image.astype(int))[0]
diameter = props.equivalent_diameter

# Display the results
cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
