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
IMG_FOLDER = "id"

# Create a new PDF file to save the combined pages
pdf_path = "./id_cards.pdf"

# Delete pdf if already exists
if os.path.exists(pdf_path):
    os.remove(pdf_path)

# Initialize a PDF writer
pdf_writer = pdfrw.PdfWriter()

# Loop through each image file in the directory
image_files = sorted(os.listdir(IMG_FOLDER))
number_of_images = len(image_files)
number_of_pages = number_of_images // (GRID_ROWS * GRID_COLS)
current_page = 1

# Calculate the padding between images
padding_x = (A3_WIDTH - GRID_COLS * IMAGE_WIDTH) // (GRID_COLS + 1)
padding_y = (A3_HEIGHT - GRID_ROWS * IMAGE_HEIGHT) // (GRID_ROWS + 1)

for i in range(0, len(image_files), GRID_ROWS * GRID_COLS):
    # Create a new page in the PDF for the next set of images
    page_image = Image.new("RGB", (A3_WIDTH, A3_HEIGHT), (255, 255, 255))

    # Loop through the next set of images and add them to the grid
    for j in range(GRID_ROWS):
        for k in range(GRID_COLS):
            image_index = i + j * GRID_COLS + k
            if image_index < len(image_files):
                # Open the image file and resize it to fit in the grid
                image_file = image_files[image_index]
                image_path = os.path.join(IMG_FOLDER, image_file)
                image = Image.open(image_path)
                image = image.resize((IMAGE_WIDTH, IMAGE_HEIGHT), Image.LANCZOS)

# Calculate the position of the image in the grid with padding
                x_pos = k * IMAGE_WIDTH + (1 + 1) * padding_x
                y_pos = j * IMAGE_HEIGHT + (1 + 1) * padding_y

                # Add the image to the grid on the current page
                page_image.paste(image, (x_pos, y_pos))

    # Save the page as a temporary PDF
    temp_pdf_path = "temp_page.pdf"
    page_image.save(temp_pdf_path, "PDF", resolution=100.0)

    # Add the temporary PDF page to the PDF writer
    pdf_writer.addPage(pdfrw.PdfReader(temp_pdf_path).pages[0])

    # Remove the temporary PDF file
    os.remove(temp_pdf_path)
    print(f"Page {current_page} / {number_of_pages} done")
    current_page += 1

print("Merging all pages into one pdf")
# Save the merged PDF pages to the output PDF file
pdf_writer.write(pdf_path)
