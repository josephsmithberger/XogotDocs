# Differences between Xogot and Godot

Notable differences in adapting Godot to iPad

## Only gdscript

Xogot does not include support for C#, nor other compiled languages, including
Swift and Rust.

## Only gdscript add-ons and plugins

Xogot only support addons and plugins that are written in gdscript.  Extensions
written in C++, C#, or other compiled languages are not currently supported.

## Project Settings

In Xogot, tap the menu button in the upper-righthand corner and choose **“Settings”**
to open Project Settings.  The individual Project Settings tabs from Godot, such as
Input Map, Autoload and Plugins, can be navigated to by tapping on the **General** in
the drop-down list at the top of the Settings dialog.

## Visual Shader Editor

While Xogot projects can include and run Visual Shaders that were created in Godot 
on the desktop, Xogot does not currently include the Visual Shader Editor, so it is
not currenlty possible to create or update Visual Shaders in Xogot.  

## Layout changes 

Xogot's UI has been adapted to better suit the iPad, including making parts of
the UI more tappable, and removing some parts of the user interface to economize
available real estate.  Many toolbar icons have been replaced with Apple's 
SF Symbols to better match the look and feel of iPadOS.  Because the iPad does 
not have the concept of hovering over a button, tooltips are not surfaced in the
UI.  <doc:Xogot-User-Interface> provides a guide to the layout and structure of 
Xogot's toolbars.
