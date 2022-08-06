from PIL import Image
import numpy as np

# Load image, ensure not palettised, and make into Numpy array
pim = Image.open('map with dots.jpg').convert('RGB')
im  = np.array(pim)

# Define the blue colour we want to find - PIL uses RGB ordering
Colour = [255, 127, 38]

# Get X and Y coordinates of all blue pixels
Y, X = np.where(np.all(im==Colour,axis=2))

print('X: ', X)
print('Y', Y)
