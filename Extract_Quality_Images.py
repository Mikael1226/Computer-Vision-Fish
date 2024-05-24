import os
import cv2
import shutil

def calculate_total_intensity(output_folders):
    images_intensity = []

    for output_folder in output_folders:
        if os.path.isdir(output_folder):
            for image_file in os.listdir(output_folder):
                image_path = os.path.join(output_folder, image_file)
                if os.path.isfile(image_path):
                    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                    if image is not None:
                        total_intensity = image.sum()
                        images_intensity.append((image_file, total_intensity))
                    else:
                        print(f"Error reading image : {image_path}")
        else:
            print(f"The specified path is not a repository : {output_folder}")

    return images_intensity

def save_images(output_folders, low_intensity_folder, high_intensity_folder, images_intensity):
    os.makedirs(low_intensity_folder, exist_ok=True)
    os.makedirs(high_intensity_folder, exist_ok=True)

    for image_name, intensity in images_intensity:
        for output_folder in output_folders:
            image_path = os.path.join(output_folder, image_name)
            if os.path.exists(image_path):  
                if intensity < threshold:
                    shutil.copy(image_path, low_intensity_folder)
                else:
                    shutil.copy(image_path, high_intensity_folder)
            else:
                print(f"This file does not exist : {image_path}")


main_folder = "path/to/your/main_folder"


output_folders = [os.path.join(main_folder, folder) for folder in os.listdir(main_folder)]


images_intensity = calculate_total_intensity(output_folders)


low_intensity_folder = "/path/you/want/to/fix/low_intensity_folder"
high_intensity_folder = "/path/you/want/to/fix/high_intensity_folder"


threshold = 146467310


save_images(output_folders, low_intensity_folder, high_intensity_folder, images_intensity)


shutil.make_archive("path_to_the_folder_images_low_intensity", 'zip', low_intensity_folder)
shutil.make_archive("path_to_the_folder_images_high_intensity", 'zip', high_intensity_folder)

