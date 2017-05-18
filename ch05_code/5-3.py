# Simple Operator with Extra Properties
class SimpleOperator(bpy.types.Operator):
    bl_idname = "object.simple_operator"
    bl_label = "Print an Encouraging Message"

    def execute(self, context):
        print("\n\n####################################################")
        print("# Add-on and Simple Operator executed succesfully!")
        print("# Encouraging Message:", context.scene.encouraging_message)
        print("# My Int:", context.scene.my_int_prop)
        print("# My Float:", context.scene.my_float_prop)
        print("# My Bool:", context.scene.my_bool_prop)
        print("# My Int Vector:", *context.scene.my_int_vector_prop)
        print("# My Float Vector:", *context.scene.my_float_vector_prop)
        print("# My Bool Vector:", *context.scene.my_bool_vector_prop)
        print("####################################################")
        return {'FINISHED'}

    @classmethod
    def register(cls):
        print("Registered class: %s " % cls.bl_label)

        bpy.types.Scene.encouraging_message = bpy.props.StringProperty(
            name="",
            description="Message to print to user",
            default="Have a nice day!")

        bpy.types.Scene.my_int_prop = bpy.props.IntProperty(
            name="My Int",
            description="Sample integer property to print to user",
            default=123,
            min=100,
            max=200)

        bpy.types.Scene.my_float_prop = bpy.props.FloatProperty(
            name="My Float",
            description="Sample float property to print to user",
            default=3.1415,
            min=0.0,
            max=10.0,
            precision=4)

        bpy.types.Scene.my_bool_prop = bpy.props.BoolProperty(
            name="My Bool",
            description="Sample boolean property to print to user",
            default=True)

        bpy.types.Scene.my_int_vector_prop = bpy.props.IntVectorProperty(
            name="My Int Vector",
            description="Sample integer vector property to print to user",
            default=(1, 2, 3, 4),
            subtype='NONE',
            size=4)

        bpy.types.Scene.my_float_vector_prop = bpy.props.FloatVectorProperty(
            name="My Float Vector",
            description="Sample float vector property to print to user",
            default=(1.23, 2.34, 3.45),
            subtype='XYZ',
            size=3,
            precision=2)

        bpy.types.Scene.my_bool_vector_prop = bpy.props.BoolVectorProperty(
            name="My Bool Vector",
            description="Sample bool vector property to print to user",
            default=(True, False, True),
            subtype='XYZ',
            size=3)

    @classmethod
    def unregister(cls):
        print("Unregistered class: %s " % cls.bl_label)
        del bpy.types.Scene.encouraging_message


# Simple button in Tools panel
class SimplePanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Simple Addon"
    bl_label = "Call Simple Operator"
    bl_context = "objectmode"

    def draw(self, context):
        self.layout.operator("object.simple_operator",
                             text="Print Encouraging Message")
        self.layout.prop(context.scene, 'encouraging_message')
        self.layout.prop(context.scene, 'my_int_prop')
        self.layout.prop(context.scene, 'my_float_prop')
        self.layout.prop(context.scene, 'my_bool_prop')
        self.layout.prop(context.scene, 'my_int_vector_prop')
        self.layout.prop(context.scene, 'my_float_vector_prop')
        self.layout.prop(context.scene, 'my_bool_vector_prop')

    @classmethod
    def register(cls):
        print("Registered class: %s " % cls.bl_label)
        # Register properties related to the class here.

    @classmethod
    def unregister(cls):
        print("Unregistered class: %s " % cls.bl_label)