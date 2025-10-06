# Customizing the mouse cursor

You might want to change the appearance of the mouse cursor in your game in
order to suit the overall design. There are two ways to customize the mouse
cursor:

1. Using project settings. This is simpler, but more limited.

1. Using a script. This is more customizable, but involves scripting.

> Note:
>
> You could display a "software" mouse cursor by hiding the mouse cursor and
> moving a Sprite2D to the cursor position in a _process() method, but
> this will add at least one frame of latency compared to a "hardware" mouse
> cursor. Therefore, it's recommended to use the approach described here
> whenever possible.
>
> If you have to use the "software" approach, consider adding an extrapolation step
> to better display the actual mouse input.
>

## Using project settings

Open the **Project Settings** and go to **Display > Mouse Cursor**. You will see the settings
[Custom Image](https://docs.godotengine.org/en/stable/classes/class_projectsettings_property_display/mouse_cursor/custom_image.html#class-projectsettings_property_display/mouse_cursor/custom_image),
[Custom Image Hotspot](https://docs.godotengine.org/en/stable/classes/class_projectsettings_property_display/mouse_cursor/custom_image_hotspot.html#class-projectsettings_property_display/mouse_cursor/custom_image_hotspot),
and [Tooltip Position Offset](https://docs.godotengine.org/en/stable/classes/class_projectsettings_property_display/mouse_cursor/tooltip_position_offset.html#class-projectsettings_property_display/mouse_cursor/tooltip_position_offset).

@Image(source: "cursor_project_settings.png")

**Custom Image** is the desired image that you would like to set as the mouse cursor.
**Custom Hotspot** is the point in the image that you would like to use as the cursor's detection point.

> Warning:
>
> The custom image **must** be 256×256 pixels at most. To avoid rendering
> issues, sizes of 128×128 or smaller are recommended.
>
> On the web platform, the maximum allowed cursor image size is 128×128.
>

## Using a script

Create a Node and attach the following script.

> Seealso:
>
> Check [Input.set_custom_mouse_cursor()](https://docs.godotengine.org/en/stable/classes/class_input_method_set_custom_mouse_cursor.html#class-input_method_set_custom_mouse_cursor)'s
> documentation for more information on usage and platform-specific caveats.
>

## Cursor list

There are multiple mouse cursors you can define, documented in the
:ref:`Input.CursorShape <enum_Input_CursorShape>` enum. Which ones you want to use
depends on your use case.
