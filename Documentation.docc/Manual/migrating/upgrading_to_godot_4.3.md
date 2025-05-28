<!-- Remove this line to publish to docs.xogot.com -->
# Upgrading from Godot 4.2 to Godot 4.3

For most games and apps made with 4.2 it should be relatively safe to migrate to 4.3.
This page intends to cover everything you need to pay attention to when migrating
your project.

## Breaking changes

If you are migrating from 4.2 to 4.3, the breaking changes listed here might
affect you. Changes are grouped by areas/systems.

This article indicates whether each breaking change affects GDScript and whether
the C# breaking change is binary compatible or source compatible:

- **Binary compatible** - Existing binaries will load and execute successfully without
recompilation, and the runtime behavior won't change.

- **Source compatible** - Source code will compile successfully without changes when
upgrading Godot.

### GDExtension

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**GDExtension** |  |  |  | 
Methodclose_libraryremoved | |❌| | |❌| | |❌| | GH-88418
Methodinitialize_libraryremoved | |❌| | |❌| | |❌| | GH-88418
Methodopen_libraryremoved | |❌| | |❌| | |❌| | GH-88418

Since it was basically impossible to use these methods in any useful way, these methods have been removed. Use GDExtensionManager::load_extension and GDExtensionManager::unload_extension instead to correctly load and unload a GDExtension.

### Animation

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**Animation** |  |  |  | 
Methodposition_track_interpolateadds a newbackwardoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-86629
Methodrotation_track_interpolateadds a newbackwardoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-86629
Methodscale_track_interpolateadds a newbackwardoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-86629
Methodblend_shape_track_interpolateadds a newbackwardoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-86629
Methodvalue_track_interpolateadds a newbackwardoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-86629
Methodtrack_find_keyadds a newlimitoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-86661
Methodtrack_find_keyadds a newbackwardoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-92861
**AnimationMixer** |  |  |  | 
Method_post_process_key_valuechangesobjectparameter type fromObjecttouint64 | |✔️| | |❌| | |❌| | GH-86687
**Skeleton3D** |  |  |  | 
Methodadd_bonechanges return type fromvoidtoint32 | |✔️| | |❌| | |✔️| | GH-88791
Signalbone_pose_changedreplaced byskeleton_updated | |❌| | |❌| | |❌| | GH-90575
**BoneAttachment3D** |  |  |  | 
Methodon_bone_pose_updatereplaced byon_skeleton_update | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-90575

### GUI nodes

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**AcceptDialog** |  |  |  | 
Methodregister_text_enterchanges parameterline_edittype fromControltoLineEdit | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-89419
Methodremove_buttonchanges parameterbuttontype fromControltoButton | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-89419

### Physics

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**PhysicsShapeQueryParameters3D** |  |  |  | 
Propertymotionchanges type fromVector2toVector3 | |❌| | |❌| | |❌| | GH-85393

> Note:
>
> In C#, the enum PhysicsServer3D.G6DofJointAxisFlag breaks compatibility because of the way the bindings generator
> detects the enum prefix. New members were added in GH-89851 to the enum that caused the enum members to be renamed.
>

### Rendering

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**RenderingDevice** |  |  |  | 
Enum fieldFinalAction.FINAL_ACTION_CONTINUEchanges value from2to0 | |✔️| | |❌| | |❌| | GH-84976
Enum fieldInitialAction.INITIAL_ACTION_CLEARchanges value from0to1 | |✔️| | |❌| | |❌| | GH-84976
Enum fieldInitialAction.INITIAL_ACTION_CLEAR_REGION_CONTINUEchanges value from2to1 | |✔️| | |❌| | |❌| | GH-84976
Enum fieldInitialAction.INITIAL_ACTION_CONTINUEchanges value from5to0 | |✔️| | |❌| | |❌| | GH-84976
Enum fieldInitialAction.INITIAL_ACTION_DROPchanges value from4to2 | |✔️| | |❌| | |❌| | GH-84976
Enum fieldInitialAction.INITIAL_ACTION_KEEPchanges value from3to0 | |✔️| | |❌| | |❌| | GH-84976
Methodbuffer_clearremovespost_barrierparameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-84976
Methodbuffer_updateremovespost_barrierparameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-84976
Methodcompute_list_beginremovesallow_draw_overlapparameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-84976
Methodcompute_list_endremovespost_barrierparameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-84976
Methoddraw_list_beginremovesstorage_texturesparameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-84976
Methoddraw_list_endremovespost_barrierparameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-84976
Methodtexture_clearremovespost_barrierparameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-84976
Methodtexture_copyremovespost_barrierparameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-84976
Methodtexture_resolve_multisampleremovespost_barrierparameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-84976
Methodtexture_updateremovespost_barrierparameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-84976
**RenderingServer** |  |  |  | 
Methodenvironment_set_fogadds a newfog_modeoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-84792
**RenderSceneBuffersRD** |  |  |  | 
Methodget_color_layeradds a newmsaaoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-80214
Methodget_depth_layeradds a newmsaaoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-80214
Methodget_velocity_layeradds a newmsaaoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-80214
Methodget_color_textureadds a newmsaaoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-80214
Methodget_depth_textureadds a newmsaaoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-80214
Methodget_velocity_textureadds a newmsaaoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-80214

