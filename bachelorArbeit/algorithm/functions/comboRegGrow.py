import cv2
import numpy as np
import os
from scipy.ndimage import median_filter
from skimage import io, exposure
from PIL import Image, ImageOps, ImageTk, ImageFilter
from medianFilterFunc import apply_median_filter, apply_sharpen_filter
from regionGrowingFunc import perform_region_growing
from calculatePerimeter import calculate_perimeter
from calculateArea import calculate_area

# Load the image
# originalImage = cv2.imread("../../images/ctisus/ctisusBmp/adrenal_1-01.bmp")
# originalImage = cv2.imread("./petCTimagesBMP/adrenal-1-02.bmp")
# originalImage = cv2.imread("./petCTimagesBMP/adrenal-1-03.bmp")
originalImage = cv2.imread("./petCTimagesBMP/adrenal-1-05.bmp")
# originalImage = cv2.imread("./petCTimagesBMP/adrenal-1-06.bmp")
# originalImage = cv2.imread("./petCTimagesBMP/adrenal-3C.bmp")
# originalImage = cv2.imread("./petCTimagesBMP/adrenal-3D.bmp")
# originalImage = cv2.imread("./petCTimagesBMP/adrenal-5B.bmp")
# originalImage = cv2.imread("./petCTimagesBMP/adrenal-7C.bmp")
# originalImage = cv2.imread("./petCTimagesBMP/adrenal-9B.bmp")
# originalImage = cv2.imread("./petCTimagesBMP/duodenum-1-03.bmp")
# originalImage = cv2.imread("./petCTimagesBMP/duodenum-1-04.bmp")
# originalImage = cv2.imread("./petCTimagesBMP/duodenum-1-05.bmp")
# originalImage = cv2.imread("./petCTimagesBMP/liver-1-01.bmp")
# originalImage = cv2.imread("./petCTimagesBMP/liver-1-02.bmp")

# Apply the median filter
medianFilteredImage = apply_median_filter(originalImage, 7)

# Apply the sharpen filter
sharpenFilteredImage = apply_sharpen_filter(medianFilteredImage)
sharpenFilteredImageArr = np.array(sharpenFilteredImage)

grayImage = cv2.cvtColor(sharpenFilteredImageArr, cv2.COLOR_BGR2GRAY)
# sharpenFilteredGrayscaleImageArr = np.array(grayImage)

# Apply region growing
segment = perform_region_growing(grayImage)

# Directory to save the segmented image
# cv2.imwrite('./segmentedImages/regGrowingSegment.bmp', segment)
cv2.imshow('Region Growing Segment', segment)

# Display the results
cv2.imshow('Original Image', originalImage)
cv2.imshow('Filtered Image', sharpenFilteredImageArr)

# Wait for key press
cv2.waitKey(0)
cv2.destroyAllWindows()

regionOfInterest = './segmentedImages/regGrowingSegment.bmp'
perimeter = calculate_perimeter(regionOfInterest)
print('Perimeter:', perimeter)

area = calculate_area(regionOfInterest)
print('Area:', area)
