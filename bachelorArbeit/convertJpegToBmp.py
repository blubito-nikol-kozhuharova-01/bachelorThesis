from PIL import Image

# Open the JPEG image
jpeg_image = Image.open('./images/adrenal-3C-edit.jpg')

# Convert the image to BMP format
bmp_image = jpeg_image.convert('RGB')

# Save the BMP image
bmp_image.save('./images/adrenal-3C-edit.bmp')
