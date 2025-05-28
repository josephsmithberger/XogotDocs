<!-- Remove this line to publish to docs.xogot.com -->
# Custom GUI controls

## So many controls...

Yet there are never enough. Creating your own custom controls that act
just the way you want them to is an obsession of almost every GUI
programmer. Godot provides plenty of them, but they may not work exactly
the way you want. Before contacting the developers with a pull-request
to support diagonal scrollbars, at least it will be good to know how to
create these controls easily from script.

## Drawing

For drawing, it is recommended to check the <doc:custom_drawing_in_2d> tutorial.
The same applies. Some functions are worth mentioning due to their
usefulness when drawing, so they will be detailed next:

### Checking control size

Unlike 2D nodes, "size" is important with controls, as it helps to
organize them in proper layouts. For this, the
[Control.size](https://docs.godotengine.org/en/stable/classes/class_control_property_size.html#class-control_property_size)
property is provided. Checking it during _draw() is vital to ensure
everything is kept in-bounds.

### Checking focus

Some controls (such as buttons or text editors) might provide input
focus for keyboard or joypad input. Examples of this are entering text
or pressing a button. This is controlled with the
[Control.focus_mode](https://docs.godotengine.org/en/stable/classes/class_control_property_focus_mode.html#class-control_property_focus_mode)
property. When drawing, and if the control supports input focus, it is
always desired to show some sort of indicator (highlight, box, etc.) to
indicate that this is the currently focused control. To check for this
status, the [Control.has_focus()](https://docs.godotengine.org/en/stable/classes/class_control_method_has_focus.html#class-control_method_has_focus) method
exists. Example

## Sizing

As mentioned before, size is important to controls. This allows
them to lay out properly, when set into grids, containers, or anchored.
Controls, most of the time, provide a minimum size to help properly
lay them out. For example, if controls are placed vertically on top of
each other using a [VBoxContainer](https://docs.godotengine.org/en/stable/classes/class_vboxcontainer.html#class-vboxcontainer),
the minimum size will make sure your custom control is not squished by
the other controls in the container.

To provide this callback, just override
[Control._get_minimum_size()](https://docs.godotengine.org/en/stable/classes/class_control_private_method__get_minimum_size.html#class-control_private_method__get_minimum_size),
for example:

Alternatively, set it using a function:

## Input

Controls provide a few helpers to make managing input events much easier
than regular nodes.

### Input events

There are a few tutorials about input before this one, but it's worth
mentioning that controls have a special input method that only works
when:

- The mouse pointer is over the control.

- The button was pressed over this control (control always
captures input until button is released)

- Control provides keyboard/joypad focus via
[Control.focus_mode](https://docs.godotengine.org/en/stable/classes/class_control_property_focus_mode.html#class-control_property_focus_mode).

This function is
[Control._gui_input()](https://docs.godotengine.org/en/stable/classes/class_control_private_method__gui_input.html#class-control_private_method__gui_input).
To use it, override it in your control. No processing needs to be set.

For more information about events themselves, check the <doc:inputevent>
tutorial.

### Notifications

Controls also have many useful notifications for which no dedicated callback
exists, but which can be checked with the _notification callback: