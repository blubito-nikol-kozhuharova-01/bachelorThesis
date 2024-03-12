from skimage import io, exposure
import cv2
import numpy as np

def apply_contrast_stretching(img):
    p2, p98 = np.percentile(img, (80, 99))
    stretched_image = exposure.rescale_intensity(img, in_range=(p2, p98))

    cv2.imshow('Contrast enhanced image', stretched_image)

    # Wait for key press
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return stretched_image
