# Adapted from Antonio Vazquez's Archimesh
import bpy

# Clear scene
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Manipulate Python lists of vertex and face data...
# Sample here creates a triangular pyramid
myvertex = [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0)]
myfaces = [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]

##############################################################

# Option #1 - bpy.ops.object.add()
bpy.ops.object.add(type='MESH')
mainobject = bpy.context.object
mainmesh = mainobject.data
mainmesh.name = 'WindowMesh'
mainobject.name = 'WindowObject'

# Write the Python data to the mesh and update it
mainmesh.from_pydata(myvertex, [], myfaces)
mainmesh.update(calc_edges = True)

##############################################################

# WARNING: Known to cause crashses and segmentation faults in
# certain operating systems. Linux builds are safe.
# Option #2 - bpy.data.meshes.new()
mainmesh = bpy.data.meshes.new("WindowMesh")
mainobject = bpy.data.objects.new("WindowObject", mainmesh)

# Link the object to the scene, activate it, and select it
bpy.context.scene.objects.link(mainobject)
bpy.context.scene.objects.active = mainobject
mainobject.select = True

# Write the Python data to the mesh and update it
mainmesh.from_pydata(myvertex, [], myfaces)
mainmesh.update(calc_edges = True)

##############################################################