> Note:
>
> While the values of the enum fields in RenderingDevice.InitialAction and RenderingDevice.FinalAction changed,
> the only method that consumed them (draw_list_begin) added a compatibility method which supports the old values.
> So in practice it doesn't break compatibility.
>

> Note:
>
> In C#, the enum RenderingDevice.DriverResource breaks compatibility because of the way the bindings generator
> detects the enum prefix. New members were added in GH-83452 to the enum that caused the enum members to be
> renamed.
>

### Text

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**Font** |  |  |  | 
Methodfind_variationadds a newbaseline_offsetoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-87668
**RichTextLabel** |  |  |  | 
Methodpush_metaadds a newunderline_modeoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-89024
**TextServer** |  |  |  | 
Methodshaped_text_get_word_breaksadds a new optionalskip_grapheme_flagsparameter | |✔️| | |✔️ with compat| | |✔️| | GH-90732
**TextServerExtension** |  |  |  | 
Method_shaped_text_get_word_breaksadds a newskip_grapheme_flagsparameter | |❌| | |❌| | |❌| | GH-90732

### Audio

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**AudioStreamPlaybackPolyphonic** |  |  |  | 
Methodplay_streamadds newplayback_type, andbusoptional parameters | |✔️| | |✔️ with compat| | |✔️| | GH-91382

### Navigation

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**AStar2D** |  |  |  | 
Methodget_id_pathadds newallow_partial_pathoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-88047
Methodget_point_pathadds newallow_partial_pathoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-88047
**AStar3D** |  |  |  | 
Methodget_id_pathadds newallow_partial_pathoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-88047
Methodget_point_pathadds newallow_partial_pathoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-88047
**AStarGrid2D** |  |  |  | 
Methodget_id_pathadds newallow_partial_pathoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-88047
Methodget_point_pathadds newallow_partial_pathoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-88047
**NavigationRegion2D** |  |  |  | 
Propertyavoidance_layersremoved | |❌| | |❌| | |❌| | GH-90747
Propertyconstrain_avoidanceremoved | |❌| | |❌| | |❌| | GH-90747
Methodget_avoidance_layer_valueremoved | |❌| | |❌| | |❌| | GH-90747
Methodset_avoidance_layer_valueremoved | |❌| | |❌| | |❌| | GH-90747

> Note:
>
> The constrain avoidance feature in NavigationRegion2D was experimental and has been discontinued with no
> replacement.
>

### TileMap

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**TileData** |  |  |  | 
Methodget_navigation_polygonadds newflip_h,flip_v, andtransposeoptional parameters | |✔️| | |✔️ with compat| | |✔️| | GH-84660
Methodget_occluderadds newflip_h,flip_v, andtransposeoptional parameters | |✔️| | |✔️ with compat| | |✔️| | GH-84660

### XR

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**WebXRInterface** |  |  |  | 
Methodget_input_source_trackerchanges return type fromXRPositionalTrackertoXRControllerTracker | |✔️| | |❌| | |✔️| | GH-90645
**XRServer** |  |  |  | 
Methodget_trackerchanges return type fromXRPositionalTrackertoXRTracker | |✔️| | |❌| | |❌| | GH-90645

