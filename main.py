import os
from PIL import Image

folder_path = "path/to/folder"

for file in os.listdir(folder_path):
    if file.endswith(".raw"):
        with open(os.path.join(folder_path, file), 'rb') as f:
            # Get the size of the image
            f.seek(0, 2) # go to end of file
            size = f.tell()
            width = int(size ** 0.5)
            height = int(size / width)
            f.seek(0) # return to beginning of file
            
            # Create image object and save it
            image = Image.frombytes('RGB', (width, height), f.read(), 'raw')
            image.save(os.path.splitext(os.path.join(folder_path, file))[0] + ".png", "PNG")
