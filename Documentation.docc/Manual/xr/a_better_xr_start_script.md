<!-- Remove this line to publish to docs.xogot.com -->
# A better XR start script

In <doc:setting_up_xr> we introduced a startup script that initialises our setup which we used as our script on our main node.
This script performs the minimum steps required for any given interface.

When using OpenXR there are a number of improvements we should do here.
For this we've created a more elaborate starting script.
You will find these used in our demo projects.

Alternatively, if you are using XR Tools (see <doc:introducing_xr_tools>) it contains a version of this script updated with some features related to XR tools.

Below we will detail out the script used in our demos and explain the parts that are added.

## Signals for our script

We are introducing 3 signals to our script so that our game can add further logic:

- focus_lost is emitted when the player takes off their headset or when the player enters the menu system of the headset.

- focus_gained is emitted when the player puts their headset back on or exits the menu system and returns to the game.

- pose_recentered is emitted when the headset requests the players position to be reset.

Our game should react accordingly to these signals.

## Variables for our script

We introduce a few new variables to our script as well:

- maximum_refresh_rate will control the headsets refresh rate if this is supported by the headset.

- xr_interface holds a reference to our XR interface, this already existed but we now type it to get full access to our [XRInterface](https://docs.godotengine.org/en/stable/classes/class_xrinterface.html#class-xrinterface) API.

- xr_is_focussed will be set to true whenever our game has focus.

## Our updated ready function

We add a few things to the ready function.

If we're using the mobile or forward+ renderer we set the viewports vrs_mode to VRS_XR.
On platforms that support this, this will enable foveated rendering.

If we're using the compatibility renderer, we check if the OpenXR foveated rendering settings
are configured and if not, we output a warning.
See <doc:openxr_settings> for further details.

We hook up a number of signals that will be emitted by the [XRInterface](https://docs.godotengine.org/en/stable/classes/class_xrinterface.html#class-xrinterface).
We'll provide more detail about these signals as we implement them.

We also quit our application if we couldn't successfully initialise OpenXR.
Now this can be a choice.
If you are making a mixed mode game you setup the VR mode of your game on success,
and setup the non-VR mode of your game on failure.
However, when running a VR only application on a standalone headset,
it is nicer to exit on failure than to hang the system.

## On session begun

This signal is emitted by OpenXR when our session is setup.
This means the headset has run through setting everything up and is ready to begin receiving content from us.
Only at this time various information is properly available.

The main thing we do here is to check our headsets refresh rate.
We also check the available refresh rates reported by the XR runtime to determine if we want to set our headset to a higher refresh rate.

Finally we match our physics update rate to our headset update rate.
Godot runs at a physics update rate of 60 updates per second by default while headsets run at a minimum of 72,
and for modern headsets often up to 144 frames per second.
Not matching the physics update rate will cause stuttering as frames are rendered without objects moving.

## On visible state

This signal is emitted by OpenXR when our game becomes visible but is not focussed.
This is a bit of a weird description in OpenXR but it basically means that our game has just started
and we're about to switch to the focussed state next,
that the user has opened a system menu or the users has just took their headset off.

On receiving this signal we'll update our focussed state,
we'll change the process mode of our node to disabled which will pause processing on this node and it's children,
and emit our focus_lost signal.

If you've added this script to your root node,
this means your game will automatically pause when required.
If you haven't, you can connect a method to the signal that performs additional changes.

> Note:
>
> While your game is in visible state because the user has opened a system menu,
> Godot will keep rendering frames and head tracking will remain active so your game will remain visible in the background.
> However controller and hand tracking will be disabled until the user exits the system menu.
>

## On focussed state

This signal is emitted by OpenXR when our game gets focus.
This is done at the completion of our startup,
but it can also be emitted when the user exits a system menu, or put their headset back on.

Note also that when your game starts while the user is not wearing their headset,
the game stays in 'visible' state until the user puts their headset on.

> Warning:
>
> It is thus important to keep your game paused while in visible mode.
> If you don't the game will keep on running while your user isn't interacting with your game.
> Also when the game returns to focussed mode,
> suddenly all controller and hand tracking is re-enabled and could have game breaking consequences
> if you do not react to this accordingly.
> Be sure to test this behaviour in your game!
>

While handling our signal we will update the focusses state, unpause our node and emit our focus_gained signal.

## On stopping state

This signal is emitted by OpenXR when we enter our stop state.
There are some differences between platforms when this happens.
On some platforms this is only emitted when the game is being closed.
But on other platforms this will also be emitted every time the player takes off their headset.

For now this method is only a place holder.

## On pose recentered

This signal is emitted by OpenXR when the user requests their view to be recentered.
Basically this communicates to your game that the user is now facing forward
and you should re-orient the player so they are facing forward in the virtual world.

As doing so is dependent on your game, your game needs to react accordingly.

All we do here is emit the pose_recentered signal.
You can connect to this signal and implement the actual recenter code.
Often it is enough to call [center_on_hmd()](https://docs.godotengine.org/en/stable/classes/class_xrserver_method_center_on_hmd.html#class-xrserver_method_center_on_hmd).

And that finished our script. It was written so that it can be re-used over multiple projects.
Just add it as the script on your main node (and extend it if needed)
or add it on a child node specific for this script.