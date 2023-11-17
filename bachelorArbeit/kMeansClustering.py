import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load the image
img = cv2.imread('./images/ctisus/ctisusBmp/adrenal_1-01.bmp')

# Convert the image from BGR to RGB format
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Reshape the image to a 2D array of pixels
pixels = img.reshape((-1, 3))

# Specify the number of clusters
# k = 4
k = 6

# Initialize the k-means algorithm
kmeans = KMeans(n_clusters=k)

# Fit the algorithm to the pixel data
kmeans.fit(pixels)

# Get the labels for each pixel
labels = kmeans.labels_

# Reshape the labels to the original image shape
labels = labels.reshape(img.shape[:2])

# Visualize the segmented image
plt.imshow(labels)
plt.show()

