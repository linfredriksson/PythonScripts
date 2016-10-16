#
# This script is based on a post made by Ryan T on CGTalk (http://forums.cgsociety.org/archive/index.php?t-726650.html)
# Link worked on 2016/10/16
#
# This script can be run in maya and added to the maya script shelf to enable easy development of scripts in
# external editors.
#

import sys
import os

def psource(module):
    """
    Load module from file
    """
    file = os.path.basename(module)
    dir = os.path.dirname(module)
    toks = file.split(".")
    modname = toks[0]
    # Check if dir is a directory
    if(os.path.exists(dir)):
        # Check if the file directory already exists in the sys.path array
        paths = sys.path
        pathfound = 0
        for path in paths:
            if(dir == path):
                pathfound = 1
        # If the directory is not part of sys.path add it
        if not pathfound:
            sys.path.append(dir)
    # exec works like MEL's eval but you need to add in globals() at the end to make sure
    # the file is imported into the global namespace else it will only be in the scope of this function
    exec("import " + modname) in globals()
    # reload the file to make sure its up to date
    exec("reload( " + modname + " )") in globals()
    # This returns the namespace of the file imported
    return modname

# When you first import a file you must give it the full path
psource("c:/someDirectory/scriptFile.py")
#scriptFile.testFunctionDefinedInScriptFile()
