from PIL import Image

# Open the JPEG image
jpeg_image = Image.open("./images/ctisus/ctisusJpeg/adrenal_1-07.jpg")

grayscale_image = jpeg_image.convert("L")

# Save the TIFF image
grayscale_image.save("./images/ctisus/ctisusTiff/adrenal_1-07.tiff")
