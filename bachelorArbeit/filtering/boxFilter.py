import cv2
from plotImages import plotImage

# Load the image
image = cv2.imread("../images/ctisus/ctisusTiff/adrenal_1-01.tiff")

# Apply a box filter with a kernel size of 3x3
filtered_image = cv2.blur(image, (3, 3))

# Display the original and filtered images
plotImage(image, filtered_image)

