<!-- Remove this line to publish to docs.xogot.com -->
# Runtime file loading and saving

> Seealso:
>
> See <doc:saving_games> for information on saving and loading game progression.
>

Sometimes, <doc:exporting_pcks> is not
ideal when you want players to be able to load user-generated content in your
project. It requires users to generate a PCK or ZIP file through the Godot
editor, which contains resources imported by Godot.

Example use cases for runtime file loading and saving include:

- Loading texture packs designed for the game.

- Loading user-provided audio tracks and playing them back in an in-game radio station.

- Loading custom levels or 3D models that can be designed with any 3D DCC that
can export to glTF (including glTF scenes saved by Godot at runtime).

- Using user-provided fonts for menus and HUD.

- Saving/loading a file format that can contain multiple files but can still
easily be read by other applications (ZIP).

- Loading files created by another game or program, or even game data files from
another game not made with Godot.

Runtime file loading can be combined with <doc:http_request_class>
to load resources from the Internet directly.

> Warning:
>
> Do **not** use this runtime loading approach to load resources that are part
> of the project, as it's less efficient and doesn't allow benefiting from
> Godot's resource handling functionality (such as translation remaps). See
> <doc:import_process> for details.
>

> Seealso:
>
> You can see how saving and loading works in action using the
> Run-time File Saving and Loading (Serialization) demo project.
>

## Plain text and binary files

Godot's [FileAccess](https://docs.godotengine.org/en/stable/classes/class_fileaccess.html#class-fileaccess) class provides methods to access files on the
filesystem for reading and writing:

```
func save_file(content):
    var file = FileAccess.open("/path/to/file.txt", FileAccess.WRITE)
    file.store_string(content)

func load_file():
    var file = FileAccess.open("/path/to/file.txt", FileAccess.READ)
    var content = file.get_as_text()
    return content
```

