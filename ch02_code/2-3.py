import bpy

def mySelector(objName, additive=False):

    # By default, clear other selections
    if not additive:
        bpy.ops.object.select_all(action='DESELECT')

    # Set the 'select' property of the datablock to True
    bpy.data.objects[objName].select = True


# Select only 'Cube'
mySelector('Cube')

# Select 'Sphere', keeping other selections
mySelector('Sphere', additive=True)

# Translate selected objects 1 unit along the x-axis
bpy.ops.transform.translate(value=(1, 0, 0))   