import cv2
import numpy as np

# Global variables
drawing = False
ix, iy = -1, -1
mask = None

# Function to handle mouse events
def mouse_callback(event, x, y, flags, param):
    global drawing, ix, iy, mask

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(mask, (ix, iy), (x, y), (255, 255, 255), 2)
            ix, iy = x, y

# Load the image
image = cv2.imread('../images/ctisus/ctisusBmp/adrenal_1-01.bmp')

# Create a mask with zeros (black) of the same size and data type as the image
mask = np.zeros_like(image, dtype=np.uint8)

# Create a window and bind the mouse callback function
cv2.namedWindow('Select Segment')
cv2.setMouseCallback('Select Segment', mouse_callback)

while True:
    # Display the image with the mask
    result = cv2.addWeighted(image, 0.7, np.where(mask, (0, 255, 0), 0).astype(np.uint8), 0.3, 0)
    cv2.imshow('Select Segment', result)

    # Exit loop if 'Esc' key is pressed
    if cv2.waitKey(1) == 27:
        break

# Convert the mask to grayscale
grayscale_mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

# Apply thresholding to create a binary image
_, binary_segment = cv2.threshold(grayscale_mask, 1, 255, cv2.THRESH_BINARY)

# Save the binary segment as an image
# cv2.imwrite('../images/ctisus/ctisusBmp/adrenal_1-01_selected_binary1.bmp', binary_segment)
cv2.imwrite('../images/ctisus/ctisusBmp/adrenal_1-01_selected_binary3.bmp', binary_segment)

print('Segment saved')

# Destroy all windows
cv2.destroyAllWindows()
