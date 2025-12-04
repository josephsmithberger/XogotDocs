<!-- Remove this line to publish to docs.xogot.com -->
# Using Viewports

## Introduction

Think of a [Viewport](https://docs.godotengine.org/en/stable/classes/class_viewport.html#class-viewport) as a screen onto which the game is projected. In order
to see the game, we need to have a surface on which to draw it. That surface is
the Root Viewport.

@Image(source: "subviewportnode.png")

are multiple surfaces to draw on. When we are drawing to a SubViewport, we call it a render target. We can access the contents
of a render target by accessing its corresponding [texture](https://docs.godotengine.org/en/stable/classes/class_viewport_method_get_texture.html#class-viewport_method_get_texture).
By using a SubViewport as render target, we can either render multiple scenes simultaneously or we can render to
a [ViewportTexture](https://docs.godotengine.org/en/stable/classes/class_viewporttexture.html#class-viewporttexture) which is applied to an object in the scene, for example a dynamic
skybox.

[SubViewports](https://docs.godotengine.org/en/stable/classes/class_subviewport.html#class-subviewport) have a variety of use cases, including:

- Rendering 3D objects within a 2D game

- Rendering 2D elements in a 3D game

- Rendering dynamic textures

- Generating procedural textures at runtime

- Rendering multiple cameras in the same scene

What all these use cases have in common is that you are given the ability to
draw objects to a texture as if it were another screen and can then choose
what to do with the resulting texture.

Another kind of Viewports in Godot are [Windows](https://docs.godotengine.org/en/stable/classes/class_window.html#class-window). They allow their content to be projected onto a window. While the Root Viewport is a Window, they are less
flexible. If you want to use the texture of a Viewport, you'll be working with [SubViewports](https://docs.godotengine.org/en/stable/classes/class_subviewport.html#class-subviewport) most of the time.

## Input

[Viewports](https://docs.godotengine.org/en/stable/classes/class_viewport.html#class-viewport) are also responsible for delivering properly adjusted and
scaled input events to their children nodes. By default [SubViewports](https://docs.godotengine.org/en/stable/classes/class_subviewport.html#class-subviewport) don't
automatically receive input, unless they receive it from their direct
[SubViewportContainer](https://docs.godotengine.org/en/stable/classes/class_subviewportcontainer.html#class-subviewportcontainer) parent node. In this case, input can be
disabled with the [Disable Input](https://docs.godotengine.org/en/stable/classes/class_viewport_property_gui_disable_input.html#class-viewport_property_gui_disable_input) property.

@Image(source: "input.png")

For more information on how Godot handles input, please read the <doc:inputevent>.

## Listener

Godot supports 3D sound (in both 2D and 3D nodes). More on this can be
found in the <doc:audio_streams>. For this type of sound to be
audible, the [Viewport](https://docs.godotengine.org/en/stable/classes/class_viewport.html#class-viewport) needs to be enabled as a listener (for 2D or 3D).
If you are using a [SubViewport](https://docs.godotengine.org/en/stable/classes/class_subviewport.html#class-subviewport) to display your [World3D](https://docs.godotengine.org/en/stable/classes/class_world3d.html#class-world3d) or
[World2D](https://docs.godotengine.org/en/stable/classes/class_world2d.html#class-world2d), don't forget to enable this!

## Cameras (2D & 3D)

When using a [Camera3D](https://docs.godotengine.org/en/stable/classes/class_camera3d.html#class-camera3d) or
[Camera2D](https://docs.godotengine.org/en/stable/classes/class_camera2d.html#class-camera2d), it will always display on the
closest parent [Viewport](https://docs.godotengine.org/en/stable/classes/class_viewport.html#class-viewport) (going towards the root). For example, in the
following hierarchy:

@Image(source: "cameras.png")

`CameraA` will display on the Root [Viewport](https://docs.godotengine.org/en/stable/classes/class_viewport.html#class-viewport) and it will draw `MeshA`. `CameraB`
will be captured by the [SubViewport](https://docs.godotengine.org/en/stable/classes/class_subviewport.html#class-subviewport) along with `MeshB`. Even though `MeshB` is in the scene
hierarchy, it will still not be drawn to the Root Viewport. Similarly, `MeshA` will not
be visible from the SubViewport because SubViewports only
capture nodes below them in the hierarchy.

There can only be one active camera per [Viewport](https://docs.godotengine.org/en/stable/classes/class_viewport.html#class-viewport), so if there is more
than one, make sure that the desired one has the [current](https://docs.godotengine.org/en/stable/classes/class_camera3d_property_current.html#class-camera3d_property_current) property set,
or make it the current camera by calling:

```
camera.make_current()
```

By default, cameras will render all objects in their world. In 3D, cameras can use their
[cull_mask](https://docs.godotengine.org/en/stable/classes/class_camera3d_property_cull_mask.html#class-camera3d_property_cull_mask) property combined with the
[VisualInstance3D's](https://docs.godotengine.org/en/stable/classes/class_visualinstance3d.html#class-visualinstance3d) [layer](https://docs.godotengine.org/en/stable/classes/class_visualinstance3d_property_layers.html#class-visualinstance3d_property_layers)
property to restrict which objects are rendered.

## Scale & stretching

[SubViewports](https://docs.godotengine.org/en/stable/classes/class_subviewport.html#class-subviewport) have a [size](https://docs.godotengine.org/en/stable/classes/class_subviewport_property_size.html#class-subviewport_property_size) property, which represents the size of the SubViewport
in pixels. For SubViewports which are children of [SubViewportContainers](https://docs.godotengine.org/en/stable/classes/class_subviewportcontainer.html#class-subviewportcontainer),
these values are overridden, but for all others, this sets their resolution.

It is also possible to scale the 2D content and make the [SubViewport](https://docs.godotengine.org/en/stable/classes/class_subviewport.html#class-subviewport) resolution
different from the one specified in size, by calling:

```
sub_viewport.set_size_2d_override(Vector2i(width, height)) # Custom size for 2D.
sub_viewport.set_size_2d_override_stretch(true) # Enable stretch for custom size.
```

For information on scaling and stretching with the Root Viewport visit the <doc:multiple_resolutions>

## Worlds

For 3D, a [Viewport](https://docs.godotengine.org/en/stable/classes/class_viewport.html#class-viewport) will contain a [World3D](https://docs.godotengine.org/en/stable/classes/class_world3d.html#class-world3d). This
is basically the universe that links physics and rendering together.
Node3D-based nodes will register using the World3D of the closest Viewport.
By default, newly created Viewports do not contain a World3D but
use the same as their parent Viewport. The Root Viewport always contains a
World3D, which is the one objects are rendered to by default.

A [World3D](https://docs.godotengine.org/en/stable/classes/class_world3d.html#class-world3d) can
be set in a [Viewport](https://docs.godotengine.org/en/stable/classes/class_viewport.html#class-viewport) using the [World 3D](https://docs.godotengine.org/en/stable/classes/class_viewport_property_world_3d.html#class-viewport_property_world_3d) property, that will separate
all children nodes of this [Viewport](https://docs.godotengine.org/en/stable/classes/class_viewport.html#class-viewport) and will prevent them from interacting with the parent
Viewport's World3D. This is especially useful in scenarios where, for
example, you might want to show a separate character in 3D imposed over
the game (like in StarCraft).

As a helper for situations where you want to create [Viewports](https://docs.godotengine.org/en/stable/classes/class_viewport.html#class-viewport) that
display single objects and don't want to create a [World3D](https://docs.godotengine.org/en/stable/classes/class_world3d.html#class-world3d), Viewport has
the option to use its [Own World3D](https://docs.godotengine.org/en/stable/classes/class_viewport_property_own_world_3d.html#class-viewport_property_own_world_3d). This is useful when you want to
instance 3D characters or objects in [World2D](https://docs.godotengine.org/en/stable/classes/class_world2d.html#class-world2d).

For 2D, each [Viewport](https://docs.godotengine.org/en/stable/classes/class_viewport.html#class-viewport) always contains its own [World2D](https://docs.godotengine.org/en/stable/classes/class_world2d.html#class-world2d).
This suffices in most cases, but in case sharing them may be desired, it
is possible to do so by setting [world_2d](https://docs.godotengine.org/en/stable/classes/class_viewport_property_world_2d.html#class-viewport_property_world_2d) on the Viewport through code.

For an example of how this works, see the demo projects 3D in 2D and 2D in 3D respectively.

## Capture

It is possible to query a capture of the [Viewport](https://docs.godotengine.org/en/stable/classes/class_viewport.html#class-viewport) contents. For the Root
Viewport, this is effectively a screen capture. This is done with the
following code:

```
# Retrieve the captured Image using get_image().
var img = get_viewport().get_texture().get_image()
# Convert Image to ImageTexture.
var tex = ImageTexture.create_from_image(img)
# Set sprite texture.
sprite.texture = tex
```

But if you use this in `_ready()` or from the first frame of the [Viewport's](https://docs.godotengine.org/en/stable/classes/class_viewport.html#class-viewport) initialization,
you will get an empty texture because there is nothing to get as texture. You can deal with
it using (for example):

```
# Wait until the frame has finished before getting the texture.
await RenderingServer.frame_post_draw
# You can get the image after this.
```

## Viewport Container

If the [SubViewport](https://docs.godotengine.org/en/stable/classes/class_subviewport.html#class-subviewport) is a child of a [SubViewportContainer](https://docs.godotengine.org/en/stable/classes/class_subviewportcontainer.html#class-subviewportcontainer), it will become active and display anything it has inside. The layout looks like this:

@Image(source: "container.png")

The [SubViewport](https://docs.godotengine.org/en/stable/classes/class_subviewport.html#class-subviewport) will cover the area of its parent [SubViewportContainer](https://docs.godotengine.org/en/stable/classes/class_subviewportcontainer.html#class-subviewportcontainer) completely
if [Stretch](https://docs.godotengine.org/en/stable/classes/class_subviewportcontainer_property_stretch.html#class-subviewportcontainer_property_stretch) is set to `true` in the SubViewportContainer.

> Note:
>
> The size of the [SubViewportContainer](https://docs.godotengine.org/en/stable/classes/class_subviewportcontainer.html#class-subviewportcontainer) cannot be smaller than the size of the [SubViewport](https://docs.godotengine.org/en/stable/classes/class_subviewport.html#class-subviewport).
>

## Rendering

Due to the fact that the [Viewport](https://docs.godotengine.org/en/stable/classes/class_viewport.html#class-viewport) is an entryway into another rendering surface, it exposes a few
rendering properties that can be different from the project settings. You can
choose to use a different level of [MSAA](https://docs.godotengine.org/en/stable/classes/class_viewport_property_msaa_2d.html#class-viewport_property_msaa_2d) for each Viewport. The default behavior is `Disabled`.

If you know that the [Viewport](https://docs.godotengine.org/en/stable/classes/class_viewport.html#class-viewport) is only going to be used for 2D, you can [Disable 3D](https://docs.godotengine.org/en/stable/classes/class_viewport_property_disable_3d.html#class-viewport_property_disable_3d). Godot will then
restrict how the Viewport is drawn.
Disabling 3D is slightly faster and uses less memory compared to enabled 3D. It's a good idea to disable 3D if your viewport doesn't render anything in 3D.

> Note:
>
> If you need to render 3D shadows in the viewport, make sure to set the viewport's [positional_shadow_atlas_size](https://docs.godotengine.org/en/stable/classes/class_viewport_property_positional_shadow_atlas_size.html#class-viewport_property_positional_shadow_atlas_size) property to a value higher than `0`.
> Otherwise, shadows won't be rendered. By default, the equivalent project setting is set to `4096` on desktop platforms and `2048` on mobile platforms.
>

Godot also provides a way of customizing how everything is drawn inside [Viewports](https://docs.godotengine.org/en/stable/classes/class_viewport.html#class-viewport) using [Debug Draw](https://docs.godotengine.org/en/stable/classes/class_viewport_property_debug_draw.html#class-viewport_property_debug_draw).
Debug Draw allows you to specify a mode which determines how the Viewport will display things drawn
inside it. Debug Draw is `Disabled` by default. Some other options are `Unshaded`, `Overdraw`, and `Wireframe`. For a full list, refer to the [Viewport Documentation](https://docs.godotengine.org/en/stable/classes/class_viewport_property_debug_draw.html#class-viewport_property_debug_draw).

- **Debug Draw = Disabled** (default): The scene is drawn normally.

@Image(source: "default_scene.png")

- **Debug Draw = Unshaded**: Unshaded draws the scene without using lighting information so all the objects appear flatly colored in their albedo color.

@Image(source: "unshaded.png")

- **Debug Draw = Overdraw**: Overdraw draws the meshes semi-transparent with an additive blend so you can see how the meshes overlap.

@Image(source: "overdraw.png")

- **Debug Draw = Wireframe**: Wireframe draws the scene using only the edges of triangles in the meshes.

@Image(source: "wireframe.png")

> Note:
>
> Debug Draw modes are currently **not** supported when using the
> Compatibility rendering method. They will appear as regular draw modes.
>

## Render target

When rendering to a [SubViewport](https://docs.godotengine.org/en/stable/classes/class_subviewport.html#class-subviewport), whatever is inside will not be
visible in the scene editor. To display the contents, you have to draw the SubViewport's [ViewportTexture](https://docs.godotengine.org/en/stable/classes/class_viewporttexture.html#class-viewporttexture) somewhere.
This can be requested via code using (for example):

```
# This gives us the ViewportTexture.
var tex = viewport.get_texture()
sprite.texture = tex
```

Or it can be assigned in the editor by selecting "New ViewportTexture"

@Image(source: "texturemenu.png")

and then selecting the [Viewport](https://docs.godotengine.org/en/stable/classes/class_viewport.html#class-viewport) you want to use.

@Image(source: "texturepath.png")

Every frame, the [Viewport's](https://docs.godotengine.org/en/stable/classes/class_viewport.html#class-viewport) texture is cleared away with the default clear color (or a transparent
color if [Transparent BG](https://docs.godotengine.org/en/stable/classes/class_viewport_property_transparent_bg.html#class-viewport_property_transparent_bg) is set to `true`). This can be changed by setting [Clear Mode](https://docs.godotengine.org/en/stable/classes/class_subviewport_property_render_target_clear_mode.html#class-subviewport_property_render_target_clear_mode) to `Never` or `Next Frame`.
As the name implies, Never means the texture will never be cleared, while next frame will
clear the texture on the next frame and then set itself to Never.

By default, re-rendering of the [SubViewport](https://docs.godotengine.org/en/stable/classes/class_subviewport.html#class-subviewport) happens when
its [ViewportTexture](https://docs.godotengine.org/en/stable/classes/class_viewporttexture.html#class-viewporttexture) has been drawn in a frame. If visible, it will be
rendered, otherwise, it will not. This behavior can be changed by setting [Update Mode](https://docs.godotengine.org/en/stable/classes/class_subviewport_property_render_target_update_mode.html#class-subviewport_property_render_target_update_mode) to `Never`, `Once`, `Always`, or `When Parent Visible`.
Never and Always will never or always re-render respectively. Once will re-render the next frame and change to Never afterwards. This can be used to manually update the Viewport.
This flexibility allows users to render an image once and then use the texture without incurring the cost of rendering every frame.

> Note:
>
> Make sure to check the Viewport demos. They are available in the
> viewport folder of the demos archive, or at
> https://github.com/godotengine/godot-demo-projects/tree/master/viewport.