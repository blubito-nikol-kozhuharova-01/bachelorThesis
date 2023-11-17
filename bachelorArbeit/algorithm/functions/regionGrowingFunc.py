import cv2
import numpy as np

#This function get8n(x, y, shape) returns a list of 8 neighboring pixels of a given pixel (x, y) within the bounds of the image with the specified shape. It handles the boundary cases to ensure that the neighboring pixels are within the image dimensions.
def get8n(x, y, shape):
    out = []
    maxx = shape[1] - 1
    maxy = shape[0] - 1

    # top left
    outx = min(max(x - 1, 0), maxx)
    outy = min(max(y - 1, 0), maxy)
    out.append((outx, outy))

    # top center
    outx = x
    outy = min(max(y - 1, 0), maxy)
    out.append((outx, outy))

    # top right
    outx = min(max(x + 1, 0), maxx)
    outy = min(max(y - 1, 0), maxy)
    out.append((outx, outy))

    # left
    outx = min(max(x - 1, 0), maxx)
    outy = y
    out.append((outx, outy))

    # right
    outx = min(max(x + 1, 0), maxx)
    outy = y
    out.append((outx, outy))

    # bottom left
    outx = min(max(x - 1, 0), maxx)
    outy = min(max(y + 1, 0), maxy)
    out.append((outx, outy))

    # bottom center
    outx = x
    outy = min(max(y + 1, 0), maxy)
    out.append((outx, outy))

    # bottom right
    outx = min(max(x + 1, 0), maxx)
    outy = min(max(y + 1, 0), maxy)
    out.append((outx, outy))

    return out

# This function region_growing(img, seed) implements the region growing algorithm. It takes an input image img and a seed pixel (seed[0], seed[1]) as parameters. The algorithm starts with an empty list list and initializes an output image outimg with the same shape as the input image. The seed pixel is added to the list, and a processed list is created to keep track of visited pixels.
#
# The while loop continues until the list is empty. Within the loop, the first pixel in the list is selected (pix = list[0]) and set to 255 (white) in the output image. The neighboring pixels of pix are obtained using the get8n() function, and if a neighboring pixel's value in the input image is non-zero, it is also set to 255 in the output image. The neighboring pixel is then checked if it has already been processed or not. If not, it is appended to the list and marked as processed.
#
# The first pixel in the list is removed (list.pop(0)), and the current progress of the region growing is displayed using cv2.imshow() and cv2.waitKey() functions.
#
# The function returns the resulting output image outimg.
def region_growing(img, seed):
    list = []
    outimg = np.zeros_like(img)
    list.append((seed[0], seed[1]))
    processed = []
    while (len(list) > 0):
        pix = list[0]
        outimg[pix[0], pix[1]] = 255
        for coord in get8n(pix[0], pix[1], img.shape):
            if (img[coord[0], coord[1]] != 0):
                outimg[coord[0], coord[1]] = 255
                if not coord in processed:
                    list.append(coord)
                processed.append(coord)
        list.pop(0)
        cv2.imshow("progress", outimg)
        cv2.waitKey(1)
    return outimg


# def perform_region_growing(image_path):
def perform_region_growing(image):
    clicks = []
    # image = cv2.imread(image_path, 0)
    ret, img = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)
    cv2.namedWindow('Input')

    def on_mouse(event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            print('Seed: ' + str(x) + ', ' + str(y), img[y, x])
            clicks.append((y, x))

    cv2.setMouseCallback('Input', on_mouse, 0, )
    cv2.imshow('Input', image)
    cv2.waitKey()

    seed = clicks[-1]
    out = region_growing(img, seed)
    cv2.imshow('Region Growing', out)
    cv2.waitKey()
    cv2.destroyAllWindows()

    return out

# source: https://github.com/zjgirl/RegionGrowing-1/blob/master/RegionGrowing.py
