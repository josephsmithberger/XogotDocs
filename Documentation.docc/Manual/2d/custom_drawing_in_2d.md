<!-- Remove this line to publish to docs.xogot.com -->
# Custom drawing in 2D

## Introduction

Godot has nodes to draw sprites, polygons, particles, text, and many other
common game development needs. However, if you need something specific
not covered with the standard nodes you can make any 2D node (for example,
[Control](https://docs.godotengine.org/en/stable/classes/class_control.html#class-control) or [Node2D](https://docs.godotengine.org/en/stable/classes/class_node2d.html#class-node2d)-based)
draw on screen using custom commands.

Custom drawing in a 2D node is really useful. Here are some use cases:

- Drawing shapes or logic that existing nodes can't do, such as an image
with trails or a special animated polygon.

- Drawing a large number of simple objects, such as a grid or a board
for a 2d game. Custom drawing avoids the overhead of using a large number
of nodes, possibly lowering memory usage and improving performance.

- Making a custom UI control. There are plenty of controls available,
but when you have unusual needs, you will likely need a custom
control.

## Drawing

Add a script to any [CanvasItem](https://docs.godotengine.org/en/stable/classes/class_canvasitem.html#class-canvasitem)
derived node, like [Control](https://docs.godotengine.org/en/stable/classes/class_control.html#class-control) or
[Node2D](https://docs.godotengine.org/en/stable/classes/class_node2d.html#class-node2d). Then override the
[_draw()](https://docs.godotengine.org/en/stable/classes/class_canvasitem_private_method__draw.html#class-canvasitem_private_method__draw) function.

Draw commands are described in the [CanvasItem](https://docs.godotengine.org/en/stable/classes/class_canvasitem.html#class-canvasitem)
class reference. There are plenty of them and we will see some of them
in the examples below.

## Updating

The [_draw](https://docs.godotengine.org/en/stable/classes/class_canvasitem_private_method__draw.html#class-canvasitem_private_method__draw) function is only called
once, and then the draw commands are cached and remembered, so further calls
are unnecessary.

If re-drawing is required because a variable or something else changed,
call [CanvasItem.queue_redraw](https://docs.godotengine.org/en/stable/classes/class_canvasitem_method_queue_redraw.html#class-canvasitem_method_queue_redraw)
in that same node and a new _draw() call will happen.

Here is a little more complex example, where we have a texture variable
that can be modified at any time, and using a
<doc:index#Basics-Setters-Getters>, it forces a redraw
of the texture when modified:

To see it in action, you can set the texture to be the Godot icon on the
editor by dragging and dropping the default icon.svg from the
FileSystem tab to the Texture property on the Inspector tab.
When changing the Texture property value while the previous script is
running, the texture will also change automatically.

In some cases, we may need to redraw every frame. For this,
call [queue_redraw](https://docs.godotengine.org/en/stable/classes/class_canvasitem_method_queue_redraw.html#class-canvasitem_method_queue_redraw)
from the [_process](https://docs.godotengine.org/en/stable/classes/class_node_private_method__process.html#class-node_private_method__process) method, like this:

## Coordinates and line width alignment

The drawing API uses the CanvasItem's coordinate system, not necessarily pixel
coordinates. This means _draw() uses the coordinate space created after
applying the CanvasItem's transform. Additionally, you can apply a custom
transform on top of it by using
[draw_set_transform](https://docs.godotengine.org/en/stable/classes/class_canvasitem_method_draw_set_transform.html#class-canvasitem_method_draw_set_transform) or
[draw_set_transform_matrix](https://docs.godotengine.org/en/stable/classes/class_canvasitem_method_draw_set_transform_matrix.html#class-canvasitem_method_draw_set_transform_matrix).

When using [draw_line](https://docs.godotengine.org/en/stable/classes/class_canvasitem_method_draw_line.html#class-canvasitem_method_draw_line), you should
consider the width of the line. When using a width that is an odd size, the
position of the start and end points should be shifted by 0.5 to keep the
line centered, as shown below.

@Image(source: "draw_line.png")

The same applies to the [draw_rect](https://docs.godotengine.org/en/stable/classes/class_canvasitem_method_draw_rect.html#class-canvasitem_method_draw_rect)
method with filled = false.

@Image(source: "draw_rect.png")

## Antialiased drawing

Godot offers method parameters in [draw_line](https://docs.godotengine.org/en/stable/classes/class_canvasitem_method_draw_line.html#class-canvasitem_method_draw_line)
to enable antialiasing, but not all custom drawing methods offer this antialiased
parameter.

For custom drawing methods that don't provide an antialiased parameter,
you can enable 2D MSAA instead, which affects rendering in the entire viewport.
This provides high-quality antialiasing, but a higher performance cost and only
on specific elements. See <doc:2d_antialiasing> for more information.

Here is a comparison of a line of minimal width (width=-1) drawn with
antialiased=false, antialiased=true, and antialiased=false with
2D MSAA 2x, 4x, and 8x enabled.

@Image(source: "draw_antialiasing_options.png")

## Tools

Drawing your own nodes might also be desired while running them in the
editor. This can be used as a preview or visualization of some feature or
behavior.

To do this, you can use the <doc:index#Tool-Mode>
on both GDScript and C#. See
<doc:draw_show_drawing_while_editing_example> and
<doc:running_code_in_the_editor> for more information.

## Example 1: drawing a custom shape

We will now use the custom drawing functionality of the Godot Engine to draw
something that Godot doesn't provide functions for. We will recreate the Godot
logo but with code- only using drawing functions.

You will have to code a function to perform this and draw it yourself.

> Note:
>
> The following instructions use a fixed set of coordinates that could be too small
> for high resolution screens (larger than 1080p). If that is your case, and the
> drawing is too small consider increasing your window scale in the project setting
> [Display > Window > Stretch > Scale](https://docs.godotengine.org/en/stable/classes/class_projectsettings_property_display/window/stretch/scale.html#class-projectsettings_property_display/window/stretch/scale)
> to adjust the project to a higher resolution (a 2 or 4 scale tends to work well).
>

### Drawing a custom polygon shape

While there is a dedicated node to draw custom polygons (
[Polygon2D](https://docs.godotengine.org/en/stable/classes/class_polygon2d.html#class-polygon2d)), we will use in this case exclusively lower
level drawing functions to combine them on the same node and be able to create
more complex shapes later on.

First, we will define a set of points -or X and Y coordinates- that will form
the base of our shape:

This format, while compact, is not the one that Godot understands to
draw a polygon. In a different scenario we could have to load
these coordinates from a file or calculate the positions while the
application is running, so some transformation may be needed.

To transform these coordinates into the right format, we will create a new
method float_array_to_Vector2Array(). Then we will override the _ready()
function, which Godot will call only once -at the start of the execution-
to load those coordinates into a variable:

To finally draw our first shape, we will use the method
[draw_polygon](https://docs.godotengine.org/en/stable/classes/class_canvasitem_method_draw_polygon.html#class-canvasitem_method_draw_polygon)
and pass the points (as an array of Vector2 coordinates) and its color,
like this:

When running it you should see something like this:

@Image(source: "draw_godot_logo_polygon.png")

Note the lower part of the logo looks segmented- this is because a low
amount of points were used to define that part. To simulate a smooth curve,
we could add more points to our array, or maybe use a mathematical function to
interpolate a curve and create a smooth shape from code (see
<doc:draw_custom_example_2>).

Polygons will always **connect its last defined point to its first
one** in order to have a closed shape.

### Drawing connected lines

Drawing a sequence of connected lines that don't close down to form a polygon
is very similar to the previous method. We will use a connected set of lines to
draw Godot's logo mouth.

First, we will define the list of coordinates that form the mouth shape, like this:

We will load these coordinates into a variable and define an additional
variable with the configurable line thickness:

And finally we will use the method
[draw_polyline](https://docs.godotengine.org/en/stable/classes/class_canvasitem_method_draw_polyline.html#class-canvasitem_method_draw_polyline) to actually
draw the line, like this:

You should get the following output:

@Image(source: "draw_godot_logo_polyline.png")

Unlike draw_polygon(), polylines can only have a single unique color
for all its points (the second argument). This method has 2 additional
arguments: the width of the line (which is as small as possible by default)
and enabling or disabling the antialiasing (it is disabled by default).

The order of the _draw calls is important- like with the Node positions on
the tree hierarchy, the different shapes will be drawn from top to bottom,
resulting in the latest shapes hiding earlier ones if they overlap. In this
case we want the mouth drawn over the head, so we put it afterwards.

Notice how we can define colors in different ways, either with a hexadecimal
code or a predefined color name. Check the class [Color](https://docs.godotengine.org/en/stable/classes/class_color.html#class-color) for other
constants and ways to define Colors.

### Drawing circles

To create the eyes, we are going to add 4 additional calls to draw the eye
shapes, in different sizes, colors and positions.

To draw a circle, you position it based on its center using the
[draw_circle](https://docs.godotengine.org/en/stable/classes/class_canvasitem_method_draw_circle.html#class-canvasitem_method_draw_circle) method. The first
parameter is a [Vector2](https://docs.godotengine.org/en/stable/classes/class_vector2.html#class-vector2) with the coordinates of its center, the second is
its radius, and the third is its color:

When executing it, you should have something like this:

@Image(source: "draw_godot_logo_circle.png")

For partial, unfilled arcs (portions of a circle shape between certain
arbitrary angles), you can use the method
[draw_arc](https://docs.godotengine.org/en/stable/classes/class_canvasitem_method_draw_arc.html#class-canvasitem_method_draw_arc).

### Drawing lines

To draw the final shape (the nose) we will use a line to approximate it.

[draw_line](https://docs.godotengine.org/en/stable/classes/class_canvasitem_method_draw_line.html#class-canvasitem_method_draw_line) can be used to draw
a single segment by providing its start and end coordinates as arguments,
like this:

You should now be able to see the following shape on screen:

@Image(source: "draw_godot_logo_line.png")

Note that if multiple unconnected lines are going to be drawn at the same time,
you may get additional performance by drawing all of them in a single call, using
the [draw_multiline](https://docs.godotengine.org/en/stable/classes/class_canvasitem_method_draw_multiline.html#class-canvasitem_method_draw_multiline) method.

### Drawing text

While using the [Label](https://docs.godotengine.org/en/stable/classes/class_label.html#class-label) Node is the most common way to add
text to your application, the low-level `_draw` function includes functionality
to add text to your custom Node drawing. We will use it to add the name "GODOT"
under the robot head.

We will use the [draw_string](https://docs.godotengine.org/en/stable/classes/class_canvasitem_method_draw_string.html#class-canvasitem_method_draw_string) method
to do it, like this:

Here we first load into the defaultFont variable the configured default theme
font (a custom one can be set instead) and then we pass the following
parameters: font, position, text, horizontal alignment, width, and font size.

You should see the following on your screen:

@Image(source: "draw_godot_logo_text.png")

Additional parameters as well as other methods related to text and characters
can be found on the [CanvasItem](https://docs.godotengine.org/en/stable/classes/class_canvasitem.html#class-canvasitem) class reference.

### Show the drawing while editing

While the code so far is able to draw the logo on a running window, it will
not show up on the 2D view on the editor. In certain cases you would
also like to show your custom Node2D or control on the editor, to position
and scale it appropriately, like most other nodes do.

To show the logo directly on the editor (without running it), you can use the
<doc:index#Tool-Mode> annotation to request the custom drawing
of the node to also appear while editing, like this:

You will need to save your scene, rebuild your project (for C# only) and reload
the current scene manually at the menu option Scene > Reload Saved Scene
to refresh the current node in the 2D view the first time you add or remove
the @tool annotation.

### Animation

If we wanted to make the custom shape change at runtime, we could modify the
methods called or its arguments at execution time, or apply a transform.

For example, if we want the custom shape we just designed to rotate, we could add
the following variable and code to the _ready and _process methods:

The problem with the above code is that because we have created the points
approximately on a rectangle starting from the upper left corner, the (0, 0)
coordinate and extending to the right and down, we see that the rotation is done
using the top left corner as pivot. A position transform change on the node
won't help us here, as the rotation transform is applied first.

While we could rewrite all of the points' coordinates to be centered around
(0, 0), including negative coordinates, that would be a lot of work.

One possible way to work around this is to use the lower level
[draw_set_transform](https://docs.godotengine.org/en/stable/classes/class_canvasitem_method_draw_set_transform.html#class-canvasitem_method_draw_set_transform)
method to fix this issue, translating all points in the CanvasItem's own space,
and then moving it back to its original place with a regular node transform,
either in the editor or in code, like this:

This is the result, rotating around a pivot now on (60, 60):

@Image(source: "draw_godot_rotation.png")

If what we wanted to animate was a property inside the _draw() call, we must remember to
call queue_redraw() to force a refresh, as otherwise it would not be updated on screen.

For example, this is how we can make the robot appear to open and close its mouth, by
changing the width of its mouth line follow a sinusoidal ([sin](https://docs.godotengine.org/en/stable/classes/class_@globalscope_method_sin.html#class-@globalscope_method_sin)) curve:

It will look somewhat like this when run:

@Image(source: "draw_godot_mouth_animation.png")

Please note that _mouth_width is a user defined property like any other
and it or any other used as a drawing argument can be animated using more
standard and high-level methods such as a [Tween](https://docs.godotengine.org/en/stable/classes/class_tween.html#class-tween) or an
[AnimationPlayer](https://docs.godotengine.org/en/stable/classes/class_animationplayer.html#class-animationplayer) Node. The only difference is
that a queue_redraw() call is needed to apply those changes so they get
shown on screen.

## Example 2: drawing a dynamic line

The previous example was useful to learn how to draw and modify nodes with
custom shapes and animations. This could have some advantages, such as using
exact coordinates and vectors for drawing, rather than bitmaps -which means
they will scale well when transformed on screen. In some cases, similar results
could be achieved composing higher level functionality with nodes such as
[sprites](https://docs.godotengine.org/en/stable/classes/class_sprite2d.html#class-sprite2d) or
[AnimatedSprites](https://docs.godotengine.org/en/stable/classes/class_animatedsprite2d.html#class-animatedsprite2d) loading SVG resources (which are
also images defined with vectors) and the
[AnimationPlayer](https://docs.godotengine.org/en/stable/classes/class_animationplayer.html#class-animationplayer) node.

In other cases that will not be possible because we will not know what the
resulting graphical representation will be before running the code. Here we
will see how to draw a dynamic line whose coordinates are not known beforehand,
and are affected by the user's input.

### Drawing a straight line between 2 points

Let's assume we want to draw a straight line between 2 points, the first one
will be fixed on the upper left corner (0, 0) and the second will be defined
by the cursor position on screen.

We could draw a dynamic line between those 2 points like this:

In this example we obtain the position of the mouse in the default viewport
every frame with the method
[get_mouse_position](https://docs.godotengine.org/en/stable/classes/class_viewport_method_get_mouse_position.html#class-viewport_method_get_mouse_position). If the
position has changed since the last draw request (a small optimization to
avoid redrawing on every frame)- we will schedule a redraw. Our _draw()
method only has one line: requesting the drawing of a green line of
width 10 pixels between the top left corner and that obtained position.

The width, color, and position of the starting point can be configured with
with the corresponding properties.

It should look like this when run:

@Image(source: "draw_line_between_2_points.png")

### Drawing an arc between 2 points

The above example works, but we may want to join those 2 points with a
different shape or function, other than a straight line.

Let's try now creating an arc (a portion of a circumference) between
both points.

Exporting the line starting point, segments, width, color, and antialiasing will
allow us to modify those properties very easily directly from the editor
inspector panel:

@Image(source: "draw_dynamic_exported_properties.png")

To draw the arc, we can use the method
[draw_arc](https://docs.godotengine.org/en/stable/classes/class_canvasitem_method_draw_arc.html#class-canvasitem_method_draw_arc). There are many
arcs that pass through 2 points, so we will chose for this example
the semicircle that has its center in the middle point between the 2 initial
points.

Calculating this arc will be more complex than in the case of the line:

The center of the semicircle will be the middle point between both points.
The radius will be half the distance between both points.
The start and end angles will be the angles of the vector from point1
to point2 and vice-versa.
Note we had to normalize the end_angle in positive values because if
end_angle is less than start_angle, the arc will be drawn
counter-clockwise, which we don't want in this case (the arc would be
upside-down).

The result should be something like this, with the arc going down and
between the points:

@Image(source: "draw_arc_between_2_points.png")

Feel free to play with the parameters in the inspector to obtain different
results: change the color, the width, the antialiasing, and increase the
number of segments to increase the curve smoothness, at the cost of extra
performance.