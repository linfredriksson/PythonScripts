import bpy
import os


def export():
    scene_path = bpy.data.filepath
    print("Blend file path: {}".format(scene_path))
    directory_path = os.path.dirname(scene_path)
    out_directory = os.path.realpath(os.path.join(directory_path, ".."))
    if not directory_path.endswith("work_files"):
        print("Blend file is not located in a work_files directory")
        print("Selected objects will not be exported")
        return False
    print("Output directory: {}".format(out_directory))
    selected_objects = bpy.context.selected_objects
    for obj in selected_objects:
        object_path = os.path.join(out_directory, obj.name)
        print("Exporting: '{}' as '{}'".format(obj.name, object_path))
        bpy.ops.export_scene.stl(filepath=object_path, check_existing=True, use_selection=True)
    return True


if __name__ == "__main__":
    status = export()
    print("Export: {}".format("Success" if status else "Failed"))
