import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from skimage import io, segmentation, color
from skimage.segmentation import flood_fill

# Load the image
img = io.imread('./images/ctisus/ctisusBmp/adrenal_1-01.bmp')

# Convert the image to grayscale
gray = color.rgb2gray(img)

# Reshape the grayscale image to a 1D array of pixels
pixels = gray.reshape((-1, 1))

# Specify the number of clusters
# k = 6
k = 5

# Initialize the k-means algorithm
kmeans = KMeans(n_clusters=k)

# Fit the algorithm to the pixel data
kmeans.fit(pixels)

# Get the labels for each pixel
labels = kmeans.labels_

# Reshape the labels to the original image shape
labels = labels.reshape(gray.shape)


# Display the image
fig, ax = plt.subplots()
ax.imshow(labels, cmap=plt.cm.gray)


# Define an event handler function for mouse clicks
def onclick(event):
    # Get the x and y coordinates of the mouse click
    x = int(event.xdata)
    y = int(event.ydata)

    # Use the flood_fill function to segment the image
    segmented_image = flood_fill(labels, (x, y), new_value=255, tolerance=1)

    # Display the segmented image
    ax.imshow(color.label2rgb(segmented_image, image=labels), cmap=plt.cm.gray)
    plt.draw()

# Connect the event handler function to the mouse click event
cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()





# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans
# from skimage import io, segmentation, color
# from skimage.segmentation import flood_fill
#
# # Load the image
# img = io.imread('./images/ctisus/ctisusBmp/adrenal_1-01.bmp')
#
# # Convert the image to grayscale
# gray = color.rgb2gray(img)
#
# # Reshape the grayscale image to a 1D array of pixels
# pixels = gray.reshape((-1, 1))
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
# labels = labels.reshape(gray.shape)
#
#
# # Display the image
# fig, ax = plt.subplots()
# ax.imshow(labels, cmap=plt.cm.gray)
#
#
# # Define an event handler function for mouse clicks
# def onclick(event):
#     # Get the x and y coordinates of the mouse click
#     x = int(event.xdata)
#     y = int(event.ydata)
#
#     # Use the flood_fill function to segment the image
#     segmented_image = flood_fill(labels, (x, y), new_value=255, tolerance=1)
#
#     # Create a mask to only color the segmented region
#     mask = np.zeros_like(segmented_image, dtype=np.uint8)
#     mask[segmented_image == 255] = 255
#
#     # Apply the mask to the original image
#     colored_image = cv2.bitwise_and(img, img, mask=mask)
#
#     # Display the colored image
#     ax.imshow(colored_image)
#     plt.draw()
#
# # Connect the event handler function to the mouse click event
# cid = fig.canvas.mpl_connect('button_press_event', onclick)
#
# plt.show()
