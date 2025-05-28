<!-- Remove this line to publish to docs.xogot.com -->
# Running code in the editor

## What is @tool?

@tool is a powerful line of code that, when added at the top of your script,
makes it execute in the editor. You can also decide which parts of the script
execute in the editor, which in game, and which in both.

You can use it for doing many things, but it is mostly useful in level design
for visually presenting things that are hard to predict ourselves. Here are some
use cases:

- If you have a cannon that shoots cannonballs affected by physics (gravity),
you can draw the cannonball's trajectory in the editor, making level design a
lot easier.

- If you have jumppads with varying jump heights, you can draw the maximum jump
height a player would reach if it jumped on one, also making level design
easier.

- If your player doesn't use a sprite, but draws itself using code, you can make
that drawing code execute in the editor to see your player.

!DANGER!

@tool scripts run inside the editor, and let you access the scene tree
of the currently edited scene. This is a powerful feature which also comes
with caveats, as the editor does not include protections for potential
misuse of @tool scripts.
Be **extremely** cautious when manipulating the scene tree, especially via
[Node.queue_free](https://docs.godotengine.org/en/stable/classes/class_node_method_queue_free.html#class-node_method_queue_free), as it can cause
crashes if you free a node while the editor runs logic involving it.

## How to use @tool

To turn a script into a tool, add the @tool annotation at the top of your code.

To check if you are currently in the editor, use: Engine.is_editor_hint().

For example, if you want to execute some code only in the editor, use:

On the other hand, if you want to execute code only in game, simply negate the
same statement:

Pieces of code that do not have either of the 2 conditions above will run both
in-editor and in-game.

Here is how a _process() function might look for you:

## Important information

Any other GDScript that your tool script uses must also be a tool. Any
GDScript without @tool used by the editor will act like an empty file!

Extending a @tool script does not automatically make the extending script
a @tool. Omitting @tool from the extending script will disable tool
behavior from the super class. Therefore the extending script should also
specify the @tool annotation.

Modifications in the editor are permanent. For example, in the next
section when we remove the script, the node will keep its rotation. Be careful
to avoid making unwanted modifications.

## Try @tool out

Add a Sprite2D node to your scene and set the texture to Godot icon. Attach
and open a script, and change it to this:

Save the script and return to the editor. You should now see your object rotate.
If you run the game, it will also rotate.

> Warning:
> You may need to restart the editor. This is a known bug found in all Godot 4 versions:
> GH-66381.
>

@Image(source: "rotating_in_editor.gif")

> Note:
>
> If you don't see the changes, reload the scene (close it and open it again).
>

Now let's choose which code runs when. Modify your _process() function to
look like this:

Save the script. Now the object will spin clockwise in the editor, but if you
run the game, it will spin counter-clockwise.

## Editing variables

Add and export a variable speed to the script. To update the speed and also reset the rotation
angle add a setter set(new_speed) which is executed with the input from the inspector. Modify
_process() to include the rotation speed.

> Note:
>
> Code from other nodes doesn't run in the editor. Your access to other nodes
> is limited. You can access the tree and nodes, and their default properties,
> but you can't access user variables. If you want to do so, other nodes have
> to run in the editor too. Autoload nodes cannot be accessed in the editor at
> all.
>

## Getting notified when resources change

Sometimes you want your tool to use a resource. However, when you change a
property of that resource in the editor, the set() method of your tool will
not be called.

To get around this problem you first have to make your resource a tool and make it
emit the changed signal whenever a property is set:

You then want to connect the signal when a new resource is set:

Lastly, remember to disconnect the signal as the old resource being used and changed somewhere else
would cause unneeded updates.

## Reporting node configuration warnings

Godot uses a node configuration warning system to warn users about incorrectly
configured nodes. When a node isn't configured correctly, a yellow warning sign
appears next to the node's name in the Scene dock. When you hover or click on
the icon, a warning message pops up. You can use this feature in your scripts to
help you and your team avoid mistakes when setting up scenes.

When using node configuration warnings, when any value that should affect or
remove the warning changes, you need to call
[update_configuration_warnings](https://docs.godotengine.org/en/stable/classes/class_node_method_update_configuration_warnings.html#class-node_method_update_configuration_warnings) .
By default, the warning only updates when closing and reopening the scene.

## Running one-off scripts using EditorScript

Sometimes, you need to run code just one time to automate a certain task that is
not available in the editor out of the box. Some examples might be:

- Use as a playground for GDScript or C# scripting without having to run a project.
print() output is displayed in the editor Output panel.

- Scale all light nodes in the currently edited scene, as you noticed your level
ends up looking too dark or too bright after placing lights where desired.

- Replace nodes that were copy-pasted with scene instances to make them easier
to modify later.

This is available in Godot by extending [EditorScript](https://docs.godotengine.org/en/stable/classes/class_editorscript.html#class-editorscript) in a script.
This provides a way to run individual scripts in the editor without having to
create an editor plugin.

To create an EditorScript, right-click a folder or empty space in the FileSystem
dock then choose **New > Script...**. In the script creation dialog, click the
tree icon to choose an object to extend from (or enter EditorScript directly
in the field on the left, though note this is case-sensitive):

@Image(source: "running_code_in_the_editor_creating_editor_script.png", alt: "Creating an editor script in the script editor creation dialog") {Creating an editor script in the script editor creation dialog}

This will automatically select a script template that is suited for
EditorScripts, with a _run() method already inserted:

```
@tool
extends EditorScript

# Called when the script is executed (using File -> Run in Script Editor).
func _run():
    pass
```

This _run() method is executed when you use **File > Run** or the keyboard
shortcut `Ctrl + Shift + X` while the EditorScript is the currently open
script in the script editor. This keyboard shortcut is only effective when
currently focused on the script editor.

Scripts that extend EditorScript must be @tool scripts to function.

> Note:
>
> EditorScripts can only be run from the Godot script editor. If you are using
> an external editor, open the script inside the Godot script editor to run it.
>

!DANGER!

EditorScripts have no undo/redo functionality, so **make sure to save your
scene before running one** if the script is designed to modify any data.

To access nodes in the currently edited scene, use the
[EditorScript.get_scene](https://docs.godotengine.org/en/stable/classes/class_editorscript_method_get_scene.html#class-editorscript_method_get_scene) method which
returns the root Node of the currently edited scene. Here's an example that
recursively gets all nodes in the currently edited scene and doubles the range
of all OmniLight3D nodes:

```
@tool
extends EditorScript

func _run():
    for node in get_all_children(get_scene()):
        if node is OmniLight3D:
            # Don't operate on instanced subscene children, as changes are lost
            # when reloading the scene.
            # See the "Instancing scenes" section below for a description of `owner`.
            var is_instanced_subscene_child = node != get_scene() and node.owner != get_scene()
            if not is_instanced_subscene_child:
                node.omni_range *= 2.0

# This function is recursive: it calls itself to get lower levels of child nodes as needed.
# `children_acc` is the accumulator parameter that allows this function to work.
# It should be left to its default value when you call this function directly.
func get_all_children(in_node, children_acc = []):
    children_acc.push_back(in_node)
    for child in in_node.get_children():
        children_acc = get_all_children(child, children_acc)

    return children_acc
```

> Tip:
>
> You can change the currently edited scene at the top of the editor even
> while the Script view is open. This will affect the return value of
> [EditorScript.get_scene](https://docs.godotengine.org/en/stable/classes/class_editorscript_method_get_scene.html#class-editorscript_method_get_scene), so make
> sure you've selected the scene you intend to iterate upon before running
> the script.
>

## Instancing scenes

You can instantiate packed scenes normally and add them to the scene currently
opened in the editor. By default, nodes or scenes added with
[Node.add_child(node)](https://docs.godotengine.org/en/stable/classes/class_node_method_add_child.html#class-node_method_add_child) are **not** visible
in the Scene tree dock and are **not** persisted to disk. If you wish the node
or scene to be visible in the scene tree dock and persisted to disk when saving
the scene, you need to set the child node's [owner](https://docs.godotengine.org/en/stable/classes/class_node_property_owner.html#class-node_property_owner)
property to the currently edited scene root.

If you are using @tool:

If you are using [EditorScript](https://docs.godotengine.org/en/stable/classes/class_editorscript.html#class-editorscript):

> Warning:
>
> Using @tool improperly can yield many errors. It is advised to first
> write the code how you want it, and only then add the @tool annotation to
> the top. Also, make sure to separate code that runs in-editor from code that
> runs in-game. This way, you can find bugs more easily.