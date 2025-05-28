<!-- Remove this line to publish to docs.xogot.com -->
# Quick start guide

- Turn on physics interpolation: [Project Settings > Physics > Common > Physics Interpolation](https://docs.godotengine.org/en/stable/classes/class_projectsettings_property_physics/common/physics_interpolation.html#class-projectsettings_property_physics/common/physics_interpolation)

- Make sure you move objects and run your game logic in _physics_process()
rather than _process(). This includes moving objects directly and
indirectly (by e.g. moving a parent, or using another mechanism to automatically
move nodes).

- Be sure to call [Node.reset_physics_interpolation](https://docs.godotengine.org/en/stable/classes/class_node_method_reset_physics_interpolation.html#class-node_method_reset_physics_interpolation)
on nodes after you first position or teleport them, to prevent "streaking".

- Temporarily try setting [Project Settings > Physics > Common > Physics Tick per Second](https://docs.godotengine.org/en/stable/classes/class_projectsettings_property_physics/common/physics_ticks_per_second.html#class-projectsettings_property_physics/common/physics_ticks_per_second)
to 10 to see the difference with and without interpolation.