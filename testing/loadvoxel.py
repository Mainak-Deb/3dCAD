import numpy as np
import trimesh
import voxelfuse

# Load a mesh model
f = open('testing/voxel_heart.stl', 'r')
mesh = trimesh.load('testing/voxel_heart.stl')

# Define the resolution of the voxel grid
resolution = (20, 20, 20)

# Voxelization: convert the mesh to a binary voxel grid
voxels = voxelfuse.mesh_to_binary_voxels(mesh, resolution)

# Morphology: perform dilation and erosion on the voxel grid
voxels = voxelfuse.dilate(voxels, iterations=2)
voxels = voxelfuse.erode(voxels, iterations=1)


print(voxels)
# Visualization: plot the resulting voxel grid
voxelfuse.plot_voxels(voxels)