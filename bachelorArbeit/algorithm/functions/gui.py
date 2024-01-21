import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import simpledialog
from medianFilterFunc import apply_median_filter, apply_sharpen_filter
from contrastStretchFunc import apply_contrast_stretching
from kMeansClusteringFunc import kMeans_segment_image
from regionGrowingFunc import perform_region_growing
from diceCoefficient import calculateDiceCoefficient
import os


root = tk.Tk()
root.geometry("1000x600")
root.title("Image Drawing Tool")

pen_color = "black"
pen_size = 5
file_path = ""
original_image = None  # Global variable to store the original image
filtered_image = None  # Global variable to store the result after each filter
size = 7
# Directory to save the segmented images
output_dir = './segmentedImages/'
segment1_path = ''
segment2_path = ''

def add_image():
    global file_path, original_image, filtered_image
    file_path = filedialog.askopenfilename(
        initialdir="./petCTimagesBMP")    # This line opens a file dialog box, which allows the user to select an image file. The askopenfilename function is a part of the filedialog module, and it opens a standard file dialog. The initialdir parameter sets the initial directory that the file dialog should open in. The selected file's path is stored in the file_path variable.
    original_image = Image.open(file_path)   # This line uses the Python Imaging Library (PIL), also known as Pillow, to open the selected image file using the file path stored in file_path. The image is then loaded into the image variable.
    canvas.config(width=original_image.width, height=original_image.height)       # This line updates the dimensions of a Tkinter canvas widget (canvas) to match the dimensions of the resized image. It sets the canvas width and height to match the resized image's width and height.
    image = ImageTk.PhotoImage(original_image)       # Here, the resized image is converted into a Tkinter PhotoImage object using the ImageTk.PhotoImage function. This allows you to display the image in a Tkinter canvas.
    canvas.image = ImageTk.PhotoImage(original_image)
    canvas.create_image(0, 0, image=canvas.image, anchor="nw")
    print("Image Dimensions:", original_image.size)
    filtered_image = original_image.copy()  # Initialize filtered_image with the original image
    print(file_path)

def add_segment1():
    global segment1_path
    segment1_path = filedialog.askopenfilename(
        initialdir="./segmentedImages")
    return segment1_path

def add_segment2():
    global segment2_path
    segment2_path = filedialog.askopenfilename(
        initialdir="./segmentedImages")
    return segment2_path

def apply_filter(filter):
    global file_path, original_image, filtered_image
    if not file_path:
        print("Please select an image first.")
        return

    filtered_image = np.array(filtered_image)
    filtered_image = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB)

    if filter == "Contrast stretch":
        filtered_image = apply_contrast_stretching(filtered_image)
    elif filter == "Median":
        filtered_image = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB)
        filtered_image = apply_median_filter(filtered_image, size)
    elif filter == "Sharpen":
        filtered_image = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB)
        filtered_image = apply_sharpen_filter(filtered_image)

def apply_segmentation(segmentation_method):
    global selected_segment_index
    if segmentation_method == "kMeans":
        segments = kMeans_segment_image(filtered_image, 4)
        for i, segment in enumerate(segments):
            segment_filename = f'segment_{i}.bmp'
            segment_path = os.path.join(output_dir, segment_filename)
            # cv2.imwrite(segment_path, segment)
            cv2.imshow(f'Segment {i}', segment)
        # Wait for key press
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        selected_segment_index = simpledialog.askinteger("Input", f"Enter segment index (0 to {len(segments) - 1}):",
                                                         parent=root, minvalue=0, maxvalue=len(segments) - 1)
        selected_segment = segments[selected_segment_index]
        segment_filename = f'selected_segment_{selected_segment_index}.bmp'
        # Get the base filename without extension
        image_name = os.path.splitext(os.path.basename(file_path))[0]
        # segment_path = os.path.join(output_dir, 'kMeansSegmentedImages/', segment_filename)
        segment_path = os.path.join(output_dir, 'kMeansSegmentedImages/', f'{image_name}_{segment_filename}')

        cv2.imwrite(segment_path, selected_segment)
        print(image_name)
        print(f"Segment {selected_segment_index} saved as {segment_path}")

        return segment_path

    elif segmentation_method == "regrow":
        grayImage = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2GRAY)
        segment = perform_region_growing(grayImage)
        # segment_path = os.path.join(output_dir, 'kMeansSegmentedImages/', segment_filename)

        cv2.imshow('Region Growing Segment', segment)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def select_ksize(ksize_str):
    global size
    try:
        size = int(ksize_str)
        # Ensure that the size is an odd number
        if size % 2 == 0:
            size += 1
    except ValueError:
        # Handle the case where ksize is not a valid integer
        size = 5  # Set a default odd value or handle it according to your application logic

    return size

left_frame = tk.Frame(root, width=200, height=600)      #This line creates a frame widget (tk.Frame) named left_frame. The frame is a rectangular area that can hold other widgets. It's given a width of 200 pixels, a height of 600 pixels, and a background color of white.
left_frame.pack(side="left", fill="y")      # This line uses the .pack() method to display the left_frame on the left side of the root window (root). It takes up the entire available vertical space due to fill="y".

canvas = tk.Canvas(root, width=750, height=600)     # This line packs the canvas widget into the root window, filling the available space.
canvas.pack()

select_image_button = tk.Button(left_frame, text="Select Image",
                         command=add_image)     #This line creates a button widget named add_image_button. The button's text is "Add Image," and it has a command associated with it (the add_image function will be executed when the button is clicked). It's placed in the left_frame with a white background.
select_image_button.pack(pady=10)

# Contrast Filter Button
contrast_stretch_image_button = tk.Button(left_frame, text="Apply Contrast Stretching",
                                          command=lambda: apply_filter("Contrast stretch"))
contrast_stretch_image_button.pack(pady=15)


# Median Filter Button
median_filter_button = tk.Button(left_frame, text="Apply Median Filter",
                                          command=lambda: apply_filter("Median"))
median_filter_button.pack()

median_filter_ksize_select = ttk.Combobox(left_frame, values=["3", "5", "7", "9"], width=5)
median_filter_ksize_select.pack(pady=15)

median_filter_ksize_select.bind("<<ComboboxSelected>>", lambda event: select_ksize(median_filter_ksize_select.get()))


# Sharpen Filter Button
sharpen_filter_button = tk.Button(left_frame, text="Apply Sharpen Filter",
                                          command=lambda: apply_filter("Sharpen"))
sharpen_filter_button.pack(pady=15)


# K-Means Clustering Button
k_means_clustering_button = tk.Button(left_frame, text="Apply k-Means Clustering",
                                          command=lambda: apply_segmentation("kMeans"))
k_means_clustering_button.pack(pady=15)

# Region Growing Button
region_growing_button = tk.Button(left_frame, text="Apply Region Growing", command=lambda: apply_segmentation("regrow"))
region_growing_button.pack(pady=15)

# Select Segment 1 Button
select_segment1_button = tk.Button(left_frame, text="Select Segment 1", command= add_segment1)
select_segment1_button.pack(pady=15)

# Select Segment 2 Button
select_segment2_button = tk.Button(left_frame, text="Select Segment 2", command= add_segment2)
select_segment2_button.pack(pady=15)



# dice_coefficient_button
dice_coefficient_button = tk.Button(left_frame, text="Calculate Dice Coefficient", command=lambda: calculateDiceCoefficient(segment1_path, segment2_path))
dice_coefficient_button.pack(pady=15)


root.mainloop()
