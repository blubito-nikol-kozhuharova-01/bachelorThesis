import cv2
import numpy as np

def kMeans_segment_image(image, num_clusters):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Reshape the image to a 2D array of pixels and convert it to float32 type
    #This line reshapes the grayscale image into a 2D array of pixels by using the reshape() function. The -1 argument in the reshape function means that the number of rows is inferred from the given dimensions while keeping a single column. The resulting array is then converted to the np.float32 data type, which is required for subsequent calculations.
    pixel_values = gray.reshape((-1, 1)).astype(np.float32)

    # Perform k-means clustering
    # These lines perform k-means clustering on the pixel values of the grayscale image using the cv2.kmeans() function. The criteria parameter specifies the termination criteria for the algorithm, flags determines the method for initializing cluster centers, and the kmeans() function returns the compactness (the sum of squared distances from each point to its corresponding center), the labels (assigned cluster labels for each pixel), and the cluster centers.
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    flags = cv2.KMEANS_RANDOM_CENTERS
    compactness, labels, centers = cv2.kmeans(pixel_values, num_clusters, None, criteria, 10, flags)

    # Reshape the labels to the shape of the original image
    segmented = labels.reshape(gray.shape)

    # Create masks for each cluster
    # These lines create a binary mask for each cluster. The masks list is initialized, and then a loop iterates over each cluster label. For each cluster, a new mask is created using np.zeros_like() to generate a mask with the same shape as the segmented array. Pixels that belong to the current cluster are set to 255 (white) in the mask, while other pixels remain 0 (black). Each mask is then appended to the masks list.
    masks = []
    for i in range(num_clusters):
        mask = np.zeros_like(segmented)
        mask[segmented == i] = 255
        masks.append(mask)

    # Apply each mask to the original image to extract segments
    # These lines extract the segmented regions from the original input image using the created masks. A loop iterates over each mask, and the cv2.bitwise_and() function is used to apply each mask to the input image. This operation retains only the pixels in the image where the mask is non-zero (white). The resulting segments are then appended to the segments list.
    segments = []
    for mask in masks:
        segment = cv2.bitwise_and(image, image, mask=mask.astype('uint8'))
        segments.append(segment)

    # Return the segments
    return segments


# In summary, this code performs k-means clustering on an input image, creates binary masks for each cluster, and extracts the segmented regions from the original image based on these masks. The resulting segments are returned as a list.