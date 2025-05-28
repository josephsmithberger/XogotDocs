<!-- Remove this line to publish to docs.xogot.com -->
# Upgrading from Godot 4.1 to Godot 4.2

For most games and apps made with 4.1 it should be relatively safe to migrate to 4.2.
This page intends to cover everything you need to pay attention to when migrating
your project.

## Breaking changes

If you are migrating from 4.1 to 4.2, the breaking changes listed here might
affect you. Changes are grouped by areas/systems.

> Warning:
>
> The [Mesh](https://docs.godotengine.org/en/stable/classes/class_mesh.html#class-mesh) resource format has changed in 4.2 to allow for
> vertex and attribute compression.
> This allows for improved rendering performance, especially on platforms
> constrained by memory bandwidth such as mobile.
>
> It is still possible to load the Godot 4.0-4.1 Mesh formats, but it is
> **not** possible to load the Godot 4.2 Mesh format in prior Godot versions.
> When opening a Godot project made with a version prior to 4.2, you may
> be presented with an upgrade dialog that offers two options:
>
> - **Restart & Upgrade:** Upgrades the mesh format for all meshes in the
> project and saves the result to disk. Once chosen, this option prevents
> downgrading the project to a Godot version prior to 4.2. Set up a
> version control system and push your changes before choosing this option!
> - **Upgrade Only:** Upgrades the mesh format in-memory without writing it
> to disk. This allows downgrading the project to a Godot version older than 4.2
> if you need to do so in the future. The downside is that loading the project
> will be slower every time as the mesh format needs to be upgraded every time
> the project is loaded. These increased loading times will also affect the
> exported project. The number and complexity of Mesh resources determines
> how much loading times are affected.
>
> If this dialog doesn't appear, use **Project > Tools > Upgrade Mesh Surfaces…**
> at the top of the editor.
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
**Node** |  |  |  | 
ConstantNOTIFICATION_NODE_RECACHE_REQUESTEDremoved | |❌| | |✔️| | |❌| | GH-84419

### Animation

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**AnimationPlayer** |  |  |  | 
Method_post_process_key_valuemoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Methodadd_animation_librarymoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Methodadvancemoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Signalanimation_finishedmoved to base classAnimationMixer | |✔️| | |❌| | |❌| | GH-80813
Signalanimation_startedmoved to base classAnimationMixer | |✔️| | |❌| | |❌| | GH-80813
Signalanimation_libraries_updatedmoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Signalanimation_list_changedmoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Propertyaudio_max_polyphonymoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Signalcaches_clearedmoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Methodclear_cachesmoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Methodfind_animationmoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Methodfind_animation_librarymoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Methodget_animationmoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Methodget_animation_librarymoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Methodget_animation_library_listmoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Methodget_animation_listmoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Methodhas_animationmoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Methodhas_animation_librarymoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Propertymethod_call_moderenamed tocallback_mode_methodand moved to base classAnimationMixer | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-80813
Propertyplayback_activerenamed toactiveand moved to base classAnimationMixer | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-80813
Propertyplayback_process_moderenamed tocallback_mode_processand moved to base classAnimationMixer | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-80813
Methodremove_animation_librarymoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Methodrename_animation_librarymoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Propertyreset_on_savemoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Propertyroot_nodemoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Methodset_reset_on_save_enabledmoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Methodseekadds a newupdate_onlyoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-80813
**AnimationTree** |  |  |  | 
Method_post_process_key_valuemoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Propertyactivemoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Methodadvancemoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Signalanimation_finishedmoved to base classAnimationMixer | |✔️| | |❌| | |❌| | GH-80813
Signalanimation_startedmoved to base classAnimationMixer | |✔️| | |❌| | |❌| | GH-80813
Propertyaudio_max_polyphonymoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Methodget_root_motion_positionmoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Methodget_root_motion_position_accumulatormoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Methodget_root_motion_rotationmoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Methodget_root_motion_rotation_accumulatormoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Methodget_root_motion_scalemoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Methodget_root_motion_scale_accumulatormoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Propertyprocess_callbackrenamed tocallback_mode_processand moved to base classAnimationMixer | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-80813
Propertyroot_motion_trackmoved to base classAnimationMixer | |✔️| | |✔️| | |✔️| | GH-80813
Propertytree_rootchanges type fromAnimationNodetoAnimationRootNode | |✔️| | |❌| | |❌| | GH-80813

### GUI nodes

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**PopupMenu** |  |  |  | 
Methodadd_icon_shortcutadds a newallow_echooptional parameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-36493
Methodadd_shortcutadds a newallow_echooptional parameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-36493
Methodclearadds a newfree_submenusoptional parameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-79965
**RichTextLabel** |  |  |  | 
Methodadd_imageadds newkey,pad,tooltip, andsize_in_percentoptional parameters | |✔️| | |✔️ with compat| | |✔️| | GH-80410

### Rendering

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**ImporterMesh** |  |  |  | 
Methodadd_surfacechangesflagsparameter type fromuint32touint64 | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-81138
Methodget_surface_formatchanges return type fromuint32touint64 | |✔️| | |❌| | |❌| | GH-81138
**MeshDataTool** |  |  |  | 
Methodcommit_to_surfaceadds a newcompression_flagsoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-81138
Methodget_formatchanges return type fromuint32touint64 | |✔️| | |❌| | |❌| | GH-81138
**RenderingDevice** |  |  |  | 
Enum fieldBarrierMask.BARRIER_MASK_RASTERchanges value from1to9 | |✔️| | |✔️| | |✔️| | GH-79911
Enum fieldBarrierMask.BARRIER_MASK_ALL_BARRIERSchanges value from7to32767 | |✔️| | |✔️| | |✔️| | GH-79911
Enum fieldBarrierMask.BARRIER_MASK_NO_BARRIERchanges value from8to32768 | |✔️| | |✔️| | |✔️| | GH-79911
Methodshader_create_from_bytecodeadds a newplaceholder_ridoptional parameter | |✔️| | |✔️ with compat| | |✔️| | GH-79606
Methodshader_get_vertex_input_attribute_askchanges return type fromuint32touint64 | |✔️| | |❌| | |❌| | GH-81138
**SurfaceTool** |  |  |  | 
Methodcommitchangesflagsparameter type fromuint32touint64 | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-81138

### Text

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**Font** |  |  |  | 
Methodset_fallbacksreplaced withfallbacksproperty | |✔️| | |❌| | |❌| | GH-78266
Methodget_fallbacksreplaced withfallbacksproperty | |✔️| | |❌| | |❌| | GH-78266
Methodfind_variationadds newspacing_top,spacing_bottom,spacing_space, andspacing_glyphoptional parameters | |✔️| | |✔️ with compat| | |✔️| | GH-80954

### GraphEdit

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**GraphEdit** |  |  |  | 
Propertyarrange_nodes_button_hiddenrenamed toshow_arrange_button | |❌| | |✔️ with compat| | |✔️ with compat| | GH-81582
Methodget_zoom_hboxrenamed toget_menu_hbox | |❌| | |✔️ with compat| | |✔️ with compat| | GH-79308
Propertysnap_distancerenamed tosnapping_distance | |❌| | |✔️ with compat| | |✔️ with compat| | GH-79308
Propertyuse_snaprenamed tosnapping_enabled | |❌| | |✔️ with compat| | |✔️ with compat| | GH-79308
**GraphNode** |  |  |  | 
Propertycommentremoved | |❌| | |❌| | |❌| | GH-79307
Signalclose_requestrenamed todelete_requestand moved to base classGraphElement | |❌| | |✔️ with compat| | |✔️ with compat| | GH-79311
Propertydraggablemoved to base classGraphElement | |✔️| | |✔️| | |✔️| | GH-79311
Propertydraggablemoved to base classGraphElement | |✔️| | |✔️| | |✔️| | GH-79311
Signaldraggedmoved to base classGraphElement | |✔️| | |❌| | |❌| | GH-79311
Methodget_connection_input_colorremoved | |❌| | |❌| | |❌| | GH-79311
Methodget_connection_input_countremoved | |❌| | |❌| | |❌| | GH-79311
Methodget_connection_input_heightremoved | |❌| | |❌| | |❌| | GH-79311
Methodget_connection_input_positionremoved | |❌| | |❌| | |❌| | GH-79311
Methodget_connection_input_slotremoved | |❌| | |❌| | |❌| | GH-79311
Methodget_connection_input_typeremoved | |❌| | |❌| | |❌| | GH-79311
Methodget_connection_output_colorremoved | |❌| | |❌| | |❌| | GH-79311
Methodget_connection_output_countremoved | |❌| | |❌| | |❌| | GH-79311
Methodget_connection_output_heightremoved | |❌| | |❌| | |❌| | GH-79311
Methodget_connection_output_positionremoved | |❌| | |❌| | |❌| | GH-79311
Methodget_connection_output_slotremoved | |❌| | |❌| | |❌| | GH-79311
Methodget_connection_output_typeremoved | |❌| | |❌| | |❌| | GH-79311
Propertylanguageremoved | |❌| | |❌| | |❌| | GH-79311
Signalnode_deselectedmoved to base classGraphElement | |✔️| | |✔️| | |✔️| | GH-79311
Signalnode_selectedmoved to base classGraphElement | |✔️| | |✔️| | |✔️| | GH-79311
Propertyoverlayremoved | |❌| | |❌| | |❌| | GH-79311
Propertyposition_offsetmoved to base classGraphElement | |✔️| | |✔️| | |✔️| | GH-79311
Signalposition_offset_changedmoved to base classGraphElement | |✔️| | |✔️| | |✔️| | GH-79311
Signalraise_requestmoved to base classGraphElement | |✔️| | |✔️| | |✔️| | GH-79311
Propertyresizablemoved to base classGraphElement | |✔️| | |✔️| | |✔️| | GH-79311
Signalresize_requestmoved to base classGraphElement | |✔️| | |❌| | |❌| | GH-79311
Propertyselectablemoved to base classGraphElement | |✔️| | |✔️| | |✔️| | GH-79311
Propertyselectedmoved to base classGraphElement | |✔️| | |✔️| | |✔️| | GH-79311
Propertyshow_closeremoved | |❌| | |❌| | |❌| | GH-79311
Propertytext_directionremoved | |❌| | |❌| | |❌| | GH-79311

### TileMap

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**TileMap** |  |  |  | 
Propertycell_quadrant_sizerenamed torendering_quadrant_size | |❌| | |✔️ with compat| | |✔️ with compat| | GH-81070

### XR

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**XRInterface** |  |  |  | 
Propertyenvironment_blend_modeadded | |✔️| | |❌| | |❌| | GH-81561

> Note:
>
> This change breaks compatibility in C# because the new property conflicts with the name of an existing enum
> and the C# bindings generator gives priority to properties, so the enum type was renamed from
> EnvironmentBlendMode to EnvironmentBlendModeEnum.
>