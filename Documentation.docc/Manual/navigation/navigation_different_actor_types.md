<!-- Remove this line to publish to docs.xogot.com -->
# Support different actor types

@Image(source: "nav_actor_sizes.png")

To support different actor types due to e.g. their sizes each type requires its own
navigation map and navigation mesh baked with an appropriated agent radius and height.
The same approach can be used to distinguish between e.g. landwalking, swimming or flying agents.

> Note:
>
> Agents are exclusively defined by a radius and height value for baking navigation meshes, pathfinding and avoidance. More complex shapes are not supported.
>