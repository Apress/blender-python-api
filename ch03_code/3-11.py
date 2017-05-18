import ut
import importlib
importlib.reload(ut)

import bpy

# Will fail if scene is empty
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

bpy.ops.mesh.primitive_cube_add(radius=0.5, location=(0, 0, 0))
bpy.context.object.name = 'Cube-1'

# Check global and local coordinates
print('\nBefore transform:')
print('Global:', ut.coords('Cube-1', 'GLOBAL')[0:2])
print('Local: ', ut.coords('Cube-1', 'LOCAL')[0:2])

# Translate it along x = y = z
# See the cube move in the 3D viewport 
bpy.ops.transform.translate(value = (3, 3, 3))

# Check global and local coordinates
print('\nAfter transform, unapplied:')
print('Global: ', ut.coords('Cube-1', 'GLOBAL')[0:2])
print('Local: ', ut.coords('Cube-1', 'LOCAL')[0:2])

# Apply transformation
# Nothing changes in 3D viewport
ut.sel.transform_apply()

# Check global and local coordinates
print('\nAfter transform, applied:')
print('Global: ', ut.coords('Cube-1', 'GLOBAL')[0:2])
print('Local: ', ut.coords('Cube-1', 'LOCAL')[0:2])


############################ Output ###########################
# Before transform:
# Global: [(-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5)]
# Local:  [(-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5)]
#
# After transform, unapplied:
# Global:  [(2.5, 2.5, 2.5), (2.5, 2.5, 3.5)]
# Local:  [(-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5)]
# 
# After transform, applied:
# Global:  [(2.5, 2.5, 2.5), (2.5, 2.5, 3.5)]
# Local:  [(2.5, 2.5, 2.5), (2.5, 2.5, 3.5)]
###############################################################