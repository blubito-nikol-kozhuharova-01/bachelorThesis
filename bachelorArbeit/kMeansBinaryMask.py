import cv2
import numpy as np
from sklearn.cluster import KMeans

# Load the image
image = cv2.imread('./images/ctisus/ctisusBmp/adrenal_1-01.bmp')

# Convert the image to a flattened array
X = image.reshape(-1, 3)

# Perform k-means clustering
kmeans = KMeans(n_clusters=6, random_state=0).fit(X)

# Assign each pixel to the cluster with the closest centroid
labels = kmeans.predict(X)

# Create a segmentation map
segmentation_map = labels.reshape(image.shape[:2])

# Create binary masks for each cluster
masks = []
for i in range(kmeans.n_clusters):
    mask = np.zeros_like(segmentation_map)
    mask[segmentation_map == i] = 1
    masks.append(mask)

# Extract the segmented images for each cluster
segmented_images = []
for mask in masks:
    segmented_image = cv2.bitwise_and(image, image, mask=mask.astype('uint8'))
    segmented_images.append(segmented_image)

# Display the segmented images
for i, segmented_image in enumerate(segmented_images):
    cv2.imshow(f'Segmented Image {i}', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
