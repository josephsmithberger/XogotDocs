<!-- Remove this line to publish to docs.xogot.com -->
# C# API differences to GDScript

This is an (incomplete) list of API differences between C# and GDScript.

## General differences

As explained in <doc:index#General-Differences>, `PascalCase` is used
to access Godot APIs in C# instead of the `snake_case` used by GDScript and
C++. Where possible, fields and getters/setters have been converted to
properties. In general, the C# Godot API strives to be as idiomatic as is
reasonably possible. See the <doc:c_sharp_style_guide>, which we encourage
you to also use for your own C# code.

In GDScript, the setters/getters of a property can be called directly, although
this is not encouraged. In C#, only the property is defined. For example, to
translate the GDScript code `x.set_name("Friend")` to C#, write
`x.Name = "Friend";`.

A C# IDE will provide intellisense, which is extremely useful when figuring out
renamed C# APIs. The built-in Godot script editor has no support for C#
intellisense, and it also doesn't provide many other C# development tools that
are considered essential. See <doc:index#Setup-External-Editor>.

## Global scope

Global functions and some constants had to be moved to classes, since C#
does not allow declaring them in namespaces.
Most global constants were moved to their own enums.

### Constants

In C#, only primitive types can be constant. For example, the `TAU` constant
is replaced by the `Mathf.Tau` constant, but the `Vector2.RIGHT` constant
is replaced by the `Vector2.Right` read-only property. This behaves similarly
to a constant, but can't be used in some contexts like `switch` statements.

Global enum constants were moved to their own enums.
For example, `ERR_*` constants were moved to the `Error` enum.

Special cases:

GDScript | C#
-------- | ---
`TYPE_*` | `Variant.Type`enum
`OP_*` | `Variant.Operator`enum

### Math functions

Math global functions, like `abs`, `acos`, `asin`, `atan` and `atan2`, are
located under `Mathf` as `Abs`, `Acos`, `Asin`, `Atan` and `Atan2`.
The `PI` constant can be found as `Mathf.Pi`.

C# also provides static System.Math and System.MathF classes that may
contain other useful mathematical operations.

### Random functions

Random global functions, like `rand_range` and `rand_seed`, are located under `GD`.
Example: `GD.RandRange` and `GD.RandSeed`.

Consider using System.Random or, if you need cryptographically strong randomness,
System.Security.Cryptography.RandomNumberGenerator.

### Other functions

Many other global functions like `print` and `var_to_str` are located under `GD`.
Example: `GD.Print` and `GD.VarToStr`.

Exceptions:

GDScript | C#
-------- | ---
`weakref(obj)` | `GodotObject.WeakRef(obj)`
`instance_from_id(id)` | `GodotObject.InstanceFromId(id)`
`is_instance_id_valid(id)` | `GodotObject.IsInstanceIdValid(id)`
`is_instance_valid(obj)` | `GodotObject.IsInstanceValid(obj)`

### Tips

Sometimes it can be useful to use the `using static` directive. This directive allows
to access the members and nested types of a class without specifying the class name.

Example:

```
using static Godot.GD;

public class Test
{
    static Test()
    {
        Print("Hello"); // Instead of GD.Print("Hello");
    }
}
```

### Full list of equivalences

List of Godot's global scope functions and their equivalent in C#:

GDScript | C#
-------- | ---
abs | Mathf.Abs
absf | Mathf.Abs
absi | Mathf.Abs
acos | Mathf.Acos
acosh | Mathf.Acosh
angle_difference | Mathf.AngleDifference
asin | Mathf.Asin
asinh | Mathf.Asinh
atan | Mathf.Atan
atan2 | Mathf.Atan2
atanh | Mathf.Atanh
bezier_derivative | Mathf.BezierDerivative
bezier_interpolate | Mathf.BezierInterpolate
bytes_to_var | GD.BytesToVar
bytes_to_var_with_objects | GD.BytesToVarWithObjects
ceil | Mathf.Ceil
ceilf | Mathf.Ceil
ceili | Mathf.CeilToInt
clamp | Mathf.Clamp
clampf | Mathf.Clamp
clampi | Mathf.Clamp
cos | Mathf.Cos
cosh | Mathf.Cosh
cubic_interpolate | Mathf.CubicInterpolate
cubic_interpolate_angle | Mathf.CubicInterpolateAngle
cubic_interpolate_angle_in_time | Mathf.CubicInterpolateInTime
cubic_interpolate_in_time | Mathf.CubicInterpolateAngleInTime
db_to_linear | Mathf.DbToLinear
deg_to_rad | Mathf.DegToRad
ease | Mathf.Ease
error_string | Error.ToString
exp | Mathf.Exp
floor | Mathf.Floor
floorf | Mathf.Floor
floori | Mathf.FloorToInt
fmod | operator %
fposmod | Mathf.PosMod
hash | GD.Hash
instance_from_id | GodotObject.InstanceFromId
inverse_lerp | Mathf.InverseLerp
is_equal_approx | Mathf.IsEqualApprox
is_finite | Mathf.IsFinite orfloat.IsFiniteordouble.IsFinite
is_inf | Mathf.IsInf orfloat.IsInfinityordouble.IsInfinity
is_instance_id_valid | GodotObject.IsInstanceIdValid
is_instance_valid | GodotObject.IsInstanceValid
is_nan | Mathf.IsNaN orfloat.IsNaNordouble.IsNaN
is_same | operator == orobject.ReferenceEquals
is_zero_approx | Mathf.IsZeroApprox
lerp | Mathf.Lerp
lerp_angle | Mathf.LerpAngle
lerpf | Mathf.Lerp
linear_to_db | Mathf.LinearToDb
log | Mathf.Log
max | Mathf.Max
maxf | Mathf.Max
maxi | Mathf.Max
min | Mathf.Min
minf | Mathf.Min
mini | Mathf.Min
move_toward | Mathf.MoveToward
nearest_po2 | Mathf.NearestPo2
pingpong | Mathf.PingPong
posmod | Mathf.PosMod
pow | Mathf.Pow
print | GD.Print
print_rich | GD.PrintRich
print_verbose | Use OS.IsStdoutVerbose and GD.Print
printerr | GD.PrintErr
printraw | GD.PrintRaw
prints | GD.PrintS
printt | GD.PrintT
push_error | GD.PushError
push_warning | GD.PushWarning
rad_to_deg | Mathf.RadToDeg
rand_from_seed | GD.RandFromSeed
randf | GD.Randf
randf_range | GD.RandRange
randfn | GD.Randfn
randi | GD.Randi
randi_range | GD.RandRange
randomize | GD.Randomize
remap | Mathf.Remap
rid_allocate_id | N/A
rid_from_int64 | N/A
rotate_toward | Mathf.RotateToward
round | Mathf.Round
roundf | Mathf.Round
roundi | Mathf.RoundToInt
seed | GD.Seed
sign | Mathf.Sign
signf | Mathf.Sign
signi | Mathf.Sign
sin | Mathf.Sin
sinh | Mathf.Sinh
smoothstep | Mathf.SmoothStep
snapped | Mathf.Snapped
snappedf | Mathf.Snapped
snappedi | Mathf.Snapped
sqrt | Mathf.Sqrt
step_decimals | Mathf.StepDecimals
str | Use$ string interpolation
str_to_var | GD.StrToVar
tan | Mathf.Tan
tanh | Mathf.Tanh
type_convert | Variant.As<T> or GD.Convert
type_string | Variant.Type.ToString
typeof | Variant.VariantType
var_to_bytes | GD.VarToBytes
var_to_bytes_with_objects | GD.VarToBytesWithObjects
var_to_str | GD.VarToStr
weakref | GodotObject.WeakRef
wrap | Mathf.Wrap
wrapf | Mathf.Wrap
wrapi | Mathf.Wrap

