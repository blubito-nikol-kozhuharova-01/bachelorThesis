## doesnt work but could give it a try
# from skimage import io, segmentation, color
# import numpy as np
#
# # Load the image
# img = io.imread('./images/ctisus/ctisusBmp/adrenal_1-01.bmp')
#
# # Define the seed point
# seed = (220, 260)
#
# # Perform region growing
# labels = segmentation.flood_fill(img, seed_point=tuple(np.flip(seed)), new_value=255, connectivity=1)
#
# # Colorize the regions
# label_image = color.label2rgb(labels, image=img)
#
# # Display the results
# io.imshow(label_image)
# io.show()








# import skimage.segmentation as seg
# import skimage.filters as filters
# from skimage import io, color
#
# # Load the image
# img = io.imread("./images/ctisus/ctisusBmp/adrenal_1-01.bmp")
#
# img = color.rgb2gray(img)
#
# # Apply a threshold to the image to create a mask
# mask = img > filters.threshold_otsu(img)
#
# # Use the mask to split the image into regions
# regions = seg.felzenszwalb(img, scale=200, sigma=0.5, min_size=50)
#
# # Display the segmented image
# io.imshow(regions)
# io.show()








############################################################ square i might need for coordinates
# import numpy as np
# import matplotlib.pyplot as plt
# from skimage import io, color, filters, morphology, restoration, segmentation
#
# # Load the medical image
# image = io.imread('./images/ctisus/ctisusBmp/adrenal_1-01.bmp')
#
# # Pre-process the image
# image = color.rgb2gray(image)
# image = restoration.denoise_tv_chambolle(image, weight=0.1)
# image = filters.median(image, selem=morphology.disk(3))
# image = filters.rank.mean(image, selem=morphology.disk(5))
# image = filters.sobel(image)
#
# # Define the ROI
# roi = np.zeros_like(image)
# roi[200:350, 150:350] = 1
#
# # Initialize the Split Operator algorithm
# num_iterations = 100
# reg_param = 0.1
# model = np.zeros_like(image)
# model[roi == 1] = 1
# gamma = np.zeros_like(image)
# f = np.zeros_like(image)
#
# # Apply the Split Operator algorithm
# for i in range(num_iterations):
#     # Update the model
#     model[roi == 1] = (image + gamma)[roi == 1] / (1 + reg_param)
#     # Update the segmentation map
#     f = (image + gamma - model) > 0
#     # Update the Lagrange multiplier
#     gamma += image - model - f
#
# # Extract the segmentation map
# segmentation_map = f.astype(int)
#
# # Post-process the segmentation map
# segmentation_map = morphology.remove_small_objects(segmentation_map, min_size=100)
#
# # Visualize the segmentation map
# fig, ax = plt.subplots()
# ax.imshow(image, cmap='gray')
# ax.imshow(segmentation_map, cmap='jet', alpha=0.3)
# plt.show()












# import numpy as np
# import cv2
# import matplotlib.pyplot as plt
#
# def regrow(full_file, t, s):
#     I = cv2.imread(full_file, cv2.IMREAD_COLOR)
#     I = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)
#     I = I.astype(np.float32) / 255.0
#     cv2.imshow("Input Image", I)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
#     print("Select a seed point of the region you want to segment.")
#     fig, ax = plt.subplots()
#     ax.imshow(I)
#     point = plt.ginput(1)[0]
#     plt.close(fig)
#     p2, p1 = int(point[1]), int(point[0])
#     print(f"Seed point: ({p1}, {p2}, {I.shape}, {point})")
#
#     # free memory for a region
#     R = np.zeros_like(I[:, :, 0])  # output
#     im_size = I.shape[:2]
#     ival_reg = I[p1, p2, 0]  # average intensity value of the region
#     reg_size = 1
#     # free memory for neighbor pixels
#     pos = 0
#     list = np.zeros((50000, 3), dtype=int)
#     pix_diff = 0
#     # neighbour candidates for the region
#     cand = np.array([[-1, 0], [1, 0], [0, -1], [0, 1]])
#
#     # do the region growing until the intensity difference between the region mean and a
#     # new pixel become larger than a certain threshold
#     while (pix_diff < t) and (reg_size < I.size):
#         for j in range(4):
#             n1 = p1 + cand[j, 0]
#             n2 = p2 + cand[j, 1]
#             # check if the neighbor is in or out of the image
#             ins = (n1 >= 0) and (n2 >= 0) and (n1 < im_size[0]) and (n2 < im_size[1])
#             if (ins) and (R[n1, n2] == 0):
#                 pos = pos + 1
#                 list[pos, :] = [n1, n2, I[n1, n2, 0] * 255.0]
#                 R[n1, n2] = 1
#
#         # new block of memory
#         if (pos + 10 > 10000):
#             list[(pos + 1):20000, :] = 0
#
#         diff = np.abs(list[1:pos, 2] - ival_reg)
#         index = np.argmin(diff)
#         pix_diff = diff[index]
#         R[p1, p2] = 1
#         reg_size = reg_size + 1
#         ival_reg = (ival_reg * reg_size + list[index, 2]) / (reg_size + 1)
#         p1 = list[index, 0]
#         p2 = list[index, 1]
#         list[index, :] = list[pos, :]
#         pos = pos - 1
#
#     # display the segmented region
#     cv2.imshow("Segmented Region", R)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
#     # Convert binary mask to 3-dimensional array with the same shape as I
#     R_3d = np.repeat(np.expand_dims(R, axis=-1), 3, axis=-1)
#
#     # display original image+region
#     cv2.imshow("Original Image + Region", I + R_3d)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
#     if s != 0:
#         pathstr, name = os.path.split(full_file)
#         name, ext = os.path.splitext(name)
#         newImagePath = os.path.join(pathstr, f"{name}_RGsegm_{t}{ext}")
#         cv2.imwrite(newImagePath, R * 255)
#
#         newImagePath = os.path.join(pathstr, f"{name}_RGsegm+orig_{t}{ext}")
#         cv2.imwrite(newImagePath, (I + R) * 255)
#
#     # convert I
#
#
# regrow('./images/ctisus/ctisusBmp/adrenal_1-01.bmp', 20, 0)








# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
#
# def regiongrowing(I, x=None, y=None, reg_maxdist=0.2):
#     if y is None:
#         plt.imshow(I, cmap='gray')
#         plt.axis('off')
#         x, y = plt.ginput(2, timeout=10000)
#         x, y = int(round(x[0])), int(round(y[0]))
#     J = np.zeros_like(I)
#     Isizes = I.shape
#     reg_mean = I[x,y]
#     reg_size = 1
#     neg_free = 10000
#     neg_pos = 0
#     neg_list = np.zeros((neg_free, 3))
#     pixdist = 0
#     neigb = np.array([[-1, 0], [1, 0], [0, -1], [0, 1]])
#     while pixdist < reg_maxdist and reg_size < np.prod(Isizes):
#         for j in range(4):
#             xn = x + neigb[j, 0]
#             yn = y + neigb[j, 1]
#             ins = (xn >= 0 and yn >= 0 and xn < Isizes[0] and yn < Isizes[1])
#             if ins and J[xn, yn] == 0:
#                 neg_pos += 1
#                 neg_list[neg_pos, :] = [xn, yn, I[xn, yn]]
#                 J[xn, yn] = 1
#         if neg_pos + 10 > neg_free:
#             neg_free += 10000
#             neg_list.resize((neg_free, 3))
#             neg_list[neg_pos + 1:, :] = 0
#         dist = np.abs(neg_list[:neg_pos, 2] - reg_mean)
#         pixdist, index = np.min(dist), np.argmin(dist)
#         J[x, y] = 2
#         reg_size += 1
#         reg_mean = (reg_mean * reg_size + neg_list[index, 2]) / (reg_size + 1)
#         x, y = int(neg_list[index, 0]), int(neg_list[index, 1])
#         neg_list[index, :] = neg_list[neg_pos, :]
#         neg_pos -= 1
#     return J.astype(np.bool)
#
# I = cv2.imread('./images/ctisus/ctisusBmp/adrenal_1-01.bmp', cv2.IMREAD_GRAYSCALE).astype(np.float64) / 255.0
# plt.imshow(I, cmap='gray')
# plt.axis('off')
# plt.show()
# J = regiongrowing(I)
# plt.imshow(I + J, cmap='gray')
# plt.axis('off')
# plt.show()




# ## GUI from Matlab
# import numpy as np
# import cv2
# import matplotlib.pyplot as plt
# from collections import deque
#
# def regrow(full_file, t, s):
#     I = cv2.imread(full_file, cv2.IMREAD_COLOR)
#     I = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)
#     I = I.astype(np.float32) / 255.0
#     cv2.imshow("Input Image", I)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
#     print("Select a seed point of the region you want to segment.")
#     fig, ax = plt.subplots()
#     ax.imshow(I)
#     point = plt.ginput(1)[0]
#     plt.close(fig)
#     p2, p1 = int(point[1]), int(point[0])
#     print(f"Seed point: ({p1}, {p2}, {I.shape}, {point})")
#
#     # free memory for a region
#     R = np.zeros_like(I[:, :, 0])  # output
#     im_size = I.shape[:2]
#     ival_reg = I[p1, p2, 0]  # average intensity value of the region
#     reg_size = 1
#     # free memory for neighbor pixels
#     pos = 0
#     q = deque(maxlen=20000)
#     pix_diff = 0
#     # neighbour candidates for the region
#     cand = np.array([[-1, 0], [1, 0], [0, -1], [0, 1]])
#
#     # do the region growing until the intensity difference between the region mean and a
#     # new pixel become larger than a certain threshold
#     while (pix_diff < t) and (reg_size < I.size):
#         for j in range(4):
#             n1 = p1 + cand[j, 0]
#             n2 = p2 + cand[j, 1]
#             # check if the neighbor is in or out of the image
#             ins = (n1 >= 0) and (n2 >= 0) and (n1 < im_size[0]) and (n2 < im_size[1])
#             if (ins) and (R[n1, n2] == 0):
#                 pos = pos + 1
#                 q.append([n1, n2, I[n1, n2, 0] * 255.0])
#                 R[n1, n2] = 1
#
#         diff = np.abs([x[2] for x in q] - ival_reg)
#         index = np.argmin(diff)
#         pix_diff = diff[index]
#         R[p1, p2] = 1
#         reg_size = reg_size + 1
#         ival_reg = (ival_reg * reg_size + q[index][2]) / (reg_size + 1)
#         p1 = q[index][0]
#         p2 = q[index][1]
#         q.remove(q[index])
#         pos = len(q)
#
#     # display the segmented region
#     cv2.imshow("Segmented Region", R)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
#     # Convert binary mask to 3-dimensional array with the same shape as I
#     R_3d = np.repeat(np.expand_dims(R, axis=-1), 3, axis=-1)
#
#     # display original image+region
#     cv2.imshow("Original Image + Region", I + R_3d)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
#     if s != 0:
#         pathstr, name = os.path.split(full_file)
#         name, ext = os.path.splitext(name)
#         newImagePath = os.path.join(pathstr, f"{name}_RGsegm_{t}{ext}")
#         cv2.imwrite(newImagePath, R * 255)
#
#         newImagePath = os.path.join(pathstr, f"{name}_RGsegm+orig_{t}{ext}")
#         cv2.imwrite(newImagePath, (I + R) * 255)
#
# regrow('./images/ctisus/ctisusBmp/adrenal_1-01.bmp', 20, 0)













