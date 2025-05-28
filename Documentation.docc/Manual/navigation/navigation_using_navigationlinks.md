<!-- Remove this line to publish to docs.xogot.com -->
# Using NavigationLinks

@Image(source: "nav_navmesh_links.png")

NavigationLinks are used to connect navigation mesh polygons from [NavigationRegion2D](https://docs.godotengine.org/en/stable/classes/class_navigationregion2d.html#class-navigationregion2d)
and [NavigationRegion3D](https://docs.godotengine.org/en/stable/classes/class_navigationregion3d.html#class-navigationregion3d) over arbitrary distances for pathfinding.

NavigationLinks are also used to consider movement shortcuts in pathfinding available through
interacting with gameplay objects e.g. ladders, jump pads or teleports.

2D and 3D versions of NavigationJumplinks nodes are available as
[NavigationLink2D](https://docs.godotengine.org/en/stable/classes/class_navigationlink2d.html#class-navigationlink2d) and
[NavigationLink3D](https://docs.godotengine.org/en/stable/classes/class_navigationlink3d.html#class-navigationlink3d) respectively.

Different NavigationRegions can connect their navigation meshes without the need for a NavigationLink
as long as they have overlapping edges or edges that are within navigation map edge_connection_margin.
As soon as the distance becomes too large, building valid connections becomes a problem - a problem that NavigationLinks can solve.

See <doc:navigation_using_navigationregions> to learn more about the use of navigation regions.
See <doc:navigation_connecting_navmesh> to learn more about how to connect navigation meshes.

@Image(source: "nav_link_properties.png")

NavigationLinks share many properties with NavigationRegions like navigation_layers.
NavigationLinks add a single connection between two positions over an arbitrary distance
compared to NavigationRegions that add a more local traversable area with a navigation mesh resource.

NavigationLinks have a start_position and end_position and can go in both directions when bidirectional is enabled.
When placed a navigationlink connects the navigation mesh polygons closest to its start_position and end_position within search radius for pathfinding.

The polygon search radius can be configured globally in the ProjectSettings under navigation/2d_or_3d/default_link_connection_radius
or set for each navigation **map** individually using the NavigationServer.map_set_link_connection_radius() function.

Both start_position and end_position have debug markers in the Editor.
The arrows indicate which direction the link can be travelled across, and the visible radius of
a position shows the polygon search radius. All navigation mesh polygons inside are compared and
the closest is picked for the edge connection. If no valid polygon is found within the search
radius the navigation link gets disabled.

@Image(source: "nav_link_debug_visuals.png")

The link debug visuals can be changed in the Editor [ProjectSettings](https://docs.godotengine.org/en/stable/classes/class_projectsettings.html#class-projectsettings) under debug/shapes/navigation.
The visibility of the debug can also be controlled in the Editor 3D Viewport gizmo menu.

A navigation link does not provide any specialized movement through the link. Instead, when
an agent reaches the position of a link, game code needs to react (e.g. through area triggers)
and provide means for the agent to move through the link to end up at the links other position
(e.g. through teleport or animation). Without that an agent will attempt to move itself along
the path of the link. You could end up with an agent walking over a bottomless pit instead of
waiting for a moving platform, or walking through a teleporter and proceeding through a wall.

## Navigation link script templates

The following script uses the NavigationServer to create a new navigation link.