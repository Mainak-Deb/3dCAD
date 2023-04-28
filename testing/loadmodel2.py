import stltovoxel
import numpy as np
import os
import cv2

input=r"testing/models/chair2.stl"
output=r"testing/models/output/output.png"
folder_path = "testing/models/output/"
resolution = 20
binary_array = np.zeros((resolution,resolution,resolution), dtype=bool)


stltovoxel.convert_file(input, output, resolution)
image_names = os.listdir(folder_path)[0:resolution]

for i, name in enumerate(image_names):
    image = cv2.imread(os.path.join(folder_path, name), cv2.IMREAD_GRAYSCALE)
    image=cv2.resize(image,(resolution,resolution))
    binary_array[i,:,:] = (image > 0)  # assume that white pixels represent "true"

print(binary_array)