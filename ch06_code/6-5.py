bl_info = {
    "name": "Simple Line and Text Drawing",
    "author": "Chris Conlan",
    "location": "View3D > Tools > Drawing",
    "version": (1, 0, 0),
    "blender": (2, 7, 8),
    "description": "Minimal add-on for line and text drawing with bgl and blf. "
                   "Adapted from Antonio Vazquez's (antonioya) Archmesh.",
    "wiki_url": "http://example.com",
    "category": "Development"
}

import bpy
import bmesh
import os

import bpy_extras
import bgl
import blf

# view3d_utils must be imported explicitly
from bpy_extras import view3d_utils

def draw_main(self, context):
    """Main function, toggled by handler"""

    scene = context.scene
    indices = context.scene.gl_measure_indices

    # Set color and fontsize parameters
    rgb_line = (0.173, 0.545, 1.0, 1.0)
    rgb_label = (1, 0.8, 0.1, 1.0)
    fsize = 16

    # Enable OpenGL drawing
    bgl.glEnable(bgl.GL_BLEND)
    bgl.glLineWidth(1)

    # Store reference to active object
    ob = context.object

    # Draw vertex indices
    if scene.gl_display_verts:
        label_verts(context, ob, rgb_label, fsize)

    # Draw measurement
    if scene.gl_display_measure:
        if(indices[1] < len(ob.data.vertices)):
            draw_measurement(context, ob, indices, rgb_line, rgb_label, fsize)

    # Draw name
    if scene.gl_display_names:
        draw_name(context, ob, rgb_label, fsize)

    # Disable OpenGL drawings and restore defaults
    bgl.glLineWidth(1)
    bgl.glDisable(bgl.GL_BLEND)
    bgl.glColor4f(0.0, 0.0, 0.0, 1.0)


class glrun(bpy.types.Operator):
    """Main operator, flicks handler on/off"""
    
    bl_idname = "glinfo.glrun"
    bl_label = "Display object data"
    bl_description = "Display aditional information in the 3D Viewport"

    # For storing function handler
    _handle = None

    # Enable GL drawing and add handler
    @staticmethod
    def handle_add(self, context):
        if glrun._handle is None:
            glrun._handle = bpy.types.SpaceView3D.draw_handler_add(
                draw_main, (self, context), 'WINDOW', 'POST_PIXEL')
            context.window_manager.run_opengl = True

    # Disable GL drawing and remove handler
    @staticmethod
    def handle_remove(self, context):
        if glrun._handle is not None:
            bpy.types.SpaceView3D.draw_handler_remove(glrun._handle, 'WINDOW')
        glrun._handle = None
        context.window_manager.run_opengl = False

    # Flicks OpenGL handler on and off
    # Make sure to flick "off" before reloading script when live editing
    def execute(self, context):
        if context.area.type == 'VIEW_3D':

            if context.window_manager.run_opengl is False:
                self.handle_add(self, context)
                context.area.tag_redraw()
            else:
                self.handle_remove(self, context)
                context.area.tag_redraw()

            return {'FINISHED'}
        else:
            print("3D Viewport not found, cannot run operator.")
            return {'CANCELLED'}


class glpanel(bpy.types.Panel):
    """Standard panel with scene variables"""
    
    bl_idname = "glinfo.glpanel"
    bl_label = "Display Object Data"
    bl_space_type = 'VIEW_3D'
    bl_region_type = "TOOLS"
    bl_category = 'Drawing'

    def draw(self, context):
        lay = self.layout
        scn = context.scene

        box = lay.box()

        if context.window_manager.run_opengl is False:
            icon = 'PLAY'
            txt = 'Display'
        else:
            icon = 'PAUSE'
            txt = 'Hide'

        box.operator("glinfo.glrun", text=txt, icon=icon)

        box.prop(scn, "gl_display_names", toggle=True, icon="OUTLINER_OB_FONT")
        box.prop(scn, "gl_display_verts", toggle=True, icon='DOT')
        box.prop(scn, "gl_display_measure", toggle=True, icon="ALIGN")
        box.prop(scn, "gl_measure_indices")

    @classmethod
    def register(cls):

        bpy.types.Scene.gl_display_measure = bpy.props.BoolProperty(
            name="Measures",
            description="Display measurements for specified indices in active mesh.",
            default=True,
        )

        bpy.types.Scene.gl_display_names = bpy.props.BoolProperty(
            name="Names",
            description="Display names for selected meshes.",
            default=True,
        )

        bpy.types.Scene.gl_display_verts = bpy.props.BoolProperty(
            name="Verts",
            description="Display vertex indices for selected meshes.",
            default=True,
        )

        bpy.types.Scene.gl_measure_indices = bpy.props.IntVectorProperty(
            name="Indices",
            description="Display measurement between supplied vertices.",
            default=(0, 1),
            min=0,
            subtype='NONE',
            size=2)

        print("registered class %s " % cls.bl_label)

    @classmethod
    def unregister(cls):
        del bpy.types.Scene.gl_display_verts
        del bpy.types.Scene.gl_display_names
        del bpy.types.Scene.gl_display_measure
        del bpy.types.Scene.gl_measure_indices

        print("unregistered class %s " % cls.bl_label)


