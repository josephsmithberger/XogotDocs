<!-- Remove this line to publish to docs.xogot.com -->
# Upgrading from Godot 4.3 to Godot 4.4

For most games and apps made with 4.3 it should be relatively safe to migrate to 4.4.
This page intends to cover everything you need to pay attention to when migrating
your project.

## Breaking changes

If you are migrating from 4.3 to 4.4, the breaking changes listed here might
affect you. Changes are grouped by areas/systems.

This article indicates whether each breaking change affects GDScript and whether
the C# breaking change is binary compatible or source compatible:

- **Binary compatible** - Existing binaries will load and execute successfully without
recompilation, and the run-time behavior won't change.

- **Source compatible** - Source code will compile successfully without changes when
upgrading Godot.

### Core

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**FileAccess** |  |  |  | 
Methodopen_encryptedadds a newivoptional parameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-98918
Methodstore_8changes return type fromvoidtobool | |✔️| | |❌| | |✔️| | GH-78289
Methodstore_16changes return type fromvoidtobool | |✔️| | |❌| | |✔️| | GH-78289
Methodstore_32changes return type fromvoidtobool | |✔️| | |❌| | |✔️| | GH-78289
Methodstore_64changes return type fromvoidtobool | |✔️| | |❌| | |✔️| | GH-78289
Methodstore_bufferchanges return type fromvoidtobool | |✔️| | |❌| | |✔️| | GH-78289
Methodstore_csv_linechanges return type fromvoidtobool | |✔️| | |❌| | |✔️| | GH-78289
Methodstore_doublechanges return type fromvoidtobool | |✔️| | |❌| | |✔️| | GH-78289
Methodstore_floatchanges return type fromvoidtobool | |✔️| | |❌| | |✔️| | GH-78289
Methodstore_halfchanges return type fromvoidtobool | |✔️| | |❌| | |✔️| | GH-78289
Methodstore_linechanges return type fromvoidtobool | |✔️| | |❌| | |✔️| | GH-78289
Methodstore_pascal_stringchanges return type fromvoidtobool | |✔️| | |❌| | |✔️| | GH-78289
Methodstore_realchanges return type fromvoidtobool | |✔️| | |❌| | |✔️| | GH-78289
Methodstore_stringchanges return type fromvoidtobool | |✔️| | |❌| | |✔️| | GH-78289
Methodstore_varchanges return type fromvoidtobool | |✔️| | |❌| | |✔️| | GH-78289
**OS** |  |  |  | 
Methodexecute_with_pipeadds a newblockingoptional parameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-94434
Methodread_string_from_stdinadds a newbuffer_sizeparameter[1] | |❌| | |✔️ with compat| | |✔️ with compat| | GH-91201
**RegEx** |  |  |  | 
Methodcompileadds a newshow_erroroptional parameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-95212
Methodcreate_from_stringadds a newshow_erroroptional parameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-95212
**Semaphore** |  |  |  | 
Methodpostadds a newcountoptional parameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-93605
**TranslationServer** |  |  |  | 
Methodstandardize_localeadds a newadd_defaultsoptional parameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-98972

Default buffer size in 4.3 is 1024.

### GUI nodes

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**RichTextLabel** |  |  |  | 
Methodpush_metaadds a newtooltipoptional parameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-99481
Methodset_table_column_expandadds a newshrinkoptional parameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-101482
**GraphEdit** |  |  |  | 
Methodconnect_nodeadds a newkeep_aliveoptional parameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-97449
Signalframe_rect_changedchangesnew_rectparameter type fromVector2toRect2 | |❌| | |❌| | |❌| | GH-102796

### Physics

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**SoftBody3D** |  |  |  | 
Methodset_point_pinnedadds a newinsert_atoptional parameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-94684

