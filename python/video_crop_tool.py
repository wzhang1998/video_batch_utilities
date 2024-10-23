import os
from PIL import Image
from pathlib import Path

def crop_tiff_sequence(input_dir, output_dir, target_width=2000, target_height=2000):
    # Ensure input and output directories exist
    if not os.path.isdir(input_dir):
        raise ValueError(f"Input directory does not exist: {input_dir}")
    os.makedirs(output_dir, exist_ok=True)

    # Get all .tiff files in the input directory
    tiff_files = sorted(Path(input_dir).glob('*.tif'))
    
    if not tiff_files:
        raise ValueError(f"No .tiff files found in {input_dir}")

    for tiff_file in tiff_files:
        with Image.open(tiff_file) as img:
            # Check if the image needs cropping
            if img.width != 4000 or img.height != 2000:
                print(f"Warning: {tiff_file.name} is not 4000x2000. Skipping.")
                continue

            # Calculate the left and right crop boundaries
            left = (img.width - target_width) // 2
            right = left + target_width

            # Crop the image
            cropped_img = img.crop((left, 0, right, target_height))

            # Save the cropped image
            output_path = os.path.join(output_dir, tiff_file.name)
            cropped_img.save(output_path)
            print(f"Cropped and saved: {output_path}")

    print(f"Cropping complete. Processed {len(tiff_files)} files.")

# Example usage
if __name__ == "__main__":
    input_directory = r"\\Vvox-nas-1\projects\PUREDEZIGN_SPHERE\005_Render\WZ\240918\0918_2k_spcamforUpscaleTest\tiff"
    output_directory = r"\\Vvox-nas-1\projects\PUREDEZIGN_SPHERE\005_Render\WZ\240918\0918_2k_spcamforUpscaleTest\tiff_cropped"
    crop_tiff_sequence(input_directory, output_directory)
