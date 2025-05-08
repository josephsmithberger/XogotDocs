# FAQ

Frequently Asked Questions

## What scripting languages are supported by Xogot?

Xogot only support's Godot's GDScript language, plugins authored in other languages are not
available on the iPad.

## What kind of plugins does Xogot support?

Xogot only supports GDScript-based plugins.   

Plugins written in C# or C++ are not available on Xogot/iPad.


## Why does Xogot seem to lock up when opening my project?

It can take a while to re-import assets for your project to the iPad, and one of
Xogot's most visible limitation currently is that the progress indicators in the
UI are not shown, which can be a little jarring when importing a large new
project and Xogot not responding.   

It may take an unexpectedly long time for the project to load.  A fix will be
coming soon.

## Why will my scene not open?
If you are unable to open scenes in your project, check if the output tab has errors like the following:

```
Texture (binding: 0, index 0) is not a valid texture.
Failed to create uniform set for batch.
Texture (binding: 0, index 0) is not a valid texture.
Failed to create uniform set for batch.
```

These indicate that you need to enable importing S3TC BPTC and ETC2 ASTC.  
       
To configure a compatible renderer, refer to this screenshot and follow the 
steps below:

@Image(source: "enable_imports.png"

1. Open settings by tapping the **...** in the upper-right corner and selecting **Settings**
2. Tap **Show Advanced** at the bottom of the *Project Settings* dialog
3. Type "*import*" in the search box
4. Enable **Import S3TC BPTC** **Import ETC2 ASTC**
5. Close the dialog

Then close and reopen the project so that these imports will run and the project should work as expected. 


## Why does my game show more of the canvas than it’s supposed to when running?

This issue might be caused by incorrect stretch settings. To resolve it:

1. Tap on the **...** button in the top-right corner of the app and select "Settings"
2. Scroll to the Display section on the left-hand column and tap "Window"
3. Scroll to the Stretch section and select a Mode of either "viewport" or "canvas_items."  

These modes will clip overflow and ensure that the game view is scaled correctly 
for the available screen space.


## Why is my TestFlight invite is expired, invalid, or having other issues?
The most likely issue is that you used a different email address than your 
Apple ID to sign up for the beta, or a new preview build was published after
your invite was sent.  

For any issues related to accessing builds on TestFlight, please 
[Contact Us](https://xogot.com/contact-us) and provide the email
address associated with your Apple account.



