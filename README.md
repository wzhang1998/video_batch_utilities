# Video Converter

This Python script converts video files from AVI format to MP4 format. It uses the `moviepy` library to perform the conversion. Optionally, it can also resize the videos while maintaining the aspect ratio.

## Prerequisites

You need to have Python installed on your system to run this script. You also need the `moviepy` library, which you can install with pip:

```bash
pip install moviepy
```

## Usage

To use this script, you need to have your AVI files in the same directory as the script. Then, you can run the script with Python:

```bash
python video_converter.py
```

When you run the script, it will ask you to enter the new size for the videos as `width,height`, for example `1080,1920`. If you want to keep the original size, you can just press Enter without typing anything.

The script will convert all AVI files in the directory to MP4 format, and it will print a message for each file it converts.


## Configuration

You can configure the script by modifying the following variables in the script:

- `selected_directory`: Set the input directory where AVI files are located.
- `resize`: Set the new size for the videos (width, height). Leave it as `None` to keep the original size.

