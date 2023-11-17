import cv2
import numpy as np

def calculate_area(segmented_image_path):

    # Load the segmented image
    segmented_image = cv2.imread(segmented_image_path)

    # Convert the segmented image to grayscale
    gray = cv2.cvtColor(segmented_image, cv2.COLOR_BGR2GRAY)

    # Find contours in the grayscale image
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Calculate the area of the largest contour
    if len(contours) > 0:
        contour = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(contour)
        return area
    else:
        return 0.0