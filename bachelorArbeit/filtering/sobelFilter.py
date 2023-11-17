import cv2
import numpy as np

# Load the image
img = cv2.imread('../images/ctisus/ctisusBmp/adrenal_1-01.bmp', cv2.IMREAD_GRAYSCALE)

# Apply the Sobel filter
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel = np.sqrt(np.square(sobelx) + np.square(sobely))

# Normalize the output
sobel = cv2.normalize(sobel, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Display the result
cv2.imshow('Sobel Edge Detection', sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()