import bpy

def mySpecifier(objName):
    # Return the datablock
    return bpy.data.objects[objName]
    
# Store a reference to the datablock
myCube = mySpecifier('Cube')

# Output the location of the origin
print(myCube.location)
  
# Works exactly the same as above
myCube = bpy.data.objects['Cube']
print(myCube.location)  