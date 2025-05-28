<!-- Remove this line to publish to docs.xogot.com -->
# Using NavigationMaps

@Image(source: "nav_maps.png")

A NavigationMap is an abstract navigation world on the NavigationServer identified by a NavigationServer [RID](https://docs.godotengine.org/en/stable/classes/class_rid.html#class-rid).

A map can hold and connect a near infinite number of navigation regions with navigation meshes to build the traversable areas of a game world for pathfinding.

A map can contain avoidance agents. Collision avoidance will be calculated based on the agents present in the map.

> Note:
>
> Different NavigationMaps are completely isolated from each other but navigation regions
> and avoidance agents can switch between different maps. Switches will become effective on NavigationServer synchronization.
>

## Default navigation maps

By default Godot creates a navigation map for each [World2D](https://docs.godotengine.org/en/stable/classes/class_world2d.html#class-world2d) and [World3D](https://docs.godotengine.org/en/stable/classes/class_world3d.html#class-world3d) of the root viewport.

The 2D default navigation map RID can be obtained with get_world_2d().get_navigation_map() from any [Node2D](https://docs.godotengine.org/en/stable/classes/class_node2d.html#class-node2d) inheriting Node.

The 3D default navigation map RID can be obtained with get_world_3d().get_navigation_map() from any [Node3D](https://docs.godotengine.org/en/stable/classes/class_node3d.html#class-node3d) inheriting Node.

## Creating new navigation maps

The NavigationServer can create and support as many navigation maps as required for specific gameplay.
Additional navigation maps are created and handled by using the NavigationServer API
directly e.g. to support different avoidance agent or actor locomotion types.

For example uses of different navigation maps see <doc:navigation_different_actor_types> and <doc:navigation_different_actor_locomotion>.

Each navigation map individually synchronizes queued changes to its navigation regions and avoidance agents.
A navigation map that has not received changes will consume little to no processing time.
Navigation regions and avoidance agents can only be part of a single navigation map but they can switch map at any time.

> Note:
>
> A navigation map switch will take effect only after the next NavigationServer synchronization.
>

> Note:
>
> There is no difference between navigation maps created with the NavigationServer2D API or the NavigationServer3D API.