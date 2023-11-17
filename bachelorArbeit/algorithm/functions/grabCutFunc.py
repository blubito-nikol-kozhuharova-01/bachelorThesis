import cv2
import numpy as np
import matplotlib.pyplot as plt

def grabcut_segmentation(image):
    # Create a mask initialized with zeros
    mask = np.zeros(image.shape[:2], np.uint8)

    # Create temporary arrays for foreground and background models
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)

    # Define the rectangular region of interest (ROI) enclosing the tumor
    # Adjust the values according to your specific image and tumor location
    x = 180
    y = 220
    width = 100
    height = 90
    rect = (x, y, width, height)

    # Apply GrabCut algorithm to segment the tumor
    cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

    # Create a mask with the probable foreground (GC_PR_FGD or GC_FGD) and definite foreground (GC_FGD) labels
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    # Apply the mask to the original image
    segmented_image = image * mask2[:, :, np.newaxis]

    return segmented_image

# Load the image
image = cv2.imread('../../images/ctisus/ctisusBmp/adrenal_1-01.bmp')

# Perform GrabCut segmentation
segmented_image = grabcut_segmentation(image)

# Display the original image and segmented tumor
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
ax1.set_title('Original Image')
ax1.axis('off')
ax2.imshow(cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB))
ax2.set_title('Segmented Tumor')
ax2.axis('off')
cv2.imwrite('./segmentedImages/grabcutSegment.bmp', segmented_image)
plt.show()