import bpy

def myActivator(objName):
    
  # Pass bpy.data.objects datablock to scene class
  bpy.context.scene.objects.active = bpy.data.objects[objName]


# Acivate the object named 'Sphere'
myActivator('Sphere')

# Verify the 'Sphere' was activated
print("Active object:", bpy.context.object.name)

# Selected objects were unaffected
print("Selected objects:", bpy.context.selected_objects)