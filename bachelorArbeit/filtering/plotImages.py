import matplotlib.pyplot as plt

def plotImage(originalImage, processedImage):
    plt.subplot(121), plt.imshow(originalImage, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(processedImage, cmap='gray')
    plt.title('Processed Image'), plt.xticks([]), plt.yticks([])
    plt.show()