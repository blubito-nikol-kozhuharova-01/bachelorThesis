from PIL import Image

def convertJpegToBmpFunc(image_path):
    # Open the JPEG image
    jpeg_image = Image.open(image_path)

    # Convert the image to BMP format
    bmp_image = jpeg_image.convert('RGB')

    # Save the BMP image
    # bmp_image.save('./petCTimagesBMP/adrenal-1-01.bmp')
    # bmp_image.save('./petCTimagesBMP/adrenal-1-02.bmp')
    # bmp_image.save('./petCTimagesBMP/adrenal-1-03.bmp')
    # bmp_image.save('./petCTimagesBMP/adrenal-1-05.bmp')
    # bmp_image.save('./petCTimagesBMP/adrenal-1-06.bmp')
    # bmp_image.save('./petCTimagesBMP/adrenal-3C.bmp')
    # bmp_image.save('./petCTimagesBMP/adrenal-3D.bmp')
    # bmp_image.save('./petCTimagesBMP/adrenal-5B.bmp')
    # bmp_image.save('./petCTimagesBMP/adrenal-7C.bmp')
    # bmp_image.save('./petCTimagesBMP/adrenal-9B.bmp')
    # bmp_image.save('./petCTimagesBMP/duodenum-1-03.bmp')
    # bmp_image.save('./petCTimagesBMP/duodenum-1-04.bmp')
    # bmp_image.save('./petCTimagesBMP/duodenum-1-05.bmp')
    bmp_image.save('./petCTimagesBMP/liver-1-01.bmp')
    # bmp_image.save('./petCTimagesBMP/liver-1-02.bmp')

# convertJpegToBmpFunc('./petCTimages/adrenal-1-01.jpg')
# convertJpegToBmpFunc('./petCTimages/adrenal-1-02.jpg')
# convertJpegToBmpFunc('./petCTimages/adrenal-1-03.jpg')
# convertJpegToBmpFunc('./petCTimages/adrenal-1-05.jpeg')
# convertJpegToBmpFunc('./petCTimages/adrenal-1-06.jpg')
# convertJpegToBmpFunc('./petCTimages/adrenal-3C.gif')
# convertJpegToBmpFunc('./petCTimages/adrenal-3D.gif')
# convertJpegToBmpFunc('./petCTimages/adrenal-5B.gif')
# convertJpegToBmpFunc('./petCTimages/adrenal-7C.gif')
# convertJpegToBmpFunc('./petCTimages/adrenal-9B.gif')
# convertJpegToBmpFunc('./petCTimages/duodenum-1-03.jpg')
# convertJpegToBmpFunc('./petCTimages/duodenum-1-04.jpg')
convertJpegToBmpFunc('./petCTimages/liver-1-01.jpg')
# convertJpegToBmpFunc('./petCTimages/liver-1-02.jpg')


