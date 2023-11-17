import cv2
import numpy as np
from scipy.ndimage import gaussian_filter
from PIL import Image
from plotImages import plotImage

# Load the image
img = np.array(Image.open("../images/ctisus/ctisusTiff/adrenal_1-01.tiff"))

# Apply the Gaussian filter
sigma = 0.5
img_filtered = gaussian_filter(img, sigma=sigma)

# Display the original and gaussian-filtered images
plotImage(img, img_filtered)