# import numpy as np
# import matplotlib.pyplot as plt
#
# # Define the image and the seed point
# img = plt.imread('./images/ctisus/ctisusBmp/adrenal_1-01.bmp')
# seed = (100, 100)
#
# # Define the connectivity criterion (4 or 8 neighbors)
# connectivity = 4
#
# # Define the initial threshold value
# threshold = img[seed]
#
# # Initialize the region
# region = np.zeros_like(img, dtype=bool)
# region[seed] = True
#
# # Define a function to check if a pixel is already part of the region or not
# def check_pixel(pixel):
#     neighbors = get_neighbors(pixel, connectivity)
#     neighbor_rows, neighbor_cols = zip(*neighbors)
#     return np.any((abs(img[pixel[0], pixel[1], :3] - threshold) < 0.1) & region[neighbor_rows, neighbor_cols])
#
# # Define a function to get the neighbors of a pixel
# def get_neighbors(pixel, connectivity):
#     # if connectivity == 4:
#     #     neighbors = [(pixel[0] + 1, pixel[1]), (pixel[0] - 1, pixel[1]), (pixel[0], pixel[1] + 1), (pixel[0], pixel[1] - 1)]
#     # elif connectivity == 8:
#     #     neighbors = [(pixel[0] + 1, pixel[1]), (pixel[0] - 1, pixel[1]), (pixel[0], pixel[1] + 1), (pixel[0], pixel[1] - 1),
#     #             (pixel[0] + 1, pixel[1] + 1), (pixel[0] - 1, pixel[1] - 1), (pixel[0] + 1, pixel[1] - 1), (pixel[0] - 1, pixel[1] + 1)]
#     if connectivity == 4:
#         neighbors = [(pixel[0] + 1, pixel[1]), (pixel[0], pixel[1]), (pixel[0], pixel[1] ), (pixel[0], pixel[1] - 1)]
#     elif connectivity == 8:
#         neighbors = [(pixel[0] + 1, pixel[1]), (pixel[0] - 1, pixel[1]), (pixel[0], pixel[1] + 1), (pixel[0], pixel[1] - 1),
#                 (pixel[0] + 1, pixel[1] + 1), (pixel[0] - 1, pixel[1] - 1), (pixel[0] + 1, pixel[1] - 1), (pixel[0] - 1, pixel[1] + 1)]
#     print(neighbors)
#     return neighbors
#
# # Iterate through the image and add connected pixels to the region
# while True:
#     added = False
#     for x in range(img.shape[0]):
#         for y in range(img.shape[1]):
#             pixel = (x, y)
#             if check_pixel(pixel) and not region[pixel]:
#                 region[pixel] = True
#                 added = True
#     if not added:
#         break
#
# plt.imshow(region, cmap='gray')
# plt.show()


# import cv2
# import numpy as np
#
# def get8n(x, y, shape):
#     out = []
#     maxx = shape[1]-1
#     maxy = shape[0]-1
#
#     #top left
#     outx = min(max(x-1,0),maxx)
#     outy = min(max(y-1,0),maxy)
#     out.append((outx,outy))
#
#     #top center
#     outx = x
#     outy = min(max(y-1,0),maxy)
#     out.append((outx,outy))
#
#     #top right
#     outx = min(max(x+1,0),maxx)
#     outy = min(max(y-1,0),maxy)
#     out.append((outx,outy))
#
#     #left
#     outx = min(max(x-1,0),maxx)
#     outy = y
#     out.append((outx,outy))
#
#     #right
#     outx = min(max(x+1,0),maxx)
#     outy = y
#     out.append((outx,outy))
#
#     #bottom left
#     outx = min(max(x-1,0),maxx)
#     outy = min(max(y+1,0),maxy)
#     out.append((outx,outy))
#
#     #bottom center
#     outx = x
#     outy = min(max(y+1,0),maxy)
#     out.append((outx,outy))
#
#     #bottom right
#     outx = min(max(x+1,0),maxx)
#     outy = min(max(y+1,0),maxy)
#     out.append((outx,outy))
#
#     return out
#
# def region_growing(img, seed):
#     list = []
#     outimg = np.zeros_like(img)
#     list.append((seed[0], seed[1]))
#     processed = []
#     while(len(list) > 0):
#         pix = list[0]
#         outimg[pix[0], pix[1]] = 255
#         for coord in get8n(pix[0], pix[1], img.shape):
#             if img[coord[0], coord[1]] != 0:
#                 outimg[coord[0], coord[1]] = 255
#                 if not coord in processed:
#                     list.append(coord)
#                 processed.append(coord)
#         list.pop(0)
#         cv2.imshow("progress",outimg)
#         cv2.waitKey(1)
#     return outimg
#
# def on_mouse(event, x, y, flags, params):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print ('Seed: ' + str(x) + ', ' + str(y), img[y,x])
#         clicks.append((y,x))
#
# clicks = []
# image = cv2.imread('./images/ctisus/ctisusBmp/adrenal_1-01.bmp', 0)
# ret, img = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)
# cv2.namedWindow('Input')
# cv2.setMouseCallback('Input', on_mouse, 0, )
# cv2.imshow('Input', image)
# cv2.waitKey()
# seed = clicks[-1]
# out = region_growing(img, seed)
# cv2.imshow('Region Growing', out)
# cv2.waitKey()
# cv2.destroyAllWindows()
#
# # source: https://github.com/zjgirl/RegionGrowing-1/blob/master/RegionGrowing.py
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#



