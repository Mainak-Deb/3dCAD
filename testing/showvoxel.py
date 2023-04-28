import vtkplotlib as vpl
from stl.mesh import Mesh


path = r"testing/models/chair2.stl"
mesh = Mesh.from_file(path)
vpl.mesh_plot(mesh)
vpl.show()