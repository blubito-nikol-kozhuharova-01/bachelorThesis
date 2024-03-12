import cv2
import numpy as np

def kMeans_segment_image(image, num_clusters):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Reshape the image to a 2D array of pixels and convert it to float32 type
    pixel_values = gray.reshape((-1, 1)).astype(np.float32)

    # Stop the algorithm if specified accuracy (epsilon) is reached or after the specified number of iterations (max_iter) is excceeded.
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

    # Randomly pick data points as the initial centroids for each cluster
    flags = cv2.KMEANS_RANDOM_CENTERS

    # Perform K-Means clustering on the pixel values with the specified number of clusters, using random initial centers, and return the compactness, cluster labels, and centroids.
    compactness, labels, centers = cv2.kmeans(pixel_values, num_clusters, None, criteria, 10, flags)

    # Reshape the labels to the shape of the original image
    segmented = labels.reshape(gray.shape)

    # Create a binary mask for each cluster
    masks = []
    for i in range(num_clusters):
        # Create a blank mask with the same size and shape as the segmented image
        mask = np.zeros_like(segmented)

        # Set pixels in the mask to white (255) where the corresponding pixel in the segmented image matches the current cluster label
        mask[segmented == i] = 255

        masks.append(mask)

    # Create an empty list to store segmented parts of the image
    segments = []

    # Extract segments from the original color image using masks - loop through each mask representing a cluster
    for mask in masks:
        # Apply bitwise AND operation between the original image and the mask (set all pixels that do not belong to the cluster to zero)
        segment = cv2.bitwise_and(image, image, mask=mask.astype('uint8'))

        segments.append(segment)

    return segments
