# Will use the cached version of ut.py from
# your first import of the Blender session
import ut
ut.create.cube('myCube')


# Will reload the module from the live script of ut.py
# and create a new cached version for the session
import importlib
importlib.reload(ut)
ut.create.cube('myCube')
        
        
# This is what the header of your main script
# should look like when editing custom modules
import ut
import importlib
importlib.reload(ut)

# Code using ut.py ...