# import cv2
# import numpy as np
#
# # Step 3: Read the Image
# image = cv2.imread("./images/ctisus/ctisusBmp/adrenal_1-01.bmp", 0)  # Read as grayscale
#
# # Step 5: Initialize the Active Contour Parameters
# alpha = 0.1
# beta = 0.3
# gamma = 0.01
# iterations = 500
#
# # Step 6: Perform Active Contour Segmentation
# snake = cv2.segmentation.active_contour(image, init_contour_points, alpha, beta, gamma, iterations)
#
# # Step 7: Visualize the Segmented Tumor
# segmented_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)  # Convert to color image
# cv2.polylines(segmented_image, np.int32([snake]), isClosed=True, color=(0, 255, 0), thickness=2)
# cv2.imshow("Segmented Tumor", segmented_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import cv2
# import numpy as np
#
# # Step 3: Read the Image
# image = cv2.imread("./images/ctisus/ctisusBmp/adrenal_1-01.bmp")
#
# # Step 4: Preprocess the Image (if needed)
#
# # Step 5: Initialize the GrabCut Parameters
# rect = (x, y, w, h)  # Rectangular region around the tumor (x, y, width, height)
# mask = np.zeros(image.shape[:2], np.uint8)
# bgd_model = np.zeros((1, 65), np.float64)
# fgd_model = np.zeros((1, 65), np.float64)
# iterations = 5  # Number of iterations for GrabCut
#
# # Step 6: Perform GrabCut Segmentation
# cv2.grabCut(image, mask, rect, bgd_model, fgd_model, iterations, cv2.GC_INIT_WITH_RECT)
#
# # Step 7: Generate the Mask
# mask = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
#
# # Step 8: Apply the Mask to the Image
# segmented_image = image * mask[:, :, np.newaxis]
#
# # Step 9: Visualize the Segmented Tumor
# cv2.imshow("Segmented Tumor", segmented_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import cv2
# import numpy as np
#
# # Global variables
# drawing = False
# ix, iy = -1, -1
# rect = (0, 0, 0, 0)
#
# # Mouse callback function
# def draw_rectangle(event, x, y, flags, param):
#     global ix, iy, drawing, rect
#
#     if event == cv2.EVENT_LBUTTONDOWN:
#         drawing = True
#         ix, iy = x, y
#
#     elif event == cv2.EVENT_LBUTTONUP:
#         drawing = False
#         cv2.rectangle(image, (ix, iy), (x, y), (0, 255, 0), 2)
#         rect = (min(ix, x), min(iy, y), abs(ix - x), abs(iy - y))
#
# # Step 1: Read the Image
# image = cv2.imread("./images/ctisus/ctisusBmp/adrenal_1-01.bmp")
#
# # Step 2: Create a window and set the mouse callback
# cv2.namedWindow("Image")
# cv2.setMouseCallback("Image", draw_rectangle)
#
# while True:
#     cv2.imshow("Image", image)
#     key = cv2.waitKey(1) & 0xFF
#
#     if key == ord('r'):  # Press 'r' to reset the drawn rectangle
#         image = cv2.imread("./images/ctisus/ctisusBmp/adrenal_1-01.bmp")
#
#     elif key == ord('s'):  # Press 's' to proceed with segmentation
#         if rect[2] > 0 and rect[3] > 0:
#             # Step 3: Preprocess the Image (if needed)
#
#             # Step 4: Initialize the GrabCut Parameters
#             mask = np.zeros(image.shape[:2], np.uint8)
#             bgd_model = np.zeros((1, 65), np.float64)
#             fgd_model = np.zeros((1, 65), np.float64)
#             iterations = 5  # Number of iterations for GrabCut
#
#             # Step 5: Perform GrabCut Segmentation
#             cv2.grabCut(image, mask, rect, bgd_model, fgd_model, iterations, cv2.GC_INIT_WITH_RECT)
#
#             # Step 6: Generate the Mask
#             mask = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
#
#             # Step 7: Apply the Mask to the Image
#             segmented_image = image * mask[:, :, np.newaxis]
#
#             # Step 8: Visualize the Segmented Tumor
#             cv2.imshow("Segmented Tumor", segmented_image)
#             cv2.waitKey(0)
#             break
#
#     elif key == 27:  # Press 'Esc' to exit
#         break
#
# cv2.destroyAllWindows()





# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# from skimage.color import rgb2gray
# from skimage import data
# from skimage.filters import gaussian
# from skimage.segmentation import active_contour
#
# img = cv2.imread("./images/ctisus/ctisusBmp/adrenal_1-01.bmp")
# img = rgb2gray(img)
#
# s = np.linspace(0, 2*np.pi, 200)
# r = 250 + 100*np.sin(s)
# c = 220 + 100*np.cos(s)
# init = np.array([r, c]).T
#
# snake = active_contour(gaussian(img, 3, preserve_range=False),
#                        init, alpha=0.015, beta=10, gamma=0.001, max_num_iter=500)
#
# fig, ax = plt.subplots(figsize=(7, 7))
# ax.imshow(img, cmap=plt.cm.gray)
# ax.plot(init[:, 1], init[:, 0], '--r', lw=3)
# ax.plot(snake[:, 1], snake[:, 0], '-b', lw=3)
# ax.set_xticks([]), ax.set_yticks([])
# ax.axis([0, img.shape[1], img.shape[0], 0])
#
# plt.show()


# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# from skimage.color import rgb2gray
# from skimage.filters import gaussian
# from skimage.segmentation import active_contour
#
# # Step 1: Read the image and convert to grayscale
# img = cv2.imread("./images/ctisus/ctisusBmp/adrenal_1-01.bmp")
# img = rgb2gray(img)
#
# # Step 2: Initialize the contour points
# s = np.linspace(0, 2*np.pi, 200)
# r = 250 + 100*np.sin(s)
# c = 220 + 100*np.cos(s)
# init = np.array([r, c]).T
#
# # Step 3: Perform active contour segmentation
# snake = active_contour(gaussian(img, 3, preserve_range=False),
#                        init, alpha=0.015, beta=10, gamma=0.001,
#                        max_num_iter=500)  # Increase the number of iterations
#
# # Step 4: Create binary image from segmented region
# binary_img = np.zeros_like(img)
# snake_int = np.round(snake).astype(int)
# binary_img[snake_int[:, 0], snake_int[:, 1]] = 1
#
# # Step 5: Visualize the binary image
# fig, ax = plt.subplots(figsize=(7, 7))
# ax.imshow(binary_img, cmap='binary')
# ax.set_xticks([]), ax.set_yticks([])
#
# plt.show()




# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# def split_merge_segmentation(image, min_region_size, similarity_threshold, max_iterations):
#     # Step 1: Convert image to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
#     # Step 2: Split the image into initial regions
#     regions = [[(0, 0, gray.shape[1], gray.shape[0])]]  # Start with a single region covering the entire image
#
#     # Step 3: Merge similar adjacent regions
#     iteration = 0
#     while len(regions) > 0 and iteration < max_iterations:
#         current_region = regions.pop(0)
#         if len(current_region) == 1:
#             x, y, w, h = current_region[0]
#             region_gray = gray[y:y + h, x:x + w]
#
#             # Calculate the variance of the region
#             variance = np.var(region_gray)
#
#             # Check if the variance is below the threshold and region size is above the minimum
#             if variance < similarity_threshold and w * h > min_region_size:
#                 # Split the region into four smaller regions
#                 new_regions = [
#                     [(x, y, w // 2, h // 2)],  # Top-left
#                     [(x + w // 2, y, w // 2, h // 2)],  # Top-right
#                     [(x, y + h // 2, w // 2, h // 2)],  # Bottom-left
#                     [(x + w // 2, y + h // 2, w // 2, h // 2)]  # Bottom-right
#                 ]
#                 regions.extend(new_regions)
#             else:
#                 # Region is homogeneous or too small, keep it as is
#                 regions.append(current_region)
#         else:
#             # Region has already been split, keep it as is
#             regions.append(current_region)
#
#         iteration += 1
#
#     # Step 4: Create a mask of the segmented tumor
#     mask = np.zeros(gray.shape, dtype=np.uint8)
#     for region in regions:
#         for rect in region:
#             x, y, w, h = rect
#             mask[y:y + h, x:x + w] = 255
#
#     return mask
#
#
# # Load the image
# image = cv2.imread('./images/ctisus/ctisusBmp/adrenal_1-01.bmp')
#
# # Parameters for segmentation
# min_region_size = 100  # Minimum region size to split
# similarity_threshold = 500  # Threshold for region similarity (variance)
# max_iterations = 100  # Maximum number of iterations
#
# # Perform split and merge segmentation
# segmented_mask = split_merge_segmentation(image, min_region_size, similarity_threshold, max_iterations)
#
# # Display the original image and segmented tumor mask
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
# ax1.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# ax1.set_title('Original Image')
# ax1.axis('off')
# ax2.imshow(segmented_mask, cmap='gray')
# ax2.set_title('Segmented Tumor Mask')
# ax2.axis('off')
# plt.show()


# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# def split_merge_segmentation(image, min_region_size, similarity_threshold):
#     # Step 1: Convert image to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
#     # Step 2: Split the image into initial regions
#     regions = [[(0, 0, gray.shape[1], gray.shape[0])]]  # Start with a single region covering the entire image
#
#     # Step 3: Merge similar adjacent regions
#     while len(regions) > 0:
#         current_region = regions.pop(0)
#         if len(current_region) == 1:
#             x, y, w, h = current_region[0]
#             region_gray = gray[y:y + h, x:x + w]
#
#             # Calculate the variance of the region
#             variance = np.var(region_gray)
#
#             # Check if the variance is below the threshold and region size is above the minimum
#             if variance < similarity_threshold and w * h > min_region_size:
#                 # Split the region into four smaller regions
#                 new_regions = [
#                     [(x, y, w // 2, h // 2)],  # Top-left
#                     [(x + w // 2, y, w // 2, h // 2)],  # Top-right
#                     [(x, y + h // 2, w // 2, h // 2)],  # Bottom-left
#                     [(x + w // 2, y + h // 2, w // 2, h // 2)]  # Bottom-right
#                 ]
#                 regions.extend(new_regions)
#             else:
#                 # Region is homogeneous or too small, keep it as is
#                 regions.append(current_region)
#         else:
#             # Region has already been split, keep it as is
#             regions.append(current_region)
#
#     # Step 4: Create a mask of the segmented tumor
#     mask = np.zeros(gray.shape, dtype=np.uint8)
#     for region in regions:
#         for rect in region:
#             x, y, w, h = rect
#             mask[y:y + h, x:x + w] = 255
#
#     return mask
#
#
# # Load the image
# image = cv2.imread('./images/ctisus/ctisusBmp/adrenal_1-01.bmp')
#
# # Parameters for segmentation
# min_region_size = 100  # Minimum region size to split
# similarity_threshold = 500  # Threshold for region similarity (variance)
#
# # Perform split and merge segmentation
# segmented_mask = split_merge_segmentation(image, min_region_size, similarity_threshold)
#
# # Display the original image and segmented tumor mask
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
# ax1.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# ax1.set_title('Original Image')
# ax1.axis('off')
# ax2.imshow(segmented_mask, cmap='gray')
# ax2.set_title('Segmented Tumor Mask')
# ax2.axis('off')
# plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt

# def grabcut_segmentation(image):
#     # Create a mask initialized with zeros
#     mask = np.zeros(image.shape[:2], np.uint8)
#
#     # Create temporary arrays for foreground and background models
#     bgd_model = np.zeros((1, 65), np.float64)
#     fgd_model = np.zeros((1, 65), np.float64)
#
#     # Define the rectangular region of interest (ROI) enclosing the tumor
#     # Adjust the values according to your specific image and tumor location
#     x = 180
#     y = 220
#     width = 100
#     height = 90
#     rect = (x, y, width, height)
#
#     # Apply GrabCut algorithm to segment the tumor
#     cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)
#
#     # Create a mask with the probable foreground (GC_PR_FGD or GC_FGD) and definite foreground (GC_FGD) labels
#     mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
#
#     # Apply the mask to the original image
#     segmented_image = image * mask2[:, :, np.newaxis]
#
#     return segmented_image
#
# # Load the image
# image = cv2.imread('./images/ctisus/ctisusBmp/adrenal_1-01.bmp')
#
# # Perform GrabCut segmentation
# segmented_image = grabcut_segmentation(image)
#
# # Display the original image and segmented tumor
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
# ax1.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# ax1.set_title('Original Image')
# ax1.axis('off')
# ax2.imshow(cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB))
# ax2.set_title('Segmented Tumor')
# ax2.axis('off')
# plt.show()




# import cv2
# import numpy as np
#
# def split_and_merge(image_path, val, s):
#     global v
#     v = val
#     I = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#
#     # Perform split and merge segmentation
#     M = split_merge(I)
#
#     # Save the segmented image if needed
#     if s != 0:
#         path, ext = image_path.rsplit('.', 1)
#         if v == 5:
#             new_image_path = f"{path}_SMcontur_moreGray.{ext}"
#         else:
#             new_image_path = f"{path}_SMcontur_betterContrast.{ext}"
#         cv2.imwrite(new_image_path, M)
#
#     return M
#
#
# def split_merge(I):
#     mindim = 2
#
#     def predicate(region):
#         sd = np.std(region)
#         mean = np.mean(region)
#         return (sd > v) and (0 < mean < 255)
#
#     def split(B, mindim, fun):
#         K = B.shape[0]
#         split_flag = False  # Initialize the split_flag to False
#         for Im in range(K):
#             quadregion = B[Im]
#             if quadregion.shape[0] <= mindim:
#                 continue  # The block shouldn't be split
#             flag1 = fun(quadregion)
#             if flag1:
#                 split_flag = True  # The block should be split if any subregion satisfies the condition
#                 break
#         return split_flag
#
#     def merge(I, S, Bmax, fun):
#         M = np.zeros_like(I)
#         marker = np.zeros_like(I)
#
#         for k in range(1, Bmax + 1):
#             vals, r, c = get_node(I, S, k)
#             if len(vals) > 0:
#                 for i in range(len(r)):
#                     xlow, ylow = r[i], c[i]
#                     xhigh, yhigh = xlow + k - 1, ylow + k - 1
#                     region = I[xlow:xhigh + 1, ylow:yhigh + 1]
#                     flag = fun(region)
#                     if flag:
#                         M[xlow:xhigh + 1, ylow:yhigh + 1] = 1
#                         marker[xlow, ylow] = 1
#
#         # Connect and label regions with bwlabel
#         cc = cv2.connectedComponentsWithStats(np.uint8(marker), connectivity=8)
#         labeled = cc[1]
#         M = labeled[0:I.shape[0], 0:I.shape[1]]
#
#         # Fill holes in the image
#         BWdfill = cv2.fillHoles(np.uint8(M))
#
#         return BWdfill
#
#     def get_node(I, S, k):
#         mask = np.zeros_like(S, dtype=np.uint8)
#         mask[S == k] = 255
#         mask = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
#         if len(mask) > 0:
#             x, y, w, h = cv2.boundingRect(max(mask, key=cv2.contourArea))
#             vals = I[y:y+h, x:x+w]
#             r, c = np.where(S[y:y+h, x:x+w] == k)
#             return vals, r + y, c + x
#         else:
#             return [], [], []
#
#     # Pad subimage with zeros to the nearest square size
#     p = 2**int(np.ceil(np.log2(max(I.shape))))
#     I = cv2.copyMakeBorder(I, 0, p - I.shape[0], 0, p - I.shape[1], cv2.BORDER_CONSTANT, value=0)
#
#     # Splitting
#     S = np.zeros_like(I, dtype=int)
#     quadtree_split(I, S, mindim, split, predicate)
#
#     # Merging
#     Bmax = S.max()
#     BWdfill = merge(I, S, Bmax, predicate)
#
#     return BWdfill
#
# def quadtree_split(I, S, mindim, split_func, predicate_func):
#     m, n = I.shape
#     quadsize = max(m, n)
#
#     if quadsize <= mindim:
#         return
#
#     t1 = I[0:m // 2, 0:n // 2]
#     t2 = I[0:m // 2, n // 2:n]
#     t3 = I[m // 2:m, 0:n // 2]
#     t4 = I[m // 2:m, n // 2:n]
#
#     if split_func(t1, mindim, predicate_func):
#         S[0:m // 2, 0:n // 2] = S.max() + 1
#         quadtree_split(t1, S[0:m // 2, 0:n // 2], mindim, split_func, predicate_func)
#
#     if split_func(t2, mindim, predicate_func):
#         S[0:m // 2, n // 2:n] = S.max() + 1
#         quadtree_split(t2, S[0:m // 2, n // 2:n], mindim, split_func, predicate_func)
#
#     if split_func(t3, mindim, predicate_func):
#         S[m // 2:m, 0:n // 2] = S.max() + 1
#         quadtree_split(t3, S[m // 2:m, 0:n // 2], mindim, split_func, predicate_func)
#
#     if split_func(t4, mindim, predicate_func):
#         S[m // 2:m, n // 2:n] = S.max() + 1
#         quadtree_split(t4, S[m // 2:m, n // 2:n], mindim, split_func, predicate_func)
#
#
#
# # Example usage:
# val = 20  # Choose a value for the segmentation
# s = 1  # Set to 1 to save the segmented image, or 0 otherwise
# image_path = './images/ctisus/ctisusBmp/adrenal_1-01.bmp'
# segmented_image = split_and_merge(image_path, val, s)


# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
# selected_roi = None
#
#
# def on_mouse_click(event, x, y, flags, param):
#     global selected_roi
#     if event == cv2.EVENT_LBUTTONDOWN:
#         selected_roi = (x, y)
#
#
# def split_and_merge(image, threshold):
#     h, w = image.shape[:2]
#
#     # Step 1: Split the image into four quadrants
#     if h > 1 and w > 1:
#         mid_h, mid_w = h // 2, w // 2
#         quadrants = [
#             image[:mid_h, :mid_w],  # Top-left
#             image[:mid_h, mid_w:],  # Top-right
#             image[mid_h:, :mid_w],  # Bottom-left
#             image[mid_h:, mid_w:],  # Bottom-right
#         ]
#
#         # Step 2: Check the variance of each quadrant
#         # If the variance is below the threshold, merge the quadrant
#         for quadrant in quadrants:
#             if np.var(quadrant) < threshold:
#                 avg_color = np.mean(quadrant)
#                 quadrant[:, :] = avg_color
#
#         # Step 3: Recursively apply the algorithm to the split quadrants
#         for quadrant in quadrants:
#             split_and_merge(quadrant, threshold)
#
#     return image
#
#
# def main():
#     input_image_path = './images/ctisus/ctisusBmp/adrenal_1-01.bmp'
#     threshold = 1000  # Adjust this threshold according to your preference
#
#     # Read the input image
#     image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
#
#     # Display the image and allow the user to select a region of interest (ROI)
#     cv2.imshow("Select ROI", image)
#     cv2.setMouseCallback("Select ROI", on_mouse_click)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
#     if selected_roi is None:
#         print("No ROI selected.")
#         return
#
#     x, y = selected_roi
#     roi_width = 1000  # Adjust the width of the ROI based on your preference
#     roi_height = 1000  # Adjust the height of the ROI based on your preference
#
#     # Crop the selected ROI from the image
#     roi = image[y:y + roi_height, x:x + roi_width]
#
#     # Perform split-and-merge segmentation on the ROI
#     segmented_roi = split_and_merge(roi, threshold)
#
#     # Display the original ROI and segmented ROI
#     plt.figure(figsize=(10, 5))
#     plt.subplot(1, 2, 1)
#     plt.title('Original ROI')
#     plt.imshow(roi, cmap='gray')
#
#     plt.subplot(1, 2, 2)
#     plt.title('Segmented ROI')
#     plt.imshow(segmented_roi, cmap='gray')
#
#     plt.show()
#
#
# main()


import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.measure import label


