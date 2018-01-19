"""
=============================
Track a series of pyart grids
=============================

"""

# Author: Mark Picel (mhpicel@gmail.com)
# License: BSD 3 clause

import os
import pyart
from tint.tracks import Cell_tracks

# Obtain sorted list of pyart grid files
data_dir = ''  # put the path to your grid files here
grid_files = os.listdir(data_dir)
grid_files = [os.path.join(data_dir, file) for file in grid_files]
grid_files.sort()

# Create generator of pyart grid objects
grid_gen = (pyart.io.read_grid(file) for file in grid_files)

# Instantiate tracks object and view parameter defaults
tracks_obj = Cell_tracks()
print(tracks_obj.params)

# Adjust size parameter
tracks_obj.params['MIN_SIZE'] = 16

# Get tracks from grid generator
tracks_obj.get_tracks(grid_gen)

# Inspect tracks
print(tracks_obj.tracks)
