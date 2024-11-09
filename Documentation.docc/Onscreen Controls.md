# Onscreen Controls in Xogot

Onscreen controls are crucial for testing and playing games directly on your iPad. For projects that are not designed for touch, Xogot offers two main ways to add onscreen controls to your project: using the **Project Setting** (available only on iOS) or adding the **Virtual Joystick Addon**. This guide will help you understand the differences between these methods and how to set each up.

## How to Enable Onscreen Controls

To enable onscreen controls, you can choose between the **Project Setting Option (iOS-only)** or the **Virtual Joystick Addon**. Each method has its own pros and cons:

### Project Setting Option (iOS-only) vs. Virtual Joystick Addon: Pros and Cons

#### Project Setting Option (iOS-only)

**Pros**:
- Directly integrated into Xogot, offering a native experience.
- Requires minimal setup and configuration.
- Automatically adapts to game settings without any extra work.

**Cons**:
- Limited to iOS devices.
- Customization options are more restricted compared to the Virtual Joystick Addon.

#### Virtual Joystick Addon

**Pros**:
- Works across all platforms where your project can run.
- Highly customizable; developers can change the appearance and behavior to suit game-specific needs.

**Cons**:
- Requires additional setup in your project.
- More effort to configure button mapping and visual elements.

## How to Enable Project Setting for Onscreen Controls

To use the **Project Setting Option** for onscreen controls:

1. **Open Your Project** in Xogot.
2. Tap the Switch button in the upper-righthand corner and choose **“Settings”**.
3. On the lefthand navigation, Find the **Input Devices** section and tap **“Virtual Controller”**.
4. Tap the toggle next to **“Enable Controller”** to turn the feature on.
5. Additionally, tap the toggle next to the buttons and thumbsticks that you want to enable or disable.  
  - Any buttons or thumbsticks that are not enabled will not be rendered
  - **Button Mapping**: Note that button names use the **Xbox naming convention** (e.g., "A," "B," "X," "Y"). Ensure your game actions are mapped appropriately to these controls for a consistent player experience.

Once these settings are saved, the onscreen controls will automatically appear when you run your project on an iPad.  The controls will automatically hide when your project is run on devices that have a physical controller connected.

## How to Add the Virtual Joystick Addon

To add the **Virtual Joystick Addon** to your project:

1. **Download the Addon**: Obtain the Virtual Joystick Addon from a trusted source like the official Godot Asset Library or GitHub.
2. **Add the Addon to Your Project**:
   - Open the **Files App** and locate the downloaded addon.
   - Copy the addon folder into your project’s **“addons”** directory inside the Xogot folder.
3. **Enable the Addon**:
   - In Xogot, go to **“Project > Project Settings”**.
   - Navigate to the **“Plugins”** tab.
   - Locate the **Virtual Joystick Addon** and toggle it to **“Enabled”**.
4. **Customize the Controls**: The Virtual Joystick can be customized by accessing the provided scripts and scenes. You can adjust the joystick visuals, size, and behavior to best fit your game.

After adding and configuring the Virtual Joystick, it will become available in your game, providing a flexible and fully customizable onscreen control option.

