# import cv2
# import numpy as np
#
# # Reading input
# img = cv2.imread('./images/ctisus/ctisusBmp/adrenal_1-01.bmp')
# h, w, c = img.shape
#
# # Initialization
# img1 = img.astype(float) / 255  # Normalizing RGB values
# seed_posn1 = (250, 160)  # Seed point
# seeds = np.array([seed_posn1])  # Matrix that will maintain record of all seed points.
# # Since only 2 clusters are to be obtained, 1 seed point is enough
# vis = np.zeros((h, w), np.uint8)  # Matrix used to check if a pixel has become a seed point or not
# moves = np.array([[1, 0, -1, 0], [0, 1, 0, -1]])  # To find pixels present in 4-neighborhood
# max_iter = 100000  # Maximum number of iterations needed
# idx = 0  # Index of first seed not visited yet
# last = 1  # Maintains size of seeds matrix
#
# # Region Growing Algorithm Implementation
# for n in range(max_iter):
#     ctr = 0  # To count number of points added to the seeds matrix
#     for i in range(idx, last):
#         sp = tuple(seeds[i])  # Seed Point
#         vis[sp[1], sp[0]] = 1  # Marking the seed as visited
#         r1, g1, b1 = img1[sp[1], sp[0]]  # RGB pixel value of seed
#         for m in range(4):
#             new_coord = sp + moves[:, m]  # Neighbor Pixel
#             x, y = new_coord
#             if 0 <= x < w and 0 <= y < h and not vis[y, x]:  # Checks if seed point is valid or not
#                 rx, gx, bx = img1[y, x]  # RGB pixel value of neighbor
#                 d = ((r1 - rx) ** 2 + (g1 - gx) ** 2 + (b1 - bx) ** 2) ** 0.5  # Measures similarity between pixel intensities
#                 if d < 0.05:  # Serves as Predicate for growing the region
#                     vis[y, x] = 1  # Marking the pixel as visited
#                     seeds = np.append(seeds, [new_coord], axis=0)  # Adding the pixels to seeds
#                     ctr += 1
#     idx = last  # Index of first seed not visited yet
#     last += ctr  # Updated size of seeds matrix
#     if idx >= last:  # Indicates that no pixels can be merged anymore
#         break
#
# # Obtaining Segmented Image
# final_im = np.zeros_like(img1)
# for i in range(seeds.shape[0]):
#     # Mark the region obtained in blue
#     final_im[seeds[i, 1], seeds[i, 0], 2] = 1
# for i in range(h):
#     for j in range(w):
#         # Mark the region left in green
#         if final_im[i, j].sum() == 0:
#             final_im[i, j, 1] = 0.5
#
# # Plotting figures
# cv2.imshow('Original Image and the initial Seed Point', img)
# cv2.waitKey()
# cv2.circle(img, seed_posn1, 5, (255, 0, 0), 2)
# cv2.imshow('Original Image and the initial', final_im)
# cv2.waitKey(0)
# cv2.destroyAllWindows()






import cv2
import numpy as np

def get8n(x, y, shape):
    out = []
    maxx = shape[1]-1
    maxy = shape[0]-1

    #top left
    outx = min(max(x-1,0),maxx)
    outy = min(max(y-1,0),maxy)
    out.append((outx,outy))

    #top center
    outx = x
    outy = min(max(y-1,0),maxy)
    out.append((outx,outy))

    #top right
    outx = min(max(x+1,0),maxx)
    outy = min(max(y-1,0),maxy)
    out.append((outx,outy))

    #left
    outx = min(max(x-1,0),maxx)
    outy = y
    out.append((outx,outy))

    #right
    outx = min(max(x+1,0),maxx)
    outy = y
    out.append((outx,outy))

    #bottom left
    outx = min(max(x-1,0),maxx)
    outy = min(max(y+1,0),maxy)
    out.append((outx,outy))

    #bottom center
    outx = x
    outy = min(max(y+1,0),maxy)
    out.append((outx,outy))

    #bottom right
    outx = min(max(x+1,0),maxx)
    outy = min(max(y+1,0),maxy)
    out.append((outx,outy))

    return out

def region_growing(img, seed):
    list = []
    outimg = np.zeros_like(img)
    list.append((seed[0], seed[1]))
    processed = []
    while(len(list) > 0):
        pix = list[0]
        outimg[pix[0], pix[1]] = 255
        for coord in get8n(pix[0], pix[1], img.shape):
            if img[coord[0], coord[1]] != 0:
                outimg[coord[0], coord[1]] = 255
                if not coord in processed:
                    list.append(coord)
                processed.append(coord)
        list.pop(0)
        cv2.imshow("progress",outimg)
        cv2.waitKey(1)
    return outimg

def on_mouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print ('Seed: ' + str(x) + ', ' + str(y), img[y,x])
        clicks.append((y,x))

clicks = []
image = cv2.imread('./images/ctisus/ctisusBmp/adrenal_1-01.bmp', 0)
ret, img = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)
cv2.namedWindow('Input')
cv2.setMouseCallback('Input', on_mouse, 0, )
cv2.imshow('Input', image)
cv2.waitKey()
seed = clicks[-1]
out = region_growing(img, seed)
cv2.imshow('Region Growing', out)
cv2.waitKey()
cv2.destroyAllWindows()

# source: https://github.com/zjgirl/RegionGrowing-1/blob/master/RegionGrowing.py


