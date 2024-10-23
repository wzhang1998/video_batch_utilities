import os
import subprocess
from pathlib import Path

def encode_exr_to_hapq(input_dir, output_file, framerate=24):
    # Ensure input directory exists
    if not os.path.isdir(input_dir):
        raise ValueError(f"Input directory does not exist: {input_dir}")

    # Get all .exr files in the input directory
    exr_files = sorted(Path(input_dir).glob('*.exr'))
    
    if not exr_files:
        raise ValueError(f"No .exr files found in {input_dir}")

    # Detect the naming pattern
    first_file = exr_files[0].name
    prefix = first_file.rsplit('.', 1)[0][:-4]  # Assuming the last 4 characters before the extension are digits
    pattern = f"{prefix}%04d.exr"  # Adjust the number of digits if necessary

    # Construct the ffmpeg command
    ffmpeg_cmd = [
        'ffmpeg',
        '-framerate', str(framerate),
        '-i', os.path.join(input_dir, pattern),
        '-c:v', 'hap',
        '-format', 'hap_q',
        '-pix_fmt', 'rgba',  # Ensure the pixel format is set to RGBA
        '-y',  # Overwrite output file if it exists
        output_file
    ]

    # Run the ffmpeg command with real-time output
    process = subprocess.Popen(ffmpeg_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    for line in process.stdout:
        print(line, end='')  # Print each line of output in real-time

    process.wait()
    if process.returncode == 0:
        print(f"Successfully encoded {len(exr_files)} frames to {output_file}")
    else:
        print(f"Error during encoding. FFmpeg exited with code {process.returncode}")

# Example usage
if __name__ == "__main__":
    input_directory = r"\\Vvox-nas-1\projects\GRANITE_PROPERTIES\011_Unreal\MovieRenders"
    output_file = r"\\Vvox-nas-1\projects\GRANITE_PROPERTIES\011_Unreal\240917_desert_12k.mov"
    encode_exr_to_hapq(input_directory, output_file)
