# Simple button in Tools panel
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

        # Create box
        box = lay.box()
        box.operator("object.simple_operator", text="Print #1")
        box.prop(scn, 'encouraging_message')

        # Create another box
        box = lay.box()
        # Create a row within it
        row = box.row()
        # We can jam a few things on the same row
        row.operator("object.simple_operator", text="Print #2")
        row.prop(scn, 'encouraging_message')

        # Create yet another box
        box = lay.box()
        # Create a row just for a label
        row = box.row()
        row.label('There is a split row below me!')
        # Create a split row within it
        row = box.row()
        splitrow = row.split(percentage=0.2)
        # Store references to each column of the split row
        left_col = splitrow.column()
        right_col = splitrow.column()
        left_col.operator("object.simple_operator", text="Print #3")
        right_col.prop(scn, 'encouraging_message')

        # Throw a separator in for white space...
        lay.separator()

        # We can create columns within rows...
        row = lay.row()
        col = row.column()
        col.prop(scn, 'my_int_prop')
        col.prop(scn, 'my_int_prop')
        col.prop(scn, 'my_int_prop')
        col = row.column()
        col.prop(scn, 'my_float_prop')
        col.label("I'm in the middle of a column")
        col.prop(scn, 'my_float_prop')

        # Throw a few separators in...
        lay.separator()
        lay.separator()
        lay.separator()

        # Same as above but with boxes...
        row = lay.row()
        box = row.box()
        box.prop(scn, 'my_int_prop')
        box.label("I'm in the box, bottom left.")
        box = row.box()
        box.prop(scn, 'my_bool_prop')
        box.operator("object.simple_operator", text="Print #4")