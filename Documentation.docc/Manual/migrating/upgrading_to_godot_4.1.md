<!-- Remove this line to publish to docs.xogot.com -->
# Upgrading from Godot 4.0 to Godot 4.1

For most games and apps made with 4.0, it should be relatively safe to migrate to 4.1.
This page intends to cover everything you need to pay attention to when migrating
your project.

## Breaking changes

If you are migrating from 4.0 to 4.1, the breaking changes listed here might
affect you. Changes are grouped by areas/systems.

> Warning:
>
> The GDExtension API completely breaks compatibility in 4.1, so it's not included
> in the table below. See the :ref:`updating_your_gdextension_for_godot_4_1` section
> for more information.
>

This article indicates whether each breaking change affects GDScript and whether
the C# breaking change is binary compatible or source compatible:

- **Binary compatible** - Existing binaries will load and execute successfully without
recompilation, and the runtime behavior won't change.

- **Source compatible** - Source code will compile successfully without changes when
upgrading Godot.

### Core

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**Basis** |  |  |  | 
Methodlooking_atadds a newuse_model_frontoptional parameter | |✔️| | |✔️| | |✔️| | GH-76082
**Object** |  |  |  | 
Methodget_meta_listchanges return type fromPackedStringArraytoArray[StringName] | |✔️| | |❌| | |❌| | GH-76418
**Transform3D** |  |  |  | 
Methodlooking_atadds a newuse_model_frontoptional parameter | |✔️| | |✔️| | |✔️| | GH-76082
**UndoRedo** |  |  |  | 
Methodcreate_actionadds a newbackward_undo_opsoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-76688
**WorkerThreadPool** |  |  |  | 
Methodwait_for_task_completionchanges return type fromvoidtoError | |✔️| | |❌| | |✔️| | GH-77143

### Animation

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**AnimationNode** |  |  |  | 
Method_processadds a newtest_onlyparameter | |❌| | |❌| | |❌| | GH-75759
Methodblend_inputadds a newtest_onlyoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-75759
Methodblend_nodeadds a newtest_onlyoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-75759
**AnimationNodeStateMachinePlayback** |  |  |  | 
Methodget_travel_pathchanges return type fromPackedStringArraytoArray[StringName] | |✔️| | |❌| | |❌| | GH-76418

### 2D nodes

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**PathFollow2D** |  |  |  | 
Propertylookaheadremoved | |❌| | |❌| | |❌| | GH-72842

### 3D nodes

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**Geometry3D** |  |  |  | 
Methodsegment_intersects_convexchangesplanesparameter type from untypedArraytoArray[Plane] | |✔️| | |✔️ with compat| | |❌| | GH-76418
**MeshInstance3D** |  |  |  | 
Methodcreate_multiple_convex_collisionsadds a newsettingsoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-72152
**Node3D** |  |  |  | 
Methodlook_atadds a newuse_model_frontoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-76082
Methodlook_at_from_positionadds a newuse_model_frontoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-76082

### GUI nodes

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**CodeEdit** |  |  |  | 
Methodadd_code_completion_optionadds a newlocationoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-75746
**RichTextLabel** |  |  |  | 
Methodpush_listadds a newbulletoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-75017
Methodpush_paragraphadds a newjustification_flagsoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-75250
Methodpush_paragraphadds a newtab_stopsoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-76401
**Tree** |  |  |  | 
Methodedit_selectedadds a newforce_editoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-76794

### Physics

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**Area2D** |  |  |  | 
Propertyprioritychanges type fromfloattoint | |❌| | |❌| | |❌| | GH-72749
**Area3D** |  |  |  | 
Propertyprioritychanges type fromfloattoint | |❌| | |❌| | |❌| | GH-72749
**PhysicsDirectSpaceState2D** |  |  |  | 
Methodcollide_shapechanges return type fromArray[PackedVector2Array]toArray[Vector2] | |❌| | |❌| | |❌| | GH-75260
**PhysicsDirectSpaceState3D** |  |  |  | 
Methodcollide_shapechanges return type fromArray[PackedVector3Array]toArray[Vector3] | |❌| | |❌| | |❌| | GH-75260

### Rendering

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**RDShaderFile** |  |  |  | 
Methodget_version_listchanges return type fromPackedStringArraytoArray[StringName] | |✔️| | |❌| | |❌| | GH-76418
**RenderingDevice** |  |  |  | 
Methoddraw_list_beginchangesstorage_texturesparameter type from untypedArraytoArray[RID] | |✔️| | |✔️ with compat| | |❌| | GH-76418
**RenderingServer** |  |  |  | 
Methodglobal_shader_parameter_get_listchanges return type fromPackedStringArraytoArray[StringName] | |✔️| | |❌| | |❌| | GH-76418
**SurfaceTool** |  |  |  | 
Methodadd_triangle_fanchangestangentsparameter type from untypedArraytoArray[Plane] | |✔️| | |✔️ with compat| | |❌| | GH-76418

