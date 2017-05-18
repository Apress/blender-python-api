bl_info = {
    "name": "XYZ-Select",
    "author": "Chris Conlan",
    "location": "View3D > Tools > XYZ-Select",
    "version": (1, 0, 0),
    "blender": (2, 7, 8),
    "description": "Precision selection in Edit Mode",
    "category": "3D View"
}


### Use these imports to during development  ###

### Use these imports to during development  ###
import ut
import importlib
importlib.reload(ut)

### Use these imports to package and ship your add-on ###
# if "bpy" in locals():
#    import importlib
#    importlib.reload(ut)
#    print('Reloaded ut.py')
# else:
#    from . import ut
#    print('Imported ut.py')


import bpy
import os
import random

# Simple Operator with Extra Properties

class xyzSelect(bpy.types.Operator):
    bl_idname = "object.xyz_select"
    bl_label = "Select pieces of objects in Edit Mode with bounding boxes"

    def execute(self, context):

        scn = context.scene

        output = ut.act.select_by_loc(lbound=scn.xyz_lower_bound,
                                      ubound=scn.xyz_upper_bound,
                                      select_mode=scn.xyz_selection_mode,
                                      coords=scn.xyz_coordinate_system)

        print("Selected " + str(output) + " " + scn.xyz_selection_mode + "s")

        return {'FINISHED'}

    @classmethod
    def register(cls):
        print("Registered class: %s " % cls.bl_label)
        bpy.types.Scene.xyz_lower_bound = bpy.props.FloatVectorProperty(
            name="Lower",
            description="Lower bound of selection bounding box",
            default=(0.0, 0.0, 0.0),
            subtype='XYZ',
            size=3,
            precision=2
        )
        bpy.types.Scene.xyz_upper_bound = bpy.props.FloatVectorProperty(
            name="Upper",
            description="Upper bound of selection bounding box",
            default=(1.0, 1.0, 1.0),
            subtype='XYZ',
            size=3,
            precision=2
        )

        # Menus for EnumProperty's
        selection_modes = [
            ("VERT", "Vert", "", 1),
            ("EDGE", "Edge", "", 2),
            ("FACE", "Face", "", 3),
        ]
        bpy.types.Scene.xyz_selection_mode = \
            bpy.props.EnumProperty(items=selection_modes, name="Mode")

        coordinate_system = [
            ("GLOBAL", "Global", "", 1),
            ("LOCAL", "Local", "", 2),
        ]
        bpy.types.Scene.xyz_coordinate_system = \
            bpy.props.EnumProperty(items=coordinate_system, name="Coords")

    @classmethod
    def unregister(cls):
        print("Unregistered class: %s " % cls.bl_label)
        del bpy.context.scene.xyz_coordinate_system
        del bpy.context.scene.xyz_selection_mode
        del bpy.context.scene.xyz_upper_bound
        del bpy.context.scene.xyz_lower_bound


# Simple button in Tools panel
class xyzPanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "XYZ-Select"
    bl_label = "Select by Bounding Box"

    @classmethod
    def poll(self, context):
        return context.object.mode == 'EDIT'

    def draw(self, context):
        scn = context.scene
        lay = self.layout
        lay.operator('object.xyz_select', text="Select Components")
        lay.prop(scn, 'xyz_lower_bound')
        lay.prop(scn, 'xyz_upper_bound')
        lay.prop(scn, 'xyz_selection_mode')
        lay.prop(scn, 'xyz_coordinate_system')

    @classmethod
    def register(cls):
        print("Registered class: %s " % cls.bl_label)

    @classmethod
    def unregister(cls):
        print("Unregistered class: %s " % cls.bl_label)


def register():
    # bpy.utils.register_module(__name__)

    bpy.utils.register_class(xyzSelect)
    bpy.utils.register_class(xyzPanel)

    print("%s registration complete\n" % bl_info.get('name'))


def unregister():
    # bpy.utils.unregister_class(xyzPanel)
    # bpy.utils.unregister_class(xyzSelect)

    bpy.utils.unregister_module(__name__)
    print("%s unregister complete\n" % bl_info.get('name'))


if __name__ == "__main__":
    try:
        unregister()
    except Exception as e:
        print(e)
        pass
        
    register()