from skimage import io, exposure
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter
from tkinter import ttk
from medianFilterFunc import apply_median_filter, apply_sharpen_filter
from contrastStretchFunc import apply_contrast_stretching

root = tk.Tk()
root.geometry("1000x600")
root.title("Image Drawing Tool")
root.config(bg="white")

pen_color = "black"
pen_size = 5
file_path = ""
original_image = None  # Global variable to store the original image
filtered_image = None  # Global variable to store the result after each filter


def add_image():
    global file_path, original_image, filtered_image
    file_path = filedialog.askopenfilename(
        initialdir="./petCTimagesBMP")    # This line opens a file dialog box, which allows the user to select an image file. The askopenfilename function is a part of the filedialog module, and it opens a standard file dialog. The initialdir parameter sets the initial directory that the file dialog should open in. The selected file's path is stored in the file_path variable.
    original_image = Image.open(file_path)   # This line uses the Python Imaging Library (PIL), also known as Pillow, to open the selected image file using the file path stored in file_path. The image is then loaded into the image variable.
    width, height = int(original_image.width / 2), int(original_image.height / 2)     # Here, the code calculates new dimensions for the image. It reduces the width and height of the image to half its original size. This will be used later to resize the image.
    original_image = original_image.resize((width, height), Image.ANTIALIAS)      # This line resizes the image to the new width and height calculated in the previous step. The Image.ANTIALIAS filter is used for a smoother, high-quality resizing.
    canvas.config(width=original_image.width, height=original_image.height)       # This line updates the dimensions of a Tkinter canvas widget (canvas) to match the dimensions of the resized image. It sets the canvas width and height to match the resized image's width and height.
    image = ImageTk.PhotoImage(original_image)       # Here, the resized image is converted into a Tkinter PhotoImage object using the ImageTk.PhotoImage function. This allows you to display the image in a Tkinter canvas.
    canvas.image = image        # This line stores the PhotoImage object in the canvas widget, making sure it's not garbage collected.
    canvas.create_image(0, 0, image=image, anchor="nw")     # Finally, this line adds the image to the canvas at the coordinates (0, 0) with an anchor point at the northwest ("nw") corner. This will display the image on the canvas at the specified location.
    filtered_image = original_image.copy()  # Initialize filtered_image with the original image
    print(file_path)

def apply_filter(filter):
    global file_path, original_image, filtered_image
    if not file_path:
        print("Please select an image first.")
        return

    # Open the image using Pillow
    # original_image = Image.open(file_path)

    # Convert the image to numpy array for OpenCV operations
    # image_np = np.array(original_image)

    if filter == "Black and White":
        image = ImageOps.grayscale(image)
    elif filter == "Blur":
        image = image.filter(ImageFilter.BLUR)
    # elif filter == "Sharpen":
    #     image = image.filter(ImageFilter.SHARPEN)
    elif filter == "Smooth":
        image = image.filter(ImageFilter.SMOOTH)
    elif filter == "Emboss":
        image = image.filter(ImageFilter.EMBOSS)
    elif filter == "Contrast stretch":
        # image = apply_contrast_stretching(image_np)
        filtered_image = apply_contrast_stretching(np.array(filtered_image))
    elif filter == "Median":
        # image = apply_median_filter(image_np, 3)
        filtered_image = apply_median_filter(np.array(filtered_image), 3)
    elif filter == "Sharpen":
        filtered_image = apply_sharpen_filter(np.array(filtered_image))


left_frame = tk.Frame(root, width=200, height=600, bg="white")      #This line creates a frame widget (tk.Frame) named left_frame. The frame is a rectangular area that can hold other widgets. It's given a width of 200 pixels, a height of 600 pixels, and a background color of white.
left_frame.pack(side="left", fill="y")      # This line uses the .pack() method to display the left_frame on the left side of the root window (root). It takes up the entire available vertical space due to fill="y".

canvas = tk.Canvas(root, width=750, height=600)     # This line packs the canvas widget into the root window, filling the available space.
canvas.pack()

select_image_button = tk.Button(left_frame, text="Select Image",
                         command=add_image, bg="white")     #This line creates a button widget named add_image_button. The button's text is "Add Image," and it has a command associated with it (the add_image function will be executed when the button is clicked). It's placed in the left_frame with a white background.
select_image_button.pack(pady=15)
print(file_path)

# contrast_stretch_image_button = tk.Button(left_frame, text="Apply Contrast Stretching",
#                          command=lambda: apply_contrast_stretching(file_path), bg="white")      #  use a lambda function to call apply_contrast_stretching only when the button is clicked and file_path has a valid image path

contrast_stretch_image_button = tk.Button(left_frame, text="Apply Contrast Stretching",
                                          command=lambda: apply_filter("Contrast stretch"), bg="white")
contrast_stretch_image_button.pack(pady=15)

median_filter_button = tk.Button(left_frame, text="Apply Median Filter",
                                          command=lambda: apply_filter("Median"), bg="white")
median_filter_button.pack(pady=15)

sharpen_filter_button = tk.Button(left_frame, text="Apply Sharpen Filter",
                                          command=lambda: apply_filter("Sharpen"), bg="white")
sharpen_filter_button.pack(pady=15)

pen_size_frame = tk.Frame(left_frame, bg="white")
pen_size_frame.pack(pady=5)

pen_size_1 = tk.Radiobutton(
    pen_size_frame, text="Small", value=3, command=lambda: change_size(3), bg="white")
pen_size_1.pack(side="left")

pen_size_2 = tk.Radiobutton(
    pen_size_frame, text="Medium", value=5, command=lambda: change_size(5), bg="white")
pen_size_2.pack(side="left")
pen_size_2.select()

pen_size_3 = tk.Radiobutton(
    pen_size_frame, text="Large", value=7, command=lambda: change_size(7), bg="white")
pen_size_3.pack(side="left")

filter_label = tk.Label(left_frame, text="Select Filter", bg="white")
filter_label.pack()
filter_combobox = ttk.Combobox(left_frame, values=["Black and White", "Blur",
                                                   "Emboss", "Sharpen", "Smooth"])
filter_combobox.pack()

filter_combobox.bind("<<ComboboxSelected>>",
                     lambda event: apply_filter(filter_combobox.get()))


root.mainloop()
