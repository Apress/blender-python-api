import bpy
import ut
import random

# Clear scene, must be in object mode
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# size of maze
maze_size = 20

# height of maze
maze_height = 1.0

# Create NxN plane
bpy.ops.mesh.primitive_plane_add(radius= maze_size/ 2, location=(0, 0, 0.1))

# Subdivide and deselect mesh
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.subdivide(number_cuts=maze_size - 1)
bpy.ops.mesh.select_all(action='DESELECT')

# Set starting point
v = [-maze_size / 2, -maze_size / 2]

# Stop iterating if point strays buf away from plane
buf = 5
b = [-maze_size / 2 - buf, maze_size / 2 + buf]

# Probability of point moving forward
fp = 0.6


while b[0] <= v[0] <= b[1] and b[0] <= v[1] <= b[1]:

    # Select square in front of v
    ut.act.select_by_loc(lbound=(v[0] - 0.5, v[1] - 0.5, 0),
                         ubound=(v[0] + 1.5, v[1] + 1.5, 1),
                         select_mode='FACE', coords='GLOBAL',
                         additive=True)

    # Returns 0 or 1
    ind = random.randint(0, 1)

    # Returns -1 or 1 with probability 1 - fp or fp
    dir = (int(random.random() > 1 - fp) * 2) - 1

    # Adjusts point
    v[ind] += dir


bpy.ops.mesh.select_all(action='INVERT')
bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value": (0, 0, maze_height),
                                                         "constraint_axis": (False, False, True)}
                                )


bpy.ops.object.mode_set(mode='OBJECT')
