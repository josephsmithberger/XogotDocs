<!-- Remove this line to publish to docs.xogot.com -->
# When and how to avoid using nodes for everything

Nodes are cheap to produce, but even they have their limits. A project may
have tens of thousands of nodes all doing things. The more complex their
behavior though, the larger the strain each one adds to a project's
performance.

Godot provides more lightweight objects for creating APIs which nodes use.
Be sure to keep these in mind as options when designing how you wish to build
your project's features.

1. [Object](https://docs.godotengine.org/en/stable/classes/class_object.html#class-object): The ultimate lightweight object, the original
Object must use manual memory management. With that said, it isn't too
difficult to create one's own custom data structures, even node structures,
that are also lighter than the [Node](https://docs.godotengine.org/en/stable/classes/class_node.html#class-node) class.

**Example:** See the [Tree](https://docs.godotengine.org/en/stable/classes/class_tree.html#class-tree) node. It supports a high level
of customization for a table of content with an arbitrary number of
rows and columns. The data that it uses to generate its visualization
though is actually a tree of [TreeItem](https://docs.godotengine.org/en/stable/classes/class_treeitem.html#class-treeitem) Objects.
**Advantages:** Simplifying one's API to smaller scoped objects helps improve
its accessibility and improve iteration time. Rather than working with the
entire Node library, one creates an abbreviated set of Objects from which
a node can generate and manage the appropriate sub-nodes.



1. **Example:** See the [Tree](https://docs.godotengine.org/en/stable/classes/class_tree.html#class-tree) node. It supports a high level
of customization for a table of content with an arbitrary number of
rows and columns. The data that it uses to generate its visualization
though is actually a tree of [TreeItem](https://docs.godotengine.org/en/stable/classes/class_treeitem.html#class-treeitem) Objects.

1. **Advantages:** Simplifying one's API to smaller scoped objects helps improve
its accessibility and improve iteration time. Rather than working with the
entire Node library, one creates an abbreviated set of Objects from which
a node can generate and manage the appropriate sub-nodes.

- **Example:** See the [Tree](https://docs.godotengine.org/en/stable/classes/class_tree.html#class-tree) node. It supports a high level
of customization for a table of content with an arbitrary number of
rows and columns. The data that it uses to generate its visualization
though is actually a tree of [TreeItem](https://docs.godotengine.org/en/stable/classes/class_treeitem.html#class-treeitem) Objects.

- **Advantages:** Simplifying one's API to smaller scoped objects helps improve
its accessibility and improve iteration time. Rather than working with the
entire Node library, one creates an abbreviated set of Objects from which
a node can generate and manage the appropriate sub-nodes.

> Note:
>
> One should be careful when handling them. One can store an Object
> into a variable, but these references can become invalid without warning.
> For example, if the object's creator decides to delete it out of nowhere,
> this would trigger an error state when one next accesses it.
>

1. [RefCounted](https://docs.godotengine.org/en/stable/classes/class_refcounted.html#class-refcounted): Only a little more complex than Object.
They track references to themselves, only deleting loaded memory when no
further references to themselves exist. These are useful in the majority of
cases where one needs data in a custom class.

**Example:** See the [FileAccess](https://docs.godotengine.org/en/stable/classes/class_fileaccess.html#class-fileaccess) object. It functions
just like a regular Object except that one need not delete it themselves.
**Advantages:** same as the Object.



1. **Example:** See the [FileAccess](https://docs.godotengine.org/en/stable/classes/class_fileaccess.html#class-fileaccess) object. It functions
just like a regular Object except that one need not delete it themselves.

1. **Advantages:** same as the Object.

1. [Resource](https://docs.godotengine.org/en/stable/classes/class_resource.html#class-resource): Only slightly more complex than RefCounted.
They have the innate ability to serialize/deserialize (i.e. save and load)
their object properties to/from Godot resource files.

**Example:** Scripts, PackedScene (for scene files), and other types like
each of the [AudioEffect](https://docs.godotengine.org/en/stable/classes/class_audioeffect.html#class-audioeffect) classes. Each of these
can be saved and loaded, therefore they extend from Resource.
**Advantages:** Much has
<doc:resources>
on [Resource](https://docs.godotengine.org/en/stable/classes/class_resource.html#class-resource)'s advantages over traditional data
storage methods. In the context of using Resources over Nodes though,
their main advantage is in Inspector-compatibility. While nearly as
lightweight as Object/RefCounted, they can still display and export
properties in the Inspector. This allows them to fulfill a purpose much
like sub-Nodes on the usability front, but also improve performance if
one plans to have many such Resources/Nodes in their scenes.



1. **Example:** Scripts, PackedScene (for scene files), and other types like
each of the [AudioEffect](https://docs.godotengine.org/en/stable/classes/class_audioeffect.html#class-audioeffect) classes. Each of these
can be saved and loaded, therefore they extend from Resource.

1. **Advantages:** Much has
<doc:resources>
on [Resource](https://docs.godotengine.org/en/stable/classes/class_resource.html#class-resource)'s advantages over traditional data
storage methods. In the context of using Resources over Nodes though,
their main advantage is in Inspector-compatibility. While nearly as
lightweight as Object/RefCounted, they can still display and export
properties in the Inspector. This allows them to fulfill a purpose much
like sub-Nodes on the usability front, but also improve performance if
one plans to have many such Resources/Nodes in their scenes.

- **Example:** See the [FileAccess](https://docs.godotengine.org/en/stable/classes/class_fileaccess.html#class-fileaccess) object. It functions
just like a regular Object except that one need not delete it themselves.

- **Advantages:** same as the Object.

- **Example:** Scripts, PackedScene (for scene files), and other types like
each of the [AudioEffect](https://docs.godotengine.org/en/stable/classes/class_audioeffect.html#class-audioeffect) classes. Each of these
can be saved and loaded, therefore they extend from Resource.

- **Advantages:** Much has
<doc:resources>
on [Resource](https://docs.godotengine.org/en/stable/classes/class_resource.html#class-resource)'s advantages over traditional data
storage methods. In the context of using Resources over Nodes though,
their main advantage is in Inspector-compatibility. While nearly as
lightweight as Object/RefCounted, they can still display and export
properties in the Inspector. This allows them to fulfill a purpose much
like sub-Nodes on the usability front, but also improve performance if
one plans to have many such Resources/Nodes in their scenes.