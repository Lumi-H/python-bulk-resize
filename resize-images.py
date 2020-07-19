from PIL import Image
import os
from resizeimage import resizeimage

def generate_new_title(category, ID, dimensions):
    return category + "_" + str(ID) + "_" + str(dimensions) + "px.jpeg"

def resize_single_image(image_file_path, new_title):
    with open(image_file_path, 'r+b') as f:
        with Image.open(f) as image:
            width, height = image.size
            if height >= width:
                width_to_height_ratio = width/height
                new_height = 600
                new_width = int(new_height * width_to_height_ratio)
            else:
                height_to_width_ratio = height/width
                print(height_to_width_ratio)
                new_width = 600
                new_height = int(new_width * height_to_width_ratio)
            cover = resizeimage.resize_cover(image, [new_width, new_height], validate=False)
            new_title_with_path = image_file_path + new_title
            cover.save(new_title_with_path, image.format)

def get_images_in_folder(folder_path):
     arr = os.listdir(folder_path)
     return arr

def resize_images_in_folder(file_array, folder_path, category, ID):
    for image_title in file_array:
        image_path = folder_path+image_title
        new_title = generate_new_title(category, ID, 600)
        ID = ID + 1
        resize_single_image(image_path, new_title)





def main():
    array = get_images_in_folder("path/to/folder")
    resize_images_in_folder(array, "path/to/folder", "category-1", 1)

main()
