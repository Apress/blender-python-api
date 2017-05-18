bpy.types.Scene.my_color_prop = bpy.props.FloatVectorProperty(
    name="My Color Property",
    description="Returns a vector of length 4",
    default=(0.322, 1.0, 0.182, 1.0),
    min=0.0,
    max=1.0,
    subtype='COLOR',
    size=4)