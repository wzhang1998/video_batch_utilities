#!/usr/bin/python

import nuke
import os
import sys
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Convert EXR sequence to 16-bit PNG sequence using Nuke')
    parser.add_argument('input_path', help='Path to EXR sequence directory')
    return parser.parse_args()

def setup_colorspace_node(input_node):
    """Set up colorspace node for Rec.709 conversion"""
    colorspace = nuke.nodes.Colorspace(inputs=[input_node])
    colorspace['colorspace_in'].setValue('linear')
    colorspace['colorspace_out'].setValue('rec709')
    return colorspace

def convert_sequence(input_path):
    """Convert EXR sequence to PNG using Nuke nodes"""
    # Get the directory containing the EXR files
    input_dir = os.path.dirname(input_path)
    
    # Create output directory
    output_dir = os.path.join(input_dir, 'png_output')
    os.makedirs(output_dir, exist_ok=True)
    
    # Set up Nuke node tree
    read_node = nuke.nodes.Read(file=input_path)
    
    # Add colorspace conversion
    colorspace_node = setup_colorspace_node(read_node)
    
    # Set up Write node
    output_path = os.path.join(output_dir, 'frame_%04d.png')
    write_node = nuke.nodes.Write(
        inputs=[colorspace_node],
        file=output_path,
        file_type='png',
        datatype='16',
        channels='rgb'
    )
    
    # Get frame range from Read node
    first_frame = read_node.firstFrame()
    last_frame = read_node.lastFrame()
    
    # Execute the node tree
    try:
        nuke.execute(write_node, first_frame, last_frame)
        print(f"Successfully converted sequence: {input_path}")
    except Exception as e:
        print(f"Error converting sequence: {str(e)}")
    finally:
        # Clean up nodes
        nuke.delete(write_node)
        nuke.delete(colorspace_node)
        nuke.delete(read_node)

def main():
    args = parse_args()
    
    # Check if path exists
    if not os.path.exists(args.input_path):
        print(f"Error: Input path {args.input_path} does not exist")
        sys.exit(1)
    
    # Convert sequence
    convert_sequence(args.input_path)

if __name__ == '__main__':
    main()
