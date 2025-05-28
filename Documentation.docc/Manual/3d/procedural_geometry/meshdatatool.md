<!-- Remove this line to publish to docs.xogot.com -->
# Using the MeshDataTool

The [MeshDataTool](https://docs.godotengine.org/en/stable/classes/class_meshdatatool.html#class-meshdatatool) is not used to generate geometry. But it is helpful for dynamically altering geometry, for example
if you want to write a script to tessellate, simplify, or deform meshes.

The MeshDataTool is not as fast as altering arrays directly using ArrayMesh. However, it provides more information
and tools to work with meshes than the ArrayMesh does. When the MeshDataTool
is used, it calculates mesh data that is not available in ArrayMeshes such as faces and edges, which are necessary
for certain mesh algorithms. If you do not need this extra information then it may be better to use an ArrayMesh.

> Note: MeshDataTool can only be used on Meshes that use the PrimitiveType Mesh.PRIMITIVE_TRIANGLES.
>

We initialize the MeshDataTool from an ArrayMesh by calling create_from_surface(). If there is already data initialized in the MeshDataTool,
calling create_from_surface() will clear it for you. Alternatively, you can call clear() yourself before re-using the MeshDataTool.

In the examples below, assume an ArrayMesh called mesh has already been created. See <doc:arraymesh> for an example of mesh generation.

create_from_surface() uses the vertex arrays from the ArrayMesh to calculate two additional arrays,
one for edges and one for faces, for a total of three arrays.

An edge is a connection between any two vertices. Each edge in the edge array contains a reference to
the two vertices it is composed of, and up to two faces that it is contained within.

A face is a triangle made up of three vertices and three corresponding edges. Each face in the face array contains
a reference to the three vertices and three edges it is composed of.

The vertex array contains edge, face, normal, color, tangent, uv, uv2, bone, and weight information connected
with each vertex.

To access information from these arrays you use a function of the form get_****():

What you choose to do with these functions is up to you. A common use case is to iterate over all vertices
and transform them in some way:

These modifications are not done in place on the ArrayMesh. If you are dynamically updating an existing ArrayMesh,
first delete the existing surface before adding a new one using [commit_to_surface()](https://docs.godotengine.org/en/stable/classes/class_meshdatatool_method_commit_to_surface.html#class-meshdatatool_method_commit_to_surface):

Below is a complete example that turns a spherical mesh called mesh into a randomly deformed blob complete with updated normals and vertex colors.
See <doc:arraymesh> for how to generate the base mesh.