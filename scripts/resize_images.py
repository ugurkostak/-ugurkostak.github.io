import os
from PIL import Image

input_dir = os.path.join(os.path.dirname(__file__), '../assets/photos')
output_dir = os.path.join(input_dir, 'small')

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Resize images
for file_name in os.listdir(input_dir):
    input_file_path = os.path.join(input_dir, file_name)
    output_file_path = os.path.join(output_dir, file_name)

    # Check if the file is an image
    if file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
        try:
            with Image.open(input_file_path) as img:
                img.thumbnail((800, 800))  # Resize to fit within 800x800, maintaining aspect ratio
                img.save(output_file_path)
                print(f"Resized: {file_name}")
        except Exception as e:
            print(f"Error resizing {file_name}: {e}")
