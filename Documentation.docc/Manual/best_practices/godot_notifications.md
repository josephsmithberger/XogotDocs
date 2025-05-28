<!-- Remove this line to publish to docs.xogot.com -->
# Godot notifications

Every Object in Godot implements a
[_notification](https://docs.godotengine.org/en/stable/classes/class_object_private_method__notification.html#class-object_private_method__notification) method. Its purpose is to
allow the Object to respond to a variety of engine-level callbacks that may
relate to it. For example, if the engine tells a
[CanvasItem](https://docs.godotengine.org/en/stable/classes/class_canvasitem.html#class-canvasitem) to "draw", it will call
_notification(NOTIFICATION_DRAW).

Some of these notifications, like draw, are useful to override in scripts. So
much so that Godot exposes many of them with dedicated functions:

- _ready(): NOTIFICATION_READY

- _enter_tree(): NOTIFICATION_ENTER_TREE

- _exit_tree(): NOTIFICATION_EXIT_TREE

- _process(delta): NOTIFICATION_PROCESS

- _physics_process(delta): NOTIFICATION_PHYSICS_PROCESS

- _draw(): NOTIFICATION_DRAW

What users might not realize is that notifications exist for types other
than Node alone, for example:

- [Object::NOTIFICATION_POSTINITIALIZE](https://docs.godotengine.org/en/stable/classes/class_object_constant_notification_postinitialize.html#class-object_constant_notification_postinitialize):
a callback that triggers during object initialization. Not accessible to scripts.

- [Object::NOTIFICATION_PREDELETE](https://docs.godotengine.org/en/stable/classes/class_object_constant_notification_predelete.html#class-object_constant_notification_predelete):
a callback that triggers before the engine deletes an Object, i.e. a
"destructor".

And many of the callbacks that do exist in Nodes don't have any dedicated
methods, but are still quite useful.

- [Node::NOTIFICATION_PARENTED](https://docs.godotengine.org/en/stable/classes/class_node_constant_notification_parented.html#class-node_constant_notification_parented):
a callback that triggers anytime one adds a child node to another node.

- [Node::NOTIFICATION_UNPARENTED](https://docs.godotengine.org/en/stable/classes/class_node_constant_notification_unparented.html#class-node_constant_notification_unparented):
a callback that triggers anytime one removes a child node from another
node.

One can access all these custom notifications from the universal
_notification() method.

> Note:
> Methods in the documentation labeled as "virtual" are also intended to be
> overridden by scripts.
>
> A classic example is the
> [_init](https://docs.godotengine.org/en/stable/classes/class_object_private_method__init.html#class-object_private_method__init) method in Object. While it has no
> NOTIFICATION_* equivalent, the engine still calls the method. Most languages
> (except C#) rely on it as a constructor.
>

So, in which situation should one use each of these notifications or
virtual functions?

## _process vs. _physics_process vs. *_input

Use _process() when one needs a framerate-dependent delta time between
frames. If code that updates object data needs to update as often as
possible, this is the right place. Recurring logic checks and data caching
often execute here, but it comes down to the frequency at which one needs
the evaluations to update. If they don't need to execute every frame, then
implementing a Timer-timeout loop is another option.

Use _physics_process() when one needs a framerate-independent delta time
between frames. If code needs consistent updates over time, regardless
of how fast or slow time advances, this is the right place.
Recurring kinematic and object transform operations should execute here.

While it is possible, to achieve the best performance, one should avoid
making input checks during these callbacks. _process() and
_physics_process() will trigger at every opportunity (they do not "rest" by
default). In contrast, *_input() callbacks will trigger only on frames in
which the engine has actually detected the input.

One can check for input actions within the input callbacks just the same.
If one wants to use delta time, one can fetch it from the related
delta time methods as needed.

## _init vs. initialization vs. export

If the script initializes its own node subtree, without a scene,
that code should execute in _init(). Other property or SceneTree-independent
initializations should also run here.

> Note:
> The C# equivalent to GDScript's _init() method is the constructor.
>

_init() triggers before _enter_tree() or _ready(), but after a script
creates and initializes its properties. When instantiating a scene, property
values will set up according to the following sequence:

1. **Initial value assignment:** the property is assigned its initialization value,
or its default value if one is not specified. If a setter exists, it is not used.

1. _init() **assignment:** the property's value is replaced by any assignments
made in _init(), triggering the setter.

1. **Exported value assignment:** an exported property's value is again replaced by
any value set in the Inspector, triggering the setter.

As a result, instantiating a script versus a scene may affect both the
initialization and the number of times the engine calls the setter.

## _ready vs. _enter_tree vs. NOTIFICATION_PARENTED

When instantiating a scene connected to the first executed scene, Godot will
instantiate nodes down the tree (making _init() calls) and build the tree
going downwards from the root. This causes _enter_tree() calls to cascade
down the tree. Once the tree is complete, leaf nodes call _ready. A node
will call this method once all child nodes have finished calling theirs. This
then causes a reverse cascade going up back to the tree's root.

When instantiating a script or a standalone scene, nodes are not
added to the SceneTree upon creation, so no _enter_tree() callbacks
trigger. Instead, only the _init() call occurs. When the scene is added
to the SceneTree, the _enter_tree() and _ready() calls occur.

If one needs to trigger behavior that occurs as nodes parent to another,
regardless of whether it occurs as part of the main/active scene or not, one
can use the [PARENTED](https://docs.godotengine.org/en/stable/classes/class_node_constant_notification_parented.html#class-node_constant_notification_parented) notification.
For example, here is a snippet that connects a node's method to
a custom signal on the parent node without failing. Useful on data-centric
nodes that one might create at runtime.