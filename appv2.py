import pyvista as pv
from pyvista import CellType
from stpyvista import stpyvista


points = [
    [0.0, 0.0, 0.0],  # 0
    [0.0, 3.0, 0.0],  # 1
    [0.3, 3.0, 0.0],  # 2
    [0.3, 0.5, 0.0],  # 3
    [0.5, 0.3, 0.0],  # 4
    [2.0, 0.3, 0.0],  # 5
    [2.0, 0.0, 0.0],  # 6
    [0.0, 0.0, 2.0],  # 7
    [0.0, 3.0, 2.0],  # 8
    [0.3, 3.0, 2.0],  # 9
    [0.3, 0.5, 2.0],  # 10
    [0.5, 0.3, 2.0],  # 11
    [2.0, 0.3, 2.0],  # 12
    [2.0, 0.0, 2.0],  # 13
]

polyhedron_connectivity = [
    # NItems will go here
    9,  # number of faces
    7,  # number of points in face0
    0,  # point index 0
    1,  # point index 1
    2,  # point index 2
    3,  # point index 3
    4,  # point index 4
    5,
    6,
    7,  # number of points in face1
    7,  # point index ...
    8,
    9,
    10,
    11,
    12,
    13,
    4,  # number of points in face2
    0,
    6,
    13,
    7,
    4,  # number of points in face3
    5,
    6,
    13,
    12,
    4,  # number of points in face4
    4,
    5,
    12,
    11,
    4, # number of points in face5
    3,
    4,
    11,
    10,
    4,  #number of points in face6
    2,
    3,
    10,
    9,
    4, # face 7
    1,
    2,
    9,
    8,
    4, #face 8
    0,
    1,
    8,
    7,
      
]

# note how we retroactively add NItems
polyhedron = [len(polyhedron_connectivity)] + polyhedron_connectivity

cells=polyhedron
celltypes = [pv.CellType.POLYHEDRON]
grid = pv.UnstructuredGrid(cells, celltypes, points)
plotter = pv.Plotter(window_size=[800,400])

plotter.add_mesh(grid) 
#plotter.add_scalar_bar()
plotter.background_color = 'black'
plotter.view_isometric()
stpyvista(plotter)