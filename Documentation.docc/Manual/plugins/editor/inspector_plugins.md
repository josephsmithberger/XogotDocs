<!-- Remove this line to publish to docs.xogot.com -->
# Inspector plugins

The inspector dock allows you to create custom widgets to edit properties
through plugins. This can be beneficial when working with custom datatypes and
resources, although you can use the feature to change the inspector widgets for
built-in types. You can design custom controls for specific properties, entire
objects, and even separate controls associated with particular datatypes.

This guide explains how to use the [EditorInspectorPlugin](https://docs.godotengine.org/en/stable/classes/class_editorinspectorplugin.html#class-editorinspectorplugin) and
[EditorProperty](https://docs.godotengine.org/en/stable/classes/class_editorproperty.html#class-editorproperty) classes to create a custom interface for integers,
replacing the default behavior with a button that generates random values
between 0 and 99.

@Image(source: "inspector_plugin_example.png") {The default behavior on the left and the end result on the right.}

## Setting up your plugin

Create a new empty plugin to get started.

> Seealso: See <doc:making_plugins> guide to set up your new plugin.
>

Let's assume you've called your plugin folder my_inspector_plugin. If so,
you should end up with a new addons/my_inspector_plugin folder that contains
two files: plugin.cfg and plugin.gd.

As before, plugin.gd is a script extending [EditorPlugin](https://docs.godotengine.org/en/stable/classes/class_editorplugin.html#class-editorplugin) and you
need to introduce new code for its _enter_tree and _exit_tree methods.
To set up your inspector plugin, you must load its script, then create and add
the instance by calling add_inspector_plugin(). If the plugin is disabled,
you should remove the instance you have added by calling
remove_inspector_plugin().

> Note: Here, you are loading a script and not a packed scene. Therefore you
> should use new() instead of instantiate().
>

## Interacting with the inspector

To interact with the inspector dock, your my_inspector_plugin.gd script must
extend the [EditorInspectorPlugin](https://docs.godotengine.org/en/stable/classes/class_editorinspectorplugin.html#class-editorinspectorplugin) class. This class provides several
virtual methods that affect how the inspector handles properties.

To have any effect at all, the script must implement the _can_handle()
method. This function is called for each edited [Object](https://docs.godotengine.org/en/stable/classes/class_object.html#class-object) and must
return true if this plugin should handle the object or its properties.

> Note: This includes any [Resource](https://docs.godotengine.org/en/stable/classes/class_resource.html#class-resource) attached to the object.
>

You can implement four other methods to add controls to the inspector at
specific positions. The _parse_begin() and _parse_end() methods are called
only once at the beginning and the end of parsing for each object, respectively.
They can add controls at the top or bottom of the inspector layout by calling
add_custom_control().

As the editor parses the object, it calls the _parse_category() and
_parse_property() methods. There, in addition to add_custom_control(),
you can call both add_property_editor() and
add_property_editor_for_multiple_properties(). Use these last two methods to
specifically add [EditorProperty](https://docs.godotengine.org/en/stable/classes/class_editorproperty.html#class-editorproperty)-based controls.

## Adding an interface to edit properties

The [EditorProperty](https://docs.godotengine.org/en/stable/classes/class_editorproperty.html#class-editorproperty) class is a special type of [Control](https://docs.godotengine.org/en/stable/classes/class_control.html#class-control)
that can interact with the inspector dock's edited objects. It doesn't display
anything but can house any other control nodes, including complex scenes.

There are three essential parts to the script extending
[EditorProperty](https://docs.godotengine.org/en/stable/classes/class_editorproperty.html#class-editorproperty):

1. You must define the _init() method to set up the control nodes'
structure.

1. You should implement the _update_property() to handle changes to the data
from the outside.

1. A signal must be emitted at some point to inform the inspector that the
control has changed the property using emit_changed.

You can display your custom widget in two ways. Use just the default add_child()
method to display it to the right of the property name, and use add_child()
followed by set_bottom_editor() to position it below the name.

Using the example code above you should be able to make a custom widget that
replaces the default [SpinBox](https://docs.godotengine.org/en/stable/classes/class_spinbox.html#class-spinbox) control for integers with a
[Button](https://docs.godotengine.org/en/stable/classes/class_button.html#class-button) that generates random values.