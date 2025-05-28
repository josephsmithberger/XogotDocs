<!-- Remove this line to publish to docs.xogot.com -->
# Optimization using Servers

Engines like Godot provide increased ease of use thanks to their high-level constructs and features.
Most of them are accessed and used via the <doc:scene_tree>. Using nodes and
resources simplifies project organization and asset management in complex games.

There are, of course, always drawbacks:

- There is an extra layer of complexity.

- Performance is lower than when using simple APIs directly.

- It is not possible to use multiple threads to control them.

- More memory is needed.

In many cases, this is not really a problem (Godot is very optimized, and most operations are handled
with signals, so no polling is required). Still, sometimes it can be. For example, dealing with
tens of thousands of instances for something that needs to be processed every frame can be a bottleneck.

This type of situation makes programmers regret they are using a game engine and wish they could go
back to a more handcrafted, low-level implementation of game code.

Still, Godot is designed to work around this problem.

> Seealso:
>
> You can see how using low-level servers works in action using the
> Bullet Shower demo project
>

## Servers

One of the most interesting design decisions for Godot is the fact that the whole scene system is
optional. While it is not currently possible to compile it out, it can be completely bypassed.

At the core, Godot uses the concept of Servers. They are very low-level APIs to control
rendering, physics, sound, etc. The scene system is built on top of them and uses them directly.
The most common servers are:

- [RenderingServer](https://docs.godotengine.org/en/stable/classes/class_renderingserver.html#class-renderingserver): handles everything related to graphics.

- [PhysicsServer3D](https://docs.godotengine.org/en/stable/classes/class_physicsserver3d.html#class-physicsserver3d): handles everything related to 3D physics.

- [PhysicsServer2D](https://docs.godotengine.org/en/stable/classes/class_physicsserver2d.html#class-physicsserver2d): handles everything related to 2D physics.

- [AudioServer](https://docs.godotengine.org/en/stable/classes/class_audioserver.html#class-audioserver): handles everything related to audio.

Explore their APIs and you will realize that all the functions provided are low-level
implementations of everything Godot allows you to do.

## RIDs

The key to using servers is understanding Resource ID ([RID](https://docs.godotengine.org/en/stable/classes/class_rid.html#class-rid)) objects. These are opaque
handles to the server implementation. They are allocated and freed manually. Almost every
function in the servers requires RIDs to access the actual resource.

Most Godot nodes and resources contain these RIDs from the servers internally, and they can
be obtained with different functions. In fact, anything that inherits [Resource](https://docs.godotengine.org/en/stable/classes/class_resource.html#class-resource)
can be directly casted to an RID. Not all resources contain an RID, though: in such cases, the RID will be empty. The resource can then be passed to server APIs as an RID.

> Warning: Resources are reference-counted (see [RefCounted](https://docs.godotengine.org/en/stable/classes/class_refcounted.html#class-refcounted)), and
> references to a resource's RID are not counted when determining whether
> the resource is still in use. Make sure to keep a reference to the resource
> outside the server, or else both it and its RID will be erased.
>

For nodes, there are many functions available:

- For CanvasItem, the [CanvasItem.get_canvas_item()](https://docs.godotengine.org/en/stable/classes/class_canvasitem_method_get_canvas_item.html#class-canvasitem_method_get_canvas_item)
method will return the canvas item RID in the server.

- For CanvasLayer, the [CanvasLayer.get_canvas()](https://docs.godotengine.org/en/stable/classes/class_canvaslayer_method_get_canvas.html#class-canvaslayer_method_get_canvas)
method will return the canvas RID in the server.

- For Viewport, the [Viewport.get_viewport_rid()](https://docs.godotengine.org/en/stable/classes/class_viewport_method_get_viewport_rid.html#class-viewport_method_get_viewport_rid)
method will return the viewport RID in the server.

- For 3D, the [World3D](https://docs.godotengine.org/en/stable/classes/class_world3d.html#class-world3d) resource (obtainable in the [Viewport](https://docs.godotengine.org/en/stable/classes/class_viewport.html#class-viewport)
and [Node3D](https://docs.godotengine.org/en/stable/classes/class_node3d.html#class-node3d) nodes)
contains functions to get the RenderingServer Scenario, and the PhysicsServer Space. This
allows creating 3D objects directly with the server API and using them.

- For 2D, the [World2D](https://docs.godotengine.org/en/stable/classes/class_world2d.html#class-world2d) resource (obtainable in the [Viewport](https://docs.godotengine.org/en/stable/classes/class_viewport.html#class-viewport)
and [CanvasItem](https://docs.godotengine.org/en/stable/classes/class_canvasitem.html#class-canvasitem) nodes)
contains functions to get the RenderingServer Canvas, and the Physics2DServer Space. This
allows creating 2D objects directly with the server API and using them.

- The [VisualInstance3D](https://docs.godotengine.org/en/stable/classes/class_visualinstance3d.html#class-visualinstance3d) class, allows getting the scenario instance and
instance base via the [VisualInstance3D.get_instance()](https://docs.godotengine.org/en/stable/classes/class_visualinstance3d_method_get_instance.html#class-visualinstance3d_method_get_instance)
and [VisualInstance3D.get_base()](https://docs.godotengine.org/en/stable/classes/class_visualinstance3d_method_get_base.html#class-visualinstance3d_method_get_base) respectively.

Try exploring the nodes and resources you are familiar with and find the functions to obtain the server RIDs.

It is not advised to control RIDs from objects that already have a node associated. Instead, server
functions should always be used for creating and controlling new ones and interacting with the existing ones.

## Creating a sprite

This is an example of how to create a sprite from code and move it using the low-level
[CanvasItem](https://docs.godotengine.org/en/stable/classes/class_canvasitem.html#class-canvasitem) API.

The Canvas Item API in the server allows you to add draw primitives to it. Once added, they can't be modified.
The Item needs to be cleared and the primitives re-added (this is not the case for setting the transform,
which can be done as many times as desired).

Primitives are cleared this way:

## Instantiating a Mesh into 3D space

The 3D APIs are different from the 2D ones, so the instantiation API must be used.

## Creating a 2D RigidBody and moving a sprite with it

This creates a [RigidBody2D](https://docs.godotengine.org/en/stable/classes/class_rigidbody2d.html#class-rigidbody2d) using the [PhysicsServer2D](https://docs.godotengine.org/en/stable/classes/class_physicsserver2d.html#class-physicsserver2d) API,
and moves a [CanvasItem](https://docs.godotengine.org/en/stable/classes/class_canvasitem.html#class-canvasitem) when the body moves.

The 3D version should be very similar, as 2D and 3D physics servers are identical (using
[RigidBody3D](https://docs.godotengine.org/en/stable/classes/class_rigidbody3d.html#class-rigidbody3d) and [PhysicsServer3D](https://docs.godotengine.org/en/stable/classes/class_physicsserver3d.html#class-physicsserver3d) respectively).

## Getting data from the servers

Try to **never** request any information from RenderingServer, PhysicsServer2D or PhysicsServer3D
by calling functions unless you know what you are doing. These servers will often run asynchronously
for performance and calling any function that returns a value will stall them and force them to process
anything pending until the function is actually called. This will severely decrease performance if you
call them every frame (and it won't be obvious why).

Because of this, most APIs in such servers are designed so it's not even possible to request information
back, until it's actual data that can be saved.