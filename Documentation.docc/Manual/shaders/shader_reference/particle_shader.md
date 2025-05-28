<!-- Remove this line to publish to docs.xogot.com -->
# Particle shaders

Particle shaders are a special type of shader that runs before the object is
drawn. They are used for calculating material properties such as color,
position, and rotation. They are drawn with any regular material for CanvasItem
or Spatial, depending on whether they are 2D or 3D.

Particle shaders are unique because they are not used to draw the object itself;
they are used to calculate particle properties, which are then used by a
<doc:canvas_item_shader> or <doc:spatial_shader>
shader. They contain two processor functions: start() and process().

Unlike other shader types, particle shaders keep the data that was output the
previous frame. Therefore, particle shaders can be used for complex effects that
take place over multiple frames.

> Note:
>
> Particle shaders are only available with GPU-based particle nodes
> ([GPUParticles2D](https://docs.godotengine.org/en/stable/classes/class_gpuparticles2d.html#class-gpuparticles2d) and [GPUParticles3D](https://docs.godotengine.org/en/stable/classes/class_gpuparticles3d.html#class-gpuparticles3d)).
>
> CPU-based particle nodes ([CPUParticles2D](https://docs.godotengine.org/en/stable/classes/class_cpuparticles2d.html#class-cpuparticles2d) and
> [CPUParticles3D](https://docs.godotengine.org/en/stable/classes/class_cpuparticles3d.html#class-cpuparticles3d)) are rendered on the GPU (which means they can
> use custom CanvasItem or Spatial shaders), but their motion is simulated
> on the CPU.
>

## Render modes

Render mode | Description
----------- | -----------
**keep_data** | Do not clear previous data on restart.
**disable_force** | Disable attractor force.
**disable_velocity** | IgnoreVELOCITYvalue.
**collision_use_scale** | Scale the particle's size for collisions.

## Built-ins

Values marked as in are read-only. Values marked as out can optionally be written to and will
not necessarily contain sensible values. Values marked as inout provide a sensible default
value, and can optionally be written to. Samplers cannot be written to so they are not marked.

## Global built-ins

Global built-ins are available everywhere, including custom functions.

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
in float**E** | AnEconstant (2.718281). Euler's number and a base of the natural logarithm.

## Start and Process built-ins

These properties can be accessed from both the start() and process() functions.

Function | Description
-------- | -----------
in float**LIFETIME** | Particle lifetime.
in float**DELTA** | Delta process time.
in uint**NUMBER** | Unique number since emission start.
in uint**INDEX** | Particle index (from total particles).
in mat4**EMISSION_TRANSFORM** | Emitter transform (used for non-local systems).
in uint**RANDOM_SEED** | Random seed used as base for random.
inout bool**ACTIVE** | truewhen the particle is active, can be setfalse.
inout vec4**COLOR** | Particle color, can be written to and accessed in mesh's vertex function.
inout vec3**VELOCITY** | Particle velocity, can be modified.
inout mat4**TRANSFORM** | Particle transform.
inout vec4**CUSTOM** | Custom particle data. Accessible from shader of mesh asINSTANCE_CUSTOM.
inout float**MASS** | Particle mass, intended to be used with attractors. Equals1.0by default.
in vec4**USERDATAX** | Vector that enables the integration of supplementary user-defined data into the particle process shader.USERDATAXare six built-ins identified by number,Xcan be numbers between 1 and 6, for exampleUSERDATA3.
in uint**FLAG_EMIT_POSITION** | A flag for using on the last argument ofemit_subparticle()function to assign a position to a new particle's transform.
in uint**FLAG_EMIT_ROT_SCALE** | A flag for using on the last argument ofemit_subparticle()function to assign the rotation and scale to a new particle's transform.
in uint**FLAG_EMIT_VELOCITY** | A flag for using on the last argument ofemit_subparticle()function to assign a velocity to a new particle.
in uint**FLAG_EMIT_COLOR** | A flag for using on the last argument ofemit_subparticle()function to assign a color to a new particle.
in uint**FLAG_EMIT_CUSTOM** | A flag for using on the last argument ofemit_subparticle()function to assign a custom data vector to a new particle.
in vec3**EMITTER_VELOCITY** | Velocity of the [Particles2D](https://docs.godotengine.org/en/stable/classes/class_gpuparticles2d.html#class-gpuparticles2d) ([3D](https://docs.godotengine.org/en/stable/classes/class_gpuparticles3d.html#class-gpuparticles3d)) node.
in float**INTERPOLATE_TO_END** | Value of [interp_to_end](https://docs.godotengine.org/en/stable/classes/class_gpuparticles2d_property_interp_to_end.html#class-gpuparticles2d_property_interp_to_end)
([3D](https://docs.godotengine.org/en/stable/classes/class_gpuparticles3d_property_interp_to_end.html#class-gpuparticles3d_property_interp_to_end)) property of Particles node.
in uint**AMOUNT_RATIO** | Value of [amount_ratio](https://docs.godotengine.org/en/stable/classes/class_gpuparticles2d_property_amount_ratio.html#class-gpuparticles2d_property_amount_ratio)
([3D](https://docs.godotengine.org/en/stable/classes/class_gpuparticles3d_property_amount_ratio.html#class-gpuparticles3d_property_amount_ratio)) property of Particles node.

> Note: In order to use the COLOR variable in a StandardMaterial3D, set vertex_color_use_as_albedo
> to true. In a ShaderMaterial, access it with the COLOR variable.
>

## Start built-ins

Built-in | Description
-------- | -----------
in bool**RESTART_POSITION** | trueif particle is restarted, or emitted without a custom position (i.e. this particle was created byemit_subparticle()without theFLAG_EMIT_POSITIONflag).
in bool**RESTART_ROT_SCALE** | trueif particle is restarted, or emitted without a custom rotation or scale (i.e. this particle was created byemit_subparticle()without theFLAG_EMIT_ROT_SCALEflag).
in bool**RESTART_VELOCITY** | trueif particle is restarted, or emitted without a custom velocity (i.e. this particle was created byemit_subparticle()without theFLAG_EMIT_VELOCITYflag).
in bool**RESTART_COLOR** | trueif particle is restarted, or emitted without a custom color (i.e. this particle was created byemit_subparticle()without theFLAG_EMIT_COLORflag).
in bool**RESTART_CUSTOM** | trueif particle is restarted, or emitted without a custom property (i.e. this particle was created byemit_subparticle()without theFLAG_EMIT_CUSTOMflag).

## Process built-ins

Built-in | Description
-------- | -----------
in bool**RESTART** | trueif the current process frame is first for the particle.
in bool**COLLIDED** | truewhen the particle has collided with a particle collider.
in vec3**COLLISION_NORMAL** | A normal of the last collision. If there is no collision detected it is equal to(0.0, 0.0, 0.0).
in float**COLLISION_DEPTH** | A length of normal of the last collision. If there is no collision detected it is equal to0.0.
in vec3**ATTRACTOR_FORCE** | A combined force of the attractors at the moment on that particle.

## Process functions

emit_subparticle() is currently the only custom function supported by
particles shaders. It allows users to add a new particle with specified
parameters from a sub-emitter. The newly created particle will only use the
properties that match the flags parameter. For example, the
following code will emit a particle with a specified position, velocity, and
color, but unspecified rotation, scale, and custom value:

```
mat4 custom_transform = mat4(1.0);
custom_transform[3].xyz = vec3(10.5, 0.0, 4.0);
emit_subparticle(custom_transform, vec3(1.0, 0.5, 1.0), vec4(1.0, 0.0, 0.0, 1.0), vec4(1.0), FLAG_EMIT_POSITION | FLAG_EMIT_VELOCITY | FLAG_EMIT_COLOR);
```

Function | Description
-------- | -----------
bool**emit_subparticle**(mat4 xform, vec3 velocity, vec4 color, vec4 custom, uint flags) | Emits a particle from a sub-emitter.