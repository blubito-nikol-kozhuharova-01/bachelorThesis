import cv2
import numpy as np
from calculateArea import calculate_area
from calculatePerimeter import calculate_perimeter

def calculateDiceCoefficient(image1, image2):
    segment = image1
    image1 = cv2.imread(image1, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(image2, cv2.IMREAD_GRAYSCALE)

    if image1 is None or image2 is None:
        print('Failed to load segmented binary images.')
    else:
        # Threshold the images to obtain binary masks
        _, binary_image1 = cv2.threshold(image1, 127, 255, cv2.THRESH_BINARY)
        _, binary_image2 = cv2.threshold(image2, 127, 255, cv2.THRESH_BINARY)

        # Calculate the intersection
        intersection = np.logical_and(binary_image1, binary_image2)

        # Calculate the sum of pixels in each image
        sum_image1 = np.count_nonzero(binary_image1)
        sum_image2 = np.count_nonzero(binary_image2)

        # Calculate the Dice coefficient
        dice_coefficient = (2 * np.sum(intersection)) / (sum_image1 + sum_image2)

        segment_area = round(calculate_area(segment), 1)
        segment_perimeter = round(calculate_perimeter(segment), 1)

        # Print the Dice coefficient
        print('Dice Coefficient:', dice_coefficient)
        # print('Sum of pixels in image 1', sum_image1)
        # print('Sum of pixels in image 2', sum_image2)
        print('Area of segment: ', segment_area)
        print('Perimeter of segment: ', segment_perimeter)


        # Display the binary images and the intersection
        cv2.imshow('Binary Image 1', binary_image1)
        cv2.imshow('Binary Image 2', binary_image2)
        cv2.imshow('Intersection', intersection.astype(np.uint8) * 255)  # Convert to uint8 for display
        cv2.waitKey(0)
        cv2.destroyAllWindows()