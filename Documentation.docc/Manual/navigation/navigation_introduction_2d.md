<!-- Remove this line to publish to docs.xogot.com -->
# 2D navigation overview

Godot provides multiple objects, classes and servers to facilitate grid-based or mesh-based navigation and pathfinding for 2D and 3D games.
The following section provides a quick overview over all available navigation related objects in Godot for 2D scenes and their primary use.

Godot provides the following objects and classes for 2D navigation:

- 
[Astar2D](https://docs.godotengine.org/en/stable/classes/class_astar2d.html#class-astar2d)
Astar2D objects provide an option to find the shortest path in a graph of weighted **points**.
The AStar2D class is best suited for cell-based 2D gameplay that does not require actors to reach any possible position within an area but only predefined, distinct positions.




- 
[AstarGrid2D](https://docs.godotengine.org/en/stable/classes/class_astargrid2d.html#class-astargrid2d)
AstarGrid2D  is a variant of AStar2D that is specialized for partial 2D grids.
AstarGrid2D is simpler to use when applicable because it doesn't require you to manually create points and connect them together.




- 
[NavigationServer2D](https://docs.godotengine.org/en/stable/classes/class_navigationserver2d.html#class-navigationserver2d)
NavigationServer2D provides a powerful server API to find the shortest path between two positions on an area defined by a navigation mesh.
The NavigationServer is best suited for 2D realtime gameplay that does require actors to reach any possible position within a navigation mesh defined area.
Mesh-based navigation scales well with large game worlds as a large area can often be defined with a single polygon when it would require many, many grid cells.
The NavigationServer holds different navigation maps that each consist of regions that hold navigation mesh data.
Agents can be placed on a map for avoidance calculation.
RIDs are used to reference internal maps, regions, and agents when communicating with the server.

The following NavigationServer RID types are available.


NavMap RID
Reference to a specific navigation map that holds regions and agents.
The map will attempt to join the navigation meshes of the regions by proximity.
The map will synchronize regions and agents each physics frame.




NavRegion RID
Reference to a specific navigation region that can hold navigation mesh data.
The region can be enabled / disabled or the use restricted with a navigation layer bitmask.




NavLink RID
Reference to a specific navigation link that connects two navigation mesh positions over arbitrary distances.




NavAgent RID
Reference to a specific avoidance agent.
The avoidance is specified by a radius value.




NavObstacle RID
Reference to a specific avoidance obstacle used to affect and constrain the avoidance velocity of agents.










- 
NavMap RID
Reference to a specific navigation map that holds regions and agents.
The map will attempt to join the navigation meshes of the regions by proximity.
The map will synchronize regions and agents each physics frame.




- 
NavRegion RID
Reference to a specific navigation region that can hold navigation mesh data.
The region can be enabled / disabled or the use restricted with a navigation layer bitmask.




- 
NavLink RID
Reference to a specific navigation link that connects two navigation mesh positions over arbitrary distances.




- 
NavAgent RID
Reference to a specific avoidance agent.
The avoidance is specified by a radius value.




- 
NavObstacle RID
Reference to a specific avoidance obstacle used to affect and constrain the avoidance velocity of agents.




Astar2D objects provide an option to find the shortest path in a graph of weighted **points**.

The AStar2D class is best suited for cell-based 2D gameplay that does not require actors to reach any possible position within an area but only predefined, distinct positions.

AstarGrid2D  is a variant of AStar2D that is specialized for partial 2D grids.

AstarGrid2D is simpler to use when applicable because it doesn't require you to manually create points and connect them together.

NavigationServer2D provides a powerful server API to find the shortest path between two positions on an area defined by a navigation mesh.

The NavigationServer is best suited for 2D realtime gameplay that does require actors to reach any possible position within a navigation mesh defined area.
Mesh-based navigation scales well with large game worlds as a large area can often be defined with a single polygon when it would require many, many grid cells.

The NavigationServer holds different navigation maps that each consist of regions that hold navigation mesh data.
Agents can be placed on a map for avoidance calculation.
RIDs are used to reference internal maps, regions, and agents when communicating with the server.

- 
NavMap RID
Reference to a specific navigation map that holds regions and agents.
The map will attempt to join the navigation meshes of the regions by proximity.
The map will synchronize regions and agents each physics frame.




- 
NavRegion RID
Reference to a specific navigation region that can hold navigation mesh data.
The region can be enabled / disabled or the use restricted with a navigation layer bitmask.




- 
NavLink RID
Reference to a specific navigation link that connects two navigation mesh positions over arbitrary distances.




- 
NavAgent RID
Reference to a specific avoidance agent.
The avoidance is specified by a radius value.




- 
NavObstacle RID
Reference to a specific avoidance obstacle used to affect and constrain the avoidance velocity of agents.




Reference to a specific navigation map that holds regions and agents.
The map will attempt to join the navigation meshes of the regions by proximity.
The map will synchronize regions and agents each physics frame.

Reference to a specific navigation region that can hold navigation mesh data.
The region can be enabled / disabled or the use restricted with a navigation layer bitmask.

Reference to a specific navigation link that connects two navigation mesh positions over arbitrary distances.

Reference to a specific avoidance agent.
The avoidance is specified by a radius value.

Reference to a specific avoidance obstacle used to affect and constrain the avoidance velocity of agents.

The following scene tree nodes are available as helpers to work with the NavigationServer2D API.

- 
[NavigationRegion2D](https://docs.godotengine.org/en/stable/classes/class_navigationregion2d.html#class-navigationregion2d) Node
A Node that holds a NavigationPolygon resource that defines a navigation mesh for the NavigationServer2D.

The region can be enabled / disabled.
The use in pathfinding can be further restricted through the navigation_layers bitmask.
The NavigationServer2D will join the navigation meshes of regions by proximity for a combined navigation mesh.





- The region can be enabled / disabled.

- The use in pathfinding can be further restricted through the navigation_layers bitmask.

- The NavigationServer2D will join the navigation meshes of regions by proximity for a combined navigation mesh.

- 
[NavigationLink2D](https://docs.godotengine.org/en/stable/classes/class_navigationlink2d.html#class-navigationlink2d) Node
A Node that connects two positions on navigation meshes over arbitrary distances for pathfinding.

The link can be enabled / disabled.
The link can be made one-way or bidirectional.
The use in pathfinding can be further restricted through the navigation_layers bitmask.

Links tell the pathfinding that a connection exists and at what cost. The actual agent handling and movement needs to happen in custom scripts.




- The link can be enabled / disabled.

- The link can be made one-way or bidirectional.

- The use in pathfinding can be further restricted through the navigation_layers bitmask.

- 
[NavigationAgent2D](https://docs.godotengine.org/en/stable/classes/class_navigationagent2d.html#class-navigationagent2d) Node
A helper Node used to facilitate common NavigationServer2D API calls for pathfinding and avoidance.
Use this Node with a Node2D inheriting parent Node.




- 
[NavigationObstacle2D](https://docs.godotengine.org/en/stable/classes/class_navigationobstacle2d.html#class-navigationobstacle2d) Node
A Node that can be used to affect and constrain the avoidance velocity of avoidance enabled agents.
This Node does NOT affect the pathfinding of agents. You need to change the navigation meshes for that instead.




A Node that holds a NavigationPolygon resource that defines a navigation mesh for the NavigationServer2D.

- The region can be enabled / disabled.

- The use in pathfinding can be further restricted through the navigation_layers bitmask.

- The NavigationServer2D will join the navigation meshes of regions by proximity for a combined navigation mesh.

A Node that connects two positions on navigation meshes over arbitrary distances for pathfinding.

- The link can be enabled / disabled.

- The link can be made one-way or bidirectional.

- The use in pathfinding can be further restricted through the navigation_layers bitmask.

Links tell the pathfinding that a connection exists and at what cost. The actual agent handling and movement needs to happen in custom scripts.

A helper Node used to facilitate common NavigationServer2D API calls for pathfinding and avoidance.
Use this Node with a Node2D inheriting parent Node.

A Node that can be used to affect and constrain the avoidance velocity of avoidance enabled agents.
This Node does NOT affect the pathfinding of agents. You need to change the navigation meshes for that instead.

The 2D navigation meshes are defined with the following resources:

- 
[NavigationPolygon](https://docs.godotengine.org/en/stable/classes/class_navigationpolygon.html#class-navigationpolygon) Resource
A resource that holds 2D navigation mesh data.
It provides polygon drawing tools to allow defining navigation areas inside the Editor as well as at runtime.

The NavigationRegion2D Node uses this resource to define its navigation area.
The NavigationServer2D uses this resource to update the navigation mesh of individual regions.
The TileSet Editor creates and uses this resource internally when defining tile navigation areas.





- The NavigationRegion2D Node uses this resource to define its navigation area.

- The NavigationServer2D uses this resource to update the navigation mesh of individual regions.

- The TileSet Editor creates and uses this resource internally when defining tile navigation areas.

A resource that holds 2D navigation mesh data.
It provides polygon drawing tools to allow defining navigation areas inside the Editor as well as at runtime.

- The NavigationRegion2D Node uses this resource to define its navigation area.

- The NavigationServer2D uses this resource to update the navigation mesh of individual regions.

- The TileSet Editor creates and uses this resource internally when defining tile navigation areas.

> Seealso:
>
> You can see how 2D navigation works in action using the
> 2D Navigation Polygon
> and Grid-based Navigation with AStarGrid2D
> demo projects.
>

## Setup for 2D scene

The following steps show the basic setup for minimal viable navigation in 2D.
It uses the NavigationServer2D and a NavigationAgent2D for path movement.

1. Add a NavigationRegion2D Node to the scene.

1. Click on the region node and add a new NavigationPolygon Resource to the region node.

@Image(source: "nav_2d_min_setup_step1.png")

1. Define the movable navigation area with the NavigationPolygon draw tool. Then click
the `Bake NavigationPolygon`` button on the toolbar.

@Image(source: "nav_2d_min_setup_step2.png") {.. note:

The navigation mesh defines the area where an actor can stand and move with its center.
Leave enough margin between the navigation polygon edges and collision objects to not get path following actors repeatedly stuck on collision.}

1. Add a CharacterBody2D node in the scene with a basic collision shape and a sprite or mesh
for visuals.

1. Add a NavigationAgent2D node below the character node.

@Image(source: "nav_2d_min_setup_step3.png")

1. Add the following script to the CharacterBody2D node. We make sure to set a movement target
after the scene has fully loaded and the NavigationServer had time to sync.

> Note:
>
> On the first frame the NavigationServer map has not synchronized region data and any path query will return empty. Wait for the NavigationServer synchronization by awaiting one frame in the script.