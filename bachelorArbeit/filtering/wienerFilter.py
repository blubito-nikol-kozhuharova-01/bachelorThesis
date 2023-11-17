import cv2
import numpy as np

def wiener_filter(img, kernel, K):
    # Compute the Fourier transform of the input image and kernel
    img_fft = np.fft.fft2(img)
    kernel_fft = np.fft.fft2(kernel, s=img.shape)

    # Compute the power spectrum of the kernel
    kernel_power = np.abs(kernel_fft) ** 2

    # Apply the Wiener filter
    output_fft = np.conj(kernel_fft) / (kernel_power + K)
    output_fft *= img_fft
    output = np.real(np.fft.ifft2(output_fft))

    # Normalize the output to [0, 255]
    output = cv2.normalize(output, None, alpha=10, beta=200, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    return output


# Read in an image and convert to grayscale
img = cv2.imread('../images/ctisus/ctisusBmp/adrenal_1-01.bmp', cv2.IMREAD_GRAYSCALE)

# Generate a Gaussian kernel
kernel_size = 10
kernel_sigma = 2
kernel = cv2.getGaussianKernel(kernel_size, kernel_sigma)

# Apply the Wiener filter
K = 3
output = wiener_filter(img, kernel, K)

# Display the original and filtered images
cv2.imshow('Original Image', img)
cv2.imshow('Filtered Image', output)
cv2.waitKey(0)
cv2.destroyAllWindows()

