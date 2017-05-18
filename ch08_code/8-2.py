import bpy

mats = bpy.data.materials
for dblock in mats:
    if not dblock.users:
        mats.remove(dblock)
        
        
texs = bpy.data.textures
for dblock in mats:
    if not dblock.users:
        texs.remove(dblock)
