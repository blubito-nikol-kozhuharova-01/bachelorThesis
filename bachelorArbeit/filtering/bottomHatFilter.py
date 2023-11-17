# from skimage import io, morphology, util
# import matplotlib.pyplot as plt
#
# # Load the input image
# image = io.imread('../images/ctisus/ctisusTiff/adrenal_1-01.tiff', as_gray=True)
#
# # Define the structuring element
# selem = morphology.disk(20)
#
# # Perform bottom hat filtering
# filtered = morphology.white_tophat(image, selem)
#
# # Plot the input and filtered images
# fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
# ax = axes.ravel()
#
# ax[0].imshow(image, cmap=plt.cm.gray)
# ax[0].set_title('Input image')
#
# ax[1].imshow(filtered, cmap=plt.cm.gray)
# ax[1].set_title('Filtered image')
#
# plt.show()



#########################################3



import cv2
from plotImages import plotImage

# Defining the kernel to be used in Top-Hat
filterSize = (50, 50)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,
                                   filterSize)

# Reading the image named 'input.jpg'
input_image = cv2.imread("../images/ctisus/ctisusTiff/adrenal_1-01.tiff")
input_image = cv2.cvtColor(input_image, cv2.COLOR_RGB2GRAY)

# Applying the Black-Hat operation
bottomhat_img = cv2.morphologyEx(input_image,
                              cv2.MORPH_BLACKHAT,
                              kernel)

plotImage(input_image, bottomhat_img)

