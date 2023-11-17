# import cv2
# import numpy as np
# from scipy.ndimage import median_filter
# from skimage import io, exposure
# from PIL import Image, ImageOps, ImageTk, ImageFilter
#
# # Load the image
# img = cv2.imread("../images/ctisus/ctisusBmp/adrenal_1-01.bmp")
#
# # Apply the median filter
# img = cv2.medianBlur(img, ksize=7)
#
# # Convert the image to grayscale
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# # Apply the sharpen filter
# pil_img = Image.fromarray(gray_img)
# sharpen = pil_img.filter(ImageFilter.SHARPEN)
#
# # Convert the sharpened image to a NumPy array
# sharpen_array = np.array(sharpen)
#
# # Define the number of clusters
# num_clusters = 6
#
# # Reshape the image to a 2D array of pixels and convert it to float32 type
# pixel_values = sharpen_array.reshape((-1, 1)).astype(np.float32)
#
# # Perform k-means clustering
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# flags = cv2.KMEANS_RANDOM_CENTERS
# compactness, labels, centers = cv2.kmeans(pixel_values, num_clusters, None, criteria, 10, flags)
#
# # Reshape the labels to the shape of the original image
# segmented = labels.reshape(sharpen_array.shape)
#
# # Create masks for each cluster
# masks = []
# for i in range(num_clusters):
#     mask = np.zeros_like(gray_img)
#     mask[segmented == i] = 255
#     masks.append(mask)
#
# # Apply each mask to the original image to extract segments
# segments = []
# for mask in masks:
#     segment = cv2.bitwise_and(img, img, mask=mask.astype('uint8'))
#     segments.append(segment)
#
# # Display the results
# cv2.imshow('Original Image', img)
# cv2.imshow('Sharpen Filtered Image', sharpen_array)
#
# for i, segment in enumerate(segments):
#     cv2.imshow(f'Segment {i}', segment)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
#
#



import cv2
import numpy as np
from scipy.ndimage import median_filter
from skimage import io, exposure
from PIL import Image, ImageOps, ImageTk, ImageFilter
import os

# Load the image
img = cv2.imread("../images/ctisus/ctisusBmp/adrenal_1-01.bmp")

# Apply the median filter
img = cv2.medianBlur(img, ksize=7)

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply the sharpen filter
pil_img = Image.fromarray(gray_img)
sharpen = pil_img.filter(ImageFilter.SHARPEN)

# Convert the sharpened image to a NumPy array
sharpen_array = np.array(sharpen)

# Define the number of clusters
num_clusters = 6

# Reshape the image to a 2D array of pixels and convert it to float32 type
pixel_values = sharpen_array.reshape((-1, 1)).astype(np.float32)

# Perform k-means clustering
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
flags = cv2.KMEANS_RANDOM_CENTERS
compactness, labels, centers = cv2.kmeans(pixel_values, num_clusters, None, criteria, 10, flags)

# Reshape the labels to the shape of the original image
segmented = labels.reshape(sharpen_array.shape)

# Create masks for each cluster
masks = []
for i in range(num_clusters):
    mask = np.zeros_like(gray_img)
    mask[segmented == i] = 255
    masks.append(mask)

# Apply each mask to the original image to extract segments
segments = []
for mask in masks:
    segment = cv2.bitwise_and(img, img, mask=mask.astype('uint8'))
    segments.append(segment)

# Directory to save the segmented images
output_dir = './segmentedImages/'

# Display the results
cv2.imshow('Original Image', img)
cv2.imshow('Sharpen Filtered Image', sharpen_array)
for i, segment in enumerate(segments):
    segment_filename = f'segment_{i}.bmp'
    segment_path = os.path.join(output_dir, segment_filename)
    cv2.imwrite(segment_path, segment)
    cv2.imshow(f'Segment {i}', segment)
cv2.waitKey(0)
cv2.destroyAllWindows()



