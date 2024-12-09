import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

DEFAULT_SCRIPT_PATH = r"C:\Users\vvox\Documents\GitHub\video_batch_utilities\nuke_utils\batchConvertNK\batchConvertNK.py"

def run_batch_convert(script_path, folder_path, image_format):
    if script_path and folder_path and image_format:
        command = f'nuke -t {script_path} {folder_path} {image_format}'
        subprocess.call(command, shell=True)
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def browse_file(entry):
    file_path = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

def browse_folder(entry):
    folder_path = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, folder_path)

def create_ui():
    root = tk.Tk()
    root.title("Batch Convert NK")

    tk.Label(root, text="Python Script Path").grid(row=0, column=0, padx=10, pady=5)
    script_path_entry = tk.Entry(root, width=50)
    script_path_entry.insert(0, DEFAULT_SCRIPT_PATH)
    script_path_entry.grid(row=0, column=1, padx=10, pady=5)
    tk.Button(root, text="Browse", command=lambda: browse_file(script_path_entry)).grid(row=0, column=2, padx=10, pady=5)

    tk.Label(root, text="Folder Path").grid(row=1, column=0, padx=10, pady=5)
    folder_path_entry = tk.Entry(root, width=50)
    folder_path_entry.grid(row=1, column=1, padx=10, pady=5)
    tk.Button(root, text="Browse", command=lambda: browse_folder(folder_path_entry)).grid(row=1, column=2, padx=10, pady=5)

    tk.Label(root, text="Image Format").grid(row=2, column=0, padx=10, pady=5)
    image_format_entry = tk.Entry(root, width=50)
    image_format_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Button(root, text="Run", command=lambda: run_batch_convert(script_path_entry.get(), folder_path_entry.get(), image_format_entry.get())).grid(row=3, column=0, columnspan=3, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_ui()