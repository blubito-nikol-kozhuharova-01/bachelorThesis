from PIL import Image
import numpy as np
from plotImages import plotImage

# Load the image
image = Image.open('../images/ctisus/ctisusTiff/adrenal_1-01.tiff')

# Create a LUT to increase the image brightness by 50%
lut = np.arange(256) + 0.2 * 255

# Apply the LUT to the image
result = image.point(lut)

plotImage(image, result)

