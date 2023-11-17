import SimpleITK as sitk
import matplotlib.pyplot as plt

# Load the medical image
image = sitk.ReadImage("../images/ctisus/ctisusTiff/adrenal_1-01.tiff")

# Convert the image to a supported pixel type
image = sitk.Cast(image, sitk.sitkFloat32)

# Perform anisotropic filtering
smoothed = sitk.CurvatureAnisotropicDiffusion(image, timeStep=0.05, conductanceParameter=1.0)

# Plot the original and filtered images
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(sitk.GetArrayFromImage(image), cmap='gray')
axs[0].set_title('Original')
axs[1].imshow(sitk.GetArrayFromImage(smoothed), cmap='gray')
axs[1].set_title('Smoothed with Ansiotropic Filter')
plt.show()