### Navigation

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**NavigationAgent2D** |  |  |  | 
Methodset_velocityreplaced withvelocityproperty | |✔️| | |❌| | |❌| | GH-69988
Propertytime_horizonsplit intotime_horizon_agentsandtime_horizon_obstacles | |❌| | |❌| | |❌| | GH-69988
**NavigationAgent3D** |  |  |  | 
Propertyagent_height_offsetrenamed topath_height_offset | |❌| | |❌| | |❌| | GH-69988
Propertyignore_yremoved | |❌| | |❌| | |❌| | GH-69988
Methodset_velocityreplaced withvelocityproperty | |✔️| | |❌| | |❌| | GH-69988
Propertytime_horizonsplit intotime_horizon_agentsandtime_horizon_obstacles | |❌| | |❌| | |❌| | GH-69988
**NavigationObstacle2D** |  |  |  | 
Propertyestimate_radiusremoved | |❌| | |❌| | |❌| | GH-69988
Methodget_ridrenamed toget_agent_rid | |❌| | |❌| | |❌| | GH-69988
**NavigationObstacle3D** |  |  |  | 
Propertyestimate_radiusremoved | |❌| | |❌| | |❌| | GH-69988
Methodget_ridrenamed toget_agent_rid | |❌| | |❌| | |❌| | GH-69988
**NavigationServer2D** |  |  |  | 
Methodagent_set_callbackrenamed toagent_set_avoidance_callback | |❌| | |❌| | |❌| | GH-69988
Methodagent_set_target_velocityremoved | |❌| | |❌| | |❌| | GH-69988
Methodagent_set_time_horizonsplit intoagent_set_time_horizon_agentsandagent_set_time_horizon_obstacles | |❌| | |❌| | |❌| | GH-69988
**NavigationServer3D** |  |  |  | 
Methodagent_set_callbackrenamed toagent_set_avoidance_callback | |❌| | |❌| | |❌| | GH-69988
Methodagent_set_target_velocityremoved | |❌| | |❌| | |❌| | GH-69988
Methodagent_set_time_horizonsplit intoagent_set_time_horizon_agentsandagent_set_time_horizon_obstacles | |❌| | |❌| | |❌| | GH-69988

### Networking

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**WebRTCPeerConnectionExtension** |  |  |  | 
Method_create_data_channelchanges return type fromObjecttoWebRTCDataChannel | |✔️| | |❌| | |✔️| | GH-78237

### Editor plugins

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**AnimationTrackEditPlugin** |  |  |  | 
TypeAnimationTrackEditPluginremoved | |❌| | |❌| | |❌| | GH-76413
**EditorInterface** |  |  |  | 
TypeEditorInterfacechanges inheritance fromNodetoObject | |✔️| | |❌| | |❌| | GH-76176
Methodset_movie_maker_enabledreplaced withmovie_maker_enabledproperty | |✔️| | |❌| | |❌| | GH-76176
Methodis_movie_maker_enabledreplaced withmovie_maker_enabledproperty | |✔️| | |❌| | |❌| | GH-76176
**EditorResourcePreviewGenerator** |  |  |  | 
Method_generateadds a newmetadataparameter | |❌| | |❌| | |❌| | GH-64628
Method_generate_from_pathadds a newmetadataparameter | |❌| | |❌| | |❌| | GH-64628
**EditorUndoRedoManager** |  |  |  | 
Methodcreate_actionadds a newbackward_undo_opsoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-76688

## Behavior changes

In 4.1 some behavior changes have been introduced, which might require you to adjust your project.

Change | Introduced
------ | ----------
**SubViewportContainer** | 
When input events should reach SubViewports and their children,SubViewportContainer.mouse_filternow needs to beMOUSE_FILTER_STOPorMOUSE_FILTER_PASS. SeeGH-79271for details. | GH-57894
Multiple layeredSubViewportContainernodes, that should all receive mouse input events, now need to be replaced byArea2Dnodes. SeeGH-79128for details. | GH-57894
**Viewport** | 
Viewportnodes, that have Physics Picking enabled, now automatically set InputEvents as handled. SeeGH-79897for workarounds. | GH-77595

## Updating your GDExtension for 4.1

GDExtension is still in beta. Until it's marked as stable, compatibility may break when
upgrading to a new minor version of Godot.

In order to fix a serious bug, in Godot 4.1 we had to break binary compatibility in a big
way and source compatibility in a small way.

This means that GDExtensions made for Godot 4.0 will need to be recompiled for Godot 4.1
(using the  4.1 branch of godot-cpp), with a small change to their source code.

In Godot 4.0, your "entry_symbol" function looks something like this:

```
GDExtensionBool GDE_EXPORT example_library_init(const GDExtensionInterface *p_interface, const GDExtensionClassLibraryPtr p_library, GDExtensionInitialization *r_initialization) {
    godot::GDExtensionBinding::InitObject init_obj(p_interface, p_library, r_initialization);

    init_obj.register_initializer(initialize_example_module);
    init_obj.register_terminator(uninitialize_example_module);
    init_obj.set_minimum_library_initialization_level(MODULE_INITIALIZATION_LEVEL_SCENE);

    return init_obj.init();
}
```

However, for Godot 4.1, it should look like:

```
GDExtensionBool GDE_EXPORT example_library_init(GDExtensionInterfaceGetProcAddress p_get_proc_address, const GDExtensionClassLibraryPtr p_library, GDExtensionInitialization *r_initialization) {
    godot::GDExtensionBinding::InitObject init_obj(p_get_proc_address, p_library, r_initialization);

    init_obj.register_initializer(initialize_example_module);
    init_obj.register_terminator(uninitialize_example_module);
    init_obj.set_minimum_library_initialization_level(MODULE_INITIALIZATION_LEVEL_SCENE);

    return init_obj.init();
}
```

There are two small changes:

1. The first argument changes from const GDExtensionInterface *p_interface to GDExtensionInterfaceGetProcAddress p_get_proc_address

1. The constructor for the `init_obj` variable now receives p_get_proc_address as its first parameter

You also need to add an extra compatibility_minimum line to your .gdextension file, so that it looks something like:

```
[configuration]

entry_symbol = "example_library_init"
compatibility_minimum = 4.1
```

This lets Godot know that your GDExtension has been updated and is safe to load in Godot 4.1.