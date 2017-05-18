import bpy
from bpy_extras import view3d_utils
import bgl
import blf

# Color and font size of text
rgb_label = (1, 0.8, 0.1, 1.0)
font_size = 16
font_id = 0

# Wrapper for mapping 3D viewport to OpenGL 2D region

def gl_pts(context, v):
    return view3d_utils.location_3d_to_region_2d(
        context.region,
        context.space_data.region_3d,
        v)

# Get the active object, find its 2D points, draw the name

def draw_name(context):

    ob = context.object
    v = gl_pts(context, ob.location)

    bgl.glColor4f(*rgb_label)

    blf.size(font_id, font_size, 72)
    blf.position(font_id, v[0], v[1], 0)
    blf.draw(font_id, ob.name)


# Add the handler
# arguments:
# function = draw_name,
# tuple of parameters = (bpy.context,),
# constant1 = 'WINDOW',
# constant2 = 'POST_PIXEL'
bpy.types.SpaceView3D.draw_handler_add(
    draw_name, (bpy.context,), 'WINDOW', 'POST_PIXEL')