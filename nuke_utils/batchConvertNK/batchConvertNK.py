import os
import sys
import nuke

if len(sys.argv) != 3:
    print('Usage: nuke -t batchConvertNK.py <folder_path> <image_format>')
    sys.exit(-1)

folder_path = sys.argv[1]
image_format = sys.argv[2]

print(f'Folder path: {folder_path}')
print(f'Image format: {image_format}')

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff', '.tif', '.exr')):
            file_path = os.path.join(root, file).replace('\\', '/')
            base_name = os.path.splitext(os.path.basename(file_path))[0]
            dir_name = os.path.dirname(file_path)
            out_name = os.path.join(dir_name, f'{base_name}.{image_format}').replace('\\', '/')
            
            print(f'Processing file: {file_path}')
            print(f'Output file: {out_name}')
            
            read_node = nuke.nodes.Read(file=file_path)
            write_node = nuke.nodes.Write(file=out_name, inputs=[read_node])
            nuke.execute(write_node, 1, 1)
            print(f'Finished processing file: {file_path}')

# example
# nuke -t batchConvertNK.py Z:\GRANITE_PROPERTIES\005_Render\WZ\241209\no_shot exr