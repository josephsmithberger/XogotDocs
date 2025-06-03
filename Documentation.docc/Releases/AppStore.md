# AppStore Release Notes

Release notes for public releases of Xogot to the App Store.

# Releases 

## Build 2413

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

This is the initial Godot release to the public on May 6th, 20254