##### Button-activated drawing functions #####

# Draw the name of the object on its origin
def draw_name(context, ob, rgb_label, fsize):
    a = gl_pts(context, ob.location)
    bgl.glColor4f(rgb_label[0], rgb_label[1], rgb_label[2], rgb_label[3])
    draw_text(a, ob.name, fsize)


# Draw line between two points, draw the distance
def draw_measurement(context, ob, pts, rgb_line, rgb_label, fsize):
    # pts = (index of vertex #1, index of vertex #2)

    a = coords(ob, pts[0])
    b = coords(ob, pts[1])

    d = dist(a, b)

    mp = midpoint(a, b)

    a = gl_pts(context, a)
    b = gl_pts(context, b)
    mp = gl_pts(context, mp)

    bgl.glColor4f(rgb_line[0], rgb_line[1], rgb_line[2], rgb_line[3])
    draw_line(a, b)

    bgl.glColor4f(rgb_label[0], rgb_label[1], rgb_label[2], rgb_label[3])
    draw_text(mp, '%.3f' % d, fsize)


# Label all possible vertices of object
def label_verts(context, ob, rgb, fsize):
    try:
        # attempt get coordinates, will except if object does not have vertices
        v = coords(ob)
        bgl.glColor4f(rgb[0], rgb[1], rgb[2], rgb[3])
        for i in range(0, len(v)):
            loc = gl_pts(context, v[i])
            draw_text(loc, str(i), fsize)
    except AttributeError:
        # Except attribute error to not fail on lights, cameras, etc
        pass

# Convert 3D points to OpenGL-compatible 2D points
def gl_pts(context, v):
    return bpy_extras.view3d_utils.location_3d_to_region_2d(
        context.region,
        context.space_data.region_3d,
        v)

##### Core drawing functions #####
# Generic function for drawing text on screen
def draw_text(v, display_text, fsize, font_id=0):
    if v:
        blf.size(font_id, fsize, 72)
        blf.position(font_id, v[0], v[1], 0)
        blf.draw(font_id, display_text)
    return

# Generic function for drawing line on screen
def draw_line(v1, v2):
    if v1 and v2:
        bgl.glBegin(bgl.GL_LINES)
        bgl.glVertex2f(*v1)
        bgl.glVertex2f(*v2)
        bgl.glEnd()
    return


##### Utilities #####

# Returns all coordinates or single coordinate of object
# Can toggle between GLOBAL and LOCAL coordinates
def coords(obj, ind=None, space='GLOBAL'):
    if obj.mode == 'EDIT':
        v = bmesh.from_edit_mesh(obj.data).verts
    elif obj.mode == 'OBJECT':
        v = obj.data.vertices

    if space == 'GLOBAL':
        if isinstance(ind, int):
            return (obj.matrix_world * v[ind].co).to_tuple()
        else:
            return [(obj.matrix_world * v.co).to_tuple() for v in v]

    elif space == 'LOCAL':
        if isinstance(ind, int):
            return (v[ind].co).to_tuple()
        else:
            return [v.co.to_tuple() for v in v]

# Returns euclidean distance between two 3D points
def dist(x, y):
    return ((x[0] - y[0])**2 + (x[1] - y[1])**2 + (x[2] - y[2])**2)**0.5

# Returns midpoint between two 3D points
def midpoint(x, y):
    return ((x[0] + y[0]) / 2, (x[1] + y[1]) / 2, (x[2] + y[2]) / 2)


##### Registration #####
def register():
    """Register objects inheriting bpy.types in current file and scope"""
    
    # bpy.utils.register_module(__name__)

    # Explicitly register objects
    bpy.utils.register_class(glrun)
    bpy.utils.register_class(glpanel)

    wm = bpy.types.WindowManager
    wm.run_opengl = bpy.props.BoolProperty(default=False)

    print("%s registration complete\n" % bl_info.get('name'))


def unregister():

    wm = bpy.context.window_manager
    p = 'run_opengl'
    if p in wm:
        del wm[p]

    # remove OpenGL data
    glrun.handle_remove(glrun, bpy.context)

    # Always unregister in reverse order to prevent error due to
    # interdependencies

    # Explicity unregister objects
    # bpy.utils.unregister_class(glpanel)
    # bpy.utils.unregister_class(glrun)

    # Unregister objects inheriting bpy.types in current file and scope
    bpy.utils.unregister_module(__name__)
    print("%s unregister complete\n" % bl_info.get('name'))


# Only called during development with 'Text Editor -> Run Script'
# When distributed as plugin, Blender will directly call register()
if __name__ == "__main__":
    try:
        os.system('clear')
        unregister()
    except Exception as e:
        print(e)
        pass
    finally:
        register()
