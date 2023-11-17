from PIL import Image

# Open the JPEG image
jpeg_image = Image.open('./images/1-01-Copy.jpg')

# Convert the image to BMP format
bmp_image = jpeg_image.convert('RGB')

# Save the BMP image
bmp_image.save('./images/1-01-Copy.bmp')
