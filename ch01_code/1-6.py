import bpy

for k in range(5):
    for j in range(5):
        for i in range(5):
            bpy.ops.mesh.primitive_cube_add(radius=0.25, location=(i, j, k))