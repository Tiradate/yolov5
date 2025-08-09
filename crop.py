import os
import shutil

parent_folder = r"D:\LPRqc"
destination_folder = r"D:\LPRqc\Crop"

# List all subdirectories in the parent folder
subdirectories = [os.path.join(parent_folder, folder) for folder in os.listdir(parent_folder)]

# Filter subdirectories to include only "Entrance" and "Exit" folders
filtered_directories = [folder for folder in subdirectories if folder.endswith(("Entrance", "Exit"))]

for folder in filtered_directories:
    entrance_or_exit = os.path.basename(folder)
    date_folders = os.listdir(folder)
    for date_folder in date_folders:
        date_path = os.path.join(folder, date_folder)
        if os.path.isdir(date_path):
            time_folders = os.listdir(date_path)
            for time_folder in time_folders:
                time_path = os.path.join(date_path, time_folder)
                if os.path.isdir(time_path):
                    image_files = [file for file in os.listdir(time_path) if file.endswith((".jpg", ".jpeg", ".png"))]
                    if image_files:
                        source_file = os.path.join(time_path, image_files[0])
                        file_name = f"{entrance_or_exit}_{date_folder}_{image_files[0]}"
                        destination_file = os.path.join(destination_folder, file_name)
                        shutil.copy2(source_file, destination_file)
