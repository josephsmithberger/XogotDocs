<!-- Remove this line to publish to docs.xogot.com -->
# Using NavigationPathQueryObjects

NavigationPathQueryObjects can be used together with NavigationServer.query_path()
to obtain a heavily **customized** navigation path including optional **meta data** about the path.

This requires more setup compared to obtaining a normal NavigationPath but lets you tailor
the pathfinding and provided path data to the different needs of a project.

NavigationPathQueryObjects consist of a pair of objects, a NavigationPathQueryParameters object holding the customization options
for the query and a NavigationPathQueryResult that receives (regular) updates with the resulting path and meta data from the query.

2D and 3D versions of NavigationPathQueryParameters are available as
[NavigationPathQueryParameters2D](https://docs.godotengine.org/en/stable/classes/class_navigationpathqueryparameters2d.html#class-navigationpathqueryparameters2d) and
[NavigationPathQueryParameters3D](https://docs.godotengine.org/en/stable/classes/class_navigationpathqueryparameters3d.html#class-navigationpathqueryparameters3d) respectively.

2D and 3D versions of NavigationPathQueryResult are available as
[NavigationPathQueryResult2D](https://docs.godotengine.org/en/stable/classes/class_navigationpathqueryresult2d.html#class-navigationpathqueryresult2d) and
[NavigationPathQueryResult3D](https://docs.godotengine.org/en/stable/classes/class_navigationpathqueryresult3d.html#class-navigationpathqueryresult3d) respectively.

Both parameters and result are used as a pair with the NavigationServer.query_path() function.

For the available customization options and their use see the class doc of the parameters.

While not a strict requirement, both objects are intended to be created once in advance, stored in a
persistent variable for the agent and reused for every followup path query with updated parameters.
This reuse avoids performance implications from frequent object creation if a project
has a large quantity of simultaneous agents that regularly update their paths.