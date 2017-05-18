# Return the names of selected objects
[k.name for k in bpy.context.selected_objects]

# Return the locations of selected objects
# (location of origin assuming no pending transformations)
[k.location for k in bpy.context.selected_objects]
