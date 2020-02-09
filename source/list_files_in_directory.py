import os

def listFiles(path, include_sub_dir=True):
    files = []
    objects = os.listdir(path)
    for object in objects:
        full_path = os.path.join(path, object)
        if include_sub_dir and os.path.isdir(full_path):
            files += listFiles(full_path)
        else:
            files.append(full_path)
    return files

files = listFiles("C:\example\directory")
