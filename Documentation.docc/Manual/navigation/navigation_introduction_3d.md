<!-- Remove this line to publish to docs.xogot.com -->
# 3D navigation overview

Godot provides multiple objects, classes and servers to facilitate grid-based or mesh-based navigation and pathfinding for 2D and 3D games.
The following section provides a quick overview over all available navigation related objects in Godot for 3D scenes and their primary use.

Godot provides the following objects and classes for 3D navigation:

- 
[Astar3D](https://docs.godotengine.org/en/stable/classes/class_astar3d.html#class-astar3d)
Astar3D objects provide an option to find the shortest path in a graph of weighted **points**.
The AStar3D class is best suited for cell-based 3D gameplay that does not require actors to reach any possible position within an area but only predefined, distinct positions.




- 
[NavigationServer3D](https://docs.godotengine.org/en/stable/classes/class_navigationserver3d.html#class-navigationserver3d)
NavigationServer3D provides a powerful server API to find the shortest path between two positions on an area defined by a navigation mesh.
The NavigationServer is best suited for 3D realtime gameplay that does require actors to reach any possible position within a navigation mesh defined area.
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
The avoidance is defined by a radius value.




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
The avoidance is defined by a radius value.




- 
NavObstacle RID
Reference to a specific avoidance obstacle used to affect and constrain the avoidance velocity of agents.




Astar3D objects provide an option to find the shortest path in a graph of weighted **points**.

The AStar3D class is best suited for cell-based 3D gameplay that does not require actors to reach any possible position within an area but only predefined, distinct positions.

NavigationServer3D provides a powerful server API to find the shortest path between two positions on an area defined by a navigation mesh.

The NavigationServer is best suited for 3D realtime gameplay that does require actors to reach any possible position within a navigation mesh defined area.
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
The avoidance is defined by a radius value.




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
The avoidance is defined by a radius value.

Reference to a specific avoidance obstacle used to affect and constrain the avoidance velocity of agents.

The following scene tree nodes are available as helpers to work with the NavigationServer3D API.

- 
[NavigationRegion3D](https://docs.godotengine.org/en/stable/classes/class_navigationregion3d.html#class-navigationregion3d) Node
A Node that holds a Navigation Mesh resource that defines a navigation mesh for the NavigationServer3D.

The region can be enabled / disabled.
The use in pathfinding can be further restricted through the navigation_layers bitmask.
The NavigationServer3D will join the navigation meshes of regions by proximity for a combined navigation mesh.





- The region can be enabled / disabled.

- The use in pathfinding can be further restricted through the navigation_layers bitmask.

- The NavigationServer3D will join the navigation meshes of regions by proximity for a combined navigation mesh.

- 
[NavigationLink3D](https://docs.godotengine.org/en/stable/classes/class_navigationlink3d.html#class-navigationlink3d) Node
A Node that connects two positions on navigation meshes over arbitrary distances for pathfinding.

The link can be enabled / disabled.
The link can be made one-way or bidirectional.
The use in pathfinding can be further restricted through the navigation_layers bitmask.

Links tell the pathfinding that a connection exists and at what cost. The actual agent handling and movement needs to happen in custom scripts.




- The link can be enabled / disabled.

- The link can be made one-way or bidirectional.

- The use in pathfinding can be further restricted through the navigation_layers bitmask.

- 
[NavigationAgent3D](https://docs.godotengine.org/en/stable/classes/class_navigationagent3d.html#class-navigationagent3d) Node
A helper Node used to facilitate common NavigationServer3D API calls for pathfinding and avoidance.
Use this Node with a Node3D inheriting parent Node.




- 
[NavigationObstacle3D](https://docs.godotengine.org/en/stable/classes/class_navigationobstacle3d.html#class-navigationobstacle3d) Node
A Node that can be used to affect and constrain the avoidance velocity of avoidance enabled agents.
This Node does NOT affect the pathfinding of agents. You need to change the navigation meshes for that instead.




A Node that holds a Navigation Mesh resource that defines a navigation mesh for the NavigationServer3D.

- The region can be enabled / disabled.

- The use in pathfinding can be further restricted through the navigation_layers bitmask.

- The NavigationServer3D will join the navigation meshes of regions by proximity for a combined navigation mesh.

A Node that connects two positions on navigation meshes over arbitrary distances for pathfinding.

- The link can be enabled / disabled.

- The link can be made one-way or bidirectional.

- The use in pathfinding can be further restricted through the navigation_layers bitmask.

Links tell the pathfinding that a connection exists and at what cost. The actual agent handling and movement needs to happen in custom scripts.

A helper Node used to facilitate common NavigationServer3D API calls for pathfinding and avoidance.
Use this Node with a Node3D inheriting parent Node.

A Node that can be used to affect and constrain the avoidance velocity of avoidance enabled agents.
This Node does NOT affect the pathfinding of agents. You need to change the navigation meshes for that instead.

The 3D navigation meshes are defined with the following resources:

- 
[NavigationMesh](https://docs.godotengine.org/en/stable/classes/class_navigationmesh.html#class-navigationmesh) Resource
A resource that holds 3D navigation mesh data.
It provides 3D geometry baking options to define navigation areas inside the Editor as well as at runtime.

The NavigationRegion3D Node uses this resource to define its navigation area.
The NavigationServer3D uses this resource to update the navigation mesh of individual regions.
The GridMap Editor uses this resource when specific navigation meshes are defined for each grid cell.





- The NavigationRegion3D Node uses this resource to define its navigation area.

- The NavigationServer3D uses this resource to update the navigation mesh of individual regions.

- The GridMap Editor uses this resource when specific navigation meshes are defined for each grid cell.

A resource that holds 3D navigation mesh data.
It provides 3D geometry baking options to define navigation areas inside the Editor as well as at runtime.

- The NavigationRegion3D Node uses this resource to define its navigation area.

- The NavigationServer3D uses this resource to update the navigation mesh of individual regions.

- The GridMap Editor uses this resource when specific navigation meshes are defined for each grid cell.

> Seealso:
>
> You can see how 3D navigation works in action using the
> 3D Navigation demo project.
>

## Setup for 3D scene

The following steps show a basic setup for minimal viable navigation in 3D.
It uses the NavigationServer3D and a NavigationAgent3D for path movement.

1. Add a NavigationRegion3D Node to the scene.

1. Click on the region node and add a new [NavigationMesh](https://docs.godotengine.org/en/stable/classes/class_navigationmesh.html#class-navigationmesh) Resource to
the region node.

@Image(source: "nav_3d_min_setup_step1.png")

1. Add a new MeshInstance3D node as a child of the region node.

1. Select the MeshInstance3D node and add a new PlaneMesh and increase the xy size to 10.

1. Select the region node again and press the "Bake Navmesh" button on the top bar.

@Image(source: "nav_3d_min_setup_step2.png")

1. Now a transparent navigation mesh appears that hovers some distance on top of the PlaneMesh.

@Image(source: "nav_3d_min_setup_step3.png")

1. Add a CharacterBody3D node in the scene with a basic collision shape and some mesh for visuals.

1. Add a NavigationAgent3D node below the character node.

@Image(source: "nav_3d_min_setup_step4.png")

1. Add a script to the CharacterBody3D node with the following content. We make sure to set a
movement target after the scene has fully loaded and the NavigationServer had time to sync.
Also, add a Camera3D and some light and environment to see something.

> Note:
>
> On the first frame the NavigationServer map has not synchronized region data and any path query will return empty. Wait for the NavigationServer synchronization by awaiting one frame in the script.