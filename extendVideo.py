import subprocess
import os

import subprocess
import os

def extend_video(video_path, files_txt, output_file, num_repeats):
    # Extract directory and filename
    directory, filename = os.path.split(video_path)
    name, ext = os.path.splitext(filename)
    
    # Create files.txt
    with open(files_txt, 'w') as f:
        for _ in range(num_repeats):
            f.write(f"file '{video_path}'\n")

    print(f'File list created with {num_repeats} entries in {files_txt}')

    # Construct the new output file path
    output_file = os.path.join(directory, f"{name}_4x{ext}")

    # Run FFmpeg command
    ffmpeg_command = [
        'ffmpeg', '-f', 'concat', '-safe', '0',
        '-i', files_txt, '-c:v', 'hap', '-format', 'hap_alpha', '-pix_fmt', 'rgba',
        output_file
    ]

    try:
        subprocess.run(ffmpeg_command, check=True)
        print(f'FFmpeg command executed successfully. Output file: {output_file}')
    except subprocess.CalledProcessError as e:
        print(f'Error occurred: {e}')



def convert_and_export_video(video_path):
    # Extract directory and filename
    directory, filename = os.path.split(video_path)
    name, ext = os.path.splitext(filename)

    # Define unique vertical resolutions and aspect ratios
    resolutions = [
        ('1080x1920', '9:16'),
        ('720x1280', '3:4'),
        ('720x1200', '3:5')
    ]

    for resolution, aspect_ratio in resolutions:
        output_file = os.path.join(directory, f"{name}_{resolution.replace('x', 'x')}_{aspect_ratio.replace(':', 'x')}{ext}")
        
        ffmpeg_command = [
            'ffmpeg', '-i', video_path,
            '-vf', f"scale={resolution},setsar=1",
            '-c:v', 'hap', '-format', 'hap_alpha', '-pix_fmt', 'rgba',
            output_file
        ]

        try:
            subprocess.run(ffmpeg_command, check=True)
            print(f'Converted video saved as: {output_file}')
        except subprocess.CalledProcessError as e:
            print(f'Error occurred: {e}')

# Example usage
video_path = r'C:\Users\wenyi\Desktop\granite_sprite_test\Videos\Flamingo_01.HD.4x.mov'
files_txt = 'files.txt'
output_file = 'extended_output.mov'
num_repeats = 25

# extend_video(video_path, files_txt, output_file, num_repeats)
convert_and_export_video(video_path)