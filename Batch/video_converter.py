# pip install moviepy
import os
from moviepy.editor import VideoFileClip

def convert_avi_to_mp4(input_directory, resize=None):
    for filename in os.listdir(input_directory):
        if filename.endswith(".avi"):
            avi_filepath = os.path.join(input_directory, filename)
            mp4_filepath = os.path.join(input_directory, filename.replace(".avi", ".mp4"))

            # Convert .avi to .mp4 using moviepy
            video_clip = VideoFileClip(avi_filepath)
            
            if resize is not None:
                width, height = resize
                aspect_ratio = width / height
                video_clip_aspect_ratio = video_clip.w / video_clip.h

                if video_clip_aspect_ratio > aspect_ratio:
                    # The video is wider than the desired aspect ratio
                    new_width = int(video_clip.h * aspect_ratio)
                    offset_x = int((video_clip.w - new_width) / 2)
                    video_clip = video_clip.crop(x_center=video_clip.w/2, width=new_width, y1=0, y2=video_clip.h)
                else:
                    # The video is taller than the desired aspect ratio
                    new_height = int(video_clip.w / aspect_ratio)
                    offset_y = int((video_clip.h - new_height) / 2)
                    video_clip = video_clip.crop(y_center=video_clip.h/2, height=new_height, x1=0, x2=video_clip.w)
            
            # Resize the video to the new size
            video_clip = video_clip.resize(resize)
            
            video_clip.write_videofile(mp4_filepath, codec='libx264', audio_codec='aac',
                           ffmpeg_params=['-profile:v', 'baseline', '-pix_fmt', 'yuv420p'])
            
            # Remove the original .avi file if needed
            # os.remove(avi_filepath)

            print(f"Conversion complete: {avi_filepath} -> {mp4_filepath}")

if __name__ == "__main__":

    # selected_directory = input("Enter the directory path where .avi files are located: ")

    # Set the input directory to the directory where the script is located
    selected_directory = os.path.dirname(os.path.realpath(__file__))

    resize_option = input("Enter the new size for the videos as 'width,height' or leave blank to keep original size: ")
    
    
    resize = None
    if resize_option:
        width, height = map(int, resize_option.split(','))
        resize = (width, height)
    
    convert_avi_to_mp4(selected_directory, resize)