List of GDScript utility functions and their equivalent in C#:

GDScript | C#
-------- | ---
assert | System.Diagnostics.Debug.Assert
char | Use explicit conversion:`(char)65`
convert | GD.Convert
dict_to_inst | N/A
get_stack | System.Environment.StackTrace
inst_to_dict | N/A
len | N/A
load | GD.Load
preload | N/A
print_debug | N/A
print_stack | GD.Print(System.Environment.StackTrace)
range | GD.Range orSystem.Linq.Enumerable.Range
type_exists | ClassDB.ClassExists(type)

`preload`, as it works in GDScript, is not available in C#.
Use `GD.Load` or `ResourceLoader.Load` instead.

## `@export` annotation

Use the `[Export]` attribute instead of the GDScript `@export` annotation.
This attribute can also be provided with optional :ref:`PropertyHint<enum_@GlobalScope_PropertyHint>` and `hintString` parameters.
Default values can be set by assigning a value.

Example:

```
using Godot;

public partial class MyNode : Node
{
    [Export]
    private NodePath _nodePath;

    [Export]
    private string _name = "default";

    [Export(PropertyHint.Range, "0,100000,1000,or_greater")]
    private int _income;

    [Export(PropertyHint.File, "*.png,*.jpg")]
    private string _icon;
}
```

See also: <doc:c_sharp_exports>.

## `signal` keyword

Use the `[Signal]` attribute to declare a signal instead of the GDScript `signal` keyword.
This attribute should be used on a `delegate`, whose name signature will be used to define the signal.
The `delegate` must have the `EventHandler` suffix, an `event` will be generated in the class with the same name but without the suffix, use that event's name with `EmitSignal`.

```
[Signal]
delegate void MySignalEventHandler(string willSendAString);
```

See also: <doc:c_sharp_signals>.

## `@onready` annotation

