<!-- Remove this line to publish to docs.xogot.com -->
# Fog shaders

Fog shaders are used to define how fog is added (or subtracted) from a scene in
a given area. Fog shaders are always used together with
[FogVolumes](https://docs.godotengine.org/en/stable/classes/class_fogvolume.html#class-fogvolume) and volumetric fog. Fog shaders only have
one processing function, the fog() function.

The resolution of the fog shaders depends on the resolution of the
volumetric fog froxel grid. Accordingly, the level of detail that a fog shader
can add depends on how close the [FogVolume](https://docs.godotengine.org/en/stable/classes/class_fogvolume.html#class-fogvolume) is to the
camera.

Fog shaders are a special form of compute shader that is called once for
every froxel that is touched by an axis aligned bounding box of the associated
[FogVolume](https://docs.godotengine.org/en/stable/classes/class_fogvolume.html#class-fogvolume). This means that froxels that just barely
touch a given [FogVolume](https://docs.godotengine.org/en/stable/classes/class_fogvolume.html#class-fogvolume) will still be used.

## Built-ins

Values marked as in are read-only. Values marked as out can optionally
be written to and will not necessarily contain sensible values. Samplers cannot
be written to so they are not marked.

## Global built-ins

Global built-ins are available everywhere, including in custom functions.

Built-in | Description
-------- | -----------
in float**TIME** | Global time since the engine has started, in seconds. It repeats after every3,600seconds (which can  be changed with the
[rollover](https://docs.godotengine.org/en/stable/classes/class_projectsettings_property_rendering/limits/time/time_rollover_secs.html#class-projectsettings_property_rendering/limits/time/time_rollover_secs)
setting). It's affected by
[time_scale](https://docs.godotengine.org/en/stable/classes/class_engine_property_time_scale.html#class-engine_property_time_scale) but not by pausing. If you need aTIMEvariable that is not affected by time scale, add your own
<doc:shading_language#Global-Uniforms> and update it each
frame.
in float**PI** | APIconstant (3.141592).
A ratio of a circle's circumference to its diameter and amount of radians in half turn.
in float**TAU** | ATAUconstant (6.283185).
An equivalent ofPI * 2and amount of radians in full turn.
in float**E** | AnEconstant (2.718281).
Euler's number and a base of the natural logarithm.

## Fog built-ins

All of the output values of fog volumes overlap one another. This allows
[FogVolumes](https://docs.godotengine.org/en/stable/classes/class_fogvolume.html#class-fogvolume) to be rendered efficiently as they can all
be drawn at once.

Built-in | Description
-------- | -----------
in vec3**WORLD_POSITION** | Position of current froxel cell in world space.
in vec3**OBJECT_POSITION** | Position of the center of the current [FogVolume](https://docs.godotengine.org/en/stable/classes/class_fogvolume.html#class-fogvolume) in world space.
in vec3**UVW** | 3-dimensional UV, used to map a 3D texture to the current [FogVolume](https://docs.godotengine.org/en/stable/classes/class_fogvolume.html#class-fogvolume).
in vec3**SIZE** | Size of the current [FogVolume](https://docs.godotengine.org/en/stable/classes/class_fogvolume.html#class-fogvolume) when its
[shape](https://docs.godotengine.org/en/stable/classes/class_fogvolume_property_shape.html#class-fogvolume_property_shape) has a size.
in vec3**SDF** | Signed distance field to the surface of the [FogVolume](https://docs.godotengine.org/en/stable/classes/class_fogvolume.html#class-fogvolume). Negative if
inside volume, positive otherwise.
out vec3**ALBEDO** | Output base color value, interacts with light to produce final color. Only written to fog
volume if used.
out float**DENSITY** | Output density value. Can be negative to allow subtracting one volume from another. Density
must be used for fog shader to write anything at all.
out vec3**EMISSION** | Output emission color value, added to color during light pass to produce final color. Only
written to fog volume if used.