<!-- Remove this line to publish to docs.xogot.com -->
# Spatial shaders

Spatial shaders are used for shading 3D objects. They are the most complex type of shader Godot offers.
Spatial shaders are highly configurable with different render modes and different rendering options
(e.g. Subsurface Scattering, Transmission, Ambient Occlusion, Rim lighting etc). Users can optionally
write vertex, fragment, and light processor functions to affect how objects are drawn.

## Render modes

For visual examples of these render modes, see <doc:standard_material_3d>.

Render mode | Description
----------- | -----------
**blend_mix** | Mix blend mode (alpha is transparency), default.
**blend_add** | Additive blend mode.
**blend_sub** | Subtractive blend mode.
**blend_mul** | Multiplicative blend mode.
**blend_premul_alpha** | Premultiplied alpha blend mode (fully transparent = add, fully opaque = mix).
**depth_draw_opaque** | Only draw depth for opaque geometry (not transparent).
**depth_draw_always** | Always draw depth (opaque and transparent).
**depth_draw_never** | Never draw depth.
**depth_prepass_alpha** | Do opaque depth pre-pass for transparent geometry.
**depth_test_disabled** | Disable depth testing.
**sss_mode_skin** | Subsurface Scattering mode for skin (optimizes visuals for human skin, e.g. boosted red channel).
**cull_back** | Cull back-faces (default).
**cull_front** | Cull front-faces.
**cull_disabled** | Culling disabled (double sided).
**unshaded** | Result is just albedo. No lighting/shading happens in material, making it faster to render.
**wireframe** | Geometry draws using lines (useful for troubleshooting).
**debug_shadow_splits** | Directional shadows are drawn using different colors for each split (useful for troubleshooting).
**diffuse_burley** | Burley (Disney PBS) for diffuse (default).
**diffuse_lambert** | Lambert shading for diffuse.
**diffuse_lambert_wrap** | Lambert-wrap shading (roughness-dependent) for diffuse.
**diffuse_toon** | Toon shading for diffuse.
**specular_schlick_ggx** | Schlick-GGX for direct light specular lobes (default).
**specular_toon** | Toon for direct light specular lobes.
**specular_disabled** | Disable direct light specular lobes. Doesn't affect reflected light (useSPECULAR = 0.0instead).
**skip_vertex_transform** | VERTEX,NORMAL,TANGENT, andBITANGENTneed to be transformed manually in thevertex()function.
**world_vertex_coords** | VERTEX,NORMAL,TANGENT, andBITANGENTare modified in world space instead of model space.
**ensure_correct_normals** | Use when non-uniform scale is applied to mesh(note: currently unimplemented).
**shadows_disabled** | Disable computing shadows in shader. The shader will not receive shadows, but can still cast them.
**ambient_light_disabled** | Disable contribution from ambient light and radiance map.
**shadow_to_opacity** | Lighting modifies the alpha so shadowed areas are opaque and
non-shadowed areas are transparent. Useful for overlaying shadows onto
a camera feed in AR.
**vertex_lighting** | Use vertex-based lighting instead of per-pixel lighting.
**particle_trails** | Enables the trails when used on particles geometry.
**alpha_to_coverage** | Alpha antialiasing mode, seeherefor more.
**alpha_to_coverage_and_one** | Alpha antialiasing mode, seeherefor more.
**fog_disabled** | Disable receiving depth-based or volumetric fog. Useful forblend_addmaterials like particles.

## Built-ins

Values marked as in are read-only. Values marked as out can optionally be written to and will
not necessarily contain sensible values. Values marked as inout provide a sensible default
value, and can optionally be written to. Samplers cannot be written to so they are not marked.

Not all built-ins are available in all processing functions. To access a vertex
built-in from the fragment() function, you can use a <doc:shading_language#Varyings>.
The same applies for accessing fragment built-ins from the light() function.

## Global built-ins

Global built-ins are available everywhere, including custom functions.

