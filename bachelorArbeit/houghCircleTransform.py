#Hough circle transform
import cv2
import numpy as np

# Load the input image
img = cv2.imread('./images/ctisus/ctisusBmp/adrenal_1-01.bmp', 0)

# Apply the Canny edge detector to the input image
edges = cv2.Canny(img, 100, 200)

# Apply the Hough Circle Transform to the edge image
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 20,
                           param1=50, param2=30, minRadius=0, maxRadius=0)

# Convert the (x, y) coordinates and radius of the circles to integers
circles = np.round(circles[0, :]).astype(int)

# Draw the detected circles on the input image
for (x, y, r) in circles:
    cv2.circle(img, (x, y), r, (0, 255, 0), 2)

# Display the input image with detected circles
cv2.imshow('Detected Circles', img)
cv2.waitKey(0)
cv2.destroyAllWindows()