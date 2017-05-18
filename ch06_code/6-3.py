import bpy
from bpy.app.handlers import persistent


@persistent
def load_diag(dummy):
    obs = bpy.context.scene.objects
    
    print('\n\n### File Diagnostics ###')
    print('Objects in Scene:', len(obs))
    for ob in obs:
        print(ob.name, 'of type', ob.type)

bpy.app.handlers.load_post.append(load_diag)


# After reloading startup file:
#
# ### File Diagnostics ###
# Objects in Scene: 3
# Cube of type MESH
# Lamp of type LAMP
# Camera of type CAMERA