GDScript has the ability to defer the initialization of a member variable until the ready function
is called with `@onready` (cf. <doc:index#Onready-Annotation>).
For example:

```
@onready var my_label = get_node("MyLabel")
```

However C# does not have this ability. To achieve the same effect you need to do this.

```
private Label _myLabel;

public override void _Ready()
{
    _myLabel = GetNode<Label>("MyLabel");
}
```

## Singletons

Singletons are available as static classes rather than using the singleton pattern.
This is to make code less verbose than it would be with an `Instance` property.

Example:

```
Input.IsActionPressed("ui_down")
```

However, in some very rare cases this is not enough. For example, you may want
to access a member from the base class `GodotObject`, like `Connect`.
For such use cases we provide a static property named `Singleton` that returns
the singleton instance. The type of this instance is `GodotObject`.

Example:

```
Input.Singleton.JoyConnectionChanged += Input_JoyConnectionChanged;
```

If you are developing main screen plugins, it is essential to note that
`EditorInterface` is not a static class in C#, unlike in GDScript.
Therefore, you must use the singleton pattern to obtain an instance of the
`EditorInterface`:

GDScript | C#
-------- | ---
`EditorInterface` | `EditorInterface.Singleton`

## String

Use `System.String` (`string`). Most of Godot's String methods have an
equivalent in `System.String` or are provided by the `StringExtensions`
class as extension methods.

Note that C# strings use UTF-16 encoding, while Godot Strings use UTF-32 encoding.

Example:

```
string text = "Get up!";
string[] bigrams = text.Bigrams(); // ["Ge", "et", "t ", " u", "up", "p!"]
```

Strings are immutable in .NET, so all methods that manipulate a string don't
modify the original string and return a newly created string with the
modifications applied. To avoid creating multiple string allocations consider
using a StringBuilder.

List of Godot's String methods and their equivalent in C#:

GDScript | C#
-------- | ---
begins_with | string.StartsWith
bigrams | StringExtensions.Bigrams
bin_to_int | StringExtensions.BinToInt
c_escape | StringExtensions.CEscape
c_unescape | StringExtensions.CUnescape
capitalize | StringExtensions.Capitalize
casecmp_to | StringExtensions.CasecmpTo or StringExtensions.CompareTo (Consider usingstring.Equalsorstring.Compare)
chr | N/A
contains | string.Contains
count | StringExtensions.Count (Consider usingRegEx)
countn | StringExtensions.CountN (Consider usingRegEx)
dedent | StringExtensions.Dedent
ends_with | string.EndsWith
erase | string.Remove(Consider usingStringBuilderto manipulate strings)
find | StringExtensions.Find (Consider usingstring.IndexOforstring.IndexOfAny)
findn | StringExtensions.FindN (Consider usingstring.IndexOforstring.IndexOfAny)
format | Use$ string interpolation
get_base_dir | StringExtensions.GetBaseDir
get_basename | StringExtensions.GetBaseName
get_extension | StringExtensions.GetExtension
get_file | StringExtensions.GetFile
get_slice | N/A
get_slice_count | N/A
get_slicec | N/A
hash | StringExtensions.Hash (Consider usingobject.GetHashCodeunless you need to guarantee the same behavior as in GDScript)
hex_decode | StringExtensions.HexDecode (Consider usingSystem.Convert.FromHexString)
hex_to_int | StringExtensions.HexToInt (Consider usingint.Parseorlong.ParsewithSystem.Globalization.NumberStyles.HexNumber)
humanize_size | N/A
indent | StringExtensions.Indent
insert | string.Insert(Consider usingStringBuilderto manipulate strings)
is_absolute_path | StringExtensions.IsAbsolutePath
is_empty | string.IsNullOrEmptyorstring.IsNullOrWhiteSpace
is_relative_path | StringExtensions.IsRelativePath
is_subsequence_of | StringExtensions.IsSubsequenceOf
is_subsequence_ofn | StringExtensions.IsSubsequenceOfN
is_valid_filename | StringExtensions.IsValidFileName
is_valid_float | StringExtensions.IsValidFloat (Consider usingfloat.TryParseordouble.TryParse)
is_valid_hex_number | StringExtensions.IsValidHexNumber
is_valid_html_color | StringExtensions.IsValidHtmlColor
is_valid_identifier | StringExtensions.IsValidIdentifier
is_valid_int | StringExtensions.IsValidInt (Consider usingint.TryParseorlong.TryParse)
is_valid_ip_address | StringExtensions.IsValidIPAddress
join | string.Join
json_escape | StringExtensions.JSONEscape
left | StringExtensions.Left (Consider usingstring.Substringorstring.AsSpan)
length | string.Length
lpad | string.PadLeft
lstrip | string.TrimStart
match | StringExtensions.Match (Consider usingRegEx)
matchn | StringExtensions.MatchN (Consider usingRegEx)
md5_buffer | StringExtensions.Md5Buffer (Consider usingSystem.Security.Cryptography.MD5.HashData)
md5_text | StringExtensions.Md5Text (Consider usingSystem.Security.Cryptography.MD5.HashDatawith StringExtensions.HexEncode)
naturalnocasecmp_to | N/A (Consider usingstring.Equalsorstring.Compare)
nocasecmp_to | StringExtensions.NocasecmpTo or StringExtensions.CompareTo (Consider usingstring.Equalsorstring.Compare)
num | float.ToStringordouble.ToString
num_int64 | int.ToStringorlong.ToString
num_scientific | float.ToStringordouble.ToString
num_uint64 | uint.ToStringorulong.ToString
pad_decimals | StringExtensions.PadDecimals
pad_zeros | StringExtensions.PadZeros
path_join | StringExtensions.PathJoin
repeat | Usestring constructoror aStringBuilder
replace | string.ReplaceorRegEx
replacen | StringExtensions.ReplaceN (Consider usingstring.ReplaceorRegEx)
reverse | N/A
rfind | StringExtensions.RFind (Consider usingstring.LastIndexOforstring.LastIndexOfAny)
rfindn | StringExtensions.RFindN (Consider usingstring.LastIndexOforstring.LastIndexOfAny)
right | StringExtensions.Right (Consider usingstring.Substringorstring.AsSpan)
rpad | string.PadRight
rsplit | N/A
rstrip | string.TrimEnd
sha1_buffer | StringExtensions.Sha1Buffer (Consider usingSystem.Security.Cryptography.SHA1.HashData)
sha1_text | StringExtensions.Sha1Text (Consider usingSystem.Security.Cryptography.SHA1.HashDatawith StringExtensions.HexEncode)
sha256_buffer | StringExtensions.Sha256Buffer (Consider usingSystem.Security.Cryptography.SHA256.HashData)
sha256_text | StringExtensions.Sha256Text (Consider usingSystem.Security.Cryptography.SHA256.HashDatawith StringExtensions.HexEncode)
similarity | StringExtensions.Similarity
simplify_path | StringExtensions.SimplifyPath
split | StringExtensions.Split (Consider usingstring.Split)
split_floats | StringExtensions.SplitFloat
strip_edges | StringExtensions.StripEdges (Consider usingstring.Trim,string.TrimStartorstring.TrimEnd)
strip_escapes | StringExtensions.StripEscapes
substr | StringExtensions.Substr (Consider usingstring.Substringorstring.AsSpan)
to_ascii_buffer | StringExtensions.ToAsciiBuffer (Consider usingSystem.Text.Encoding.ASCII.GetBytes)
to_camel_case | StringExtensions.ToCamelCase
to_float | StringExtensions.ToFloat (Consider usingfloat.TryParseordouble.TryParse)
to_int | StringExtensions.ToInt (Consider usingint.TryParseorlong.TryParse)
to_lower | string.ToLower
to_pascal_case | StringExtensions.ToPascalCase
to_snake_case | StringExtensions.ToSnakeCase
to_upper | string.ToUpper
to_utf16_buffer | StringExtensions.ToUtf16Buffer (Consider usingSystem.Text.Encoding.UTF16.GetBytes)
to_utf32_buffer | StringExtensions.ToUtf32Buffer (Consider usingSystem.Text.Encoding.UTF32.GetBytes)
to_utf8_buffer | StringExtensions.ToUtf8Buffer (Consider usingSystem.Text.Encoding.UTF8.GetBytes)
to_wchar_buffer | StringExtensions.ToUtf16Buffer in Windows and StringExtensions.ToUtf32Buffer in other platforms
trim_prefix | StringExtensions.TrimPrefix
trim_suffix | StringExtensions.TrimSuffix
unicode_at | string[int]indexer
uri_decode | StringExtensions.URIDecode (Consider usingSystem.Uri.UnescapeDataString)
uri_encode | StringExtensions.URIEncode (Consider usingSystem.Uri.EscapeDataString)
validate_node_name | StringExtensions.ValidateNodeName
xml_escape | StringExtensions.XMLEscape
xml_unescape | StringExtensions.XMLUnescape

List of Godot's PackedByteArray methods that create a String and their C# equivalent:

GDScript | C#
-------- | ---
get_string_from_ascii | StringExtensions.GetStringFromAscii (Consider usingSystem.Text.Encoding.ASCII.GetString)
get_string_from_utf16 | StringExtensions.GetStringFromUtf16 (Consider usingSystem.Text.Encoding.UTF16.GetString)
get_string_from_utf32 | StringExtensions.GetStringFromUtf32 (Consider usingSystem.Text.Encoding.UTF32.GetString)
get_string_from_utf8 | StringExtensions.GetStringFromUtf8 (Consider usingSystem.Text.Encoding.UTF8.GetString)
hex_encode | StringExtensions.HexEncode (Consider usingSystem.Convert.ToHexString)

> Note:
>
> .NET provides path utility methods under the
> System.IO.Path
> class. They can only be used with native OS paths, not Godot paths
> (paths that start with `res://` or `user://`).
> See <doc:data_paths>.
>

## NodePath

The following method was converted to a property with a different name:

GDScript | C#
-------- | ---
`is_empty()` | `IsEmpty`

## Signal

The following methods were converted to properties with their respective names changed:

GDScript | C#
-------- | ---
`get_name()` | `Name`
`get_object()` | `Owner`

The `Signal` type implements the awaitable pattern which means it can be used with
the `await` keyword. See <doc:c_sharp_differences#Await>.

Instead of using the `Signal` type, the recommended way to use Godot signals in C# is
to use the generated C# events. See <doc:c_sharp_signals>.

## Callable

The following methods were converted to properties with their respective names changed:

GDScript | C#
-------- | ---
`get_object()` | `Target`
`get_method()` | `Method`

Currently C# supports `Callable` if one of the following holds:

- `Callable` was created using the C# `Callable` type.

- `Callable` is a basic version of the engine's `Callable`. Custom `Callable`s
are unsupported. A `Callable` is custom when any of the following holds:

`Callable` has bound information (`Callable`s created with `bind`/`unbind` are unsupported).
`Callable` was created from other languages through the GDExtension API.



- `Callable` has bound information (`Callable`s created with `bind`/`unbind` are unsupported).

- `Callable` was created from other languages through the GDExtension API.

- `Callable` has bound information (`Callable`s created with `bind`/`unbind` are unsupported).

- `Callable` was created from other languages through the GDExtension API.

Some methods such as `bind` and `unbind` are not implemented, use lambdas instead:

```
string name = "John Doe";
Callable callable = Callable.From(() => SayHello(name));

void SayHello(string name)
{
    GD.Print($"Hello {name}");
}
```

The lambda captures the `name` variable so it can be bound to the `SayHello` method.

## RID

This type is named `Rid` in C# to follow the .NET naming convention.

The following methods were converted to properties with their respective names changed:

GDScript | C#
-------- | ---
`get_id()` | `Id`
`is_valid()` | `IsValid`

## Basis

Structs cannot have parameterless constructors in C#. Therefore, `new Basis()`
initializes all primitive members to their default value. Use `Basis.Identity`
for the equivalent of `Basis()` in GDScript and C++.

The following method was converted to a property with a different name:

GDScript | C#
-------- | ---
`get_scale()` | `Scale`

## Transform2D

Structs cannot have parameterless constructors in C#. Therefore, `new Transform2D()`
initializes all primitive members to their default value.
Please use `Transform2D.Identity` for the equivalent of `Transform2D()` in GDScript and C++.

The following methods were converted to properties with their respective names changed:

GDScript | C#
-------- | ---
`get_rotation()` | `Rotation`
`get_scale()` | `Scale`
`get_skew()` | `Skew`

## Transform3D

Structs cannot have parameterless constructors in C#. Therefore, `new Transform3D()`
initializes all primitive members to their default value.
Please use `Transform3D.Identity` for the equivalent of `Transform3D()` in GDScript and C++.

The following methods were converted to properties with their respective names changed:

GDScript | C#
-------- | ---
`get_rotation()` | `Rotation`
`get_scale()` | `Scale`

## Rect2

The following field was converted to a property with a slightly different name:

GDScript | C#
-------- | ---
`end` | `End`

The following method was converted to a property with a different name:

GDScript | C#
-------- | ---
`get_area()` | `Area`

## Rect2i

This type is named `Rect2I` in C# to follow the .NET naming convention.

The following field was converted to a property with a slightly different name:

GDScript | C#
-------- | ---
`end` | `End`

The following method was converted to a property with a different name:

GDScript | C#
-------- | ---
`get_area()` | `Area`

## AABB

This type is named `Aabb` in C# to follow the .NET naming convention.

The following method was converted to a property with a different name:

GDScript | C#
-------- | ---
`get_volume()` | `Volume`

## Quaternion

Structs cannot have parameterless constructors in C#. Therefore, `new Quaternion()`
initializes all primitive members to their default value.
Please use `Quaternion.Identity` for the equivalent of `Quaternion()` in GDScript and C++.

## Projection

Structs cannot have parameterless constructors in C#. Therefore, `new Projection()`
initializes all primitive members to their default value.
Please use `Projection.Identity` for the equivalent of `Projection()` in GDScript and C++.

## Color

Structs cannot have parameterless constructors in C#. Therefore, `new Color()`
initializes all primitive members to their default value (which represents the transparent black color).
Please use `Colors.Black` for the equivalent of `Color()` in GDScript and C++.

The global `Color8` method to construct a Color from bytes is available as a static method
in the Color type.

The Color constants are available in the `Colors` static class as readonly properties.

The following method was converted to a property with a different name:

GDScript | C#
-------- | ---
`get_luminance()` | `Luminance`

The following method was converted to a method with a different name:

GDScript | C#
-------- | ---
`html(String)` | `FromHtml(ReadOnlySpan<char>)`

The following methods are available as constructors:

GDScript | C#
-------- | ---
`hex(int)` | `Color(uint)`
`hex64(int)` | `Color(ulong)`

## Array

The equivalent of packed arrays are `System.Array`.

See also <doc:c_sharp_collections#Packedarray>.

Use `Godot.Collections.Array` for an untyped `Variant` array.
`Godot.Collections.Array<T>` is a type-safe wrapper around `Godot.Collections.Array`.

See also <doc:c_sharp_collections#Array>.

## Dictionary

Use `Godot.Collections.Dictionary` for an untyped `Variant` dictionary.
`Godot.Collections.Dictionary<TKey, TValue>` is a type-safe wrapper around `Godot.Collections.Dictionary`.

See also <doc:c_sharp_collections#Dictionary>.

## Variant

`Godot.Variant` is used to represent Godot's native [Variant](https://docs.godotengine.org/en/stable/classes/class_variant.html#class-variant) type.
Any :ref:`Variant-compatible type <c_sharp_variant_compatible_types>` can be converted from/to it.

See also: <doc:c_sharp_variant>.

## Communicating with other scripting languages

This is explained extensively in <doc:cross_language_scripting>.

## `await` keyword

Something similar to GDScript's `await` keyword can be achieved with C#'s
await keyword.

The `await` keyword in C# can be used with any awaitable expression. It's commonly
used with operands of the types Task, Task<TResult>, ValueTask, or ValueTask<TResult>.

An expression `t` is awaitable if one of the following holds:

- `t` is of compile-time type `dynamic`.

- `t` has an accessible instance or extension method called `GetAwaiter` with no
parameters and no type parameters, and a return type `A` for which all of the
following hold:

`A` implements the interface `System.Runtime.CompilerServices.INotifyCompletion`.
`A` has an accessible, readable instance property `IsCompleted` of type `bool`.
`A` has an accessible instance method `GetResult` with no parameters and no type
parameters.



- `A` implements the interface `System.Runtime.CompilerServices.INotifyCompletion`.

- `A` has an accessible, readable instance property `IsCompleted` of type `bool`.

- `A` has an accessible instance method `GetResult` with no parameters and no type
parameters.

- `A` implements the interface `System.Runtime.CompilerServices.INotifyCompletion`.

- `A` has an accessible, readable instance property `IsCompleted` of type `bool`.

- `A` has an accessible instance method `GetResult` with no parameters and no type
parameters.

An equivalent of awaiting a signal in GDScript can be achieved with the `await` keyword and
`GodotObject.ToSignal`.

Example:

```
public async Task SomeFunction()
{
    await ToSignal(timer, Timer.SignalName.Timeout);
    GD.Print("After timeout");
}
```