### Editor plugins

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**EditorInspectorPlugin** |  |  |  | 
Methodadd_property_editoradds a newlabeloptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-92322
**EditorPlugin** |  |  |  | 
Methodadd_control_to_bottom_paneladds a newshortcutoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-88081
Methodadd_control_to_dockadds a newshortcutoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-88081
**EditorSceneFormatImporterFBX** |  |  |  | 
Type renamed toEditorSceneFormatImporterFBX2GLTF | |❌| | |❌| | |❌| | GH-81746

## Behavior changes

In 4.3 some behavior changes have been introduced, which might require you to adjust your project.

### Core

> Note:
>
> Binary serialization was modified to fix some issues with the serialization of scripted Objects and typed Arrays (GH-78219).
> This breaks compat with script encoding/decoding.
>

> Note:
>
> PackedByteArray is now able to use a more compact base64 encoding for storage. But the trade-off is that it breaks
> compatibility, meaning that older versions of Godot may not be able to open resources saved by 4.3 (GH-89186).
>
> To maximize compatibility, this new storage format will only be enabled for resources and scenes that contain large
> PackedByteArrays for now. Support for this new format will also be added in patch updates for older versions of Godot.
> Once all supported Godot versions are able to read the new format, we will gradually retire the compatibility measures
> and have all resources and scenes use the new storage format.
>

> Note:
>
> In C#, the Transform3D.InterpolateWith implementation was fixed to use the right order of operations, applying the rotation before the scale (GH-89843).
>

> Note:
>
> In C#, the Aabb.GetSupport implementation was fixed to properly return the support vector (GH-88919).
>

> Note:
>
> In C#, the Variant types' ToString implementation now defaults to using the InvariantCulture (GH-89547)
> which means Vector2(1.2, 3.4) is formatted using . as the decimal separator independently of the language
> of the operating system that the program is running on.
>

### Animation

> Note:
>
> AnimationMixer replaced its Capture mode with a new Capture feature that works much better than the old one,
> this replaces the existing cache (GH-86715).
>

> Note:
>
> AnimationNode has a reworked process for retrieving the semantic time info. This ensures that time-related
> behavior works as expected, but changes the blending behavior. Implementors of the _process virtual method
> should also note that this method is now deprecated and will be replaced by a new one in the future (GH-87171).
>

More information about the changes to Animation can be found in the
Migrating Animations from Godot 4.0 to 4.3
article.

### GUI nodes

> Note:
>
> The default font outline color was changed from white to black (GH-54641).
>

> Note:
>
> The auto_translate property is deprecated in favor of the auto_translate_mode property which is now in Node (GH-87530).
> The default value for auto_translate_mode is AUTO_TRANSLATE_INHERIT, which means nodes inherit the auto_translate_mode value
> from their parent. This means, existing nodes with the auto_translate property set to true may no longer be translated if they
> are children of a node with the auto_translate property set to false.
>

### Multiplayer

> Note:
>
> The SceneMultiplayer caching protocol was changed to send the received ID instead of the Node path when sending a node removal confirmation packet (GH-90027).
>
> This is a breaking change for the high-level multiplayer protocol making it incompatible with previous Godot versions.
> Upgrade both your server and client versions to Godot 4.3 to handle this change gracefully.
>
> Note that high-level multiplayer facilities are only ever meant to be compatible with server and client using the same Godot version. It is recommended to implement some kind of version checking.
>

### Rendering

> Note:
>
> Decals now convert the modulate color from an sRGB color to a linear color, like all other inputs, to ensure proper
> blending (GH-89849). Existing projects that were using the decal's modulate property will notice a change in
> their visuals.
>

> Note:
>
> The reverse Z depth buffer technique is now implemented. This may break compatibility for some shaders.
> Read the Introducing Reverse Z (AKA I'm sorry for breaking your shader)
> article for more information and guidance on how to fix common scenarios.
>

### TileMap

> Note:
>
> TileMap layers were moved to individual nodes (GH-87379 and GH-89179).
>

### Android

> Note:
>
> Android permissions are no longer requested automatically because it goes against the recommended best practices (GH-87080).
> Use the request_permission method in OS and the on_request_permissions_result signal on MainLoop to request
> permissions and wait for the user response.
>