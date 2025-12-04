<!-- Remove this line to publish to docs.xogot.com -->
# C# exported properties

In Godot, class members can be exported. This means their value gets saved along
with the resource (such as the [scene](https://docs.godotengine.org/en/stable/classes/class_packedscene.html#class-packedscene)) they're
attached to. They will also be available for editing in the property editor.
Exporting is done by using the `[Export]` attribute.

```
using Godot;

public partial class ExportExample : Node3D
{
    [Export]
    public int Number { get; set; } = 5;
}
```

In that example the value `5` will be saved, and after building the current project
it will be visible in the property editor.

One of the fundamental benefits of exporting member variables is to have
them visible and editable in the editor. This way, artists and game designers
can modify values that later influence how the program runs. For this, a
special export syntax is provided.

Exporting can only be done with :ref:`c_sharp_variant_compatible_types`.

> Note:
>
> Exporting properties can also be done in GDScript, for information on that
> see <doc:gdscript_exports>.
>

## Basic use

Exporting works with fields and properties. They can have any access modifier.

```
[Export]
private int _number;

[Export]
public int Number { get; set; }
```

Exported members can specify a default value; otherwise, the default value of the type is used instead.

An `int` like `Number` defaults to `0`. `Text` defaults to null because
`string` is a reference type.

```
[Export]
public int Number { get; set; }

[Export]
public string Text { get; set; }
```

Default values can be specified for fields and properties.

```
[Export]
private string _greeting = "Hello World";

[Export]
public string Greeting { get; set; } = "Hello World";
```

Properties with a backing field use the default value of the backing field.

```
private int _number = 2;

[Export]
public int NumberWithBackingField
{
    get => _number;
    set => _number = value;
}
```

> Note:
>
> A property's `get` is not actually executed to determine the default
> value. Instead, Godot analyzes the C# source code. This works fine for most
> cases, such as the examples on this page. However, some properties are too
> complex for the analyzer to understand.
>
> For example, the following property attempts to use math to display the
> default value as `5` in the property editor, but it doesn't work:
>
> .. code-block:: csharp
>
> [Export]
> public int NumberWithBackingField
> {
> get => _number + 3;
> set => _number = value - 3;
> }
>
> private int _number = 2;
>
> The analyzer doesn't understand this code and falls back to the default
> value for `int`, `0`. However, when running the scene or inspecting a
> node with an attached tool script, `_number` will be `2`, and
> `NumberWithBackingField` will return `5`. This difference may cause
> confusing behavior. To avoid this, don't use complex properties. Alternatively,
> if the default value can be explicitly specified, it can be overridden with the
> [_PropertyCanRevert()](https://docs.godotengine.org/en/stable/classes/class_object_private_method__property_can_revert.html#class-object_private_method__property_can_revert) and
> [_PropertyGetRevert()](https://docs.godotengine.org/en/stable/classes/class_object_private_method__property_get_revert.html#class-object_private_method__property_get_revert) methods.
>

Any type of `Resource` or `Node` can be exported. The property editor shows
a user-friendly assignment dialog for these types. This can be used instead of
`GD.Load` and `GetNode`. See <doc:c_sharp_exports#Nodes>.

```
[Export]
public PackedScene PackedScene { get; set; }

[Export]
public RigidBody2D RigidBody2D { get; set; }
```

## Grouping exports

It is possible to group your exported properties inside the Inspector with the `[ExportGroup]`
attribute. Every exported property after this attribute will be added to the group. Start a new
group or use `[ExportGroup("")]` to break out.

```
[ExportGroup("My Properties")]
[Export]
public int Number { get; set; } = 3;
```

The second argument of the attribute can be used to only group properties with the specified prefix.

Groups cannot be nested, use `[ExportSubgroup]` to create subgroups within a group.

```
[ExportSubgroup("Extra Properties")]
[Export]
public string Text { get; set; } = "";
[Export]
public bool Flag { get; set; } = false;
```

You can also change the name of your main category, or create additional categories in the property
list with the `[ExportCategory]` attribute.

```
[ExportCategory("Main Category")]
[Export]
public int Number { get; set; } = 3;
[Export]
public string Text { get; set; } = "";

[ExportCategory("Extra Category")]
[Export]
public bool Flag { get; set; } = false;
```

> Note:
>
> The list of properties is organized based on the class inheritance, and new categories break
> that expectation. Use them carefully, especially when creating projects for public use.
>

## Strings as paths

Property hints can be used to export strings as paths

String as a path to a file.

```
[Export(PropertyHint.File)]
public string GameFile { get; set; }
```

String as a path to a directory.

```
[Export(PropertyHint.Dir)]
public string GameDirectory { get; set; }
```

String as a path to a file, custom filter provided as hint.

```
[Export(PropertyHint.File, "*.txt,")]
public string GameFile { get; set; }
```

Using paths in the global filesystem is also possible,
but only in scripts in tool mode.

String as a path to a PNG file in the global filesystem.

```
[Export(PropertyHint.GlobalFile, "*.png")]
public string ToolImage { get; set; }
```

String as a path to a directory in the global filesystem.

```
[Export(PropertyHint.GlobalDir)]
public string ToolDir { get; set; }
```

The multiline annotation tells the editor to show a large input
field for editing over multiple lines.

```
[Export(PropertyHint.MultilineText)]
public string Text { get; set; }
```

## Limiting editor input ranges

Using the range property hint allows you to limit what can be
input as a value using the editor.

Allow integer values from 0 to 20.

```
[Export(PropertyHint.Range, "0,20,")]
public int Number { get; set; }
```

Allow integer values from -10 to 20.

```
[Export(PropertyHint.Range, "-10,20,")]
public int Number { get; set; }
```

Allow floats from -10 to 20 and snap the value to multiples of 0.2.

```
[Export(PropertyHint.Range, "-10,20,0.2")]
public float Number { get; set; }
```

If you add the hints "or_greater" and/or "or_less" you can go above
or below the limits when adjusting the value by typing it instead of using
the slider.

```
[Export(PropertyHint.Range, "0,100,1,or_greater,or_less")]
public int Number { get; set; }
```

## Floats with easing hint

Display a visual representation of the [ease](https://docs.godotengine.org/en/stable/classes/class_@globalscope_method_ease.html#class-@globalscope_method_ease)
function when editing.

```
[Export(PropertyHint.ExpEasing)]
public float TransitionSpeed { get; set; }
```

## Export with suffix hint

Display a unit hint suffix for exported variables. Works with numeric types,
such as floats or vectors:

```
[Export(PropertyHint.None, "suffix:m/s\u00b2")]
public float Gravity { get; set; } = 9.8f;
[Export(PropertyHint.None, "suffix:m/s")]
public Vector3 Velocity { get; set; }
```

In the above example, `\u00b2` is used to write the "squared" character
(`²`).

## Colors

Regular color given as red-green-blue-alpha value.

```
[Export]
public Color Color { get; set; }
```

Color given as red-green-blue value (alpha will always be 1).

```
[Export(PropertyHint.ColorNoAlpha)]
public Color Color { get; set; }
```

## Nodes

Nodes can also be directly exported without having to use NodePaths.

```
[Export]
public Node Node { get; set; }
```

A specific type of node can also be directly exported. The list of nodes shown
after pressing "Assign" in the inspector is filtered to the specified type, and
only a correct node can be assigned.

```
[Export]
public Sprite2D Sprite2D { get; set; }
```

Custom node classes can also be exported directly. The filtering behavior
depends on whether the custom class is a
<doc:c_sharp_global_classes>.

Exporting NodePaths like in Godot 3.x is still possible, in case you need it:

```
[Export]
public NodePath NodePath { get; set; }

public override void _Ready()
{
    var node = GetNode(NodePath);
}
```

## Resources

```
[Export]
public Resource Resource { get; set; }
```

In the Inspector, you can then drag and drop a resource file
from the FileSystem dock into the variable slot.

Opening the inspector dropdown may result in an
extremely long list of possible classes to create, however.
Therefore, if you specify a type derived from Resource such as:

```
[Export]
public AnimationNode AnimationNode { get; set; }
```

The drop-down menu will be limited to AnimationNode and all
its derived classes. Custom resource classes can also be used,
see <doc:c_sharp_global_classes>.

It must be noted that even if the script is not being run while in the
editor, the exported properties are still editable. This can be used
in conjunction with a <doc:index#Tool-Mode>.

## Exporting bit flags

Members whose type is an enum with the `[Flags]` attribute can be exported and
their values are limited to the members of the enum type.
The editor will create a widget in the Inspector, allowing to select none, one,
or multiple of the enum members. The value will be stored as an integer.

A flags enum uses powers of 2 for the values of the enum members. Members that
combine multiple flags using logical OR (`|`) are also possible.

```
[Flags]
public enum SpellElements
{
    Fire = 1 << 1,
    Water = 1 << 2,
    Earth = 1 << 3,
    Wind = 1 << 4,

    FireAndWater = Fire | Water,
}

[Export]
public SpellElements MySpellElements { get; set; }
```

Integers used as bit flags can store multiple `true`/`false` (boolean)
values in one property. By using the `Flags` property hint, any of the given
flags can be set from the editor.

```
[Export(PropertyHint.Flags, "Fire,Water,Earth,Wind")]
public int SpellElements { get; set; } = 0;
```

You must provide a string description for each flag. In this example, `Fire`
has value 1, `Water` has value 2, `Earth` has value 4 and `Wind`
corresponds to value 8. Usually, constants should be defined accordingly (e.g.
`private const int ElementWind = 8` and so on).

You can add explicit values using a colon:

```
[Export(PropertyHint.Flags, "Self:4,Allies:8,Foes:16")]
public int SpellTargets { get; set; } = 0;
```

Only power of 2 values are valid as bit flags options. The lowest allowed value
is 1, as 0 means that nothing is selected. You can also add options that are a
combination of other flags:

```
[Export(PropertyHint.Flags, "Self:4,Allies:8,Self and Allies:12,Foes:16")]
public int SpellTargets { get; set; } = 0;
```

Export annotations are also provided for the physics and render layers defined in the project settings.

```
[Export(PropertyHint.Layers2DPhysics)]
public uint Layers2DPhysics { get; set; }
[Export(PropertyHint.Layers2DRender)]
public uint Layers2DRender { get; set; }
[Export(PropertyHint.Layers3DPhysics)]
public uint Layers3DPhysics { get; set; }
[Export(PropertyHint.Layers3DRender)]
public uint Layers3DRender { get; set; }
```

Using bit flags requires some understanding of bitwise operations.
If in doubt, use boolean variables instead.

## Exporting enums

Members whose type is an enum can be exported and their values are limited to the members
of the enum type. The editor will create a widget in the Inspector, enumerating the
following as "Thing 1", "Thing 2", "Another Thing". The value will be stored as an integer.

```
public enum MyEnum
{
    Thing1,
    Thing2,
    AnotherThing = -1,
}

[Export]
public MyEnum MyEnumCurrent { get; set; }
```

Integer and string members can also be limited to a specific list of values using the
`[Export]` annotation with the `PropertyHint.Enum` hint.
The editor will create a widget in the Inspector, enumerating the following as Warrior,
Magician, Thief. The value will be stored as an integer, corresponding to the index
of the selected option (i.e. `0`, `1`, or `2`).

```
[Export(PropertyHint.Enum, "Warrior,Magician,Thief")]
public int CharacterClass { get; set; }
```

You can add explicit values using a colon:

```
[Export(PropertyHint.Enum, "Slow:30,Average:60,Very Fast:200")]
public int CharacterSpeed { get; set; }
```

If the type is `string`, the value will be stored as a string.

```
[Export(PropertyHint.Enum, "Rebecca,Mary,Leah")]
public string CharacterName { get; set; }
```

If you want to set an initial value, you must specify it explicitly:

```
[Export(PropertyHint.Enum, "Rebecca,Mary,Leah")]
public string CharacterName { get; set; } = "Rebecca";
```

## Exporting inspector buttons with `[ExportToolButton]`

If you want to create a clickable button in the inspector, you can use the
`[ExportToolButton]` attribute.  This exports a Callable property or field as
a clickable button. Since this runs in the editor, usage of the <doc:running_code_in_the_editor> attribute is required. When the button is
pressed, the callable is called:

```
[Tool]
public partial class MyNode : Node
{
    [ExportToolButton("Click me!")]
    public Callable ClickMeButton => Callable.From(ClickMe);

    public void ClickMe()
    {
        GD.Print("Hello world!");
    }
}
```

You can also set an icon for the button with a second argument. If specified, an
icon will be fetched via [GetThemeIcon()](https://docs.godotengine.org/en/stable/classes/class_control_method_get_theme_icon.html#class-control_method_get_theme_icon),
from the `"EditorIcons"` theme type.

```
[ExportToolButton("Click me!", Icon = "CharacterBody2D")]
public Callable ClickMeButton => Callable.From(ClickMe);
```

## Exporting collections

As explained in the <doc:c_sharp_variant> documentation, only
certain C# arrays and the collection types defined in the `Godot.Collections`
namespace are Variant-compatible, therefore, only those types can be exported.

### Exporting Godot arrays

```
[Export]
public Godot.Collections.Array Array { get; set; }
```

Using the generic `Godot.Collections.Array<T>` allows specifying the type of the
array elements, which will be used as a hint for the editor. The Inspector will
restrict the elements to the specified type.

```
[Export]
public Godot.Collections.Array<string> Array { get; set; }
```

The default value of Godot arrays is null. A different default can be specified:

```
[Export]
public Godot.Collections.Array<string> CharacterNames { get; set; } =
[
    "Rebecca",
    "Mary",
    "Leah",
];
```

Arrays with specified types which inherit from resource can be set by
drag-and-dropping multiple files from the FileSystem dock.

```
[Export]
public Godot.Collections.Array<Texture> Textures { get; set; }

[Export]
public Godot.Collections.Array<PackedScene> Scenes { get; set; }
```

### Exporting Godot dictionaries

```
[Export]
public Godot.Collections.Dictionary Dictionary { get; set; }
```

Using the generic `Godot.Collections.Dictionary<TKey, TValue>` allows specifying
the types of the key and value elements of the dictionary.

```
[Export]
public Godot.Collections.Dictionary<string, int> Dictionary { get; set; }
```

The default value of Godot dictionaries is null. A different default can be specified:

```
[Export]
public Godot.Collections.Dictionary<string, int> CharacterLives { get; set; } = new Godot.Collections.Dictionary<string, int>
{
    ["Rebecca"] = 10,
    ["Mary"] = 42,
    ["Leah"] = 0,
};
```

### Exporting C# arrays

C# arrays can exported as long as the element type is a :ref:`Variant-compatible type <c_sharp_variant_compatible_types>`.

```
[Export]
public Vector3[] Vectors { get; set; }

[Export]
public NodePath[] NodePaths { get; set; }
```

The default value of C# arrays is null. A different default can be specified:

```
[Export]
public Vector3[] Vectors { get; set; } =
[
    new Vector3(1, 2, 3),
    new Vector3(3, 2, 1),
];
```

## Setting exported variables from a tool script

When changing an exported variable's value from a script in
<doc:index#Tool-Mode>, the value in the inspector won't be updated
automatically. To update it, call
[NotifyPropertyListChanged()](https://docs.godotengine.org/en/stable/classes/class_object_method_notify_property_list_changed.html#class-object_method_notify_property_list_changed)
after setting the exported variable's value.

## Advanced exports

Not every type of export can be provided on the level of the language itself to
avoid unnecessary design complexity. The following describes some more or less
common exporting features which can be implemented with a low-level API.

Before reading further, you should get familiar with the way properties are
handled and how they can be customized with
[_Set()](https://docs.godotengine.org/en/stable/classes/class_object_private_method__set.html#class-object_private_method__set),
[_Get()](https://docs.godotengine.org/en/stable/classes/class_object_private_method__get.html#class-object_private_method__get), and
[_GetPropertyList()](https://docs.godotengine.org/en/stable/classes/class_object_private_method__get_property_list.html#class-object_private_method__get_property_list) methods as
described in <doc:accessing_data_or_logic_from_object>.

> Seealso: For binding properties using the above methods in C++, see
> <doc:binding_properties_using_set_get_property_list>.
>

> Warning: The script must operate in the `tool` mode so the above methods
> can work from within the editor.