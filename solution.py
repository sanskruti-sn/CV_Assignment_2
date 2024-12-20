import cv2 # type: ignore
import numpy as np
import os

def split_price_tags(img_path, output_folder, rows=6, cols=3):
    """
    Splits an image into smaller sections based on specified rows and columns
    and saves the sections to the specified output folder.
    
    Parameters:
        img_path (str): Path to the input image.
        output_folder (str): Folder to save the cropped images.
        rows (int): Number of rows to split the image into. Default is 6.
        cols (int): Number of columns to split the image into. Default is 3.
    """
    # Read the image
    img = cv2.imread(img_path)
    if img is None:
        print(f"Error: Unable to read the image at '{img_path}'. Check the file path.")
        return

    height, width, _ = img.shape
    print(f"Image Dimensions: {height}x{width} (HxW)")

    # Calculate dimensions of each segment
    split_height = -(-height // rows)  # Ceiling integer division for height
    split_width = -(-width // cols)    # Ceiling integer division for width
    print(f"Each segment size: {split_height}x{split_width} (HxW)")

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Split the image and save each segment
    for row in range(rows):
        for col in range(cols):
            # Define cropping boundaries
            x1, y1 = col * split_width, row * split_height
            x2, y2 = min((col + 1) * split_width, width), min((row + 1) * split_height, height)

            # Extract the segment
            segment = img[y1:y2, x1:x2]

            # Save the segment with a descriptive filename
            filename = f"price_tag_row{row + 1}_col{col + 1}.jpg"
            filepath = os.path.join(output_folder, filename)
            success = cv2.imwrite(filepath, segment)
            if success:
                print(f"Saved: {filepath}")
            else:
                print(f"Error: Failed to save {filename}")

    print(f"Splitting completed! {rows * cols} images saved in '{output_folder}'.")

# Parameters for the script
image_path = r'C:\Users\Sanskruti\OneDrive\Desktop\CV_Assignments\CV_Assignment_2\pricetagimage.jpg'
output_folder = "cropped_images"

# Call the function
split_price_tags(image_path, output_folder)