### Rendering

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**CPUParticles2D** |  |  |  | 
Methodrestartadds a newkeep_seedoptional parameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-92089
**CPUParticles3D** |  |  |  | 
Methodrestartadds a newkeep_seedoptional parameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-92089
**GPUParticles2D** |  |  |  | 
Methodrestartadds a newkeep_seedoptional parameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-92089
**GPUParticles3D** |  |  |  | 
Methodrestartadds a newkeep_seedoptional parameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-92089
**RenderingDevice** |  |  |  | 
Methoddraw_list_beginadds a newbreadcrumboptional parameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-90993
Methoddraw_list_beginremoves many parameters | |❌| | |✔️ with compat| | |✔️ with compat| | GH-98670
Methodindex_buffer_createadds a newenable_device_addressoptional parameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-100062
Methoduniform_buffer_createadds a newenable_device_addressoptional parameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-100062
Methodvertex_buffer_createadds a newenable_device_addressoptional parameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-100062
**RenderingServer** |  |  |  | 
Methodmultimesh_allocate_dataadds a newuse_indirectoptional parameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-99455
**Shader** |  |  |  | 
Methodget_default_texture_parameterchanges return type fromTexture2DtoTexture | |✔️| | |❌| | |❌| | GH-95126
Methodset_default_texture_parameterchangestextureparameter type fromTexture2DtoTexture | |✔️| | |❌| | |✔️| | GH-95126
**VisualShaderNodeCubemap** |  |  |  | 
Propertycube_mapchanges type fromCubemaptoTextureLayered | |✔️| | |❌| | |❌| | GH-95126
**VisualShaderNodeTexture2DArray** |  |  |  | 
Propertytexture_arraychanges type fromTexture2DArraytoTextureLayered | |✔️| | |❌| | |❌| | GH-95126

> Note:
>
> In C#, the enum RenderingDevice.StorageBufferUsage breaks compatibility because of the way the bindings generator
> detects the enum prefix. New members where added in GH-100062 to the enum that caused the enum members to be renamed.
>

### Navigation

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**NavigationServer2D** |  |  |  | 
Methodquery_pathadds a newcallbackoptional parameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-100129
**NavigationServer3D** |  |  |  | 
Methodquery_pathadds a newcallbackoptional parameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-100129

### Editor plugins

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced
------ | ------------------- | -------------------- | -------------------- | ----------
**EditorInterface** |  |  |  | 
Methodopen_scene_from_pathadds a newset_inheritedoptional parameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-90057
Methodpopup_node_selectoradds a newcurrent_valueoptional parameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-94323
Methodpopup_property_selectoradds a newcurrent_valueoptional parameter | |✔️| | |✔️ with compat| | |✔️ with compat| | GH-94323
**EditorSceneFormatImporter** |  |  |  | 
Method_get_import_flagsremoved | |❌| | |❌| | |❌| | GH-101531
**EditorTranslationParserPlugin** |  |  |  | 
Method_parse_filechanges return type toArrayand removesmsgidsandmsgids_context_pluralparameters | |❌| | |❌| | |❌| | GH-99297

> Note:
>
> The method _get_import_flags was never used by the engine. It was removed despite the
> compatibility breakage as there's no way for users to rely on this affecting engine behavior.
>

## Behavior changes

### Core

> Note:
>
> The Curve resource now enforces its value range, so min_value and max_value need to be changed
> if any of the points fall outside of the default [0, 1] range.
>

### Rendering

> Note:
>
> The VisualShaderNodeVec4Constant shader node had its input type changed to Vector4. Users need to
> recreate the values in their constants.
>

### CSG

> Note:
>
> The CSG implementation now uses Emmett Lalish's Manifold library (GH-94321).
> The new implementation is more consistent with manifold definitions and fixes a number of bugs and stability
> issues. As a result, non-manifold meshes are no longer supported. You can use MeshInstance3D for
> rendering non-manifold geometry, such as quads or planes.
>

### Android

> Note:
>
> Android sensor events are no longer enabled by default (GH-94799). Projects that use sensor events can
> enable them as needed in Project Settings under **Input Devices > Sensors**.
>