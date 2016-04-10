bl_info = {
	"name": "Name Of Plugin",
	"author": "Firstname Lastname",
	"category": "Object"
}

import bpy
import math
import mathutils

class ExamplePanel(bpy.types.Panel):
	"""Example tooltip text"""
	bl_space_type = "PROPERTIES"
	bl_region_type = "WINDOW"
	bl_context = "object"
	bl_label = "Example Plugin"
	def draw(self, context):
		layout = self.layout
		col = layout.column(align=True)
		row = col.row(align=True)
		row.label(text="example label:")
		row.operator("mesh.example_operators", text="Examble button")
		row = col.row(align=True)
		row.label(text="bool variable: ")
		row.prop(bpy.context.scene, "boolVariable")
		row = col.row(align=True)
		row.label(text="float variable: ")
		row.prop(bpy.context.scene, "floatVariable")

class ExampleOperators(bpy.types.Operator):
	bl_idname = "mesh.example_operators"
	bl_label = "Test Hej"
	bl_options = {"UNDO"}
	def invoke(self, context, event):
		print("do stuff")
		return {"FINISHED"}

def register():
	bpy.utils.register_class(ExampleOperators)
	bpy.utils.register_class(ExamplePanel)
	bpy.types.Scene.boolVariable = bpy.props.BoolProperty(name="bool", default=True)
	bpy.types.Scene.floatVariable = bpy.props.FloatProperty(name="float", default = 10, min = 0, max = 100, description="float example variable")

def unregister():
	bpy.utils.unregister_class(ExampleOperators)
	bpy.utils.unregister_class(ExamplePanel)
	del bpy.types.Scene.boolVariable
	del bpy.types.Scene.floatVariable

if __name__ == "__main__":
	register()