# def split_and_merge(f, mindim, fun):
#     # Pad image with zeros to guarantee that function qtdecomp will
#     # split regions down to size 1-by-1.
#     Q = 2 ** int(np.ceil(np.log2(max(f.shape))))
#     f = np.pad(f, ((0, Q - f.shape[0]), (0, Q - f.shape[1])), mode='constant')
#
#     # Perform splitting first.
#     S = qtdecomp(f, mindim, fun)
#
#     # Now merge by looking at each quadregion and setting all its
#     # elements to 1 if the block satisfies the predicate.
#
#     # Get the size of the largest block. Use full because S is sparse.
#     Lmax = int(np.max(S))
#     # Set the output image initially to all zeros. The MARKER array is
#     # used later to establish connectivity.
#     g = np.zeros_like(f)
#     MARKER = np.zeros_like(f, dtype=bool)
#
#     # Begin the merging stage.
#     for K in range(1, Lmax + 1):
#         vals, r, c = qtgetblk(f, S, K)
#         if len(vals) > 0:
#             # Check the predicate for each of the regions
#             # of size K-by-K with coordinates given by vectors
#             # r and c.
#             for I in range(len(r)):
#                 xlow, ylow = r[I], c[I]
#                 xhigh, yhigh = xlow + K - 1, ylow + K - 1
#                 region = f[xlow:xhigh + 1, ylow:yhigh + 1]
#                 flag = fun(region)
#                 if flag:
#                     g[xlow:xhigh + 1, ylow:yhigh + 1] = 1
#                     MARKER[xlow, ylow] = 1
#
#     # Finally, obtain each connected region and label it with a
#     # different integer value using function label.
#     g = label(MARKER & g)
#
#     # Crop and exit
#     g = g[:f.shape[0], :f.shape[1]]
#
#     return g
#
#
# def qtdecomp(f, mindim, fun):
#     H, W = f.shape
#     full_size = 2 ** int(np.ceil(np.log2(max(H, W))))
#     padded_f = np.pad(f, ((0, full_size - H), (0, full_size - W)), mode='constant')
#
#     S = np.zeros((full_size, full_size), dtype=int)
#     S[:H, :W] = 1
#
#     split_region(S, padded_f, full_size, mindim, fun)
#
#     return S
#
#
# def split_region(S, f, N, mindim, fun):
#     if N <= mindim:
#         return
#
#     for i in range(2):
#         for j in range(2):
#             subregion = f[i * N // 2:(i + 1) * N // 2, j * N // 2:(j + 1) * N // 2]
#             if (lambda region: np.std(region) > 10 and 0 < np.mean(region) < 125)(subregion):
#                 split_region(S, f, N // 2, mindim, fun)
#             else:
#                 S[i * N // 2:(i + 1) * N // 2, j * N // 2:(j + 1) * N // 2] = 0
#
#
# def qtgetblk(f, S, K):
#     rows, cols = np.where(S == K)
#     if len(rows) > 0:
#         xlow, ylow = np.min(rows), np.min(cols)
#         xhigh, yhigh = np.max(rows), np.max(cols)
#         vals = f[xlow:xhigh + 1, ylow:yhigh + 1]
#         return vals, rows, cols
#     else:
#         return [], [], []
#
#
# # Replace this function with your custom predicate function.
# def predicate(region):
#     return (np.std(region) > 10) and (0 < np.mean(region) < 125)
#
#
# def main():
#     input_image_path = './images/ctisus/ctisusBmp/adrenal_1-01.bmp'
#     mindim = 16  # Minimum dimension of quadtree regions (must be a power of 2)
#
#     # Read the input image
#     image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
#
#     # Perform split-and-merge segmentation with the custom predicate function
#     segmented_image = split_and_merge(image, mindim, predicate)
#
#     # Display the segmented image
#     plt.imshow(segmented_image, cmap='jet')
#     plt.axis('off')
#     plt.show()
#
#
# main()



# import cv2
#
# def apply_clahe(image, clip_limit, grid_size):
#     # Convert the image to grayscale if it's not already
#     if len(image.shape) == 3:
#         gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     else:
#         gray_image = image
#
#     # Create a CLAHE object
#     clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=grid_size)
#
#     # Apply CLAHE to the grayscale image
#     enhanced_image = clahe.apply(gray_image)
#
#     return enhanced_image
#
# # Load an image
# image = cv2.imread('./images/ctisus/ctisusBmp/adrenal_1-01.bmp')
#
# # Apply CLAHE with custom parameters
# enhanced_image = apply_clahe(image, clip_limit=1.0, grid_size=(8, 8))
#
# # Save or display the thresholded image
# cv2.imshow('thresholded image', enhanced_image)
# # Wait for key press
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# from skimage import io, exposure
#
# # Load the image
# image = io.imread('./images/ctisus/ctisusBmp/adrenal_1-01.bmp')
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Apply contrast stretching
# p2, p98 = np.percentile(gray_image, (50, 99))
# stretched_image = exposure.rescale_intensity(gray_image, in_range=(p2, p98))
# colormap_image = cv2.applyColorMap(stretched_image, cv2.COLORMAP_JET)
#
# cv2.imshow('thresholded image', colormap_image)
# # Wait for key press
# cv2.waitKey(0)
# cv2.destroyAllWindows()



from skimage import io, exposure

# Load the image
image = io.imread('./images/ctisus/ctisusBmp/adrenal_1-01.bmp')
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply contrast stretching
p2, p98 = np.percentile(image, (80, 99))
stretched_image = exposure.rescale_intensity(image, in_range=(p2, p98))
# colormap_image = cv2.applyColorMap(stretched_image, cv2.COLORMAP_JET)
rgb_stretched_image = cv2.cvtColor(stretched_image, cv2.COLOR_BGR2RGB)
gray_image = cv2.cvtColor(stretched_image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray image', gray_image)
cv2.imshow('rgb stretched image', rgb_stretched_image)
cv2.imshow('thresholded image', stretched_image)
# Wait for key press
cv2.waitKey(0)
cv2.destroyAllWindows()