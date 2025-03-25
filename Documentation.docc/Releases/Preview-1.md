# TestFlight Release Notes

Release notes for our preview release of Xogot to TestFlight.

## Known Limitations

### Running

- There is currently no support for Feature Tags when running your game (these
  are like “ifdefs”)  (#614).

### UI

- A handful of confirmation dialogs that will be ported over to SwiftUI remain
  written in Godot, let us know of any common ones, so we can prioritize them
  (#540) 

- Currently only the English locale is supported (#440)

# Releases 

## Build 1960

### Features

- New native TileMapLayer editor, a companion to our new TileSet plugin - it is
  currently running side-by-side the original Godot editor, you must tap "WIP"
  in the bottom bar to enable (Task #667).

### Crash Fixes

- Import/Rescan crash has been fixed (#1190).

- Prevent crash when users sent Xogot to the background while it was loading and
  came back (#1204).

- Prevent crash that happened when users attempted to interact with Xogot, while
  it was still initializing (#1207).

- Prevents a crash when stopping a project, this was one of our top crashes
  (#1202, Testflight).

### Small Features

- The keyboard accessory bar now has '_' as a shortcut, and we moved the "("
  and ")" to a more prominent location (#955).

- Added cut and paste to the keyboard accessory bar (#928).

- Learning Center content is now downloaded from the network, rather than being
  bundled.

- Add "Insert spaces for tab" editor setting (#936).

- It is now possible to retry downloads for starter projects

- Added Smooth Scrolling to SpriteSheetImport and tile set: This allows for
  smooth scrolling, improves performance with large grids and also does auto
  scalling to fill view size if image is smaller than container view. 

- TileSet editor now uses the toaster notifications to report errors.

- Project Info on the launch page will now display the location for a project
  (#1187).

### Fixes

- Fixes dynamic content on the Inspector that was not updating (example,
  enabling "Region" in Sprite2D - #1169).

- Learning Center will now use all space - this was noticeable if you hooked up
  your iPad to a larger display (#1136).

- Learning Center detail view had icons that were too small (#965).

- Numbers in the Sprite Sheet importer now scale (#898).

- Fixes the property array editor not updating on add/delete operations (#1197).

- Fixes crashes on projects that were using the OpenGL compatibility driver
  (#1191, Discord).

- Fixes overlay grid on TileSet, move toolbar to separate view for TileMap.

- "Open Shader" now filters using shader types, instead of using the default
  resource filters.

- Changing the project settings on projects that were imported from a new
  location has been fixes (#1189, Discord).


## Build 1902

- Memory leak fix.   With Build 1876 that introduced our 4.4 support for Godot,
  the code that dealt with "Reload Project" prevented the resources used by the
  game from being released, causing a memory leak.   This impacted all uses of
  Xogot, not just project being upgraded.

- Updated Learning Center templates to 4.4 and Forward+ renderer where possible.


## Build 1898

- This release disables our Metal Shader cache, as this was causing crashes when
running games with the 'mobile' rendering method, or when you had edited a game
with the 'mobile' rendering method.   

- New "Rescan" directory option on the FilePad, for when you make changes
  externally to your document folder and you want to force a rescan (for example
  with iPadOS file system providers like iCloud Drive).

- Fixes the visual rendering of the import pad (#1164)

- Fixes duplicate labels for some inspector properties (#1080)

- Brings back "Rename" on the ScenePad context menu (it was accidentally
  disabled).


## Build 1886

This is a quick release to address a couple of regressions introduced in the new
features.   The EditorProgress dialog was showing up for background tasks (which
was triggered when you come back from the background) and it would show the
game controls on top of the game editor window (Discord)

### Features

* When creating  controls like labels, menus, menu buttons, or text meshes, they
  will now default to having some text when created, similar to what a UI
  designer would do - rather than being empty.

* Small improvements to the Asset Catalog.

* Smaller download due to fewer precompiled shaders bundled (we now only bundle
  those that Godot uses at startup).


## Build 1880

### Features

* Additional tune up for TileSet editor, and we have officially deprecated
  Godot's original TileSet editor tab, so it is no longer available.

* Upgraded from Godot 4.4 Release Candiate 1 to Godot 4.4 official release.

### TileSet editor

* Improving performance for big tile sets (for example 2000 x 1500) and making
  it initialize in normal time also added indicator for creating tiles progress

* Added terrain sets and implemented terrain paint that lets you apply terrain and peering bits

* Fixed some edge cases for Polygon editor and made whole process smoother

* Finished tile merge tool and added save of merged tile to atlas tiles

### Bug fixes

* Brought various Godot fixes from Godot for shaders and the Metal backend
  rendering.   They should prevent a deadlock on startup when loading projects
  with a lot of shaders and bring additional stability to Metal.

* Now will honor the rendering mode/driver you set on the project - I made a
  mistake on the previous release: so now you can  choose between Metal or
  Vulkan rendering engines, you can do this from the project launcher, by
  selecting "Get Info" and setting the desired renderer options (#1148) as well
  as allowing you to configure the rendering method: before you
  start a game: Mobile, Forward+ or OpenGL.


## Build 1876

### Godot 4.4

Upgraded Godot to the 4.4 Release Candidate 1 release and switched from Vulkan
to the Metal renderer engine.  There might be some hiccups as we work through
some of the differences from our pre-4.3 release to our 4.4-based Godot.
  
This fixes the long-standing "The editor does not fill the screen when using an
external display" (Testflight Feedback #22, Internal #689)

This introduces support for the new Shader Global Variable type "External" (#1119).

The sample projects have been updated to 4.4

### Features

- Implemented support for reloading the current project (#701, Discord), which
  became more important as Godot 4.4 will want to upgrade Godot 4.3 projects.

- You can now choose between Metal or Vulkan rendering engines, you can do this
  from the project launcher, by selecting "Get Info" and setting the desired
  renderer options (#1148).   
  
- The above UI additionally lets you configure the rendering method before you
  start a game: Mobile, Forward+ or OpenGL.

- Editor Progress Reporting (#619) has been implemented, so no longer will you
  have to wonder "What is taking so long for the editor to launch?".   You will
  now be the first one to know.

- New native iOS TileSet is ready for testing!   This is one of our last
  components that we are rewriting with a native UI given the high-traffic
  nature of this feature - so we would love your feedback on it.

  (We are starting work on the last chapter before the launch: the TileMap
  native editor pane).

- Preview of the Asset Catalog for iOS is now available - we are tweaking the UI
  and the backend, but we finally have a pipeline to assist users in getting
  their plugins.

### Fixes

- If you enable HDR in your game, the editor will still work correctly, this was
  reported on Discord (#901).

- Internal fixes to our inspector (#1138)

- Fixes game updating, when a new version of an existing game has been
  published.

- GameShare popup, and the user profile view now have "Dismiss" buttons and use
  the same style as other dialogs.

- Godot should now detect changes done to the files if you modified them
  externally (#1000, Testflight feedback).

- Allow reimport of assets to be done without having to change any properties in
  the import pad.

- Initialize iOS's AudioSession following the project settings.

## Build 1854

- Replaced the icon for the menu from being a set of switches to be the more
  common idiom, the ellipsis.   The previous choice of an icon was a source of
  confusion (Discord, months of agonizing over it).

- CreateNode: now it is easy to add images to a 3D scene, we take care of
  loading the ImageTexture and setting the image texture for you when creating
  Meshes (#1127).   This also adds the Constructive Solid Geometry nodes to the
  3D tab.

- CreateNode wrap up: added construcive solid geometry nodes to the 3D tab.

- CPU/GPU 3D/2D particle emitters interaction dialogs have been moved over to
  be iOS native as well.

- The inspector now has a documentation button to easily learn about the type
  you are editing, and the documentation now also renders information about what
  this class inherits from, to easily learn more about their base classes (#275).

## Build 1851

- Additional improvements to the Create New Node dialog, for the Mesh options,
  we try to create a CollisionShape that matches your request when you select
  RigidBody or StaticBody.   You can still replace it with your own, but the
  default will work out of the box.

- When creating Rigid and Solid bodies, we now name the child mesh with the mesh
  type, to make the result clearer.

- Switch to use SF-Symbols based icons for the app, rather than the Godot icons.
  Might make this optional in the future.


## Build 1850

- Hides an old-style toolbar that was accidentally left enabled in Godot 2D
  editor.

- Fixes the "Add" node to auto-dimiss the Create Node Dialog when you are in the
  "All" tab. 

## Build 1846

### Improvements

- Brand new "Create Node" that categorizes the node types in 3D, 2D, Controls
  and other.   The 3D mode in particular makes it easier to create 3D meshes,
  rigid bodies and static bodies in one step.

  It will automatically pick the most relevant section depending on your
  context, or if you choose to use the "All" option, you will continue to use
  the traditional class-based/search-based node picker.

- The Inspector gains some hints for Control/Layout, tracking the same behavior
  in Godot, up until now, we did not display that guidance.  #337.

- Small style touch up to the Inspector to make title sections more prominent
  (#444).

- FilePad: when duplicating a file, we will now propose a new file name, rather
  than making one up behind the scenes after you have chosen one, and will warn
  of a conflict instead of silently failing.

### Bug Fixes

- ScenePad: adjusted the UI for the Node Information slightly, to follow iOS
  conventions and idioms a little better, and display updated signal connections
  and groups (issue spotted on Discord).


- Recently, we started showing the keying on the inspector if there was an
  animation active - even if the animation pad was hidden.  Rectify this.

- Various 2D plugins were not working correctly due to a mistake introduced some
  months ago.  Their failures were subtle and not exactly obvious, like not
  being able to add points to a path, or immediately losing the focus.   Fixes
  #971 and various others.

- The CreateNode UI will now render the markup documentation correctly, rather
  than displaying markup (#1125).

- The "Export Game" option has moved into the menu, to avoid accidentally
  attemtping to export while developing a game.

- Project Launcher: It will no longer show "On my iPad" on iPhone, Vision or
  Macs, it will use the proper name and icon.

### Infrastrucutre Work

- Ongoing work on the new TileSet Editor.

- Various internal cleanups in preparation for localization, and long-term
  maintenance (like adopting internally Swift Lint).


## Build 1841

### Improvements

- Quick Open and Open Shader now have a "Recent" tab, fixing #87.

- You can now adjust the sizes for the ScenePad and FilePads, and updated the
  color of the divider bar, so it is easier to spot (both for these, as well as
  for the bottom plugin pads).

- Breakpoint line numbers are now white making them easy to read, completes the
  work for #288.

- Find Pad improvements: when using a keyboard shortcut, the "Find" field will
  be auto-selected;   New command "Find Next in Project" to navigate your find
  matches in the project;   It now highlights the line you tap on the Find
  Results.
  
- 2D Toolbar now hosts the Zoom control, and we added a new convenience method
  "Zoom to Fit" technicall not in Godot, but present in Apple's Freeform, it
  seemed like a good match.   Both the Godot custom center-selection and zoom
  controls are now removed from the UI.

- SpriteFrame pad is now sticky: if you open this pad, it will no longer vanish
  if you select another object.  Fixes #1109.

- Adds support for various kinds of samples (2d, 3d, 2d arrays) in the Shader
  Globals, this completes the support.   Fixes #147.

### Bug fixes

- The inspector now honors the read-only mode for the editor, fixes #939.

- Fixes support for closing a scene or project, when you had certain plugins
  activated (most noticeably, the Skeleton3D Editor triggered this), fixes
  #1107.

- Fixes project deletion not working for projects that were loaded externally,
  bug #1110.

- Fixes the "Create New Node" dialog not collapsing nodes when requested, 
  bug #1099.

- Fixes Input map list overlaps toggle, bug #981.

- Create New Node no longer reselects the first match if a windowing event
  happens (#1116).

- Dragging of files from the FilePad behavior matches Files.app behavior.

### Infrastructure

- Various internal refactorings from SwiftGodot class registration fixes, to
  cleaning up the interface between the file pad and Xogot.

- Ongoing work for the iOS native TileSet editor.

## Build 1835

- Game Sharing will now publish WebAssembly players, in addition to Xogot
  players.

- New shortcut handling: for users with a keyboard, rather than exposing all the
  keyboard shortcuts as a big "Xogot Shortcuts", they are now classified and
  organized in groups.   This was an important change, as I did not want to keep
  adding ad-hoc shortcuts because they ended up polluting the list, now we can
  add more shortcuts and keep them organized.

- Bring the SpriteFrame UI improvements to the Animation Player as well.

- Skeleton3D mode now works well with the Animation Editor.

- Makes Buttons in various Godot plugins easier to tap, following the changes in
  the general toolbars (#1093).

- Improved icons for the CollisionPolygon2D, and now they properly track their
  state (#1094), but this change also will improve any other Godot toolbar
  items.
  
- When renaming a node in the ScenePad, tapping anywhere else will complete the
  renaming operation.

- Various bugs that appeared when you opened a second project have been fixed
  (we noticed that signals could not be hooked up, but the core problem would
  manifest in other ways).   Fixes #1090, #770.

- Renamed the 'Recents' tab to 'Projects', and will no longer purely list recent
  files, but any projects you have opened.

- Debugger: when the program stops due to an error, you can get additional
  details by tapping on the error.

- Favorite nodes and recent nodes will always be saved, even if you dismiss the
  dialog.

- Panning on the 3D editor should not trigger auto-selection by accident (#907).

- Completed the array editing support, so it should be possible on the inspector
  to add certain kinds of objects (most noticeable, "Streams" into playlists,
  but would also happen in a few other places).  Completes the work on #787 and
  #634.
  
- SpriteFramesEditor: images were not updating right away, required switching
  tabs to update (#1092, #1086).

- The 2D editor no longer includes the "Center View" button as part of the 2D
  improvement efforts, the option is already available in the toolbar in the
  commands as "Center Selection"

- The old animation player UI is gone, giving us back some UI space.

## Build 1828

We are done with all the core features to sharing games (build a game and send a
link to another Xogot user to test) as well completing the new iPad native
interface for the Animation Editor - we would love to get your feedback on these
and to help us improve it.

### SpriteFrame Editor

Usability improvements:

* Control buttons have been adjusted to have a larger tappable region as well as
  adding additional space between the controls.
  
* Playback will now provide visual feedback.
  
* When selecting the sprite frame editor the first animation will be   
  auto-selected, rather than forcing you to select one first.

* When adding a new "SpriteFrames" to a resource, the SpriteFrame tabs will
  automatically show up, you no longer need to switch nodes to activate (#1085)

* Additionally, fixes a crash/hang if you had "inspected" the SpriteFrames and
  navigated out (#1087)

### General

* Various confirmation dialogs now use the standard system style as well.

* In Godot, while some data is stored outside of the range of values, their UI
  auto-clamps, so added support for auto-clamping these.  This was visible in
  particular in the "Theme Overrides" (#1083).

* Fonts for touch numeric input will match the font for other properties across
  the board (#1077)

* Tapping favorites or recents on the "Create New Node" will no longer match
  using a fuzzy match, but be precise up until the user types again (#1049).

* Placement of the popup for numeric input should now be automatic, rather than
  hardcoded (which was sometimes wrong, #1082)

* Adding a script with no template should instead use the "Empty" template
  (#1084), before this, it was ignoring the request.


## Build 1822

We are done with all the core features to sharing games (build a game and send a
link to another Xogot user to test) as well completing the new iPad native
interface for the Animation Editor - we would love to get your feedback on these
and to help us improve it.

### Usability Improvements:

* Performance improvements: switching from a node to another is now much faster,
  done by removing the peer work being done by Godot.

* Ability to set the Main Scene from the FilePad (it was possible from settings,
  but this is a convenience long-press option - #1065).

* When triggering a runtime error, the debugger will now display the information
  associated with the problem - previously, the debugger just stopped with no
  additional information (Discord).

* When creating new animations in the Animation Pad, we automatically switch to
  it.

* When adding a new "Other Node" on a fresh scene, we will go automatically into
  rename-mode.

* Bezier track and Subanimations are now supported in the Animation Editor -
  this completes all the editing tasks.

* When adding a new Animation track, we auto-select it.

* Most of our confirmation dialogs moved to use the style of iOS's alert.

### Fixes

* Steppers for the Snap Grid parameter are now 1, not 0.1 (#1073)

* Fixes accidental creation of points when using two-finger pan (#1059).

* Animation Key editing for setting animations (#1072)

* When selecting projects on the main screen, we no longer auto-launch one of
  them - oops (#1067), 

* Moving files over themselves on the file manager is a no-op, rather than
  corruption (#1081)

* Moving files over others that might get overwritten now has a SwiftUI native
  dialog (#989)

### Foundational Work

* Ongoing work on the new TileSet editor.

## Build 1800

### Changes to the New Animation Editor in Xogot

* When a new node is created, it will now start in "Rename Mode" in the
  ScenePad: we are experimenting with this new default as we replicate various
  tutorials to ensure a smooth operation (#1058)

* You can now create animations from the popup menu in the Animation tab (#1064).

* Moving keys in the Animation Track lanes now go into the undo/redo stack.

* The Animation Library now supports saving animations, libraries of animations
  and loading libraries of animations.   This completes that pending task.

* Volume tracks now render like Godot, with a color gradient for the volume -
  but I also bumped the size to be larger to read.

* Fixed a serious regression in SwiftGodot (#1024) which was manifesting itself
  as a crash while configuring the Input Event, but could happen in other
  places.

### SpriteFrame Editor

Changed the style to match the UI in the new Animation Editor, I cover this in
more detail here: https://blog.la-terminal.net/xogot-animations-tab/

### Overall Changes

* Games now show previously shared games with the option to re-download if your
  logged in! As well as all of your shared games

* Dropped the duplicate "Instantiate Child Scene" which gives us a little bit
  more space to work with.

* We harmonized the UI in the SpriteFrame pad to more closely match the user
  interface idioms of the new Animation Pad, so they are both more consistent,
  but it also helped clear up the user interface (#1055).

* Fixes to the 2D snap parameters, some properties were rendering degrees
  incorrectly, and two properties were loaded as zeroes due to a type mismatch. 

* Improves the look of the swipe icons on the ScenePad (#996, #1062)

### Testing Wanted: New Animation Editor

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

Known limitations:

* Confirmation for adding multiple tracks to the RESET track is not required.

* Can not currently add sub-animation tracks.

* The timeline rendering currentl only displays the timeline in seconds, but not
  in frames.

* Various advanced commands are not implemented: Bake Animation, Optimize
  Animation, Cleanup Animation, Make Easing Keys. 

* Missing Onion Support.

## Build 1788

### Changes New Animation Editor for Xogot

* Setting the snap value for an animation has been implemented.

* Renaming an animation without using the library has been implemented.

* Help is shown for both property nodes (when selecting a target for the
  animation) and for methods (when selecting a method to invoke in the animation
track).

* Added a convenience "Sprite Animation Track" option to "Add Track", which will
  automatically filter nodes to sprites, and will filter properties to those you
  can set - to reduce the complexity of animating sprites (#1041).

* It is now possible to edit sprite animations that were using sprite
  coordinates rather than just sprite frames.

* Ergonomics: When switching animations, we no longer default to the "RESET"
  track.

### Testing Wanted: New Animation Editor

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


Known limitations:

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

### Changes and Fixes

* When loading a scene that contained assigned nodes, we were discarding them
  from Node selectors - this has been fixed (Discord, #1056)

* Easing properties are now rendered with a small graph showing the effect in
  addition to the numeric value - and pressing long-press displays presets that
  you can use.

* The File Pad no longer shows the "search" input line by default, this now
  requires toggling it on - it provides an additional row of text to see the
  contents of your project.

* Fixes to integer property editors that were not refreshing when selecting new
  objects (very noticeable in AnimationKey inspection, #1053).

* Controlling gizmos on the 3D editor should be easier, as the touch area has
  been expanded (#652, TestFlight feedback)

* The SpriteEditor will no longer hang if you try to inspect objects while it is
  open (#863).

* The inspector will no longer undo/redo operations for animation keys,
  following the same behavior as the Godot editor (#938).

* Removing tracks from the animation editor now works (#1054).

* Auto-mapped Godot toolbar items are easier to tap, with a wider tap
  region. 

* Menus in auto-mapped toolbars that do not contain any text are now displayed
  with an ellipsis, previously they were completely hidden (#1030).

## Build 1774

* We now display the menu with options for animations in the 2D Editor that were
  previously not shown (#1030).

* Improved onboarding to animation: opening the animation tab will now offer to
  open an existing animation or create one.  And when an AnimationPlayer lacks
  animations, the option to create one is more prominent.

* The new AnimationEditor is now sticky, just like the original godot one, so
  you can explore all sorts of properties - including the animation themselves
  and property keys, solving one of the previously documented limitations.

* Fixes various corner cases in the new animation editor (#1045)

Major update from the last release, copying and adjusting here, as we would love
testing on it:


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
