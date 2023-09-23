#!/bin/bash

# Set the directory containing the still images
STILLS_DIR="stills"

# Check if the directory exists
if [ ! -d "$STILLS_DIR" ]; then
    echo "Directory $STILLS_DIR does not exist."
    exit 1
fi

# Generate a list of images in the directory
IMG_LIST=$(find "$STILLS_DIR" -type f \( -iname "*.jpg" -o -iname "*.png" -o -iname "*.jpeg" \) | sort)

# echo $IMG_LIST

# Check if we found any images
if [ -z "$IMG_LIST" ]; then
    echo "No images found in $STILLS_DIR."
    exit 1
fi

# Use ffmpeg to generate the video
# Note: ffmpeg interprets the -r flag as 'fps', so for 300ms per image, that's roughly 3.33 fps (1 frame every 0.3 seconds)
ffmpeg -y -f concat -safe 0 -i <(for f in $IMG_LIST; do echo "file '$PWD/$f'"; done) -vf "fps=1/0.1" -pix_fmt yuv420p old-zeke.mp4

echo "Video generated as old-zeke.mp4"
