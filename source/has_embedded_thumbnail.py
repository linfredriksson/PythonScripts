import subprocess
import json
import sys
import os


def runSubprocess(command): 
    return subprocess.check_output(command)


def readMetaAsJson(path):
    result = runSubprocess(["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", "-show_streams", path])
    return json.loads(result)


def hasEmbeddedThumbnail(path):
    data = readMetaAsJson(sys.argv[1])
    if "streams" not in data:
        print("Unable to read streams")
        return False
    for stream in data["streams"]:
        if "tags" not in stream:
            continue
        if "filename" not in stream["tags"]:
            continue
        if stream["tags"]["filename"] == "":
            continue
        return True
    return False


def main():
    if len(sys.argv) < 2:
        print("Missing arguments")
        print("Example Use: 'python has_embedded_thumbnail.py path/to/video'")
        return
    if not os.path.exists(sys.argv[1]):
        print("File not found")
        return
    if hasThumbnailEmbedded(sys.argv[1]):
        print("Thumbnail embedded")
    else:
        print("No Thumbnail embedded")

main()
