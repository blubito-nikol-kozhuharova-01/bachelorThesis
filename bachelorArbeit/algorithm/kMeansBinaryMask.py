# import cv2
# import numpy as np
# from sklearn.cluster import KMeans
#
# # Load the image
# image = cv2.imread('../images/ctisus/ctisusBmp/adrenal_1-01.bmp')
#
# # Convert the image to a flattened array
# X = image.reshape(-1, 3)
#
# # Perform k-means clustering
# kmeans = KMeans(n_clusters=6, random_state=0).fit(X)
#
# # Assign each pixel to the cluster with the closest centroid
# labels = kmeans.predict(X)
#
# # Create a segmentation map
# segmentation_map = labels.reshape(image.shape[:2])
#
# # Create binary masks for each cluster
# masks = []
# for i in range(kmeans.n_clusters):
#     mask = np.zeros_like(segmentation_map)
#     mask[segmentation_map == i] = 1
#     masks.append(mask)
#
# # Extract the segmented images for each cluster
# segmented_images = []
# for mask in masks:
#     segmented_image = cv2.bitwise_and(image, image, mask=mask.astype('uint8'))
#     segmented_images.append(segmented_image)
#
# # Display the segmented images
# for i, segmented_image in enumerate(segmented_images):
#     cv2.imshow(f'Segmented Image {i}', segmented_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
import numpy as np

# Load the image and convert it to grayscale
image = cv2.imread('../images/ctisus/ctisusBmp/adrenal_1-01.bmp')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



# Define the number of clusters
num_clusters = 6
# Reshape the image to a 2D array of pixels and convert it to float32 type
pixel_values = gray.reshape((-1, 1)).astype(np.float32)

# Perform k-means clustering
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
flags = cv2.KMEANS_RANDOM_CENTERS
compactness, labels, centers = cv2.kmeans(pixel_values, num_clusters, None, criteria, 10, flags)


# Reshape the labels to the shape of the original image
segmented = labels.reshape(gray.shape)

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
for i, segment in enumerate(segments):
    cv2.imshow(f'Segment {i}', segment)
cv2.waitKey(0)
cv2.destroyAllWindows()



# In the code, the mask is created as a numpy array of zeros, with the same shape as the segmented image. Then, for each cluster, the pixels in the segmented image that belong to that cluster are set to 255 in the corresponding mask, while the pixels that do not belong to that cluster remain zero.
#
# The mask is used to extract the segment for each cluster from the original image using the cv2.bitwise_and function. This function performs a bitwise AND operation between the mask and the original image. Pixels in the original image that correspond to zero values in the mask are set to zero in the output image, while pixels that correspond to non-zero values in the mask retain their original values.
#
# Overall, the mask is used to isolate the pixels that belong to a particular cluster, while ignoring the pixels that belong to other clusters.

