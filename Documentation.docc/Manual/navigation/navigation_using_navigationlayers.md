<!-- Remove this line to publish to docs.xogot.com -->
# Using NavigationLayers

NavigationLayers are an optional feature to further control which navigation meshes are considered in a path query.
They work similar to how physics layers control collision between collision objects or how visual layers control what is rendered to the Viewport.

NavigationLayers can be named in the **ProjectSettings** the same as physics layers or visual layers.

@Image(source: "navigationlayers_naming.png")

If a region has not a single compatible navigation layer with the navigation_layers parameter of a path query this regions navigation mesh will be skipped in pathfinding.
See <doc:navigation_using_navigationpaths> for more information on querying the NavigationServer for paths.

NavigationLayers are a single int value that is used as a **bitmask**.
Many navigation related nodes have set_navigation_layer_value() and
get_navigation_layer_value() functions to set and get a layer number directly
without the need for more complex bitwise operations.

In scripts the following helper functions can be used to work with the navigation_layers bitmask.

Changing navigation layers for path queries is a performance friendly alternative to
enabling / disabling entire navigation regions. Compared to region changes a
navigation path query with different navigation layers does not
trigger large scale updates on the NavigationServer.

Changing the navigation layers of NavigationAgent nodes will have an immediate
effect on the next path query. Changing the navigation layers of
regions will have an effect after the next NavigationServer sync.