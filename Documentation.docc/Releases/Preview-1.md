# First Preview Release Notes

Release notes for our first preview release of Xogot.

## Known Limitations

The most visible limitation currently is that the progress indicators in the UI
are not shown, which can be a little jarring when importing a large new project
and Xogot not responding.   This fix will be coming soon.


### Renderer
- Xogot is based on Godot 4.3-based: and it imposes a few limitations when it
  comes to the renderers when running on device (Forward+, Forward Mobile work,
  but OpenGL in this release is not working).   You might need to adjust your
  settings for your game to fully work on iPad.   For the final release, we will
  be switching to a Godot-4.4-based system which will support all three modes.

- Currently we do not use the new Godot Metal-based renderer, we are hoping to
  bring it soon.

### Game Editor
- QuickOpen is missing a “Recents” tab (#87)
- Godot-native UI is not tracking the dark/light mode (#627)
- Godot-native is not using the system fonts (#176)
- You must name a new scene before “Save All” will save it (#519)
- IO Errors are reported with the old UI (#544)
- Dragging entire directory hierarchies from Files.app into Xogot does not preserve the top-level directory (#570)

### Text Editor
- The breakpoint indicator foreground color is too hard to see (#288)

### Inspector
- Does not show signals in attached scripts (#608)
- Missing signals for nodes with attached scripts (#630)
- No computed expression support for numeric values (#369)
- Some buttons on embedded controls are too small (#445)
- Some warnings for controls are not shown inline (#337)
- AudioStream property inspector is missing some features (#634)

### Debugger Panel
- The debugger does not currently surface any of the performance profiling capabilities (#636)

### Output Panel
- The output panel does not display RichText output, it will render as plain text (#574)

### Sprite Animation Editor
- We are aware that this is a high-traffic area, and we have an implementation in the works, but will come in a future release (#633)

### Exporting Projects
- Godot has a notion of Exporting projects for publishing your games.   This functionality is currently not exposed, but is coming up (#637)

### Features
- Motion Manager APIs are currently off, waiting on a fix  (#9)

### Running
- There is currently no support for Feature Tags when running your game (these are like “ifdefs”)  (#614)

### UI
- Various confirmation dialogs that will be ported over to SwiftUI remain
  written in Godot, let us know of any common ones, so we can prioritize them
  (#540) 
- Currently on the English locale is supported (#440)
- Editor Toaster Notifications are not currently shown (#383)

### Shader Globals
- It is currently not possible to edit values of sampler2D/sampler3D values
  (#147)

# Releases

## Build 1245

* Adds 3D editor, "Align Transform with View" and "Align Rotation with View" are
  now available on the viewport menu.

* Reliability: many scenarios that crashed where going back to the "Project
  List" are fixed, this is the result of a long-term effort, and the proper
  solution just landed.

## Build 1237

* 3D Node Editor, surface the "Use Local Space" coordinate option to the toolbar

* Fixes the text input in the inspector

* If you have a node selected in the scenepad and tap the "Script" icon at the
  top automatically load that script (only happens if you do not have any
  scripts opened).

* Quick Open dialog, Pick scene dialog, sprite frame editor: tapping anywhere in
  the row selects the row, not just the part with the text.

* "Run Specific Scene" and "Run Current Scene" work now, they were always
  running the main scene.

* You can now select the new SpriteFrameEditor from the settings menu.


## Build 1230

* Fixes the bug where if you were running your game in full screen, the stop
  button would not stop it.

* Disabled localization of Godot (it was mixing English and your local
  language), for now only English is supported.

* Double tapping on a row in the "Create New Node" will create the item,
    without having to tap "Add"