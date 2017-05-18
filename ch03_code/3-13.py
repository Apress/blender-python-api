import ut
import importlib
importlib.reload(ut)

import bpy

# Will fail if scene is empty
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

bpy.ops.mesh.primitive_uv_sphere_add(size=0.5, location=(0, 0, 0))
bpy.ops.transform.resize(value = (5, 5, 5))
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='DESELECT')

# Selects upper right quadrant of sphere
ut.act.select_by_loc((0, 0, 0), (1, 1, 1), 'VERT', 'LOCAL')

# Selects nothing 
ut.act.select_by_loc((0, 0, 0), (1, 1, 1), 'VERT', 'GLOBAL')

# Selects upper right quadrant of sphere
ut.act.select_by_loc((0, 0, 0), (5, 5, 5), 'VERT', 'LOCAL')

# Mess with it
bpy.ops.transform.translate(value = (1, 1,1))
bpy.ops.transform.resize(value = (2, 2, 2))


# Selects lower half of sphere
ut.act.select_by_loc((-5, -5, -5), (5, 5, -0.5), 'EDGE', 'GLOBAL')

# Mess with it
bpy.ops.transform.translate(value = (0, 0, 3))
bpy.ops.transform.resize(value = (0.1, 0.1, 0.1))

bpy.ops.object.mode_set(mode='OBJECT')