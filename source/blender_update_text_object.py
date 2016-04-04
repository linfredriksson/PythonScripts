import bpy

# Simple handler that updates the text in a text object in blender.
# - nameOfTextObject: the name of the text object in the blender scene.
# - newText: the new text data to put in the text object.
def textUpdateHandler(scene):
    nameOfTextObject = "Text"
    currentFrame = scene.frame_current
    endFrame = scene.frame_end
    exampleNumber = "%.0f" % currentFrame
    newText = exampleNumber
    scene.objects[nameOfTextObject].data.body = newText

# make the handler run every time the current frame is changed.
bpy.app.handlers.frame_change_pre.append(textUpdateHandler)
