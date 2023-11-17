import cv2
import numpy as np
from plotImages import plotImage

def plot_contrast_strech_image(image_path):

    # Load the MRI tumor image
    img = cv2.imread(image_path, 0)

    # Calculate the minimum and maximum pixel intensity values
    min_value = np.min(img)
    max_value = np.max(img)

    # Define the new range of pixel intensity values
    new_min_value = 0
    new_max_value = 255

    # Apply contrast stretching to each pixel in the image
    stretched_img = ((img - min_value) / (max_value - min_value)) * (new_max_value - new_min_value) + new_min_value

    # Convert the pixel values to integers between 0 and 255
    stretched_img = stretched_img.astype(np.uint8)

    # Display the original and contrast-stretched images
    plotImage(img, stretched_img)


plot_contrast_strech_image('../images/ctisus/ctisusTiff/adrenal_1-01.tiff')