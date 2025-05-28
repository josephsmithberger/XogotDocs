<!-- Remove this line to publish to docs.xogot.com -->
# Overridable functions

Godot's Node class provides virtual functions you can override to update nodes
every frame or on specific events, like when they enter the scene tree.

This document presents the ones you'll use most often.

> Seealso: Under the hood, these functions rely on Godot's low-level
> notifications system. To learn more about it, see
> <doc:godot_notifications>.
>

Two functions allow you to initialize and get nodes besides the class's
constructor: _enter_tree() and _ready().

When the node enters the Scene Tree, it becomes active and the engine calls its
_enter_tree() method. That node's children may not be part of the active scene yet. As
you can remove and re-add nodes to the scene tree, this function may be called
multiple times throughout a node's lifetime.

Most of the time, you'll use _ready() instead. This function is called only
once in a node's lifetime, after _enter_tree(). _ready() ensures that all children
have entered the scene tree first, so you can safely call get_node() on them.

> Seealso: To learn more about getting node references, read
> <doc:nodes_and_scene_instances>.
>

Another related callback is _exit_tree(), which the engine calls every time
a node is about to exit the scene tree. This can be when you call [Node.remove_child()](https://docs.godotengine.org/en/stable/classes/class_node_method_remove_child.html#class-node_method_remove_child) or when you free a node.

The two virtual methods _process() and _physics_process() allow you to
update the node, every frame and every physics frame respectively. For more
information, read the dedicated documentation:
<doc:idle_and_physics_processing>.

Two more essential built-in node callback functions are
[Node._unhandled_input()](https://docs.godotengine.org/en/stable/classes/class_node_private_method__unhandled_input.html#class-node_private_method__unhandled_input) and
[Node._input()](https://docs.godotengine.org/en/stable/classes/class_node_private_method__input.html#class-node_private_method__input), which you use to both receive
and process individual input events. The _unhandled_input() method receives
every key press, mouse click, etc. that have not been handled already in an
_input() callback or in a user interface component. You want to use it for
gameplay input in general. The _input() callback allows you to intercept and
process input events before _unhandled_input() gets them.

To learn more about inputs in Godot, see the :ref:`Input section <toc-learn-features-inputs>`.

There are some more overridable functions like
[Node._get_configuration_warnings()](https://docs.godotengine.org/en/stable/classes/class_node_private_method__get_configuration_warnings.html#class-node_private_method__get_configuration_warnings). Specialized node types provide
more callbacks like [CanvasItem._draw()](https://docs.godotengine.org/en/stable/classes/class_canvasitem_private_method__draw.html#class-canvasitem_private_method__draw) to
draw programmatically or [Control._gui_input()](https://docs.godotengine.org/en/stable/classes/class_control_private_method__gui_input.html#class-control_private_method__gui_input) to handle clicks and input on UI elements.