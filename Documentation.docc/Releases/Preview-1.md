# TestFlight Release Notes

Release notes for our preview release of Xogot to TestFlight.

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
- Godot-native is not using the system fonts (#176)

### Inspector
- No computed expression support for numeric values (#369)
- Some buttons on embedded controls are too small (#445)
- Some warnings for controls are not shown inline (#337)
- AudioStream property inspector is missing some features (#634)

### Debugger Panel
- The debugger does not currently surface any of the performance profiling
  capabilities (#636).

### Output Panel
- The output panel does not display RichText output, it will render as plain
  text (#574).

### Exporting Projects
- Godot has a notion of Exporting projects for publishing your games.   This
  functionality is currently not exposed, but is coming up (#637).

### Running
- There is currently no support for Feature Tags when running your game (these
  are like “ifdefs”)  (#614).

### UI
- Various confirmation dialogs that will be ported over to SwiftUI remain
  written in Godot, let us know of any common ones, so we can prioritize them
  (#540) 
- Currently on the English locale is supported (#440)

### Shader Globals
- It is currently not possible to edit values of sampler2D/sampler3D values
  (#147)

# Releases 

## Build 1761

### Features

### New native Animation Editor for Xogot.

We just landed the new animation editor, it will appear now whenever you select
an animation and you activate the the "Animation" bottom panel.   When you do,
you still have an option to go back to the old UI.

This new editor has been adapted to be a good iPad citizen, and being a complete
SwiftUI rewrite, gives us opportunities to improve the editor over time with
more native features.

We are particularly interestd in feedback on how the experience feels to touch -
and make sure that everything that you need to do is present, but also that it
is an enjoyable experience - so feel free to send us feedback on Discord or via
TestFlight on any issues you might have - no matter how small.

There are some features missing in the current editor, we are actively working
on them, and they will be coming in the next few releases:

* It is not possible to "inspect" a key when you select it on the inspector.

* Snapping has not been surfaced in the UI

* No help is displayed when selecting a node property or a method from the Add
  Track selector.

* Confirmation for adding multiple tracks to the RESET track is not required.

* Can not currently add sub-animation tracks.

* Volume tracks merely render as data points, does not show volume levels.

* The Animation Library Editor is missing Save-as functionality.

* The timeline rendering currentl only displays the timeline in seconds, but not
  in frames.

* Various advanced commands are not implemented: Bake Animation, Optimize
  Animation, Cleanup Animation, Make Easing Keys. 

* Missing Onion Support.

* Missing Bezier Editor.

### Sharing
  
You can now tap the share button in the upper-right corner of the app to 
share a build of your project that can playtested by anyone else running Xogot.

### Bug Fixes

* Makes the shell buttons for the left-side panes easier to tap (#1029,
  TestFlight feedback).

* We are starting to test the capability of sharing your games with other Xogot
  users.  

* Signal pad: change the colors for signals to be the secondary color, and the
  connections to use the primary color to be easier to spot.

* Arrow keys no longer "stick" when running a game (#1002, TestFlight feedback).

## Build 1732

* Fixes for multiple editor windows being opened, it was not possible to open
  projects, with the error "Another editor is already active"

* Updated profile page.

* Fixes the "jumpy" behavior while dragging public bug report #25 (Internal
  #889). 

## Build 1717

* Opening the property inspector should now be snappy, at the cost of a cute
  animation (#669, public bug #4, and multiple Testflight feedbacks).

* Crash fix reported via Testflight crash reporting in the 2D editor(#957), this
  happened a lot, but we never had good instructions on how to reproduce it.  

* Prevent a scenario where we would display the game controllers on the Game
  Editor window (#987, Discord feedback).

* Fixes node renaming on the scenepad not working on landscape mode (#1017).

* Fixes the multiple-editor check at startup.

* When popping up the numeric input, resign the input from other input boxes, so
  that there is no confusion as to where the input is going both in practice and
  visually (#982).

* Fixes the regression reported on Discord for the editor panning not working
  because it assumed that you were trying to zoom and it overrides the pan.
  The trigger was too sensitive.

* Shell updates, we are redoing a few things, we dropped the "Export" tab, which
  is not ready to be used.  Added a new on-demand "Games" tab that will contain
  games that have been shared with you.

* Not enabled: work in progress on the new Animation Editor and the TileMap
  Editor. 


## Build 1678

* Stops audio playback when you stop a game (#968)

* Multi-touch events now responds to multiple-finger inputs, and does not ignore
  the second touch (#909, follow up from #854 and the improvements in build
  1567).
  
* Fixes a crash when going back to the homescreen that was introduced in the
  last release.

* Short-term fix for Skeleton/Bones editor crash (Xcode Crash reports), with 
  telemetry to try to find the root cause.

* Shift+two finger move on the trackpad will now pan, rather than rotate (#913).

* Pinch gestures on the trackpad no longer zoom too much (#904).

* Renaming on the Scene Pad and the Sprite Editor now requires a long-press and
  selecting "Rename", rather than being a "Rename on tapping a selected element"
  #988.   We are hoping that this will be a slightly better experience.

* Fixes icons not showing up for projects that are created in an external
  location (#997 and public bug #57).

## Build 1660

* IO Errors are now reported on a native UI, rather than the Godot native UI
  (#544).

* Internal: avoid an invalid idiom in Swift, which mostly works, I had been
  warned against, but "works for me" had carried me for weeks.  Decided to
  finally fix every instance of the problem (#618).

* New Scene dialog will now work if you are editing in half-screen (for example,
  if you are running side by side, Discord Feedback, #774)

* Potential crash fix related to the Joypad (#850).   Some users had their Xogot
  crash due to us invoking Joypad methods, we believe that there was a scenario
  where we could invoke the Joypad methods on the wrong process/thread.   We
  hope that this fixes the problem.  

* Fixes the launch screen display for large displays - this only happens when
  you connect an external display to your iPad at a higher resolution (#923).

* Avoid inserting quotes when it is not necessary when dragging nodes from the
  scenepad into the text editor (fine tuning #973)

* SpriteAnimationEditor: the FPS value was not being set on the animation, now
  it is (Discord, #994).

* SpriteAnimationEditor: inputing a value on the FPS display on the sprite frame
  editor will auto-dismiss.

## Build 1648

* Tapping on the Script icon when you are already on script mode, will bring up
  the "Quick Open" dialog for scripts.

* Will now show warnings when the system is low on memory, the messages are
  displayed with a new toaster-like notification system, and we will be wiring
  up some Godot messages here too (#977)

* Editor Toast notifications are now shown (fixes #383)

* Fixes drag-and-dropping of scene pad nodes into the text editor, it will now
  insert the optimal path, rather than the raw node id (Fixes #973)

* Internals: add additional logging to help us track down crashes.

* Game runtime errors are now rendered with an error description, not just the
  high-level warning, as it was confusing as to what exactly this was.

* The UI will no longer fight you when single-stepping in the debugger if you do
  not have a keyboard attached (#491).

* The ScenePad's Node/Info contains triggers to open connections and groups, and
  an easier region to tap them.

* The ScenePad Info popup will now format the brief documentation for the node
  and will show the entire brief description.

* SignalPad: "Get Info" on a signal will now render its documentation, previousy
  it would only render it for the signals on the most-derived class.

* Undo/Redo buttons on the code editor are wired up when not using the physical
  keyboard. Fixes #941.

## Build 1636

* Some resource previews on the inspector were not being dispayed if the
  resource renderer did not support generating tiny versions of the image (which
  we did not even use).  Fixes #837.

* Fixes the missing Output data when debugging a program (Discord feedback).

* Allows Animation Key Frames to be edited in the inspector (Testflight
  feedback, internal #795).

## Build 1631

* Confirmation and accept dialogs mapped from Godot to SwiftUI will have the
  primary action at the end, following the iOS platform conventions (#963)

* Temporarily remove the "Minimize debugger" option, which produced an ugly UI,
  proper fix will come soon (#922).

* Breakpoints on early code (typically _ready) are now honored (Testflight
  feedback, #761)

* Fixes a lifecycle bug that we caught thanks to recent hardening of the
  runtime.   We noticed a few scenarios that were wrong and addressed them.

* Actions on multiple scene nodes now works with the Swipe-based actions (#950).

* Selecting a new file on the FilePad should now update the inspector
  accordingly (#953)

* The code editors are not reset after switching tabs anymore (public bug #55).

## Build 1620

* Crash fix on the Project Settings if you modified a text input field and
  switched tabs.  But it means that in Stage Manager, an extra empty row 
  is shown when a hardware keyboard is attached when editing text (Xcode crash
  reports, internal #964)

## Build 1616

### Features

* Add support for "Property Keying", this is the feature that shows a small
  "key" object next to a property when the Animation pad is selected and there
  is an active animation (Issue #995, feedback from recent survey).

* Added comment/uncomment shortcut for code (various feedback requests, among
  those #40, Testflight and survey feedback).

* The Inspector will now show the object name/type when inspecting it, but only
  if the name is different than the first category name (#948).

### Bug Fixes

* Take into consideration the size of the resizing handle to set the minimum
  bottom bar panel sizes for fixed panels (like the Audio one).   #931.

* Fixes the scenario where the completion window could become too small.
  Testtflight feedback.

* Reworked the ownership model in SwiftGodot, which fixes a fundamental design
  flaw which we had worked around by leaking.

* Fixes the code completion window not being large enough after running a
  program with an error (#921), Testflight feedback.

* Fixes a scenario that took up too much space in the debugger (#922),
  Testflight feedback.

* Fixes Drag gestures: Camera jumps on transition from moving to dragging
  (public bug #45).

* Look and Feel: Create New Dialog does not have uneven row sizes (#952).

* 
## Build 1594 - a Christmas Miracle!

* The Godot Embedded content will now track the system color scheme.  While
  Xogot already did this, the embedded Godot code did not, it was running in 
  dark mode (#924, #627, #715)

* By popular demand, the ScenePad now shows the Godot icons for the node types,
  as folks say that this is an important visual cue to determine what things
  are.  Initially, I thought the colors were pretty bad, but thanks to DETOX,
  and SigitSP on Discord, they pointed out that the colors were dynamic and
  based on the theme.

* New size font picker for the code editor (#906, based on survey feedback).

* Added a nested array editing capability, this was surfaced as lacking support
  for adding an InputEventAction (#920, based on Testflight feedback).

* Show type icons on the scenepad.

## Build 1582

* Surface "Create Shader" in the FilePad "+" menu (#894)

* 3D Editor: the viewport menu now offers commands to focus on the origin, or
  focus on the selection, these have also been bound to the keyboard shortcuts
  "o" and "f" respectively, similar to Godot on Desktop (#762 + survey
  feedback).

* Fixes 3D Viewport commands "Align Transform with View" and "Align Rotation
  with View".

* Will not request to upgrade projects that had
  rendering_method="gl_compatibility" (#905).

* Visual Shaders are now available on the new Shader Editor tab.

* When you create shaders, we will open the shader editor right away.

* Fixes a bug when trying to rename a scene node, and the keyboard would cover
  up the pad, and dismiss the rename operation (#919, Testflight feedback).

* Add additional space to the "trash" icon on the output window, so that it is
  easier to close (#927, Testflight feedback).

## Build 1572

* Create Shader and Create Script dialogs will now select the part of the
  filename so that it becomes easier to rename those fields at creation time.

* New shaders now get a unique name by default.

* You can now import photos from your library straight into the FilePad (#625).

* Magic trackpad support for panning (Part of #17).

* Fix an infinite loop in the bottombar update.

## Build 1567

* Fixes the touchesEnded event being delayed with multiple finger inputs
  (#823, submitted as Testflight feedback).

* Further refinements to the multi-touch handling (improvement over the fix for
  #854 from Build 1552).

* SpriteSheetImporter: allow users to change the background of the image, to
  simplify importing images that might be white on transparent colors (Discord feedback).

* Launch Screen: no longer overloads the [+] button to be new game or browse
  locations.  The browse location option is now on the toolbar (#891)

* If you do not have a physical keyboard attached, we will not auto-focus the
  search field in the "Create New Node" dialog, going to experiment if this is a
  better workflow for users (#749).   But if you have a keybaord, it will
  autofocus.
  
* Launch Screen: style changes for the "Delete Project" confirmation dialog
  (#821).

* Xogot will no longer show the convenience keyboard input accessory if you have
  a hardware keyboard attached.

* New SwiftUI-based Shader Editor, it is currently missing the
  VisualShaderEditor, but will allow us to tune the UI and experience for the
  shader editor (Discord feedback, #703).

* Improved the heuristics for positioning the code completion window, it should
  not jump anymore (Discord feedback).

  
## Build 1552

* When loading a Godot project, if the configured renderer is not support in
  Xogot, you will get a chance to change it to the "mobile" renderer.   Fixes
  public #50.

* Sprite Editor: commits a rename change, even if you tap away (report from
  Discord).

* Introduce multi-touch input options for the running game.   This version will
  by default dispatch raw multi-touch input to your program, but we introduced
  an option in project settings
  input_devices/pointing/ios/enable_pan_and_scale_gestures, similar to the
  option that exists for Android that will instead turn multi-touch input events
  into pan or scaling gestures (that was our non-configurable, old behavior).
  Fixes #854 and public #24.

* Various Autoload features were completed (#883): Autoload renaming, allow
  enable/disable of autoloads, expose as global.

* Multiple files can now be dragged from the FilePad into the editor surface
  (#867).

* Fixes the "Tile Set" tab bar not showing when a new TileSet resource was
  created.  This is a proper fix for #14, which we had not quite fixed, and we
  had just grown used to
  select-another-node-and-come-back-and-select-the-tilemap.   The issue was that
  we were tracking items being hidden from the bottom bar, but not items being
  shown.  So this would have impacted other plugins as well that were not
  activated on demand.

## Build 1546

* Fix a regression introduced in 1541 that prevented the bottom tab actions from
  activating.   This was a bug introduced due to a fix preventing a hang for
  Theme resources in 1541

## Build 1541

* Godot-native popups would sometimes show up and not get the focus, and users
  had to tap around to force the focus to enter, without this, it would give the
  feeling that the app was "stuck".   Fixes #843, a bug initially reported on
  Discord when it was not possible to rename an animation.

* Rename dialog on the FilePad sometimes would not show up.

* Option to show the available memory.

* Fixes signals not showing up for nodes that had scripts attached.

* Re-enables the MotionManager, so your app can now get those events (we
  disabled it very early on in the project).

* Editing Node names on the scene pad in landscape mode will no longer dismiss
  the keyboard (#872).

* Numeric Input for the sprite editor and sprite sheet importer: hardcoded
  proper locations for the numeric input, as we were creating views that would
  not allow data input (#708 and user reports on Discord).

* Project launcher will now show the last date used for the projects (#382).

* Fixes debugger breakpoints on built-in scripts (partial fix for #877).

* Fixes an issue with array elements crashing the editor (Crashlytics).

* Fixes a hang when activating certain resources on the inspector (reported on Discord).
  
## Build 1516

* Improvements to the signal connection dialog:

  * When connecting a signal, we now stub the signal in the target method
    (#873), this is what users of Godot expect, and we accidentally dropped this
    support when we switched to the native editors.

  * Save the Godot scripts using the resource API, ensuring that the list of
    available methods is reflected when the user needs them on the connection
    dialog (#870).

  * Change the filter options to use a button toggle-style, rather than a menu
    picker, as it is faster to switch between the options.

* Syncs the ScenePad collapsed state, avoiding a rare scenario that would
  forcefully collapse the ScenePad (#781).

* When importing assets, prevent read-only fields from being modified (#816)

* Fixes a crash with plugin extensions, this was mostly noticeable when opening
  Skeleton objects, but could potentially happen elsewhere.   Now every
  extension is shut-down immediately when navigating in the inspector (#849).

## Build 1508

* When downloading samples, if the remote server does not include a
  Content-length, display a generic progress view.

* Fixes double-tapping to select on various places.

* Add support for the soft-keyboard return key accepting a completion option
  (prevously, it only worked for the physical keyboard).

* Fixed a crash spotted on Crashlytics related to Godot embedded views

* Implemented recursive "Make Resource Unique" feature for resources, it was
  missing (Crashlytics)

* Make sure that the snap value editor can be displayed, regardless of the
  toolbar position.

* Snap value editor now uses scrolling input for degrees (Internal #260, #864)

* When using the "Show Node in Tree" option in the inspector, we now use a
  different color than the selection to highlight those nodes (#817)

* SpriteFramEditor: the new editor now goes through the Godot undo/redo system,
  fixing a plethora of bugs identified.

* We now show a quick tooltip for items in the toolbar to guide users on what
  the features are (#661)

## Build 1479

* Pan and zoom events can now be used across the application together.

* Styled the editor so that breakpoints lines are more clearly visible, it used
  to be dark enough that it was unpleasant to look at.

* Code Editor: "Replace" functionality is now working (Testflight feedback)

* Prevent iOS 18.0 users from going back to the main screen, as this triggers an
  iOS 18.0 bug.

* SceneImporter: fixes the inspector in the UI, so navigation now works properly
  on that window.

* Undo operations are now reflected on the Inspector.

* Multi-touch input is now sent to Godot scripts.   Partial fix for  https://github.com/xibbon/XogotIssues/issues/24.

## Build 1465

* Interacting with embedded inspector plugins will no longer scroll the
  inspector as you scroll inside those elements. 

* Gradient previews will now properly show.

* Embedded controls on the inspector will no longer vanish

* Follow up to picking custom locations: there were a few file pickers in Godot
  that defaulted to the wrong file system location if you had picked a custom
  location. 

* Panning: panning across the Godot controls should now track the finger, as
  expected by ipad users, rather than the accelerated mode that is more suitable
  for desktop users.  This should be visible in various places that implemented
  panning in the Godot controls.

* New Text Editor Setting for completion: add type hints on/off toggle, feedback
  from Testflight.


## Build 1464

* Now renders inspector plugins for nested elements of an object.   Fixes #796.

* Prevents a crash that happened after a game was stopped.

## Build 1459

* Makes the swipe action on the ScenePad and FilePad less sensitive.

* Code completion for GDScript code is back.

## Build 1457

* Project Manager: it is now possible to select many projects and delete them in
  one go.

* Clears memory used after a game terminates, this also fixes crashes that
  happen when restarting a game (AppStore crashes)..

* Fixes an imbalance of objects, that prevents another crash from happening   
  (#833)

## Build 1452

* Due to popular demand, we now support saving your projects on a location of
  your choice, so that you are not limited to saving files into your iPad, you
  can now choose an external USB drive, iCloud drive or any other external
  locations.

* Deleting a project will now require confirmation - this is not a sign of
  weakness, but an acknowledgement that certain actions in life are
  irreversible, so we leverage the best technologies in SwiftUI to ensure that
  you have a second chance.

## Build 1449

* Fixes a crash when an object is removed via undo, while the inspector was
  still editing it.

* Fixes the issue that crashed Xogot when a game was launched, a regression
  introduced for the fix in Build 1439 for animations.

## Build 1444

* Bring back the scrolling input editors.   Sadly, this interferes with the
  swipe gestures.   So I disabled the swipe gestures on the inspector, and will
  have to figure out a good UI for it.

* Fixes the Setting crasher 

## Build 1439

* Fixes another class of crashes, this time triggered by the animation editor,
  but this is a general fix that will apply to many more scenarios (internal
  #825)

* 2D Editor: Disable rotation line, when pinch or pan event occurred, also seen
  as "Pinch to zoom causes node to move if transform tool is selected" reported
  via Testflight.

* Sets the minimum hardware requirements required by Godot, as older iPads (7th
  generation and older) do not have the GPU support that the Godot editor
  requires.

* Fixes a crash on the code editor (Crashlytics)

## Build 1433

* Fixes the scrolling not working, regression introduced in 1430 the fix is to
  loosen up the sensitivity of the swipe handlers.

## Build 1430

* Backported another Tile Editor fix

* Swipe actions on inspector properties now exposes "copy path" operation, as
  well as copy value and paste value (internal #623)

* Swipe actions on ScenePad now allow selection/deleting.

* Swipe actions on FilePad now allow selection.

* Make it easier to tap on menus in resources (it was too easy to navigate into
  the subresource, internal #737)

## Build 1425

* Groups Editor now support Global groups in addition to scene groups.

* Bring back the stricter object tracking.

* You can now type in any place in a row in the "Create New" dialog (Testflight
  report).

* In the Project Manager, the delete option is properly colored (red, internal
  #800

* Dictionaries and array editors no longer use pagiation for consistency with
  the other editors.  Internal #810.

* When deleting files from the FilePad, we will now show the user the impact
  that deleting the files would have on the project, fixes #779.

* Signals declared in scripts are show on the inspector, fixes internal #608

## Build 1415

* Fixes crash in the tile editor when painting with a physics layer.

* Create Node dialog now hides deprecated and experimental by default, but
  allows you to show them if needed.  

* Create Node dialog can be expanded to have more space to see the node types. 

* Undoes the stricter object tracking, as it has a design flaw.

## Build 1411

* Qualify of life improvement: for resources that only have a single type,
  rather than offering a "New" submenu, just inline the value, like "New
  TileSet"

* Quality of life: when pausing a program, if the program is paused and there 
  is not script to highlight, rather than showing the debugger pad, show the
  output pad, internal #772.

* We introduced a vastly stricter binding from SwiftUI to Godot in 1399, which
  will cause a few crashes in the next few days in - this version contains fixes
  for the early crashes that have been spotted.

## Build 1402

* Fixes the issue that prevented data input in text fields in sheets triggered
  from the inspector view (Public report #41), this also should fix other similar scenarios.

* Additional fixes for the new more stringent object tracking, fixes a crash
  (reported by Joseph - internal #801)

* Create Node now flags experimental and deprecated nodes.in

## Build 1399

* Fix regression that prevented the debuggee from closing its window.

* Looks: removed extra padding that was added to some BottomBar pads to leave
  room for a drag-handle, before I changed course to the current approach.

* Adds support for dropping files into Resource picker and file pickers.

* Fixes setVirtualControllerCallbacks

* Fixes a series of crashes that we tracked via Testflight related to spawning a
  game and the editor.

* Related, fixes a crash on the virtual controller that might crash.

* Implemented support for editing arrays of certain elements in the inspector -
  most notably folks reported it missing in things like TileSet (User feedback)

## Build 1387

* Fix a crash on the audio interruption handler (Testflight feedback)

* Additional telemetry to track down the MoltenVK issue that crashes on certain
  projects at startup.

* Disable Developer mode, there are lots of crashes coming from users that have
  done something behind Xogot's back, and I want to rule the reasons out.

* Launch screen: if you were in select mode, but switch to another tab,
  the select mode will be reset.

* Launch screen: long-press on a project now has a "Delete" option.

* FilePad: dragging a file into itself, or in the same directory no longer
  triggers an error.

* Bumped version to 1.0.3 to make it easier to diagnose.

* Fixes objects not being inspectable in some scenarios, tracked via Crashlytics.

## Build 1379

* Fixes the scenario where directories removed from the filepad would not be
  removed from the file listing.

* Start to roll out a system to track objects that Godot releases but that the
  UI still holds, this will help me track down the places where this is
  happening (SwiftGodot Resilience).

## Build 1375

* Fixes the issue where the controller would not work if it was paired before
  your game started.   This was finally removed as an issue from these very
  release notes! (#283)

* Restoration will no longer start with a blank screen, that turned out to be an
  attempt to restore your game - but this should not even be allowed

## Build 1372

* Completes the audio setup for the game, so audio for your game will follow the
  settings you had configured when it plays.

* Should fix the "Crashes when you close a scene" (Testflight crash/feedback)


## Build 1370

* Fixes crash on dictionary editors for unknown data types, and adds support for
  using "Objects" as keys and values in the godot editor for dictionaries.

* "Pad" menu becomes more noticeable when launching an app.

* Dirty-file indicator is now properly tracked (Discord, Testflight feedback).

* Fixes the icon alignment on the toolbars.

* Bring a visual indicator that "select mode" is active in 2D and 3D toolbars.

* Bring back the Display Type Selector in te 3DViewport options.

* Work in progress: audio modes from the game are saved when the game pauses and
  the system defaults are put back in place, and restored when the game resumes (Discord feedback).

* Built-in scripts will now get their proper name when creating them.

* Fixed scrolling on launch screen for the learning projects (Testflight
  feedback)

## Build 1360

* Updates MoltenVK to v1.2.11, hoping that this fixes a number of crashes that 
happen on startup (Testflight feedback)

* Removes an assertion for a resource that was not released (Testflight crash report)

* Reduces the FPS to 60 frames per second while using the editor, and keeps it
  at 120 while running games.   This should reduce battery usage a little, but
  there is more work to do here (Testflight feedback)

* Fixes a crash on the dictionary editor for unknown dictionary types
  (Testflight crash)

* Fixed: Attempting to scroll Godot node selection dialogs drags instead of
  scrolling (Testflight feedback).

## Build 1354

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