To handle custom binary formats (such as loading file formats not supported by
Godot), [FileAccess](https://docs.godotengine.org/en/stable/classes/class_fileaccess.html#class-fileaccess) provides several methods to read/write integers,
floats, strings and more. These FileAccess methods have names that start with
get_ and store_.

If you need more control over reading binary files or need to read binary
streams that are not part of a file, [PackedByteArray](https://docs.godotengine.org/en/stable/classes/class_packedbytearray.html#class-packedbytearray) provides
several helper methods to decode/encode series of bytes to integers, floats,
strings and more. These PackedByteArray methods have names that start with
decode_ and encode_. See also <doc:binary_serialization_api>.

## Images

Image's [Image.load_from_file](https://docs.godotengine.org/en/stable/classes/class_image_method_load_from_file.html#class-image_method_load_from_file) static method
handles everything, from format detection based on file extension to reading the
file from disk.

If you need error handling or more control (such as changing the scale an SVG is
loaded at), use one of the following methods depending on the file format:

- [Image.load_jpg_from_buffer](https://docs.godotengine.org/en/stable/classes/class_image_method_load_jpg_from_buffer.html#class-image_method_load_jpg_from_buffer)

- [Image.load_ktx_from_buffer](https://docs.godotengine.org/en/stable/classes/class_image_method_load_ktx_from_buffer.html#class-image_method_load_ktx_from_buffer)

- [Image.load_png_from_buffer](https://docs.godotengine.org/en/stable/classes/class_image_method_load_png_from_buffer.html#class-image_method_load_png_from_buffer)

- [Image.load_svg_from_buffer](https://docs.godotengine.org/en/stable/classes/class_image_method_load_svg_from_buffer.html#class-image_method_load_svg_from_buffer)
or [Image.load_svg_from_string](https://docs.godotengine.org/en/stable/classes/class_image_method_load_svg_from_string.html#class-image_method_load_svg_from_string)

- [Image.load_tga_from_buffer](https://docs.godotengine.org/en/stable/classes/class_image_method_load_tga_from_buffer.html#class-image_method_load_tga_from_buffer)

- [Image.load_webp_from_buffer](https://docs.godotengine.org/en/stable/classes/class_image_method_load_webp_from_buffer.html#class-image_method_load_webp_from_buffer)

Several image formats can also be saved by Godot at runtime using the following
methods:

- [Image.save_png](https://docs.godotengine.org/en/stable/classes/class_image_method_save_png.html#class-image_method_save_png)
or [Image.save_png_to_buffer](https://docs.godotengine.org/en/stable/classes/class_image_method_save_png_to_buffer.html#class-image_method_save_png_to_buffer)

- [Image.save_webp](https://docs.godotengine.org/en/stable/classes/class_image_method_save_webp.html#class-image_method_save_webp)
or [Image.save_webp_to_buffer](https://docs.godotengine.org/en/stable/classes/class_image_method_save_webp_to_buffer.html#class-image_method_save_webp_to_buffer)

- [Image.save_jpg](https://docs.godotengine.org/en/stable/classes/class_image_method_save_jpg.html#class-image_method_save_jpg)
or [Image.save_jpg_to_buffer](https://docs.godotengine.org/en/stable/classes/class_image_method_save_jpg_to_buffer.html#class-image_method_save_jpg_to_buffer)

- [Image.save_exr](https://docs.godotengine.org/en/stable/classes/class_image_method_save_exr.html#class-image_method_save_exr)
or [Image.save_exr_to_buffer](https://docs.godotengine.org/en/stable/classes/class_image_method_save_exr_to_buffer.html#class-image_method_save_exr_to_buffer)
(only available in editor builds, cannot be used in exported projects)

The methods with the to_buffer suffix save the image to a PackedByteArray
instead of the filesystem. This is useful to send the image over the network or
into a ZIP archive without having to write it on the filesystem. This can
increase performance by reducing I/O utilization.

> Note:
>
> If displaying the loaded image on a 3D surface, make sure to call
> [Image.generate_mipmaps](https://docs.godotengine.org/en/stable/classes/class_image_method_generate_mipmaps.html#class-image_method_generate_mipmaps)
> so that the texture doesn't look grainy when viewed at a distance.
> This is also useful in 2D when following instructions on
> <doc:multiple_resolutions#Reducing-Aliasing-On-Downsampling>.
>

Example of loading an image and displaying it in a [TextureRect](https://docs.godotengine.org/en/stable/classes/class_texturerect.html#class-texturerect) node
(which requires conversion to [ImageTexture](https://docs.godotengine.org/en/stable/classes/class_imagetexture.html#class-imagetexture)):

```
# Load an image of any format supported by Godot from the filesystem.
var image = Image.load_from_file(path)
# Optionally, generate mipmaps if displaying the texture on a 3D surface
# so that the texture doesn't look grainy when viewed at a distance.
#image.generate_mipmaps()
$TextureRect.texture = ImageTexture.create_from_image(image)

# Save the loaded Image to a PNG image.
image.save_png("/path/to/file.png")

# Save the converted ImageTexture to a PNG image.
$TextureRect.texture.get_image().save_png("/path/to/file.png")
```

## Audio/video files

Godot supports loading Ogg Vorbis, MP3, and WAV audio at runtime. Note that not all
files with an .ogg extension are Ogg Vorbis files. Some may be Ogg Theora
videos, or contain Opus audio within an Ogg container. These files will **not**
load correctly as audio files in Godot.

Example of loading an Ogg Vorbis audio file in an [AudioStreamPlayer](https://docs.godotengine.org/en/stable/classes/class_audiostreamplayer.html#class-audiostreamplayer) node:

```
$AudioStreamPlayer.stream = AudioStreamOggVorbis.load_from_file(path)
```

Example of loading an Ogg Theora video file in a [VideoStreamPlayer](https://docs.godotengine.org/en/stable/classes/class_videostreamplayer.html#class-videostreamplayer) node:

```
var video_stream_theora = VideoStreamTheora.new()
# File extension is ignored, so it is possible to load Ogg Theora videos
# that have an `.ogg` extension this way.
video_stream_theora.file = "/path/to/file.ogv"
$VideoStreamPlayer.stream = video_stream_theora

# VideoStreamPlayer's Autoplay property won't work if the stream is empty
# before this property is set, so call `play()` after setting `stream`.
$VideoStreamPlayer.play()
```

## 3D scenes

Godot has first-class support for glTF 2.0, both in the editor and exported
projects. Using [gltfdocument](https://docs.godotengine.org/en/stable/classes/class_gltfdocument.html#class-gltfdocument) and [gltfstate](https://docs.godotengine.org/en/stable/classes/class_gltfstate.html#class-gltfstate) together,
Godot can load and save glTF files in exported projects, in both text
(.gltf) and binary (.glb) formats. The binary format should be preferred
as it's faster to write and smaller, but the text format is easier to debug.

Example of loading a glTF scene and appending its root node to the scene:

```
# Load an existing glTF scene.
# GLTFState is used by GLTFDocument to store the loaded scene's state.
# GLTFDocument is the class that handles actually loading glTF data into a Godot node tree,
# which means it supports glTF features such as lights and cameras.
var gltf_document_load = GLTFDocument.new()
var gltf_state_load = GLTFState.new()
var error = gltf_document_load.append_from_file("/path/to/file.gltf", gltf_state_load)
if error == OK:
    var gltf_scene_root_node = gltf_document_load.generate_scene(gltf_state_load)
    add_child(gltf_scene_root_node)
else:
    show_error("Couldn't load glTF scene (error code: %s)." % error_string(error))

# Save a new glTF scene.
var gltf_document_save := GLTFDocument.new()
var gltf_state_save := GLTFState.new()
gltf_document_save.append_from_scene(gltf_scene_root_node, gltf_state_save)
# The file extension in the output `path` (`.gltf` or `.glb`) determines
# whether the output uses text or binary format.
# `GLTFDocument.generate_buffer()` is also available for saving to memory.
gltf_document_save.write_to_filesystem(gltf_state_save, path)
```

> Note:
>
> When loading a glTF scene, a base path must be set so that external
> resources like textures can be loaded correctly. When loading from a file,
> the base path is automatically set to the folder containing the file. When
> loading from a buffer, this base path must be manually set as there is no
> way for Godot to infer this path.
>
> To set the base path, set
> [GLTFState.base_path](https://docs.godotengine.org/en/stable/classes/class_gltfstate_property_base_path.html#class-gltfstate_property_base_path) on your
> GLTFState instance before calling
> [GLTFDocument.append_from_buffer](https://docs.godotengine.org/en/stable/classes/class_gltfdocument_method_append_from_buffer.html#class-gltfdocument_method_append_from_buffer)
> or [GLTFDocument.append_from_file](https://docs.godotengine.org/en/stable/classes/class_gltfdocument_method_append_from_file.html#class-gltfdocument_method_append_from_file).
>

## Fonts

[FontFile.load_dynamic_font](https://docs.godotengine.org/en/stable/classes/class_fontfile_method_load_bitmap_font.html#class-fontfile_method_load_bitmap_font) supports the following
font file formats: TTF, OTF, WOFF, WOFF2, PFB, PFM

On the other hand, [FontFile.load_bitmap_font](https://docs.godotengine.org/en/stable/classes/class_fontfile_method_load_bitmap_font.html#class-fontfile_method_load_bitmap_font) supports
the BMFont format (.fnt or .font).

Additionally, it is possible to load any font that is installed on the system using
Godot's support for <doc:using_fonts_system_fonts>.

Example of loading a font file automatically according to its file extension,
then adding it as a theme override to a [Label](https://docs.godotengine.org/en/stable/classes/class_label.html#class-label) node:

```
var path = "/path/to/font.ttf"
var path_lower = path.to_lower()
var font_file = FontFile.new()
if (
        path_lower.ends_with(".ttf")
        or path_lower.ends_with(".otf")
        or path_lower.ends_with(".woff")
        or path_lower.ends_with(".woff2")
        or path_lower.ends_with(".pfb")
        or path_lower.ends_with(".pfm")
):
    font_file.load_dynamic_font(path)
elif path_lower.ends_with(".fnt") or path_lower.ends_with(".font"):
    font_file.load_bitmap_font(path)
else:
    push_error("Invalid font file format.")

if not font_file.data.is_empty():
    # If font was loaded successfully, add it as a theme override.
    $Label.add_theme_font_override("font", font_file)
```

## ZIP archives

Godot supports reading and writing ZIP archives using the [zipreader](https://docs.godotengine.org/en/stable/classes/class_zipreader.html#class-zipreader)
and [zippacker](https://docs.godotengine.org/en/stable/classes/class_zippacker.html#class-zippacker) classes. This supports any ZIP file, including files
generated by Godot's "Export PCK/ZIP" functionality (although these will contain
imported Godot resources rather than the original project files).

> Note:
>
> Use [ProjectSettings.load_resource_pack](https://docs.godotengine.org/en/stable/classes/class_projectsettings_method_load_resource_pack.html#class-projectsettings_method_load_resource_pack)
> to load PCK or ZIP files exported by Godot as
> <doc:exporting_pcks>. That approach is preferred
> for DLCs, as it makes interacting with additional data packs seamless (virtual filesystem).
>

This ZIP archive support can be combined with runtime image, 3D scene and audio
loading to provide a seamless modding experience without requiring users to go
through the Godot editor to generate PCK/ZIP files.

Example that lists files in a ZIP archive in an [ItemList](https://docs.godotengine.org/en/stable/classes/class_itemlist.html#class-itemlist) node,
then writes contents read from it to a new ZIP archive (essentially duplicating the archive):

```
# Load an existing ZIP archive.
var zip_reader = ZIPReader.new()
zip_reader.open(path)
var files = zip_reader.get_files()
# The list of files isn't sorted by default. Sort it for more consistent processing.
files.sort()
for file in files:
    $ItemList.add_item(file, null)
    # Make folders disabled in the list.
    $ItemList.set_item_disabled(-1, file.ends_with("/"))

# Save a new ZIP archive.
var zip_packer = ZIPPacker.new()
var error = zip_packer.open(path)
if error != OK:
    push_error("Couldn't open path for saving ZIP archive (error code: %s)." % error_string(error))
    return

# Reuse the above ZIPReader instance to read files from an existing ZIP archive.
for file in zip_reader.get_files():
    zip_packer.start_file(file)
    zip_packer.write_file(zip_reader.read_file(file))
    zip_packer.close_file()

zip_packer.close()
```