# import cv2
# from PIL import Image
# import numpy as np
# from plotImages import plotImage
# from scipy.ndimage import median_filter

######## Lookup table with median filter

# # Load the image
# img = Image.open('./images/ctisus/ctisusTiff/adrenal_1-01.tiff')
#
# # Create a LUT to increase the image brightness by 50%
# lut = np.arange(256) + 0.2 * 255
#
# # Apply the LUT to the image
# result = img.point(lut)
#
# # Apply the median filter
# size = 3
# img_filtered = median_filter(result, size=size)
#
# # Display the original and median-filtered images
# plotImage(img, img_filtered)




#3 Load the image
# img = Image.open('./images/ctisus/ctisusTiff/adrenal_1-01.tiff')
#
# # Apply the median filter
# size = 3
# img_filtered = median_filter(img, size=size)
#
# # Create a LUT to increase the image brightness by 50%
# lut = np.arange(256) + 0.2 * 255
#
# # Apply the LUT to the image
# pil_img_filtered = Image.fromarray(img_filtered)
# result = pil_img_filtered.point(lut)
#
# plotImage(img, result)










# k-means clustering + region growing

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans
# from skimage import io, segmentation, color
#
# # Load the image
# img = cv2.imread('./images/ctisus/ctisusBmp/adrenal_1-01.bmp')
#
# # Convert the image from BGR to RGB format
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#
# # Reshape the image to a 2D array of pixels
# pixels = img.reshape((-1, 3))
#
# # Specify the number of clusters
# # k = 6
# k = 5
#
# # Initialize the k-means algorithm
# kmeans = KMeans(n_clusters=k)
#
# # Fit the algorithm to the pixel data
# kmeans.fit(pixels)
#
# # Get the labels for each pixel
# labels = kmeans.labels_
#
# # Reshape the labels to the original image shape
# labels = labels.reshape(img.shape[:2])
#
#
#
#
# # Define the seed point for region growing
# seed_point = (100, 100)
#
# # Define the threshold for region growing
# tolerance = 0.1
#
#
# # Segment the image using region growing
# segment = segmentation.flood(labels, seed_point, tolerance=tolerance)
#
# # Visualize the segmentation
# out = color.label2rgb(segment, labels, kind='avg')
#
#
#
# # Visualize the segmented image
# plt.imshow(out)
# plt.show()




########## works

import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from skimage import io, segmentation, color
# Load the image
img = io.imread('./images/ctisus/ctisusBmp/adrenal_1-01.bmp')

# Convert the image to grayscale
gray = color.rgb2gray(img)

# Reshape the grayscale image to a 1D array of pixels
pixels = gray.reshape((-1, 1))

# Specify the number of clusters
k = 5

# Initialize the k-means algorithm
kmeans = KMeans(n_clusters=k)

# Fit the algorithm to the pixel data
kmeans.fit(pixels)

# Get the labels for each pixel
labels = kmeans.labels_

# Reshape the labels to the original image shape
labels = labels.reshape(gray.shape)

# Define the seed point for region growing
seed_point = (200, 250)

# Define the tolerance for region growing
tolerance = 0.1

# Segment the image using region growing
segment = segmentation.flood(labels, seed_point, tolerance=tolerance)

# Visualize the segmentation
out = color.label2rgb(segment, img, kind='avg')

# Display the result
io.imshow(out)
io.show()

#######################################33