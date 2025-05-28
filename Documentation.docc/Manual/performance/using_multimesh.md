<!-- Remove this line to publish to docs.xogot.com -->
# Optimization using MultiMeshes

For large amount of instances (in the thousands), that need to be constantly processed
(and certain amount of control needs to be retained),
<doc:using_servers> is the recommended optimization.

When the amount of objects reach the hundreds of thousands or millions,
none of these approaches are efficient anymore. Still, depending on the requirements, there
is one more optimization possible.

## MultiMeshes

A [MultiMesh](https://docs.godotengine.org/en/stable/classes/class_multimesh.html#class-multimesh) is a single draw primitive that can draw up to millions
of objects in one go. It's extremely efficient because it uses the GPU hardware to do this.

The only drawback is that there is no screen or frustum culling possible for individual instances.
This means, that millions of objects will be always or never drawn, depending on the visibility
of the whole MultiMesh. It is possible to provide a custom visibility rect for them, but it will always
be all-or-none visibility.

If the objects are simple enough (just a couple of vertices), this is generally not much of a problem
as most modern GPUs are optimized for this use case. A workaround is to create several MultiMeshes
for different areas of the world.

It is also possible to execute some logic inside the vertex shader (using the INSTANCE_ID or
INSTANCE_CUSTOM built-in constants). For an example of animating thousands of objects in a MultiMesh,
see the <doc:animating_thousands_of_fish> tutorial. Information
to the shader can be provided via textures (there are floating-point [Image](https://docs.godotengine.org/en/stable/classes/class_image.html#class-image) formats
which are ideal for this).

Another alternative is to use a GDExtension and C++, which should be extremely efficient (it's possible
to set the entire state for all objects using linear memory via the
[RenderingServer.multimesh_set_buffer()](https://docs.godotengine.org/en/stable/classes/class_renderingserver_method_multimesh_set_buffer.html#class-renderingserver_method_multimesh_set_buffer)
function). This way, the array can be created with multiple threads, then set in one call, providing
high cache efficiency.

Finally, it's not required to have all MultiMesh instances visible. The amount of visible ones can be
controlled with the [MultiMesh.visible_instance_count](https://docs.godotengine.org/en/stable/classes/class_multimesh_property_visible_instance_count.html#class-multimesh_property_visible_instance_count)
property. The typical workflow is to allocate the maximum amount of instances that will be used,
then change the amount visible depending on how many are currently needed.

## Multimesh example

Here is an example of using a MultiMesh from code. Languages other than GDScript may be more
efficient for millions of objects, but for a few thousands, GDScript should be fine.