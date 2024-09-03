import os
import json
import shutil

def find_and_copy_folders(root_path, target_display_name, destination_path):
    print(f"Starting search in: {root_path}")
    # Walk through all folders under the root path
    for foldername, subfolders, filenames in os.walk(root_path):
        print(f"Checking folder: {foldername}")
        # Check if metadata.json is in the current folder
        if 'metadata.json' in filenames:
            metadata_file_path = os.path.join(foldername, 'metadata.json')
            print(f"Found metadata.json in: {foldername}")
            
            try:
                # Open and read the metadata.json file
                with open(metadata_file_path, 'r') as f:
                    data = json.load(f)

                # Check if displayName matches the target_display_name
                if data.get('user', {}).get('displayName') == target_display_name:
                    # Copy the entire folder to the destination path
                    destination_folder_path = os.path.join(destination_path, os.path.basename(foldername))
                    shutil.copytree(foldername, destination_folder_path)
                    print(f"Copied folder: {foldername} to {destination_folder_path}")

            except (json.JSONDecodeError, FileNotFoundError) as e:
                print(f"Error reading {metadata_file_path}: {e}")

if __name__ == "__main__":
    # Define paths and target display name
    root_path = r"\\vvox-nas-1\PROJECTS\_____ASSETS\_VVOX BRAND\TEAM FILES\3DScans\\"  # Replace with the path you want to search through
    destination_path = "C:\\Users\\wenyi\\Desktop\\files"  # Destination directory on your desktop
    target_display_name = "Wenyi Zhang"
    
    # Ensure the destination directory exists
    os.makedirs(destination_path, exist_ok=True)
    print(f"Destination directory: {destination_path}")

    # Call the function to find and copy folders
    find_and_copy_folders(root_path, target_display_name, destination_path)