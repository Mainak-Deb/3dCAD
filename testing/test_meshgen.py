import numpy as np
from stl import mesh
import vtkplotlib as vpl
from voxelfuse.voxel_model import VoxelModel
from voxelfuse.mesh import Mesh
from voxelfuse.primitives import generateMaterials

if __name__=='__main__':
    sponge = [
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ],
        [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]
        ],
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
    ]
    print("sponge",sponge)
    model = VoxelModel(sponge, generateMaterials(4))  #4 is aluminium.
    mesh = Mesh.fromVoxelModel(model)
    vpl.mesh_plot(mesh)
    vpl.show()