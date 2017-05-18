import bpy
import datetime

# Clear the scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Create an object for our clock
bpy.ops.object.text_add(location=(0, 0, 0))
bpy.context.object.name = 'MyTextObj'

# Create a handler function
def tell_time(dummy):
    current_time = datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3]
    bpy.data.objects['MyTextObj'].data.body = current_time
   
# Add to the list of handler functions "scene_update_pre"
bpy.app.handlers.scene_update_pre.append(tell_time)