Built-in | Description
-------- | -----------
in float**TIME** | Global time since the engine has started, in seconds. It repeats after every3,600seconds (which can  be changed with the
[rollover](https://docs.godotengine.org/en/stable/classes/class_projectsettings_property_rendering/limits/time/time_rollover_secs.html#class-projectsettings_property_rendering/limits/time/time_rollover_secs)
setting). It's affected by [time_scale](https://docs.godotengine.org/en/stable/classes/class_engine_property_time_scale.html#class-engine_property_time_scale) but not by pausing.
If you need aTIMEvariable that is not affected by time scale, add your own
<doc:shading_language#Global-Uniforms> and update it each
frame.
in float**PI** | APIconstant (3.141592).
A ratio of a circle's circumference to its diameter and amount of radians in half turn.
in float**TAU** | ATAUconstant (6.283185).
An equivalent ofPI * 2and amount of radians in full turn.
in float**E** | AnEconstant (2.718281). Euler's number and a base of the natural logarithm.
in bool**OUTPUT_IS_SRGB** | truewhen output is in sRGB color space (this istruein the Compatibility
renderer,falsein Forward+ and Mobile).
in float**CLIP_SPACE_FAR** | Clip space farzvalue.
In the Forward+ or Mobile renderers, it's0.0.
In the Compatibility renderer, it's-1.0.

## Vertex built-ins

Vertex data (VERTEX, NORMAL, TANGENT, and BITANGENT) are presented in model space
(also called local space). If not written to, these values will not be modified and be
passed through as they came, then transformed into view space to be used in fragment().

They can optionally be presented in world space by using the world_vertex_coords render mode.

Users can disable the built-in modelview transform (projection will still happen later) and do
it manually with the following code:

```
shader_type spatial;
render_mode skip_vertex_transform;

void vertex() {
    VERTEX = (MODELVIEW_MATRIX * vec4(VERTEX, 1.0)).xyz;
    NORMAL = normalize((MODELVIEW_MATRIX * vec4(NORMAL, 0.0)).xyz);
    BINORMAL = normalize((MODELVIEW_MATRIX * vec4(BINORMAL, 0.0)).xyz);
    TANGENT = normalize((MODELVIEW_MATRIX * vec4(TANGENT, 0.0)).xyz);
}
```

Other built-ins, such as UV, UV2, and COLOR, are also passed through to the fragment() function if not modified.

Users can override the modelview and projection transforms using the POSITION built-in. If POSITION is written
to anywhere in the shader, it will always be used, so the user becomes responsible for ensuring that it always has
an acceptable value. When POSITION is used, the value from VERTEX is ignored and projection does not happen.
However, the value passed to the fragment shader still comes from VERTEX.

For instancing, the INSTANCE_CUSTOM variable contains the instance custom data. When using particles, this information
is usually:

- **x**: Rotation angle in radians.

- **y**: Phase during lifetime (0.0 to 1.0).

- **z**: Animation frame.

This allows you to easily adjust the shader to a particle system using default particles material. When writing a custom particle
shader, this value can be used as desired.

Built-in | Description
-------- | -----------
in vec2**VIEWPORT_SIZE** | Size of viewport (in pixels).
in mat4**VIEW_MATRIX** | World space to view space transform.
in mat4**INV_VIEW_MATRIX** | View space to world space transform.
in mat4**MAIN_CAM_INV_VIEW_MATRIX** | View space to world space transform of camera used to
draw the current viewport.
in mat4**INV_PROJECTION_MATRIX** | Clip space to view space transform.
in vec3**NODE_POSITION_WORLD** | Node position, in world space.
in vec3**NODE_POSITION_VIEW** | Node position, in view space.
in vec3**CAMERA_POSITION_WORLD** | Camera position, in world space.
in vec3**CAMERA_DIRECTION_WORLD** | Camera direction, in world space.
in uint**CAMERA_VISIBLE_LAYERS** | Cull layers of the camera rendering the current pass.
in int**INSTANCE_ID** | Instance ID for instancing.
in vec4**INSTANCE_CUSTOM** | Instance custom data (for particles, mostly).
in int**VIEW_INDEX** | The view that we are rendering.VIEW_MONO_LEFT(0) for Mono (not multiview) or
left eye,VIEW_RIGHT(1) for right eye.
in int**VIEW_MONO_LEFT** | Constant for Mono or left eye, always0.
in int**VIEW_RIGHT** | Constant for right eye, always1.
in vec3**EYE_OFFSET** | Position offset for the eye being rendered.
Only applicable for multiview rendering.
inout vec3**VERTEX** | Position of the vertex, in model space.
In world space ifworld_vertex_coordsis used.
in int**VERTEX_ID** | The index of the current vertex in the vertex buffer.
inout vec3**NORMAL** | Normal in model space.
In world space ifworld_vertex_coordsis used.
inout vec3**TANGENT** | Tangent in model space.
In world space ifworld_vertex_coordsis used.
inout vec3**BINORMAL** | Binormal in model space.
In world space ifworld_vertex_coordsis used.
out vec4**POSITION** | If written to, overrides final vertex position in clip
space.
inout vec2**UV** | UV main channel.
inout vec2**UV2** | UV secondary channel.
inout vec4**COLOR** | Color from vertices.
out float**ROUGHNESS** | Roughness for vertex lighting.
inout float**POINT_SIZE** | Point size for point rendering.
inout mat4**MODELVIEW_MATRIX** | Model/local space to view space transform
(use if possible).
inout mat3**MODELVIEW_NORMAL_MATRIX** | 
in mat4**MODEL_MATRIX** | Model/local space to world space transform.
in mat3**MODEL_NORMAL_MATRIX** | 
inout mat4**PROJECTION_MATRIX** | View space to clip space transform.
in uvec4**BONE_INDICES** | 
in vec4**BONE_WEIGHTS** | 
in vec4**CUSTOM0** | Custom value from vertex primitive. When using extra
UVs,xyis UV3 andzwis UV4.
in vec4**CUSTOM1** | Custom value from vertex primitive. When using extra
UVs,xyis UV5 andzwis UV6.
in vec4**CUSTOM2** | Custom value from vertex primitive. When using extra
UVs,xyis UV7 andzwis UV8.
in vec4**CUSTOM3** | Custom value from vertex primitive.

> Note:
>
> MODELVIEW_MATRIX combines both the MODEL_MATRIX and VIEW_MATRIX and is better suited when floating point issues may arise. For example, if the object is very far away from the world origin, you may run into floating point issues when using the separated MODEL_MATRIX and VIEW_MATRIX.
>

> Note:
>
> INV_VIEW_MATRIX is the matrix used for rendering the object in that pass, unlike MAIN_CAM_INV_VIEW_MATRIX, which is the matrix of the camera in the scene. In the shadow pass, INV_VIEW_MATRIX's view is based on the camera that is located at the position of the light.
>

## Fragment built-ins

The default use of a Godot fragment processor function is to set up the material properties of your object
and to let the built-in renderer handle the final shading. However, you are not required to use all
these properties, and if you don't write to them, Godot will optimize away the corresponding functionality.

Built-in | Description
-------- | -----------
in vec2**VIEWPORT_SIZE** | Size of viewport (in pixels).
in vec4**FRAGCOORD** | Coordinate of pixel center in screen space.xyspecifies position in window. Origin is lower
left.zspecifies fragment depth. It is also used as the output value for the fragment depth
unlessDEPTHis written to.
in bool**FRONT_FACING** | trueif current face is front facing,falseotherwise.
in vec3**VIEW** | Normalized vector from fragment position to camera (in view space). This is the same for both
perspective and orthogonal cameras.
in vec2**UV** | UV that comes from thevertex()function.
in vec2**UV2** | UV2 that comes from thevertex()function.
in vec4**COLOR** | COLOR that comes from thevertex()function.
in vec2**POINT_COORD** | Point coordinate for drawing points withPOINT_SIZE.
in mat4**MODEL_MATRIX** | Model/local space to world space transform.
in mat3**MODEL_NORMAL_MATRIX** | Model/local space to world space transform for normals. This is the same asMODEL_MATRIXby default unless the object is scaled non-uniformly, in which case this is set totranspose(inverse(mat3(MODEL_MATRIX))).
in mat4**VIEW_MATRIX** | World space to view space transform.
in mat4**INV_VIEW_MATRIX** | View space to world space transform.
in mat4**PROJECTION_MATRIX** | View space to clip space transform.
in mat4**INV_PROJECTION_MATRIX** | Clip space to view space transform.
in vec3**NODE_POSITION_WORLD** | Node position, in world space.
in vec3**NODE_POSITION_VIEW** | Node position, in view space.
in vec3**CAMERA_POSITION_WORLD** | Camera position, in world space.
in vec3**CAMERA_DIRECTION_WORLD** | Camera direction, in world space.
in uint**CAMERA_VISIBLE_LAYERS** | Cull layers of the camera rendering the current pass.
in vec3**VERTEX** | Position of the fragment (pixel), in view space. It is theVERTEXvalue fromvertex()interpolated between the face's vertices and transformed into view space.
Ifskip_vertex_transformis enabled, it may not be in view space.
inout vec3**LIGHT_VERTEX** | A writable version ofVERTEXthat can be used to alter light and shadows. Writing to this
will not change the position of the fragment.
in int**VIEW_INDEX** | The view that we are rendering. Used to distinguish between views in multiview/stereo rendering.VIEW_MONO_LEFT(0) for Mono (not multiview) or
left eye,VIEW_RIGHT(1) for right eye.
in int**VIEW_MONO_LEFT** | Constant for Mono or left eye, always0.
in int**VIEW_RIGHT** | Constant for right eye, always1.
in vec3**EYE_OFFSET** | Position offset for the eye being rendered. Only applicable for multiview rendering.
sampler2D**SCREEN_TEXTURE** | Removed in Godot 4. Use asampler2Dwithhint_screen_textureinstead.
in vec2**SCREEN_UV** | Screen UV coordinate for current pixel.
sampler2D**DEPTH_TEXTURE** | Removed in Godot 4. Use asampler2Dwithhint_depth_textureinstead.
out float**DEPTH** | Custom depth value (range of[0.0, 1.0]). IfDEPTHis being written to in any shader
branch, then you are responsible for setting theDEPTHfor**all**other branches.
Otherwise, the graphics API will leave them uninitialized.
inout vec3**NORMAL** | Normal that comes from thevertex()function, in view space.
Ifskip_vertex_transformis enabled, it may not be in view space.
inout vec3**TANGENT** | Tangent that comes from thevertex()function, in view space.
Ifskip_vertex_transformis enabled, it may not be in view space.
inout vec3**BINORMAL** | Binormal that comes from thevertex()function, in view space.
Ifskip_vertex_transformis enabled, it may not be in view space.
out vec3**NORMAL_MAP** | Set normal here if reading normal from a texture instead ofNORMAL.
out float**NORMAL_MAP_DEPTH** | Depth fromNORMAL_MAP. Defaults to1.0.
out vec3**ALBEDO** | Albedo (default white). Base color.
out float**ALPHA** | Alpha (range of[0.0, 1.0]). If read from or written to, the material will go to the
transparent pipeline.
out float**ALPHA_SCISSOR_THRESHOLD** | If written to, values below a certain amount of alpha are discarded.
out float**ALPHA_HASH_SCALE** | Alpha hash scale when using the alpha hash transparency mode. Defaults to1.0.
Higher values result in more visible pixels in the dithering pattern.
out float**ALPHA_ANTIALIASING_EDGE** | The threshold below which alpha to coverage antialiasing should be used. Defaults to0.0.
Requires thealpha_to_coveragerender mode. Should be set to a value lower thanALPHA_SCISSOR_THRESHOLDto be effective.
out vec2**ALPHA_TEXTURE_COORDINATE** | The texture coordinate to use for alpha-to-coverge antialiasing. Requires thealpha_to_coveragerender mode. Typically set toUV * vec2(albedo_texture_size)wherealbedo_texture_sizeis the size of the albedo texture in pixels.
out float**PREMUL_ALPHA_FACTOR** | Premultiplied alpha factor. Only effective ifrender_mode blend_premul_alpha;is used.
This should be written to when using ashadedmaterial with premultiplied alpha blending for
interaction with lighting. This is not required for unshaded materials.
out float**METALLIC** | Metallic (range of[0.0, 1.0]).
out float**SPECULAR** | Specular (not physically accurate to change). Defaults to0.5.0.0disables reflections.
out float**ROUGHNESS** | Roughness (range of[0.0, 1.0]).
out float**RIM** | Rim (range of[0.0, 1.0]). If used, Godot calculates rim lighting.
Rim size depends onROUGHNESS.
out float**RIM_TINT** | Rim Tint, range of0.0(white) to1.0(albedo). If used, Godot calculates rim lighting.
out float**CLEARCOAT** | Small specular blob added on top of the existing one. If used, Godot calculates clearcoat.
out float**CLEARCOAT_GLOSS** | Gloss of clearcoat. If used, Godot calculates clearcoat.
out float**ANISOTROPY** | For distorting the specular blob according to tangent space.
out vec2**ANISOTROPY_FLOW** | Distortion direction, use with flowmaps.
out float**SSS_STRENGTH** | Strength of subsurface scattering. If used, subsurface scattering will be applied to the object.
out vec4**SSS_TRANSMITTANCE_COLOR** | Color of subsurface scattering transmittance. If used, subsurface scattering transmittance
will be applied to the object.
out float**SSS_TRANSMITTANCE_DEPTH** | Depth of subsurface scattering transmittance. Higher values allow the effect to reach deeper
into the object.
out float**SSS_TRANSMITTANCE_BOOST** | Boosts the subsurface scattering transmittance if set above0.0. This makes the effect
show up even on directly lit surfaces
inout vec3**BACKLIGHT** | Color of backlighting (works like direct light, but it's received even if the normal
is slightly facing away from the light). If used, backlighting will be applied to the object.
Can be used as a cheaper approximation of subsurface scattering.
out float**AO** | Strength of ambient occlusion. For use with pre-baked AO.
out float**AO_LIGHT_AFFECT** | How much ambient occlusion affects direct light (range of[0.0, 1.0], default0.0).
out vec3**EMISSION** | Emission color (can go over(1.0, 1.0, 1.0)for HDR).
out vec4**FOG** | If written to, blends final pixel color withFOG.rgbbased onFOG.a.
out vec4**RADIANCE** | If written to, blends environment map radiance withRADIANCE.rgbbased onRADIANCE.a.
out vec4**IRRADIANCE** | If written to, blends environment map irradiance withIRRADIANCE.rgbbased onIRRADIANCE.a.

> Note:
>
> Shaders going through the transparent pipeline when ALPHA is written to
> may exhibit transparency sorting issues. Read the
> <doc:3d_rendering_limitations#Transparency-Sorting>
> for more information and ways to avoid issues.
>

## Light built-ins

Writing light processor functions is completely optional. You can skip the light() function by using
the unshaded render mode. If no light function is written, Godot will use the material properties
written to in the fragment() function to calculate the lighting for you (subject to the render mode).

The light() function is called for every light in every pixel. It is called within a loop for each light type.

Below is an example of a custom light() function using a Lambertian lighting model:

```
void light() {
    DIFFUSE_LIGHT += clamp(dot(NORMAL, LIGHT), 0.0, 1.0) * ATTENUATION * LIGHT_COLOR / PI;
}
```

If you want the lights to add together, add the light contribution to DIFFUSE_LIGHT using +=, rather than overwriting it.

> Warning:
>
> The light() function won't be run if the vertex_lighting render mode is enabled, or if
> [Rendering > Quality > Shading > Force Vertex Shading](https://docs.godotengine.org/en/stable/classes/class_projectsettings_property_rendering/shading/overrides/force_vertex_shading.html#class-projectsettings_property_rendering/shading/overrides/force_vertex_shading)
> is enabled in the Project Settings. (It's enabled by default on mobile platforms.)
>

Built-in | Description
-------- | -----------
in vec2**VIEWPORT_SIZE** | Size of viewport (in pixels).
in vec4**FRAGCOORD** | Coordinate of pixel center in screen space.xyspecifies position in window,zspecifies fragment depth ifDEPTHis not used.
Origin is lower-left.
in mat4**MODEL_MATRIX** | Model/local space to world space transform.
in mat4**INV_VIEW_MATRIX** | View space to world space transform.
in mat4**VIEW_MATRIX** | World space to view space transform.
in mat4**PROJECTION_MATRIX** | View space to clip space transform.
in mat4**INV_PROJECTION_MATRIX** | Clip space to view space transform.
in vec3**NORMAL** | Normal vector, in view space.
in vec2**SCREEN_UV** | Screen UV coordinate for current pixel.
in vec2**UV** | UV that comes from thevertex()function.
in vec2**UV2** | UV2 that comes from thevertex()function.
in vec3**VIEW** | View vector, in view space.
in vec3**LIGHT** | Light vector, in view space.
in vec3**LIGHT_COLOR** | [Light color](https://docs.godotengine.org/en/stable/classes/class_light3d_property_light_color.html#class-light3d_property_light_color) multiplied by
[light energy](https://docs.godotengine.org/en/stable/classes/class_light3d_property_light_energy.html#class-light3d_property_light_energy) multiplied byPI. ThePImultiplication is present because
physically-based lighting models include a division byPI.
in float**SPECULAR_AMOUNT** | For [OmniLight3D](https://docs.godotengine.org/en/stable/classes/class_omnilight3d.html#class-omnilight3d) and [SpotLight3D](https://docs.godotengine.org/en/stable/classes/class_spotlight3d.html#class-spotlight3d),2.0multiplied by
[light_specular](https://docs.godotengine.org/en/stable/classes/class_light3d_property_light_specular.html#class-light3d_property_light_specular).
For [DirectionalLight3D](https://docs.godotengine.org/en/stable/classes/class_directionallight3d.html#class-directionallight3d),1.0.
in bool**LIGHT_IS_DIRECTIONAL** | trueif this pass is a [DirectionalLight3D](https://docs.godotengine.org/en/stable/classes/class_directionallight3d.html#class-directionallight3d).
in float**ATTENUATION** | Attenuation based on distance or shadow.
in vec3**ALBEDO** | Base albedo.
in vec3**BACKLIGHT** | 
in float**METALLIC** | Metallic.
in float**ROUGHNESS** | Roughness.
out vec3**DIFFUSE_LIGHT** | Diffuse light result.
out vec3**SPECULAR_LIGHT** | Specular light result.
out float**ALPHA** | Alpha (range of[0.0, 1.0]). If written to, the material will go
to the transparent pipeline.

> Note:
>
> Shaders going through the transparent pipeline when ALPHA is written to
> may exhibit transparency sorting issues. Read the
> <doc:3d_rendering_limitations#Transparency-Sorting>
> for more information and ways to avoid issues.
>
> Transparent materials also cannot cast shadows or appear in
> hint_screen_texture and hint_depth_texture uniforms. This in turn prevents those
> materials from appearing in screen-space reflections or refraction.
> <doc:using_sdfgi> sharp reflections are not visible on transparent
> materials (only rough reflections are visible on transparent materials).