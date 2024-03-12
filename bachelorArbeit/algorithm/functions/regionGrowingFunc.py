import cv2
import numpy as np

# Returns a list of 8 neighboring pixels of a given pixel (x, y)
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

def region_growing(img, seed):
    list = []

    # Initialize an output image with the same shape as the input image
    outimg = np.zeros_like(img)
    list.append((seed[0], seed[1]))

    # Processed list to keep track of visited pixels.
    processed = []

    # Continue loop until the list is empty
    while (len(list) > 0):
        pix = list[0]
        outimg[pix[0], pix[1]] = 255

        # Iterate through 8 neighboring pixels of the current pixel
        for coord in get8n(pix[0], pix[1], img.shape):

            # Check if pixel is part of the region
            if (img[coord[0], coord[1]] != 0):
                outimg[coord[0], coord[1]] = 255

                # Check if the pixel has been processed before
                if not coord in processed:
                    list.append(coord)
                processed.append(coord)
        list.pop(0)

        # Show current progress
        cv2.imshow("progress", outimg)
        cv2.waitKey(1)
    return outimg

def perform_region_growing(image):
    clicks = []

    # Pixels with intensity values greater than or equal to 150 are considered as part of the region of interest
    ret, img = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)
    cv2.namedWindow('Input')

    # Mouse callback function to capture seed point
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
