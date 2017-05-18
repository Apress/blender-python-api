if "bpy" in locals():
    # Runs if add-ons are being reloaded with F8
    import importlib
    importlib.reload(ut)
    print('Reloaded ut.py')
else:
    # Runs first time add-on is loaded
    from . import ut
    print('Imported ut.py')
    
# bpy should be imported after this block of code
import bpy