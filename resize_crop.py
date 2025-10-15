#!/usr/bin/env python
import os
from atomicfile import AtomicFile
from PIL import Image

# The desired size that all images in the data directory should
# be normalized to.
# DESIRED_SIZE = (500, 500)
DESIRED_WIDTH = 500

for root, subdirs, files in os.walk('data'):
    for file in files:
        path = os.path.join(root, file)
        try:
            print("Opening " + path)
            im = Image.open(path)
            if im.width != DESIRED_WIDTH:
                print("Cropping / resizing", path, " to ", DESIRED_WIDTH)
                # im = im.resize(DESIRED_SIZE, Image.Resampling.LANCZOS)
                # im.save(path)
                width_percent = (DESIRED_WIDTH / float(im.size[0]))
                new_height = int((float(im.size[1]) * float(width_percent)))
                
                # Resize and save the image
                im = im.resize((DESIRED_WIDTH, new_height), Image.Resampling.LANCZOS)
                im.save(path)
        except IOError:
            print("Could not open image or process path:", path)
