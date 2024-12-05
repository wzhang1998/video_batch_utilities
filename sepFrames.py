import os
import shutil

def copy_odd_frames(source_dir, dest_dir):
    # Create destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # Get list of files in source directory
    files = os.listdir(source_dir)
    
    # Copy odd-numbered frames
    for filename in files:
        # Extract frame number from filename (removing extension first)
        try:
            base_name = os.path.splitext(filename)[0]  # Remove extension
            frame_number = int(base_name.split('_')[-1])
            if frame_number % 2 != 0:  # Check if frame number is odd
                src_path = os.path.join(source_dir, filename)
                dst_path = os.path.join(dest_dir, filename)
                shutil.copy2(src_path, dst_path)
                print(f"Copied frame {frame_number}: {filename}")
        except ValueError:
            print(f"Skipping {filename} - unable to extract frame number")

if __name__ == "__main__":
    # Set your source and destination directories
    source_directory = r"\\Vvox-nas-1\projects\PUREDEZIGN_SPHERE\005_Render\WZ\241028\005_s01_Desert_Sequence_v003_60fps_1350_1650"
    destination_directory = r"\\Vvox-nas-1\projects\PUREDEZIGN_SPHERE\005_Render\WZ\241028\New folder"
    
    copy_odd_frames(source_directory, destination_directory) 