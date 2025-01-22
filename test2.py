bl_info = {
    "name": "test2",
    "author": "Brecht",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add Mesh",
    "description": "just for testing purposes",
    "category": "3D View",
}

import bpy




class Testing(bpy.types.Operator):
    "test"
    bl_idname = "test.testing"
    bl_label = "test"

    def execute(self,context):

        import bpy
        import mathutils
        import bmesh
        import math
        
        
        from os import path as next

        selected_objects = bpy.context.selected_objects
        output_path = next.join(next.expanduser("~/Desktop"), "objects-data.pts")

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')

        bm = bmesh.new()
        ob = bpy.context.active_object
        bm = bmesh.from_edit_mesh(ob.data)
        

        with open(output_path, "w") as output:
            output.write("BEGIN_Polyline\n")

            points = []
            for v in bm.verts:
                if (v.select == True):
                    obMat = ob.matrix_world
                    points.append(obMat @ v.co)

            output.write(f"{points.count}\n")     

            current = points[0]
            seen = [current]

            for _ in points:
                distance = float("inf")

                closest = points[0]

                for next in points:
                    if next in seen:
                        continue
                    d = current.distance(next)
                    if d < distance:
                        distance = d
                        closest = next

                seen.append(closest)
                output.write(f"{current.x} {current.y} {current.z}\n")
                current = closest

        return {'FINISHED'}
    

class SamplePanel(bpy.types.Panel):
    
    bl_label = "Ortho Addons2"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    
    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.operator("test.testing", icon="MESH_CUBE")


classes = (
        SamplePanel,
        Testing,
        
        )

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
