class SimplePanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Simple Addon"
    bl_label = "Call Simple Operator"

    def draw(self, context):
        # Store reference to context.scene
        scn = context.scene

        # Store reference to self.layout
        lay = self.layout

        # Create a row within it
        row = lay.row()
        row.operator("object.simple_operator", text="#1", icon='OBJECT_DATA')
        row.operator("object.simple_operator", text="#2", icon='WORLD_DATA')
        row.operator("object.simple_operator", text="#3", icon='LAMP_DATA')

        row = lay.row()
        row.operator("object.simple_operator", text="#4", icon='SOUND')
        row.operator("object.simple_operator", text="#5", icon='MATERIAL')
        row.operator("object.simple_operator", text="#6", icon='ERROR')

        row = lay.row()
        row.operator("object.simple_operator", text="#7", icon='CANCEL')
        row.operator("object.simple_operator", text="#8", icon='PLUS')
        row.operator("object.simple_operator", text="#9", icon='LOCKED')

        row = lay.row()
        row.operator("object.simple_operator", text="#10", icon='HAND')
        row.operator("object.simple_operator", text="#11", icon='QUIT')
        row.operator("object.simple_operator", text="#12", icon='GAME')

        row = lay.row()
        row.operator("object.simple_operator", text="#13", icon='PARTICLEMODE')
        row.operator("object.simple_operator", text="#14", icon='MESH_MONKEY')
        row.operator("object.simple_operator", text="#15", icon='FONT_DATA')

        row = lay.row()
        row.operator("object.simple_operator",
                     text="#16", icon='SURFACE_NSPHERE')
        row.operator("object.simple_operator", text="#17", icon='COLOR_RED')
        row.operator("object.simple_operator", text="#18",
                     icon='FORCE_LENNARDJONES')

        row = lay.row()
        row.operator("object.simple_operator", text="#19", icon='MODIFIER')
        row.operator("object.simple_operator", text="#20", icon='MOD_SOFT')
        row.operator("object.simple_operator", text="#21", icon='MOD_DISPLACE')

        row = lay.row()
        row.operator("object.simple_operator", text="#22", icon='IPO_CONSTANT')
        row.operator("object.simple_operator", text="#23", icon='GRID')
        row.operator("object.simple_operator", text="#24", icon='FILTER')
