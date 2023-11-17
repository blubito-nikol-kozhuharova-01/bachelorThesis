# # from skimage import io, morphology, util
# # import matplotlib.pyplot as plt
# #
# # # Load the input image
# # image = io.imread('../images/ctisus/ctisusTiff/adrenal_1-01.tiff', as_gray=True)
# #
# # # Define the structuring element
# # selem = morphology.disk(20)
# #
# # # Perform top hat filtering
# # filtered = morphology.black_tophat(image, selem)
# #
# # # Plot the input and filtered images
# # fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
# # ax = axes.ravel()
# #
# # ax[0].imshow(image, cmap=plt.cm.gray)
# # ax[0].set_title('Input image')
# #
# # ax[1].imshow(filtered, cmap=plt.cm.gray)
# # ax[1].set_title('Filtered image')
# #
# # plt.show()
#
# ################################
#
#
# import cv2
# import numpy as np
# from plotImages import plotImage
#
# # Load the image in grayscale mode
# img = cv2.imread('../images/ctisus/ctisusTiff/adrenal_1-01.tiff', cv2.IMREAD_GRAYSCALE)
#
# # Define the kernel size
# kernel_size = (70, 70)
#
# # Create a kernel of ones with the specified size
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
#
# # Apply the Top Hat filter
# tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
#
# # Display the result
# plotImage(img, tophat)
#


import cv2
import numpy as np
from plotImages import plotImage

# Load the image in grayscale mode
img = cv2.imread('../images/ctisus/ctisusBmp/adrenal_1-01.bmp', cv2.IMREAD_GRAYSCALE)

# Define the kernel size and shape
kernel_size = 70
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))

# Apply the Top Hat filter
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# Display the result
plotImage(img, tophat)
