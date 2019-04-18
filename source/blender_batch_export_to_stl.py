import bpy
import os

def export(path):
    if not os.path.exists(path):
        os.makedirs(path)
    selected_objects = bpy.context.selected_objects
    for object in selected_objects:
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.scene.objects.active = object
        object.select = True
        stl_path = "%s%s.stl" % (path, object.name)
        print("Saving: %s" % stl_path)
        bpy.ops.export_mesh.stl(filepath=stl_path, use_selection=True)

path = bpy.path.abspath(r"C:/Path/To/Output/Folder/")
export(path)
