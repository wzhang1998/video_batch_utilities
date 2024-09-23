import os
import OpenEXR
import Imath
from PIL import Image
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox

def resize_exr(input_path, output_path, scale=0.5):
    # Open the EXR file
    exr_file = OpenEXR.InputFile(input_path)
    
    # Get the data window and compute the size
    dw = exr_file.header()['dataWindow']
    width = dw.max.x - dw.min.x + 1
    height = dw.max.y - dw.min.y + 1
    
    # Read the channels
    channels = exr_file.header()['channels'].keys()
    channels_data = {channel: exr_file.channel(channel, Imath.PixelType(Imath.PixelType.FLOAT)) for channel in channels}
    
    # Convert the channels to numpy arrays
    channels_data = {channel: np.frombuffer(data, dtype=np.float32).reshape(height, width) for channel, data in channels_data.items()}
    
    # Resize the channels
    new_width = int(width * scale)
    new_height = int(height * scale)
    resized_channels = {channel: Image.fromarray(data).resize((new_width, new_height), Image.LANCZOS) for channel, data in channels_data.items()}
    
    # Convert the resized channels back to numpy arrays
    resized_channels = {channel: np.array(data) for channel, data in resized_channels.items()}
    
    # Create an output EXR file
    exr_out = OpenEXR.OutputFile(output_path, OpenEXR.Header(new_width, new_height))
    
    # Write the resized channels to the output file
    exr_out.writePixels({channel: data.tobytes() for channel, data in resized_channels.items()})
    exr_out.close()

def process_directory(input_dir, output_dir, scale=0.5):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.endswith('.exr'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"resized_{filename}")
            resize_exr(input_path, output_path, scale)
            print(f"Resized {filename} and saved to {output_path}")

def select_input_directory():
    input_dir = filedialog.askdirectory(title="Select Input Directory")
    input_dir_var.set(input_dir)

def select_output_directory():
    output_dir = filedialog.askdirectory(title="Select Output Directory")
    output_dir_var.set(output_dir)

def start_processing():
    input_dir = input_dir_var.get()
    output_dir = output_dir_var.get()
    if not input_dir or not output_dir:
        messagebox.showerror("Error", "Please select both input and output directories.")
        return
    process_directory(input_dir, output_dir)
    messagebox.showinfo("Success", "Processing complete.")

# Create the main window
root = tk.Tk()
root.title("EXR Resize Tool")

# Create and set the input directory variable
input_dir_var = tk.StringVar()
output_dir_var = tk.StringVar()

# Create the UI elements
tk.Label(root, text="Input Directory:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=input_dir_var, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_input_directory).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Output Directory:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=output_dir_var, width=50).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_output_directory).grid(row=1, column=2, padx=10, pady=10)

tk.Button(root, text="Start Processing", command=start_processing).grid(row=2, column=0, columnspan=3, pady=20)

# Run the main loop
root.mainloop()