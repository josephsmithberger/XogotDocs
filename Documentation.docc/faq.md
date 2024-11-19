# FAQ

Frequently Asked Questions

## Why does Xogot seem to lock up when opening my project?

It can take a while to re-import assets for your project to the iPad, and one of
Xogot's most visible limitation currently is that the progress indicators in the
UI are not shown, which can be a little jarring when importing a large new
project and Xogot not responding.   

It may take an unexpectedly long time for the project to load.  A fix will be
coming soon.

## Why can I not see my game when my project loads?

If you open your project Xogot and your viewport is missing (as in the image
below), you might need to adjust your settings for your game to fully work on
iPad.   

@Image(source: "RendererOpenGL.png",
       alt: "A screenshot of Xogot with an entirely white viewport")


Xogot is based on Godot 4.3, which imposes a few limitations when it
comes to the renderers running on mobile devices (Forward+ and Mobile work,
but OpenGL does not).   

To configure a compatible renderer, refer to this screenshot and follow the 
steps below:

@Image(source: "ConfigureRenderer.png",
       alt: "A screenshot of Xogot with Renderer Project Settings displayed")

1. Tap on the switch button in the top-right corner of the app and select "Settings".  
2. Scroll to the Rendering section on the left-hand column and tap "Renderer" 
3. Make sure that you do not have OpenGL selected.
4. Once you have selected a compatible renderer, close and re-open the project

For the final release, we will be switching to a Godot-4.4-based system which
will support all three renderers.
