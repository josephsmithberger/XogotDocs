<!-- Remove this line to publish to docs.xogot.com -->
# Logic preferences

Ever wondered whether one should approach problem X with strategy Y or Z?
This article covers a variety of topics related to these dilemmas.

## Adding nodes and changing properties: which first?

When initializing nodes from a script at runtime, you may need to change
properties such as the node's name or position. A common dilemma is, when
should you change those values?

It is the best practice to change values on a node before adding it to the
scene tree. Some property's setters have code to update other
corresponding values, and that code can be slow! For most cases, this code
has no impact on your game's performance, but in heavy use cases such as
procedural generation, it can bring your game to a crawl.

For these reasons, it is usually best practice to set the initial values
of a node before adding it to the scene tree. There are some exceptions where
values can't be set before being added to the scene tree, like setting global
position.

## Loading vs. preloading

In GDScript, there exists the global
[preload](https://docs.godotengine.org/en/stable/classes/class_@gdscript_method_preload.html#class-@gdscript_method_preload) method. It loads resources as
early as possible to front-load the "loading" operations and avoid loading
resources while in the middle of performance-sensitive code.

Its counterpart, the [load](https://docs.godotengine.org/en/stable/classes/class_@gdscript_method_load.html#class-@gdscript_method_load) method, loads a
resource only when it reaches the load statement. That is, it will load a
resource in-place which can cause slowdowns when it occurs in the middle of
sensitive processes. The load() function is also an alias for
[ResourceLoader.load(path)](https://docs.godotengine.org/en/stable/classes/class_resourceloader_method_load.html#class-resourceloader_method_load) which is
accessible to all scripting languages.

So, when exactly does preloading occur versus loading, and when should one use
either? Let's see an example:

Preloading allows the script to handle all the loading the moment one loads the
script. Preloading is useful, but there are also times when one doesn't wish
for it. To distinguish these situations, there are a few things one can
consider:

1. If one cannot determine when the script might load, then preloading a
resource, especially a scene or script, could result in further loads one
does not expect. This could lead to unintentional, variable-length
load times on top of the original script's load operations.

1. If something else could replace the value (like a scene's exported
initialization), then preloading the value has no meaning. This point isn't
a significant factor if one intends to always create the script on its own.

1. If one wishes only to 'import' another class resource (script or scene),
then using a preloaded constant is often the best course of action. However,
in exceptional cases, one may wish not to do this:

If the 'imported' class is liable to change, then it should be a property
instead, initialized either using an @export or a load() (and
perhaps not even initialized until later).
If the script requires a great many dependencies, and one does not wish
to consume so much memory, then one may wish to, load and unload various
dependencies at runtime as circumstances change. If one preloads
resources into constants, then the only way to unload these resources
would be to unload the entire script. If they are instead loaded
properties, then one can set them to null and remove all references
to the resource entirely (which, as a
[RefCounted](https://docs.godotengine.org/en/stable/classes/class_refcounted.html#class-refcounted)-extending type, will cause the
resources to delete themselves from memory).



1. If the 'imported' class is liable to change, then it should be a property
instead, initialized either using an @export or a load() (and
perhaps not even initialized until later).

1. If the script requires a great many dependencies, and one does not wish
to consume so much memory, then one may wish to, load and unload various
dependencies at runtime as circumstances change. If one preloads
resources into constants, then the only way to unload these resources
would be to unload the entire script. If they are instead loaded
properties, then one can set them to null and remove all references
to the resource entirely (which, as a
[RefCounted](https://docs.godotengine.org/en/stable/classes/class_refcounted.html#class-refcounted)-extending type, will cause the
resources to delete themselves from memory).

1. If the 'imported' class is liable to change, then it should be a property
instead, initialized either using an @export or a load() (and
perhaps not even initialized until later).

1. If the script requires a great many dependencies, and one does not wish
to consume so much memory, then one may wish to, load and unload various
dependencies at runtime as circumstances change. If one preloads
resources into constants, then the only way to unload these resources
would be to unload the entire script. If they are instead loaded
properties, then one can set them to null and remove all references
to the resource entirely (which, as a
[RefCounted](https://docs.godotengine.org/en/stable/classes/class_refcounted.html#class-refcounted)-extending type, will cause the
resources to delete themselves from memory).

## Large levels: static vs. dynamic

If one is creating a large level, which circumstances are most appropriate?
Should they create the level as one static space? Or should they load the
level in pieces and shift the world's content as needed?

Well, the simple answer is, "when the performance requires it." The
dilemma associated with the two options is one of the age-old programming
choices: does one optimize memory over speed, or vice versa?

The naive answer is to use a static level that loads everything at once.
But, depending on the project, this could consume a large amount of
memory. Wasting users' RAM leads to programs running slow or outright
crashing from everything else the computer tries to do at the same time.

No matter what, one should break larger scenes into smaller ones (to aid
in reusability of assets). Developers can then design a node that manages the
creation/loading and deletion/unloading of resources and nodes in real-time.
Games with large and varied environments or procedurally generated
elements often implement these strategies to avoid wasting memory.

On the flip side, coding a dynamic system is more complex, i.e. uses more
programmed logic, which results in opportunities for errors and bugs. If one
isn't careful, they can develop a system that bloats the technical debt of
the application.

As such, the best options would be...

1. To use a static level for smaller games.

1. If one has the time/resources on a medium/large game, create a library or
plugin that can code the management of nodes and resources. If refined
over time, so as to improve usability and stability, then it could evolve
into a reliable tool across projects.

1. Code the dynamic logic for a medium/large game because one has the coding
skills, but not the time or resources to refine the code (game's
gotta get done). Could potentially refactor later to outsource the code
into a plugin.

For an example of the various ways one can swap scenes around at runtime,
please see the <doc:change_scenes_manually>
documentation.