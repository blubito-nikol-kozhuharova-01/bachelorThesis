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
# image = cv2.imread("../images/ctisus/ctisusBmp/adrenal_1-01.bmp")
#
# # Convert the image to grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Apply the median filter
# size = 4
# gray_filtered = median_filter(gray, size=size)
#
# # Apply the sharpen filter
# alpha = 1.7
# beta = 0
# sharpen_filtered = sharpen_filter(gray_filtered, alpha, beta)
#
# # Define the number of clusters
# num_clusters = 7
#
# # Reshape the image to a 2D array of pixels and convert it to float32 type
# pixel_values = sharpen_filtered.reshape((-1, 1)).astype(np.float32)
#
# # Perform k-means clustering
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# flags = cv2.KMEANS_RANDOM_CENTERS
# compactness, labels, centers = cv2.kmeans(pixel_values, num_clusters, None, criteria, 10, flags)
#
#
# # Reshape the labels to the shape of the original image
# segmented = labels.reshape(sharpen_filtered.shape)
#
# # Create masks for each cluster
# masks = []
# for i in range(num_clusters):
#     mask = np.zeros_like(segmented)
#     mask[segmented == i] = 255
#     masks.append(mask)
#
# # Apply each mask to the original image to extract segments
# segments = []
# for mask in masks:
#     segment = cv2.bitwise_and(image, image, mask=mask.astype('uint8'))
#     segments.append(segment)
#
#
# # Display the results
# cv2.imshow('Original Image', image)
# cv2.imshow('Sharpen Filtered Image', sharpen_filtered)
#
# for i, segment in enumerate(segments):
#     cv2.imshow(f'Segment {i}', segment)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
#
#
#
#
#
#
#
#
#

# import cv2
# import numpy as np
#
# def sharpen_filter(img, alpha, beta):
#     kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
#     output = cv2.filter2D(img, -1, alpha * kernel + beta)
#     return output
#
# # Load the image
# image = cv2.imread("../images/ctisus/ctisusBmp/adrenal_1-01.bmp")
#
# # Apply the median filter
# image = cv2.medianBlur(image, ksize=5)
#
# # Apply the sharpen filter
# alpha = 1.7
# beta = 0
# sharpen_filtered = sharpen_filter(image, alpha, beta)
#
# # Split the image into RGB channels
# b, g, r = cv2.split(sharpen_filtered)
#
# # Define the number of clusters
# num_clusters = 5
#
# # Perform k-means clustering for each channel
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# flags = cv2.KMEANS_RANDOM_CENTERS
#
# # Process each channel separately
# channels = [b, g, r]
# segmented_channels = []
#
# for channel in channels:
#     # Reshape the channel to a 2D array of pixels and convert it to float32 type
#     pixel_values = channel.reshape((-1, 1)).astype(np.float32)
#
#     # Perform k-means clustering
#     _, labels, centers = cv2.kmeans(pixel_values, num_clusters, None, criteria, 10, flags)
#
#     # Reshape the labels to the shape of the original channel
#     segmented_channel = labels.reshape(channel.shape)
#     segmented_channels.append(segmented_channel)
#
# # Merge the segmented channels back into an RGB image
# segmented_image = cv2.merge(segmented_channels)
# segmented_image = segmented_image.astype(np.uint8)
#
# # Display the results
# cv2.imshow('Original Image', image)
# cv2.imshow('Sharpen Filtered Image', sharpen_filtered)
# cv2.imshow('Segmented Image', segmented_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()











# import cv2
# import numpy as np
#
# def sharpen_filter(img, alpha, beta):
#     kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
#     output = cv2.filter2D(img, -1, alpha * kernel + beta)
#     return output
#
# # Load the image
# image = cv2.imread("../images/ctisus/ctisusBmp/adrenal_1-01.bmp")
#
# # Apply the median filter
# image = cv2.medianBlur(image, ksize=5)
#
# # Apply the sharpen filter
# alpha = 1.7
# beta = 0
# sharpen_filtered = sharpen_filter(image, alpha, beta)
#
#
# gray = cv2.cvtColor(sharpen_filtered, cv2.COLOR_BGR2GRAY)
#
#
# # Define the number of clusters
# num_clusters = 10
# # Reshape the image to a 2D array of pixels and convert it to float32 type
# pixel_values = gray.reshape((-1, 1)).astype(np.float32)
#
# # Perform k-means clustering
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# flags = cv2.KMEANS_RANDOM_CENTERS
# compactness, labels, centers = cv2.kmeans(pixel_values, num_clusters, None, criteria, 10, flags)
#
#
# # Reshape the labels to the shape of the original image
# segmented = labels.reshape(gray.shape)
#
# # Create masks for each cluster
# masks = []
# for i in range(num_clusters):
#     mask = np.zeros_like(segmented)
#     mask[segmented == i] = 255
#     masks.append(mask)
#
# # Apply each mask to the original image to extract segments
# segments = []
# for mask in masks:
#     segment = cv2.bitwise_and(image, image, mask=mask.astype('uint8'))
#     segments.append(segment)
#
# # Display the results
# cv2.imshow('Original Image', image)
# cv2.imshow('Sharpen Filtered Image', sharpen_filtered)
# # for i, segment in enumerate(segments):
# #     cv2.imshow(f'Segment {i}', segment)
# cv2.waitKey(0)
# cv2.destroyAllWindows()














import cv2
import numpy as np
from scipy.ndimage import median_filter
from PIL import Image
from skimage import io, exposure
import matplotlib.pyplot as plt

def sharpen_filter(img, alpha, beta):
    # Define the kernel for the sharpen filter
    # kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

    # Apply the filter to the input image
    output = cv2.filter2D(img, -1, alpha * kernel + beta)

    return output

# Load the image
image = cv2.imread("../images/ctisus/ctisusBmp/adrenal_1-01.bmp")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply the median filter
size = 4
gray_filtered = median_filter(gray, size=size)

# Apply the sharpen filter
alpha = 1.7
beta = 0
sharpen_filtered = sharpen_filter(gray_filtered, alpha, beta)

# gamma_corrected = exposure.adjust_gamma(sharpen_filtered, gamma=2)

# Define the number of clusters
num_clusters = 6

# Reshape the image to a 2D array of pixels and convert it to float32 type
pixel_values = sharpen_filtered.reshape((-1, 1)).astype(np.float32)

# Perform k-means clustering
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
flags = cv2.KMEANS_RANDOM_CENTERS
compactness, labels, centers = cv2.kmeans(pixel_values, num_clusters, None, criteria, 10, flags)


# Reshape the labels to the shape of the original image
segmented = labels.reshape(sharpen_filtered.shape)

# Create masks for each cluster
masks = []
for i in range(num_clusters):
    mask = np.zeros_like(segmented)
    mask[segmented == i] = 255
    masks.append(mask)

# Apply each mask to the original image to extract segments
segments = []
for mask in masks:
    segment = cv2.bitwise_and(image, image, mask=mask.astype('uint8'))
    segments.append(segment)


# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Sharpen Filtered Image', sharpen_filtered)
cv2.imshow('Contrast Enhanced Image with Gamma Correction', sharpen_filtered)

for i, segment in enumerate(segments):
    cv2.imshow(f'Segment {i}', segment)
cv2.waitKey(0)
cv2.destroyAllWindows()

