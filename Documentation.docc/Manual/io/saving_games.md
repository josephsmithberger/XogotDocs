# Saving games

## Introduction

Save games can be complicated. For example, it may be desirable
to store information from multiple objects across multiple levels.
Advanced save game systems should allow for additional information about
an arbitrary number of objects. This will allow the save function to
scale as the game grows more complex.

> Note:
>
> If you're looking to save user configuration, you can use the
> [ConfigFile](https://docs.godotengine.org/en/stable/classes/class_configfile.html#class-configfile) class for this purpose.
>

> Seealso:
>
> You can see how saving and loading works in action using the
> Saving and Loading (Serialization) demo project.
>

## Identify persistent objects

Firstly, we should identify what objects we want to keep between game
sessions and what information we want to keep from those objects. For
this tutorial, we will use groups to mark and handle objects to be saved,
but other methods are certainly possible.

We will start by adding objects we wish to save to the "Persist" group. We can
do this through either the GUI or script. Let's add the relevant nodes using the
GUI:

@Image(source: "groups.png")

Once this is done, when we need to save the game, we can get all objects
to save them and then tell them all to save with this script:

## Serializing

The next step is to serialize the data. This makes it much easier to
read from and store to disk. In this case, we're assuming each member of
group Persist is an instanced node and thus has a path. GDScript
has the helper class [JSON](https://docs.godotengine.org/en/stable/classes/class_json.html#class-json) to convert between dictionary and string.
Our node needs to contain a save function that returns this data.
The save function will look like this:

This gives us a dictionary with the style
{ "variable_name":value_of_variable }, which will be useful when
loading.

## Saving and reading data

As covered in the <doc:filesystem> tutorial, we'll need to open a file
so we can write to it or read from it. Now that we have a way to
call our groups and get their relevant data, let's use the class [JSON](https://docs.godotengine.org/en/stable/classes/class_json.html#class-json) to
convert it into an easily stored string and store them in a file. Doing
it this way ensures that each line is its own object, so we have an easy
way to pull the data out of the file as well.

Game saved! Now, to load, we'll read each
line. Use the [parse](https://docs.godotengine.org/en/stable/classes/class_json_method_parse.html#class-json_method_parse) method to read the
JSON string back to a dictionary, and then iterate over
the dict to read our values. But we'll need to first create the object
and we can use the filename and parent values to achieve that. Here is our
load function:

Now we can save and load an arbitrary number of objects laid out
almost anywhere across the scene tree! Each object can store different
data depending on what it needs to save.

## Some notes

We have glossed over setting up the game state for loading. It's ultimately up
to the project creator where much of this logic goes.
This is often complicated and will need to be heavily
customized based on the needs of the individual project.

Additionally, our implementation assumes no Persist objects are children of other
Persist objects. Otherwise, invalid paths would be created. To
accommodate nested Persist objects, consider saving objects in stages.
Load parent objects first so they are available for the [add_child()](https://docs.godotengine.org/en/stable/classes/class_node_method_add_child.html#class-node_method_add_child)
call when child objects are loaded. You will also need a way to link
children to parents as the [NodePath](https://docs.godotengine.org/en/stable/classes/class_nodepath.html#class-nodepath) will likely be invalid.

## JSON vs binary serialization

For simple game state, JSON may work and it generates human-readable files that are easy to debug.

But JSON has many limitations. If you need to store more complex game state or
a lot of it, <doc:binary_serialization_api>
may be a better approach.

### JSON limitations

Here are some important gotchas to know about when using JSON.

- **Filesize:**
JSON stores data in text format, which is much larger than binary formats.

- **Data types:**
JSON only offers a limited set of data types. If you have data types
that JSON doesn't have, you will need to translate your data to and
from types that JSON can handle. For example, some important types that JSON
can't parse are: Vector2, Vector3, Color, Rect2, and Quaternion.

- **Custom logic needed for encoding/decoding:**
If you have any custom classes that you want to store with JSON, you will
need to write your own logic for encoding and decoding those classes.

### Binary serialization

<doc:binary_serialization_api> is an alternative
approach for storing game state, and you can use it with the functions
get_var and store_var of [FileAccess](https://docs.godotengine.org/en/stable/classes/class_fileaccess.html#class-fileaccess).

- Binary serialization should produce smaller files than JSON.

- Binary serialization can handle most common data types.

- Binary serialization requires less custom logic for encoding and decoding
custom classes.

Note that not all properties are included. Only properties that are configured
with the [PROPERTY_USAGE_STORAGE](https://docs.godotengine.org/en/stable/classes/class_@globalscope_constant_property_usage_storage.html#class-@globalscope_constant_property_usage_storage)
flag set will be serialized. You can add a new usage flag to a property by overriding the
[_get_property_list](https://docs.godotengine.org/en/stable/classes/class_object_private_method__get_property_list.html#class-object_private_method__get_property_list)
method in your class. You can also check how property usage is configured by
calling Object._get_property_list.
See :ref:`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` for the
possible usage flags.
