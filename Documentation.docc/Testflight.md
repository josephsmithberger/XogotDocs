# Xogot: Godot on iPad

Thank you for your interest in testing Godot for iPad, this small guide will explain how to get the most of out this TestFlight release.

Xogot layers an iOS-native user experience on top of the existing Godot Editor
engine, so your projects should be fully compatible with the desktop edition of
Godot, and you should be able to move projects back and forth the two platforms.

One of our principles was to surface all the capabilities that you would need
for full interoperability in your project, so everything that you need should be
there, if it is missing, it should be considered a defect.   But it also means
that we took liberties to simplify the user interface when it comes to the Godot
editor itself, we only surface a handful of configuration options on purpose,
but we are open to bringing back a handful of those. 

# Desired Feedback

We really want to hear your feedback, you can give us feedback in any of these
ways:

- Taking a screenshot of the issue, and then selecting "Send Feedback" from the
  "Done" drop down button.
- Sending us an email to support@xibbon.com
- Filing an issue on
  [github.com/xibbon/XogotIssues](https://github.com/xibbon/XogotIssues).

- Bugs in Xogot: we are interested in finding bugs, crashes or unexpected
  behaviors in the application.   If you find a bug, we would love if you could
  describe how you triggered it, so we can fix it.
    
- Poor User Experience: while we worked hard to make sure that we provide a good
  user experience for iPad users, we have also gotten used to it, and we want to
  find out what things do not work as expected, are confusing or could be
  improved.   We are interested in improving the user experience for iPad users,
  both by ensuring that the UI works well on the iPad and its various input
  systems as well as living up to the expectations of users on iPadOS.


- Improving over Godot’s defaults.   We think that we have a unique opportunity
  to improve the workflow of using Godot that go beyond the surface [1].  Some
  of the design choices and default choices from Godot make sense for
  professionals using a desktop computer, but those are not necessarily great
  for mobile users, we would love to hear what you think could be improved
  overall to make your journey more pleasant. 


- Missed opportunities: we prioritized what we thought were the high-traffic
  areas of the user interface, but we might have missed some.   Let us know if
  there are areas of the user interface that you are using extensively and you
  would prefer a native user experience to be provided. 

We expose a new user interface for high-traffic parts of the application, and
fallback to the Godot-based UI when a piece of the UI has not been rewritten.

# Known Limitations

The most visible limitation currently is that the progress indicators in the UI
are not shown, which can be a little jarring when importing a large new project
and Xogot not responding.   This fix will be coming soon.


## Renderer
- Xogot is based on Godot 4.3-based: and it imposes a few limitations when it
  comes to the renderers when running on device (Forward+, Forward Mobile work,
  but OpenGL in this release is not working).   You might need to adjust your
  settings for your game to fully work on iPad.   For the final release, we will
  be switching to a Godot-4.4-based system which will support all three modes.

- Currently we do not use the new Godot Metal-based renderer, we are hoping to
  bring it soon.

## Game Editor
- QuickOpen is missing a “Recents” tab (#87)
- Godot-native UI is not tracking the dark/light mode (#627)
- Godot-native is not using the system fonts (#176)
- You must name a new scene before “Save All” will save it (#519)
- IO Errors are reported with the old UI (#544)
- Dragging entire directory hierarchies from Files.app into Xogot does not preserve the top-level directory (#570)

## Text Editor
- The breakpoint indicator foreground color is too hard to see (#288)

## Inspector
- Does not show signals in attached scripts (#608)
- Missing signals for nodes with attached scripts (#630)
- No computed expression support for numeric values (#369)
- Some buttons on embedded controls are too small (#445)
- Some warnings for controls are not shown inline (#337)
- AudioStream property inspector is missing some features (#634)

## Debugger Panel
- The debugger does not currently surface any of the performance profiling capabilities (#636)

## Output Panel
- The output panel does not display RichText output, it will render as plain text (#574)

## Sprite Animation Editor
- We are aware that this is a high-traffic area, and we have an implementation in the works, but will come in a future release (#633)

## Exporting Projects
- Godot has a notion of Exporting projects for publishing your games.   This functionality is currently not exposed, but is coming up (#637)

## Features
- Motion Manager APIs are currently off, waiting on a fix  (#9)

## Running
- There is currently no support for Feature Tags when running your game (these are like “ifdefs”)  (#614)

## UI
- Various confirmation dialogs that will be ported over to SwiftUI remain
  written in Godot, let us know of any common ones, so we can prioritize them
  (#540) 
- Currently on the English locale is supported (#440)
- Editor Toaster Notifications are not currently shown (#383)

## Shader Globals
- It is currently not possible to edit values of sampler2D/sampler3D values
  (#147)

# Notes

[1] For example, while we currently provide a compatible “Add Node” UI in Xogot,
we are aware that we could vastly improve this experience by replacing the
object-oriented system that displays the controls with common operations and
sensible defaults for different kinds of nodes.