# Testing Xogot: Godot on iPad 

Xogot is an iPadOS UI for the Godot game engine.  

If you want an invitation to participate in the early testing of Godot 
for iPad, you can sign up at [beta.xogot.com](https://beta.xogot.com).

Thank you for your interest in testing Xogot:  Godot for iPad. This small guide
will explain how to get the most of out this TestFlight release.

Xogot layers an iOS-native user experience on top of the existing Godot Editor
engine, so your projects should be fully compatible with the desktop edition of
Godot, and you should be able to move projects back and forth the two platforms.

One of our principles was to surface all the capabilities that you would need
for full interoperability in your project, so everything that you need should be
there, if it is missing, it should be considered a defect.   But it also means
that we took liberties to simplify the user interface when it comes to the Godot
editor itself, we only surface a handful of configuration options on purpose,
but we are open to bringing back a handful of those. 

## Providing Feedback

We really want to hear your feedback! You can give us feedback in any of these
ways:

- Inside Xogot: Take a screenshot of the issue by simultaneously pressing and 
  quickly releasing the "top button" (power button) and either volume button at 
  the same time, and then select **"Send Feedback"** from the "Done" drop down button.
- Open the TestFlight app and tap the **"Send Feedback"** button at the top of the Xogot page.
- Send us an email at support@xibbon.com
- File an issue on
  [github.com/xibbon/XogotIssues](https://github.com/xibbon/XogotIssues).

### Join the Community
We've set up a [Xogot Discord server](https://discord.gg/TDEcyfHZAh).  Please join us there!

### Bugs in Xogot
We are interested in finding bugs, crashes or unexpected
behaviors in the application.   If you find a bug, we would love if you could
describe how you triggered it, so we can fix it.
    
### Poor User Experience
While we worked hard to make sure that we provide a good
user experience for iPad users, we have also gotten used to it, and we want to
find out what things do not work as expected, are confusing or could be
improved.   We are interested in improving the user experience for iPad users,
both by ensuring that the UI works well on the iPad and its various input
systems as well as living up to the expectations of users on iPadOS.

### Improving over Godot’s defaults   
We think that we have a unique opportunity
to improve the workflow of using Godot that go beyond the surface [1].  Some
of the design choices and default choices from Godot make sense for
professionals using a desktop computer, but those are not necessarily great
for mobile users, we would love to hear what you think could be improved
overall to make your journey more pleasant. 

### Missed opportunities 
We prioritized what we thought were the high-traffic
areas of the user interface, but we might have missed some.   Let us know if
there are areas of the user interface that you are using extensively and you
would prefer a native user experience to be provided. 

We expose a new user interface for high-traffic parts of the application, and
fallback to the Godot-based UI when a piece of the UI has not been rewritten.

## Known Limitations

Please read the <doc:Preview-1> document for a list of known limitations in this
initial release.

## Notes

[1] For example, while we currently provide a compatible “Add Node” UI in Xogot,
we are aware that we could vastly improve this experience by replacing the
object-oriented system that displays the controls with common operations and
sensible defaults for different kinds of nodes.
