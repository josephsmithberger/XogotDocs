<!-- Remove this line to publish to docs.xogot.com -->
# Cross-language scripting

Godot allows you to mix and match scripting languages to suit your needs.
This means a single project can define nodes in both C# and GDScript.
This page will go through the possible interactions between two nodes written
in different languages.

The following two scripts will be used as references throughout this page.

## Instantiating nodes

If you're not using nodes from the scene tree, you'll probably want to
instantiate nodes directly from the code.

### Instantiating C# nodes from GDScript

Using C# from GDScript doesn't need much work. Once loaded
(see <doc:index#Classes-As-Resources>), the script can be instantiated
with [new()](https://docs.godotengine.org/en/stable/classes/class_csharpscript_method_new.html#class-csharpscript_method_new).

```
var MyCSharpScript = load("res://Path/To/MyCSharpNode.cs")
var my_csharp_node = MyCSharpScript.new()
```

> Warning:
>
> When creating .cs scripts, you should always keep in mind that the class
> Godot will use is the one named like the .cs file itself. If that class
> does not exist in the file, you'll see the following error:
> Invalid call. Nonexistent function `new` in base.
>
> For example, MyCoolNode.cs should contain a class named MyCoolNode.
>
> The C# class needs to derive a Godot class, for example GodotObject.
> Otherwise, the same error will occur.
>
> You also need to check your .cs file is referenced in the project's
> .csproj file. Otherwise, the same error will occur.
>

### Instantiating GDScript nodes from C#

From the C# side, everything work the same way. Once loaded, the GDScript can
be instantiated with [GDScript.New()](https://docs.godotengine.org/en/stable/classes/class_gdscript_method_new.html#class-gdscript_method_new).

```
var myGDScript = GD.Load<GDScript>("res://path/to/my_gd_script.gd");
var myGDScriptNode = (GodotObject)myGDScript.New(); // This is a GodotObject.
```

Here we are using an [Object](https://docs.godotengine.org/en/stable/classes/class_object.html#class-object), but you can use type conversion like
explained in <doc:c_sharp_features#Type-Conversion-And-Casting>.

## Accessing fields

### Accessing C# fields from GDScript

Accessing C# fields from GDScript is straightforward, you shouldn't have
anything to worry about.

```
# Output: "my c# value".
print(my_csharp_node.MyProperty)
my_csharp_node.MyProperty = "MY C# VALUE"
# Output: "MY C# VALUE".
print(my_csharp_node.MyProperty)
```

### Accessing GDScript fields from C#

As C# is statically typed, accessing GDScript from C# is a bit more
convoluted. You will have to use [GodotObject.Get()](https://docs.godotengine.org/en/stable/classes/class_object_method_get.html#class-object_method_get)
and [GodotObject.Set()](https://docs.godotengine.org/en/stable/classes/class_object_method_set.html#class-object_method_set). The first argument is the name of the field you want to access.

```
// Output: "my gdscript value".
GD.Print(myGDScriptNode.Get("my_property"));
myGDScriptNode.Set("my_property", "MY GDSCRIPT VALUE");
// Output: "MY GDSCRIPT VALUE".
GD.Print(myGDScriptNode.Get("my_property"));
```

Keep in mind that when setting a field value you should only use types the
GDScript side knows about.
Essentially, you want to work with built-in types as described in
<doc:index#Builtin-Types> or classes extending [Object](https://docs.godotengine.org/en/stable/classes/class_object.html#class-object).

## Calling methods

### Calling C# methods from GDScript

Again, calling C# methods from GDScript should be straightforward. The
marshalling process will do its best to cast the arguments to match
function signatures.
If that's impossible, you'll see the following error: Invalid call. Nonexistent function `FunctionName`.

```
# Output: "my_gd_script_node" (or name of node where this code is placed).
my_csharp_node.PrintNodeName(self)
# This line will fail.
# my_csharp_node.PrintNodeName()

# Outputs "Hello there!" twice, once per line.
my_csharp_node.PrintNTimes("Hello there!", 2)

# Output: "a", "b", "c" (one per line).
my_csharp_node.PrintArray(["a", "b", "c"])
# Output: "1", "2", "3"  (one per line).
my_csharp_node.PrintArray([1, 2, 3])
```

### Calling GDScript methods from C#

To call GDScript methods from C# you'll need to use
[GodotObject.Call()](https://docs.godotengine.org/en/stable/classes/class_object_method_call.html#class-object_method_call). The first argument is the
name of the method you want to call. The following arguments will be passed
to said method.

```
// Output: "MyCSharpNode" (or name of node where this code is placed).
myGDScriptNode.Call("print_node_name", this);
// This line will fail silently and won't error out.
// myGDScriptNode.Call("print_node_name");

// Outputs "Hello there!" twice, once per line.
myGDScriptNode.Call("print_n_times", "Hello there!", 2);

string[] arr = ["a", "b", "c"];
// Output: "a", "b", "c" (one per line).
myGDScriptNode.Call("print_array", arr);
// Output: "1", "2", "3"  (one per line).
myGDScriptNode.Call("print_array", new int[] { 1, 2, 3 });
// Note how the type of each array entry does not matter
// as long as it can be handled by the marshaller.
```

## Connecting to signals

### Connecting to C# signals from GDScript

Connecting to a C# signal from GDScript is the same as connecting to a signal
defined in GDScript:

```
my_csharp_node.MySignal.connect(my_signal_handler)

my_csharp_node.MySignalWithParams.connect(my_signal_with_params_handler)
```

### Connecting to GDScript signals from C#

Connecting to a GDScript signal from C# only works with the Connect method
because no C# static types exist for signals defined by GDScript:

```
myGDScriptNode.Connect("my_signal", Callable.From(MySignalHandler));

myGDScriptNode.Connect("my_signal_with_params", Callable.From<string, int>(MySignalWithParamsHandler));
```

## Inheritance

A GDScript file may not inherit from a C# script. Likewise, a C# script may not
inherit from a GDScript file. Due to how complex this would be to implement,
this limitation is unlikely to be lifted in the future. See
this GitHub issue
for more information.