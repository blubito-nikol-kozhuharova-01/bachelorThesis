## canny for the whole image
# import cv2
# import numpy as np
# from sklearn.cluster import KMeans
#
# # Load the image
# image = cv2.imread('./images/ctisus/ctisusBmp/adrenal_1-01.bmp')
#
# # Convert the image to a flattened array
# X = image.reshape(-1, 3)
#
# # Perform k-means clustering
# kmeans = KMeans(n_clusters=5, random_state=0).fit(X)
#
# # Assign each pixel to the cluster with the closest centroid
# labels = kmeans.predict(X)
#
# # Create a segmentation map
# segmentation_map = labels.reshape(image.shape[:2])
#
# # Apply a binary threshold to the segmentation map
# _, thresholded_map = cv2.threshold(segmentation_map.astype(np.uint8), 2, 255, cv2.THRESH_BINARY)
#
# # Perform Canny edge detection on the thresholded map
# edges = cv2.Canny(thresholded_map, 100, 200)
#
# # Display the original image, thresholded map, and edges
# cv2.imshow('Original Image', image)
# cv2.imshow('Thresholded Map', thresholded_map)
# cv2.imshow('Edges', edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



## segment after canny edge
import cv2
import numpy as np

# Load the medical image
img = cv2.imread('./images/1-01-Copy.bmp', 0)

# Apply a Gaussian filter to smooth the image and reduce noise
img = cv2.GaussianBlur(img, (5, 5), 0)

# Apply the Canny edge detector to identify the edges of the tumor
edges = cv2.Canny(img, 100, 200)

# Use morphological operations to clean up the edges and fill in gaps
kernel = np.ones((5,5), np.uint8)
dilation = cv2.dilate(edges, kernel, iterations=1)
erosion = cv2.erode(dilation, kernel, iterations=1)

# Identify the enclosed area within the edges
contours, hierarchy = cv2.findContours(erosion, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
largest_contour = max(contours, key=cv2.contourArea)

# Fill in the enclosed area to segment the tumor
mask = np.zeros_like(img)
cv2.fillPoly(mask, [largest_contour], 255)

# Display the segmented tumor
segmented = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('Segmented Tumor', segmented)
cv2.waitKey(0)
cv2.destroyAllWindows()