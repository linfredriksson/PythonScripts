#
# File should be placed in "%USERNAME%\AppData\Local\Agisoft\PhotoScan Pro\scripts" for agisoft to load it at startup
#
import PhotoScan

def function1():
    """
    Example function 1
    """
    doc = PhotoScan.app.document
    print("Running function1")
    return 1

def function2():
    """
    Example function 2
    """
    doc = PhotoScan.app.document
    print("Running function2")
    return 1

label = "ExampleMenu/ExampleScript1"
PhotoScan.app.addMenuItem(label, function1, "ctrl+alt+i")
label = "ExampleMenu/ExampleScript2"
PhotoScan.app.addMenuItem(label, function2, "ctrl+alt+o")
