#!/bin/env python3
import os
from PIL import Image
import pdfrw

# Define the size of the A3 page in pixels and the size of each image in the grid
A3_WIDTH, A3_HEIGHT = (3508, 4960)
IMAGE_WIDTH, IMAGE_HEIGHT = (1122, 1594)

# Define the number of images to place in each row and column of the grid
GRID_ROWS, GRID_COLS = (3, 3)

# Image folder
IMG_FOLDER = "."

# Create a new PDF file to save the combined pages
pdf_path = "./back-a3.pdf"

# Delete pdf if already exists
if os.path.exists(pdf_path):
    os.remove(pdf_path)

# Calculate the padding between images
padding_x = (A3_WIDTH - GRID_COLS * IMAGE_WIDTH) // (GRID_COLS + 1)
padding_y = (A3_HEIGHT - GRID_ROWS * IMAGE_HEIGHT) // (GRID_ROWS + 1)

# Create a new page in the PDF for the next set of images
page_image = Image.new("RGB", (A3_WIDTH, A3_HEIGHT), (255, 255, 255))

# Loop through the next set of images and add them to the grid
for j in range(GRID_ROWS):
    for k in range(GRID_COLS):
        if True:
            # Open the image file and resize it to fit in the grid
            image_file = "template.jpg"
            image_path = os.path.join(IMG_FOLDER, image_file)
            image = Image.open(image_path)
            image = image.resize((IMAGE_WIDTH, IMAGE_HEIGHT), Image.LANCZOS)

# Calculate the position of the image in the grid with padding
            x_pos = k * IMAGE_WIDTH + (1 + 1) * padding_x
            y_pos = j * IMAGE_HEIGHT + (1 + 1) * padding_y

            # Add the image to the grid on the current page
            page_image.paste(image, (x_pos, y_pos))

# Save the page as a temporary PDF
page_image.save(pdf_path, "PDF", resolution=100.0)
