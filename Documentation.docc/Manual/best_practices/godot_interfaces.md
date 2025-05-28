<!-- Remove this line to publish to docs.xogot.com -->
# Godot interfaces

Often one needs scripts that rely on other objects for features. There
are 2 parts to this process:

1. Acquiring a reference to the object that presumably has the features.

1. Accessing the data or logic from the object.

The rest of this tutorial outlines the various ways of doing all this.

## Acquiring object references

For all [Object](https://docs.godotengine.org/en/stable/classes/class_object.html#class-object)s, the most basic way of referencing them
is to get a reference to an existing object from another acquired instance.

The same principle applies for [RefCounted](https://docs.godotengine.org/en/stable/classes/class_refcounted.html#class-refcounted) objects.
While users often access [Node](https://docs.godotengine.org/en/stable/classes/class_node.html#class-node) and
[Resource](https://docs.godotengine.org/en/stable/classes/class_resource.html#class-resource) this way, alternative measures are available.

Instead of property or method access, one can get Resources by load
access.

Note the following:

1. There are many ways in which a language can load such resources.

1. When designing how objects will access data, don't forget
that one can pass resources around as references as well.

1. Keep in mind that loading a resource fetches the cached resource
instance maintained by the engine. To get a new object, one must
[duplicate](https://docs.godotengine.org/en/stable/classes/class_resource_method_duplicate.html#class-resource_method_duplicate) an existing reference
or instantiate one from scratch with new().

Nodes likewise have an alternative access point: the SceneTree.

## Accessing data or logic from an object

Godot's scripting API is duck-typed. This means that if a script executes an
operation, Godot doesn't validate that it supports the operation by **type**.
It instead checks that the object **implements** the individual method.

For example, the [CanvasItem](https://docs.godotengine.org/en/stable/classes/class_canvasitem.html#class-canvasitem) class has a visible
property. All properties exposed to the scripting API are in fact a setter and
getter pair bound to a name. If one tried to access
[CanvasItem.visible](https://docs.godotengine.org/en/stable/classes/class_canvasitem_property_visible.html#class-canvasitem_property_visible), then Godot would do the
following checks, in order:

- If the object has a script attached, it will attempt to set the property
through the script. This leaves open the opportunity for scripts to override
a property defined on a base object by overriding the setter method for the
property.

- If the script does not have the property, it performs a HashMap lookup in
the ClassDB for the "visible" property against the CanvasItem class and all
of its inherited types. If found, it will call the bound setter or getter.
For more information about HashMaps, see the
<doc:data_preferences> docs.

- If not found, it does an explicit check to see if the user wants to access
the "script" or "meta" properties.

- If not, it checks for a _set/_get implementation (depending on type
of access) in the CanvasItem and its inherited types. These methods can
execute logic that gives the impression that the Object has a property. This
is also the case with the _get_property_list method.

Note that this happens even for non-legal symbol names, such as names
starting with a digit or containing a slash.



- Note that this happens even for non-legal symbol names, such as names
starting with a digit or containing a slash.

- Note that this happens even for non-legal symbol names, such as names
starting with a digit or containing a slash.

As a result, this duck-typed system can locate a property either in the script,
the object's class, or any class that object inherits, but only for things
which extend Object.

Godot provides a variety of options for performing runtime checks on these
accesses:

- A duck-typed property access. These will be property checks (as described above).
If the operation isn't supported by the object, execution will halt.

- A method check. In the case of
[CanvasItem.visible](https://docs.godotengine.org/en/stable/classes/class_canvasitem_property_visible.html#class-canvasitem_property_visible), one can
access the methods, set_visible and is_visible like any other method.

- Outsource the access to a [Callable](https://docs.godotengine.org/en/stable/classes/class_callable.html#class-callable). These may be useful
in cases where one needs the max level of freedom from dependencies. In
this case, one relies on an external context to setup the method.

These strategies contribute to Godot's flexible design. Between them, users
have a breadth of tools to meet their specific needs.