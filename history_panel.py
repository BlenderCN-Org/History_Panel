# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
import bpy

bl_info = {
    "name": "History Panel",
    "description": "Brings back the «History» panel with all its history managment including the famous Undo & Redo buttons.",
    "author": "Loïc «L0Lock» Dautry",
    "version": (0, 0, 1),
    "blender": (2, 81, 0),
    "location": "3D Viewport > Sidebar > Tool tab.",
    "warning": "",
    "wiki_url": "https://github.com/L0Lock/History_Panel",
    "tracker_url": "https://github.com/L0Lock/History_Panel/issues",
    "category": "3D View"
}


class VIEW3D_PT_UndoRedo(bpy.types.Panel):
    bl_label = "History"
    bl_idname = "VIEW3D_PT_undo_redo"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'
    
    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        obj = context.object

        col = layout.column(align=True)
        row = col.row(align=True)
        row.operator("ed.undo", icon='LOOP_BACK')
        row.operator("ed.redo", icon='LOOP_FORWARDS')
        col.operator("ed.undo_history", icon='BACK')

        col = layout.column(align=True)
        col.label(text="Repeat:")
        col.operator("screen.repeat_last", icon='FILE_REFRESH')
        col.operator("screen.repeat_history", text="History...", icon='SORTTIME')

classes = (
    VIEW3D_PT_UndoRedo,
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

if __name__ == "__main__":
    register()