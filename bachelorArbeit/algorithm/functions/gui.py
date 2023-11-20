import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import ttk
from medianFilterFunc import apply_median_filter, apply_sharpen_filter
from contrastStretchFunc import apply_contrast_stretching

root = tk.Tk()
root.geometry("1000x600")
root.title("Image Drawing Tool")

pen_color = "black"
pen_size = 5
file_path = ""
original_image = None  # Global variable to store the original image
filtered_image = None  # Global variable to store the result after each filter
size = 7

def add_image():
    global file_path, original_image, filtered_image
    file_path = filedialog.askopenfilename(
        initialdir="./petCTimagesBMP")    # This line opens a file dialog box, which allows the user to select an image file. The askopenfilename function is a part of the filedialog module, and it opens a standard file dialog. The initialdir parameter sets the initial directory that the file dialog should open in. The selected file's path is stored in the file_path variable.
    original_image = Image.open(file_path)   # This line uses the Python Imaging Library (PIL), also known as Pillow, to open the selected image file using the file path stored in file_path. The image is then loaded into the image variable.
    canvas.config(width=original_image.width, height=original_image.height)       # This line updates the dimensions of a Tkinter canvas widget (canvas) to match the dimensions of the resized image. It sets the canvas width and height to match the resized image's width and height.
    image = ImageTk.PhotoImage(original_image)       # Here, the resized image is converted into a Tkinter PhotoImage object using the ImageTk.PhotoImage function. This allows you to display the image in a Tkinter canvas.
    # canvas.image = image        # This line stores the PhotoImage object in the canvas widget, making sure it's not garbage collected.
    # canvas.create_image(0, 0, image=image, anchor="nw")     # Finally, this line adds the image to the canvas at the coordinates (0, 0) with an anchor point at the northwest ("nw") corner. This will display the image on the canvas at the specified location.
    canvas.image = ImageTk.PhotoImage(original_image)
    canvas.create_image(0, 0, image=canvas.image, anchor="nw")
    print("Image Dimensions:", original_image.size)
    filtered_image = original_image.copy()  # Initialize filtered_image with the original image
    print(file_path)

def apply_filter(filter):
    global file_path, original_image, filtered_image
    if not file_path:
        print("Please select an image first.")
        return

    if filter == "Contrast stretch":
        # image = apply_contrast_stretching(image_np)
        filtered_image = apply_contrast_stretching(np.array(filtered_image))
    elif filter == "Median":
        # image = apply_median_filter(image_np, 3)
        filtered_image = apply_median_filter(np.array(filtered_image), size)
    elif filter == "Sharpen":
        filtered_image = apply_sharpen_filter(np.array(filtered_image))

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
select_image_button.pack(pady=15)

print(file_path)
# Get Tkinter version using Tcl command
tcl_version = tk.Tcl().eval('info patchlevel')
print("Tkinter version:", tcl_version)

# Contrast Filter Button
contrast_stretch_image_button = tk.Button(left_frame, text="Apply Contrast Stretching",
                                          command=lambda: apply_filter("Contrast stretch"))
contrast_stretch_image_button.pack(pady=15)


# Median Filter Button
median_filter_button = tk.Button(left_frame, text="Apply Median Filter",
                                          command=lambda: apply_filter("Median"))
median_filter_button.pack()

median_filter_ksize_select = ttk.Combobox(left_frame, values=["3", "5", "7", "9"], width=5)
median_filter_ksize_select.pack()

median_filter_ksize_select.bind("<<ComboboxSelected>>", lambda event: select_ksize(median_filter_ksize_select.get()))


# Sharpen Filter Button
sharpen_filter_button = tk.Button(left_frame, text="Apply Sharpen Filter",
                                          command=lambda: apply_filter("Sharpen"))
sharpen_filter_button.pack(pady=15)

root.mainloop()
