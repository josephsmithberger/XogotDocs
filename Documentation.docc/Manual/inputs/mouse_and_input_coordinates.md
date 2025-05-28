<!-- Remove this line to publish to docs.xogot.com -->
# Mouse and input coordinates

## About

The reason for this small tutorial is to clear up many common mistakes
about input coordinates, obtaining mouse position and screen resolution,
etc.

## Hardware display coordinates

Using hardware coordinates makes sense in the case of writing complex
UIs meant to run on PC, such as editors, MMOs, tools, etc. However, it does
not make as much sense outside of that scope.

## Viewport display coordinates

Godot uses viewports to display content, and viewports can be scaled by
several options (see <doc:multiple_resolutions> tutorial). Use, then, the
functions in nodes to obtain the mouse coordinates and viewport size,
for example:

Alternatively, it's possible to ask the viewport for the mouse position:

> Note: When the mouse mode is set to Input.MOUSE_MODE_CAPTURED, the event.position value from InputEventMouseMotion is the center of the screen. Use event.relative instead of event.position and event.velocity to process mouse movement and position changes.