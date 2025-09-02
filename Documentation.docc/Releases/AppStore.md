# AppStore Release Notes

Release notes for public releases of Xogot to the App Store.

# Releases 

## 1.2.0 (Build 2757)

Two major themes.   Xogot comes to iPhone, and we now have a free tier edition,
check our blog post for additional details.

## Improvements

* New 'use_hidpi' setting under the display/window/stretch settings, which is
  independent of the previous attempt we had to support HIDPI by extending the
  meaning of the 'display/window/stretch/scale_mode' to have an 'auto' mode,
  which was not compatible with Desktop Godot.

* It is now possible to edit the labels of collission masks - the feature had
  not been wired up before (Discord, #1488)

* Double-tapping a node in the create node dialog will create the node, this
  makes it consistent with the existing behavior in the "All" tree-view that
  allowed this behavior (#1481).

* Dropping files from the file pad into the scene pad should work if you drop in
  an empty region, and not just when you drop on top of an existing node
  (Discord, #1492).

* We completed a memory leak journey, we have been chasing some pesky memory
  leaks when closing a project and going back to the main screen.   This will
  also improve the reliability after closing a project, because these dangling
  objects kept running for a little while after the editor closed, and this
  should no longer happen.

* True and false keywords should now be highlighted (Discord, #1491)

* Import button on the toolbar now shows a menu, which will help users determine
  that this is an import operation with a label, and adding a simple option to
  import Photos from the user's photo library (#1482).

* Rectangle Editor: in a few places, the rectangle editor will now display
  'Edit Rectangle' and when pressed, it will show up an
  interactive view to select a region from the image (Discord, #1465).

* SpriteSheetImport: will now remember the settings that you had when importing
  a new texture if the size of the texture matches the previous size (Discord
  request).
  
* Grouped numeric input: we will now auto-select in the popup the entry that you
  tapped on (Discord).

* UI consistency: in places where we guide our users to the next step, rather
  than rolling our own UI, we now use the system ContentUnavailableView idiom
  for more consistency.

* Better support for iOS 2026 user interface, even if it is not using those APIs
  just yet. 

* The virtual controllers that are displayed when you start a game automatically
  hide if you switch out of the "Game" mode (#1282)

* It is now possible to start a new chat from the Chat window.

* Add ability to extract TileMapLayer from TileMap #1509

* You can now configure in Xogot Settings your default execution target, either
  the embedded window, or a separate window.   

* You can now copy the error message when there is a runtime error (#1122)

* Happier colors for the launch screen, it was making me sad, and additionally
  Axolotl Rex will greet you on your gaming journey.

* You can now change the font for the code editor and consume system fonts, my
  previous attempt merely allowed you to pick a different fixed font, now you
  can pick any user-installed fonts (#1539, Discord).

The TileMap and TileSet plugins can now be docked on the left or right sides,
  to assist in your editing needs (#1529, Discord)

* Added keyboard shortcuts for various operations (Cut, Copy, Delete, Duplicate
  Nodes and Select All).   Some of these shortcuts might only be visible on iOS
  26, as they are exposed via the built-in system commands (#1549, Discord).

* Animation editor tab: significant performance improvements when switching
  animations and when playing back animations (#1562, Discord).


* TextureRegionEditor will now auto-size to a convenient size, and the handles
  will be scaled accordingly.   Plus various small improvements to it (#1557)

* When switching an animation, stop a playing animation (#1561)


* Expression Evaluator: The Godot REPL is now available in Xogot (#1412), there
  is a new option that you can toggle on the bottom of the screen when the
  debugger is selected to switch to the REPL window.

* Inspector: reviewed the padding of some elements and discovered a handful of
  pixels here and there that were needlessly consuming space that was needed.   

* Reparenting of nodes will now report an error if you are editing a foreign
  scene, and the operation is not allowed (Discord).  My preference would have
  been to remove the menu, but new Apple guidance on menus is to not make menus
  conditional, so we are going to start moving into that direction.

* On an empty scene, the "Other Node" or tapping the "+" sign will bring up the
  new node selection dialog, rather than defaulting to the limited tree-view
  one (#1501)

* The reference guide now has an index to search by words in the documetnation
  (#1379, Discord).


* Reference Guide: when searching for keywords, it now allows multiple words to
  be specified, requiring all matches to be present, as well as the notation
  "-word" to exclude any matches containing that word.

* Added keyboard shortcuts to increase and decreate the text editor font size
  using Command-Shift-minus and Command-shift-plus.  (Discord, #1323)

* Provides visual guidance that the editor is closing down a project when you go
  back to the main screen (#1454).

* The Free Edition will now have the debugger available, but will limit the
  project size.

* Added support for sub-property picking in the AnimationPlayer - be warned that
  while both Xogot and Godot support this, the feature is not fully baked in
  Godot, and has various limitations:
  https://github.com/godotengine/godot/issues/99115
  
* Godot native popovers now use our Floating Window (the feature part of a bug
  request #1531).


* The Animation Player editor previously had a number of options under the menu
  for the animation, but there was also an "Options" menu for one single task,
  so I unified those.

* For built games, if the game uses audio permissions, it will ask before
  launching, to make sure you have permissions to use those features (Completes
  the last part of #1456).


## 1.1.2 (Build 2413)

* If you have an Apple Pencil, when you hover over properties in the inspector, you will get a documentation tooltip.

* It is now possible to search for text in the documentation pages and trigger search with Command-F in the code editor.

* It is now possible to select multiple nodes and alter their common properties together by changing the values in the inspector.

* Your games can now take advantage of the accelerometer

* You can now use the drag gesture on numeric values on the grouped editors to alter values without having to type the numbers.

* Navigation to linked resources is now consistent, tapping on it will always disclose it, in the past, some resource required tapping on "..." and then "Inspect".

* Project Settings, Input Map now includes a letters and numbers filter option, to more easily connect keys and numbers to events.

* Simplifies the view switching, rather than using Command-Shift-Number, you can now just use Command-Number

* Added more keyboard shortcuts, they are contextual and visible by holding the command key.

* Performance improvements to the TileSet and TileMap editors.

* It is now possible to alter the scaling behavior in the UI (freeform vs uniform) when resizing objects.

* When you have a hardware keyboard, the shift, control, alt and meta keyboard modifiers can now be used to modify certain operations in the 2D and 3D editors like uniform resizing.

* Made it simpler to set the "Expand" flags when editing a SizeFlags property, it no longer requires opening up a popup menu, and polished the UI.

* You can now drag images into the TileSet editor.

* Error messages are no longer obscured by the disclosure buttons.

* Dividers no longer use a different color, which was making the user interface feel bumpy.

* We no longer reset the help browser position when you switch tabs.

* On the FilePad, Tapping on a favorited folder will scroll down to that folder.

* Modifying numeric values for nodes are now reflected immediately in the object when dragging values.

* Fixed a slowdown during debugging when selecting a remote node that had a preview image.

* Fixed a problem with some array values that could not be reordered.

* Fixed a case where dragging the root node into a child node would remove the nodes.

* Fixed several crashing conditions.

## Build 2353

* Fixed a crash that would trigger when importing new projects

## Build 2299

* Shader Editor now surfaces a "File" menu for common file operations on shaders.

* Added keyboard shortcuts for toggling various user interface elements on and off, running and stopping programs.

* The "Add Node" dialog now has a convenience "ColorRect" added.

* The animation editor will automatically scroll the view as you navigate using the arrow buttons at the bottom of the screen.

* FilePad: added a swipe gesture to delete a node.

* FilePad: input text will now give additional space when editing by hiding unused items.

* Added support for running Editor Scripts.

* Animation Editor has further guiding posts to help you get started, and will now trigger the toolbar keying support for new animations, without requring opening and closing the tab.

* Performance improvements to the TileSet and TileMap editors.

* Now supports other subscription tiers.

* Fixes a bug that prevented games from running twice in some conditions.

* Fixes the list of viewport display modes, we were missing one display mode.

* Changing the size of the text editor now updates immediately.

* 3D Editor: it is now possible to change the color of the sun.

* VisualShaderEditor: it is now possible to add new shader editor nodes.

* Inspector: Fixes an array editor bug, shows the current anchor selection, colors for animation keys can now be updated continuously, 

* Text Editor: Option+Delete and Option+Left now work correctly, and you can jump to a line using the Command-L shortcut.

* Consistency changes to double-tapping on file selectors.

* Xogot would enter dark mode, but could not go back to light mode, this has been fixed.

* Fixed inconsistency of icons in the Add Node vs Scene Pad views.

## Build 2225

* We clear error messages when we restart a game

* Bottom tabs no longer collapse when an action takes place on them (Animations, Sprite Editor).

* By default scripts and scenes are automatically synchronized during development, like Godot on desktop does.

* It is now possible to edit array of NodePaths exported by scripts in the inspector.

* The animation lenght no longer auto-resets to one second.

* It is now possible to zoom out from TileSets and not force the full size.

* Selected Tiles in the Tile pads now get a more prominent selection indicator.

* Rendering options for the 3D viewport now match their descriptions.

* Virtual controllers that were sticky after a game ended now get properly removed from the screen.

* When Xogot is running in half-screen, tapping on the "Script" icon, will now automatically hide the sidebar, so you can see your script.

## Build 2220

This is the initial Godot release to the public on May 6th, 2025
