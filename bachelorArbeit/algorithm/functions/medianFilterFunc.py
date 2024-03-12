import cv2
import numpy as np
from PIL import Image, ImageFilter

def apply_median_filter(img, ksize):
    img = cv2.medianBlur(img, ksize)

    cv2.imshow('Median filtered image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img

def apply_sharpen_filter(image):
    pil_img = Image.fromarray(image)

    # Apply the sharpen filter
    sharpen = pil_img.filter(ImageFilter.SHARPEN)
    sharpen = np.array(sharpen)

    cv2.imshow('Sharpen filtered image', sharpen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return sharpen
