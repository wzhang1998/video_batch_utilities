import os
import subprocess
from PIL import Image

import os

# Define your video file and output settings
video_file = r"D:\Efiles\Unreal_Projects\20240321_PipelineDebug\Medias\Functionless.mp4"
output_folder = os.path.dirname(video_file)
output_gif = os.path.join(output_folder, "output.gif")
frame_rate = 10  # Adjust based on your preference

# Ensure the output directory exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Step 1: Extract frames from the video, making black transparent
# Using ffmpeg to extract frames and convert black to transparent
ffmpeg_cmd = f"ffmpeg -i {video_file} -vf fps={frame_rate},colorkey=0x000000:0.1:0.1 {output_folder}/frame_%04d.png"
subprocess.run(ffmpeg_cmd, shell=True)

# Step 2: Compile frames into a transparent GIF using Pillow
frames = []

# Load all the frames and append to list
for frame in sorted(os.listdir(output_folder)):
    if frame.endswith(".png"):
        frame_path = os.path.join(output_folder, frame)
        frames.append(Image.open(frame_path))

# Save the frames as a GIF
frames[0].save(output_gif, save_all=True, append_images=frames[1:], optimize=False, duration=40, loop=0, transparency=0)

print(f"GIF created: {output_gif}")
