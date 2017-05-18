# Add modifier to selected objects
bpy.ops.object.modifier_add(type='EDGE_SPLIT')

# Set split threshold in radians
bpy.context.object.modifiers["EdgeSplit"].split_angle = (3.1415 / 180) * 5

# Apply modifier
bpy.ops.object.modifier_apply(apply_as='DATA', modifier='EdgeSplit')