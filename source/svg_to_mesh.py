import bpy

def curveToMesh():
    print("Converting curves to mesh")
    for ob in bpy.data.objects:
        if ob.type == "CURVE":
            bpy.ops.object.select_all(action='DESELECT')
            print("Object: %s" % ob.name)
            ob.select = True
            bpy.context.scene.objects.active = ob
            try:
                bpy.ops.object.convert(target="MESH", keep_original=True)
                print("  Converted to mesh")
            except Exception as e:
                print("  Error: %s" % str(e))
    print("Done")

curveToMesh()
