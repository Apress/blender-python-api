# Will only work if `tell_time` is in scope
bpy.app.handlers.scene_update_pre.remove(tell_time)

# Useful in development for a clean slate
bpy.app.handlers.scene_update_pre.clear()

# Remove handler at the end of the list and return it
bpy.app.handlers.scene_update_pre.pop()