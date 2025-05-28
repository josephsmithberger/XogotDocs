<!-- Remove this line to publish to docs.xogot.com -->
# Using the ArrayMesh

This tutorial will present the basics of using an [ArrayMesh](https://docs.godotengine.org/en/stable/classes/class_arraymesh.html#class-arraymesh).

To do so, we will use the function [add_surface_from_arrays()](https://docs.godotengine.org/en/stable/classes/class_arraymesh_method_add_surface_from_arrays.html#class-arraymesh_method_add_surface_from_arrays),
which takes up to five parameters. The first two are required, while the last three are optional.

The first parameter is the PrimitiveType, an OpenGL concept that instructs the GPU
how to arrange the primitive based on the vertices given, i.e. whether they represent triangles,
lines, points, etc. See :ref:`Mesh.PrimitiveType <enum_Mesh_PrimitiveType>` for the options available.

The second parameter, arrays, is the actual Array that stores the mesh information. The array is a normal Godot array that
is constructed with empty brackets []. It stores a Packed**Array (e.g. PackedVector3Array,
PackedInt32Array, etc.) for each type of information that will be used to build the surface.

Common elements of arrays are listed below, together with the position they must have within arrays.
See :ref:`Mesh.ArrayType <enum_Mesh_ArrayType>` for a full list.

Index | Mesh.ArrayType Enum | Array type
----- | ------------------- | ----------
0 | ARRAY_VERTEX | [PackedVector3Array](https://docs.godotengine.org/en/stable/classes/class_packedvector3array.html#class-packedvector3array) or [PackedVector2Array](https://docs.godotengine.org/en/stable/classes/class_packedvector2array.html#class-packedvector2array)
1 | ARRAY_NORMAL | [PackedVector3Array](https://docs.godotengine.org/en/stable/classes/class_packedvector3array.html#class-packedvector3array)
2 | ARRAY_TANGENT | [PackedFloat32Array](https://docs.godotengine.org/en/stable/classes/class_packedfloat32array.html#class-packedfloat32array) or [PackedFloat64Array](https://docs.godotengine.org/en/stable/classes/class_packedfloat64array.html#class-packedfloat64array) of groups of 4 floats. The first 3 floats determine the tangent, and the last float the binormal
direction as -1 or 1.
3 | ARRAY_COLOR | [PackedColorArray](https://docs.godotengine.org/en/stable/classes/class_packedcolorarray.html#class-packedcolorarray)
4 | ARRAY_TEX_UV | [PackedVector2Array](https://docs.godotengine.org/en/stable/classes/class_packedvector2array.html#class-packedvector2array) or [PackedVector3Array](https://docs.godotengine.org/en/stable/classes/class_packedvector3array.html#class-packedvector3array)
5 | ARRAY_TEX_UV2 | [PackedVector2Array](https://docs.godotengine.org/en/stable/classes/class_packedvector2array.html#class-packedvector2array) or [PackedVector3Array](https://docs.godotengine.org/en/stable/classes/class_packedvector3array.html#class-packedvector3array)
10 | ARRAY_BONES | [PackedFloat32Array](https://docs.godotengine.org/en/stable/classes/class_packedfloat32array.html#class-packedfloat32array) of groups of 4 floats or [PackedInt32Array](https://docs.godotengine.org/en/stable/classes/class_packedint32array.html#class-packedint32array) of groups of 4 ints. Each group lists indexes of 4 bones that affects a given vertex.
11 | ARRAY_WEIGHTS | [PackedFloat32Array](https://docs.godotengine.org/en/stable/classes/class_packedfloat32array.html#class-packedfloat32array) or [PackedFloat64Array](https://docs.godotengine.org/en/stable/classes/class_packedfloat64array.html#class-packedfloat64array) of groups of 4 floats. Each float lists the amount of weight the corresponding bone inARRAY_BONEShas on a given vertex.
12 | ARRAY_INDEX | [PackedInt32Array](https://docs.godotengine.org/en/stable/classes/class_packedint32array.html#class-packedint32array)

In most cases when creating a mesh, we define it by its vertex positions. So usually, the array of vertices (at index 0) is required, while the index array (at index 12) is optional and
will only be used if included. It is also possible to create a mesh with only the index array and no vertex array, but that's beyond the scope of this tutorial.

All the other arrays carry information about the vertices. They are optional and will only be used if included. Some of these arrays (e.g. ARRAY_COLOR)
use one entry per vertex to provide extra information about vertices. They must have the same size as the vertex array. Other arrays (e.g. ARRAY_TANGENT) use
four entries to describe a single vertex. These must be exactly four times larger than the vertex array.

For normal usage, the last three parameters in [add_surface_from_arrays()](https://docs.godotengine.org/en/stable/classes/class_arraymesh_method_add_surface_from_arrays.html#class-arraymesh_method_add_surface_from_arrays) are typically left empty.

## Setting up the ArrayMesh

In the editor, create a [MeshInstance3D](https://docs.godotengine.org/en/stable/classes/class_meshinstance3d.html#class-meshinstance3d) and add an [ArrayMesh](https://docs.godotengine.org/en/stable/classes/class_arraymesh.html#class-arraymesh) to it in the Inspector.
Normally, adding an ArrayMesh in the editor is not useful, but in this case it allows us to access the ArrayMesh
from code without creating one.

Next, add a script to the MeshInstance3D.

Under _ready(), create a new Array.

This will be the array that we keep our surface information in - it will hold
all the arrays of data that the surface needs. Godot will expect it to be of
size Mesh.ARRAY_MAX, so resize it accordingly.

Next create the arrays for each data type you will use.

Once you have filled your data arrays with your geometry you can create a mesh
by adding each array to surface_array and then committing to the mesh.

> Note: In this example, we used Mesh.PRIMITIVE_TRIANGLES, but you can use any primitive type
> available from mesh.
>

Put together, the full code looks like:

The code that goes in the middle can be whatever you want. Below we will present some
example code for generating a sphere.

## Generating geometry

Here is sample code for generating a sphere. Although the code is presented in
GDScript, there is nothing Godot specific about the approach to generating it.
This implementation has nothing in particular to do with ArrayMeshes and is just a
generic approach to generating a sphere. If you are having trouble understanding it
or want to learn more about procedural geometry in general, you can use any tutorial
that you find online.

## Saving

Finally, we can use the [ResourceSaver](https://docs.godotengine.org/en/stable/classes/class_resourcesaver.html#class-resourcesaver) class to save the ArrayMesh.
This is useful when you want to generate a mesh and then use it later without having to re-generate it.