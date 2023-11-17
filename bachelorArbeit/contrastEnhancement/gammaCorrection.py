from skimage import io, exposure
import matplotlib.pyplot as plt
from plotImages import plotImage

# Load a medical image in tif format
img = io.imread('../images/ctisus/ctisusTiff/adrenal_1-01.tiff')

# Perform gamma correction
gamma_corrected = exposure.adjust_gamma(img, gamma=2)
# gamma_corrected = exposure.adjust_gamma(img, gamma=0.5)

plotImage(img, gamma_corrected)