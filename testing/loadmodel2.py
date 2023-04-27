import stltovoxel
import numpy as np

input=r"testing/voxel_heart.stl"
output=r"testing/output/output.png"
resolution = 6 #Resolution, into how many layers the model should be divided
stltovoxel.convert_file(input, output, resolution)