# First Preview Release Notes

Release notes for our first preview release of Xogot.

## Known Limitations

The most visible limitation currently is that the progress indicators in the UI
are not shown, which can be a little jarring when importing a large new project
and Xogot not responding.   This fix will be coming soon.


### Renderer
- Xogot is based on Godot 4.3, which imposes a few limitations when it comes to
  the renderers running on mobile devices (Forward+ and Mobile work, but OpenGL
  does not).   You might need to adjust your settings for your game to fully
  work on iPad.   For the final release, we will be switching to a
  Godot-4.4-based system which will support all three renderers.

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

### Bluetooth Controllers
- A bluetooth controller will not work if it was connected before running (#283)
  You can work around this by waiting to connect your controller until after the game
  is up and running.  

# Releases

## Build TBD

* Inspector now also capitalizes properties that use camel case, so things like
  "playerSpeed" are rendered as "Player Speed".  #10

* Adds shortcuts for select, move, rotate, scale, group, pan, ruler, lock,
  center selection, frame selection, local coords, snap.

* Compliance: states the purpose of accessing the microphone, this prevents a
  crash when trying to use games that want to record audio.  #29

* Launching Xogot will no longer interrupt audio playback.   There is still
  additional work necessary to allow games to change those settings. #37

* Property editors for dictionaries are now exposed.

## Build 1347

* Additional analytics to try to track down a crash that is happening with a
  popup, but none of the crashes have any feedback associated with it.

* Improve the numeric data input, the small arrow keys will now at least
  increment values in 0.1, instead of the hardcoded values in Godot, as
  sometimes those would be as small as 0.001 which were barelly noticeable

* Numeric Input changes: for users with keyboards using a modifier with the up
  and down arrow keys now change the value like this:

  ** Option: 0.1 units
  ** Shift: 10 units
  ** Control: 100 units

## Build 1342

* Resource pickers will now have the proper filters for the data type being
  edited, instead of defaulting to a useles default that did not show the right
  files.

## Build 1338

* Additional breadcrumbs for catching crashes.

## Build 1334

* Documentation should be rendered again

* Fixed the tab colors in the text editor, the ghost text is gone

* Help page now has proper rounded corners

## Build 1333

* Fixes crashes caused by background messages being posted to the output log

* Additional debug information for some crashes we are tracking

* Fixes double-tapping on FilePad, ScenePad and CreateDialog, once you tapped
a row, the second tap was always considered a double-tap.

* Double tap on directories toggles the directory expansion state, rather that
  opening the inspector.

* Prevents a crash on when the collision gizmo is enabled (this looks like a
  potential Godot upstream bug: c8424cfce77ca9536c7fdb0c03345a2fbcc39bba)

* List selection mode in the 3D editor is now working.

## Build 1328

* Fixes the Skeleton3D plugin editor that would lead to a crash, but this
  surfaced a series of issues related to toolbars for plugins and inspector
  plugins - all those issues have now been fixed.

* Fixes crashes stemming from partial deinitializations of the editor.

* Surfaces incomplete project properties into the Project Settings (like
  General/Wind, but will work for other properties that are only 2-levels rather
  than the standard 3-levels)

* Map Layer editor now supports Pinch and Pan.

* Enabled the Mac-command like shortcuts in Godot, rather than the default
  Windows-based ones (visible in things like "Select All" in a Godot Text
  editor, now it is Command-A rather than Control-A).

## Build 1320

* Allows cinematic preview to be disabled.

* Fixes physical keyboard input for special keys.

## Build 1317

* When selecting a file from a property in the UI, it will now use the
  configured filters by default, rather than the system default.

* Tapping "Select" on a file selector property without having picked a file will
  now reset the value to empty.

* Made the debugging control line at least 44 points tall so it is easier to tap
  the buttons there.

* Made the completion entries larger so they are easier to tap.

* Use debug builds to help us isolate a couple of crashes.

* Fixes the debugger window positioning when there is no target running.

* Added debugging symbols for the Godot component, it turns out that the
crash reports were getting very hard to see due to the lack of this information.

* Fixes the crash that was triggered when tapping on the sky or sun in the 3D
  editor, finally tracked it down.  This only happened in release builds.  A
  lovely gift from the C++ optimizer to us.

* Importer and other properties: avoid replicating the last section in
  properties with implicit categories.

## Build 1307

* Makes sure that a deprecated toolbar is not shown while editing controls.

* Does not restore Built-in script loading, like Godot does.

* Internal improvements (Godot rehosting code).

* Saves all scenes and scripts before running, to match Godot on desktop, and
  also is much better UX.

* Fixes crash on the Groups pad.

* Brings Crashlytics, hoping to find the location of some ellusive bugs being reported.

## Build 1296

* Native SpriteSheetImporter implemented.

* Fixes loading and saving of built-in scripts (those that do not have a
  separate file).

* Fixes running not picking up saved changes.

* Project Manager now offers long-press options to rename projects and launch projects.

* Fixed some ranges in the 3D toolbar light properties that were out of range
  and one property that could not be changed.

## Build 1283

* Should fix crashes related to the inspector and custom resources that were
  triggered under various different conditions.

## Build 1280

* Fixes the scenario where tapping the filepad and scenepad icons to
hide the sidebar would cause the sidebar to not be shown again (#446).

* *Did not set min/max settings for windows when resizing, which
caused runtime warnings, now we are correct (#437)

* Clip the top window, so that we do not overdraw (no bug filed, but
preemptive).

* Tracks the state of the code editor and the bottom bars, and the
last used gets the priority for the display.  The priority is very
simple, if the text editor just became the first responder, then when
the keyboard appears on the screen, we hide the bottom bar.  Fixes
#375.

* Allows the dragging handle to be used when a bottom pad is
maximized.

* It is now possible to tap anwyhere in a row on the Create New Dialog,

* Disable node 3D editor plugin mouse motion event handling if pinch or pan
  event occurred.

* Adds Command-shift-C shortcut to copy the node path

* Adds Command-Shift-[ and Command-Shift-] to go move across editor tabs.

* Style: search boxes no longer auto-capitalize.


## Build 1274

* Now it valides project names

* Fixes slow response times on dialogs, this fixes a regression from when I
  added double-tap to activate. 

* Fixes the ratio-lock button not working.

* SwiftGodot upgrade (just internal, nothing really visible)

* Fixes the popup closing errors.

* When using StageManager, there is an iPadOS bug that shows an empty bar at the
  bottom when doing text entry, so we deployed a workaround.

## Build 1260

* Font color in the filepad search is now visible in dark themes.

* A serious bug that would prevent plenty of components of Xogot to work on the
  second project opened has been fixed.   It was most obviously manifest as
  buttons or objects not responding sometimes to taps, and a "SignalProxy" error
  logged in the output window.

* Duplicate labels in the Project Settings have been fixed.

* Searching in the FilePad will automatically expand folder nodes when there are
  matches inside a closed folder.

## Build 1256

* Numeric popups no longer move as the values change.

* Additional improvements at Project Shutdown to prevent it from crashing, an
orderly shutdown has been implemented now.

## Build 1253

* Toolbar Animation icons are now displayed.

* Double-tapping on an item on the the Quick Open Dialog will open the item.

* Recent files were being saved with an incorrect filename, polluting the space.

* Fixed a crash in the CodeEditor triggering while reporting IO errors.

* Prominent Import files button in the toolbar.

* Clear option in a Resource should now clear the value.


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