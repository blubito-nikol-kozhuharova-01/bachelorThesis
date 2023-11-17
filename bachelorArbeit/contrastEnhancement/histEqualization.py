import cv2
import matplotlib.pyplot as plt
from plotImages import plotImage

def plot_histogram_equalized_image(image_path):
    # read the image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # perform histogram equalization
    equ = cv2.equalizeHist(img)

    # plt.show()
    plotImage(img, equ)

plot_histogram_equalized_image('../images/ctisus/ctisusTiff/adrenal_1-01.tiff')

#In this example, we use the OpenCV library to read the input image
# and perform histogram equalization using the cv2.equalizeHist() function.
# We then use Matplotlib to display the original and equalized images side-by-side.
# The cmap='gray' argument specifies that the images should be displayed in grayscale.
