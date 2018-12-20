''' property classes should be self contained.  They may include:
    PropertyGroup class
        with properties that can be attached to a blender ID type
        methods for syncing these properties
    And panel classes for displaying these properties

    The idea here is to keep all the properties syncing, data, display etc in one place.
    Basically a "model/view" type pattern where we bring them together for ease of maintenance.
    Slightly inspired by vue.js

    TODO could we use decorators to register???
'''

import bpy


__all__ = ('RPR_Properties', 'register', 'unregister')


class RPR_Properties(bpy.types.PropertyGroup):
    def sync(self, rpr_context):
        ''' Sync will update this object in the context.
            And call any sub-objects that need to be synced
            rpr_context object in the binding will be the only place we keep
        "lists of items synced." '''
        pass


# Register/unregister all required classes of RPR properties in one go
from . import (
    render,
    mesh,
    object,
    light,
    camera,
    material,
    world,
)

register, unregister = bpy.utils.register_classes_factory([
    render.RPR_RenderDevicesProperties,
    render.RPR_LightPathsProperties,
    render.RPR_SamplingProperties,
    render.RPR_RenderProperties,

    mesh.RPR_MeshProperties,
    object.RPR_ObjectProperites,
    light.RPR_LightProperties,
    camera.RPR_CameraProperties,

    world.RPR_WORLD_PROP_environment_ibl,
    world.RPR_WORLD_PROP_environment_sun_sky,
    world.RPR_WORLD_PROP_environment,

    material.RPR_MATERIAL_OT_UseShadingNodes,
    material.RPR_MATERIAL_parser,
    material.RPR_MATERIAL_PT_context,
    material.RPR_MATERIAL_PT_preview,
    material.RPR_MATERIAL_PT_material,
    material.RPR_MATERIAL_PT_surface,
])
