import cv2
import numpy as np

def calculateDiceCoefficient(image1, image2):
    image1 = cv2.imread(image1, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(image2, cv2.IMREAD_GRAYSCALE)

    if image1 is None or image2 is None:
        print('Failed to load segmented images.')
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

        # Find contours of tumors
        contours, _ = cv2.findContours(image1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Iterate through each tumor
        for i, contour in enumerate(contours):
            # Calculate area
            area = cv2.contourArea(contour)

            # Calculate perimeter
            perimeter = cv2.arcLength(contour, True)

            print(f"Tumor {i + 1}: Area = {area}, Perimeter = {perimeter}")

        print('Dice Coefficient:', dice_coefficient)

        # Display the binary images and the intersection
        cv2.imshow('Binary Image 1', binary_image1)
        cv2.imshow('Binary Image 2', binary_image2)
        cv2.imshow('Intersection', intersection.astype(np.uint8) * 255)  # Convert to uint8 for display
        cv2.waitKey(0)
        cv2.destroyAllWindows()