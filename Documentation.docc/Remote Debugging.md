# Remote Debugging

Remote Debugging lets you develop and debug your project on one device
while running it on another. 

Remote Debugging lets you develop and debug your project on one device
while running it on another. For example, you can edit and inspect your project
on iPad while testing how it feels on iPhone — or connect any two devices in
whichever configuration works best for you.  

If you’re using Godot on your desktop and want to debug your project on an iPad 
or iPhone running Xogot, see <doc:Xogot-Connect>.

Remote Debugging uses Apple’s Multipeer Connectivity Framework to communicate
between devices. The devices do not need to be on the same Wi-Fi network, but
both must be nearby and signed into the same Xogot account.

---

## Setting Up the Remote Device

@Image(source: "iPhoneRemoteTab.png",
       alt: "A screenshot of Xogot on iPhone navigated to the Remote tab")

1. **Open the Remote tab.** Launch Xogot on the device where you want to run
   your game (for example, an iPhone) and switch to the **Remote** tab.

@Image(source: "iPhoneRemoteLogin.png",
       alt: "A screenshot of Xogot on iPhone waiting to log in")

2. **Sign in.** If you haven’t logged in before, you’ll see a **Login Required**
   message and a **Login** button. Tap **Login** and sign in with either **Sign
   in with Apple** or your **email address**.

@Image(source: "iPhoneRemoteDiscover.png",
       alt: "A screenshot of Xogot on iPhone navigated to the Remote tab waiting to log in")

3. **Make the device discoverable.** Once logged in, tap **Make Discoverable**.
   When prompted, grant Xogot permission to access the local network.

   If you are not prompted to grant permission, or you previously denied Xogot 
   Local Network access, you will need to open Settings app, search for Xogot, 
   and ensure that the Local Network setting is enabled.

@Image(source: "iPhoneRemotePermission.png",
       alt: "A screenshot of Xogot on iPhone warning of missing network permissions")

   After granting permission, the Remote tab will display **“Waiting for
   Connection”**. The device is now ready to receive a game from another Xogot
   installation.

@Image(source: "iPhoneRemoteWaiting.png",
       alt: "A screenshot of Xogot on iPhone waiting for a remote device to connect")

---

## Preparing the Host Device

@Image(source: "iPadRemoteGame.png",
       alt: "A screenshot of Xogot on iPad game view tab")

1. **Open your project.** On the device where you’ll be building and debugging
   (for example, an iPad), open your project and switch to the **Embedded Game
   View** tab (🎮).

@Image(source: "iPadRemoteLogin.png",
       alt: "A screenshot of Xogot on iPad game view tab waiting to log in")

2. **Sign in using the same account.** If you haven’t logged in before, tap the
   **Login** button and sign in using the **same Apple or email account** as on
   the remote device.

3. **Verify network access.** Xogot needs Local Network access to find nearby
   devices. To confirm this setting, open the **Settings** app, find **Xogot**,
   and make sure **Local Network** is enabled.

---

## Launching a Remote Session

@Image(source: "iPadRemoteSearch.png",
       alt: "A screenshot of Xogot on iPad game view ready to search for devices")

1. **Search for peer devices.** In the **Remote Device** section of the Game
   tab, tap **Search Peer Devices**. Your remote device should appear in the
   list once both devices are signed in and nearby.

@Image(source: "iPadRemoteStart.png",
       alt: "A screenshot of Xogot on iPad game view tab ready to start a remote connection")

2. **Start the session.** Select the target device and tap **Start**.

   * On the **host device** (for example, iPad), Xogot will display *“Syncing…”*
     along with a **Cancel Launching** button.
   * On the **remote device** (for example, iPhone), you’ll see *“Sync request
     received”* while the project is being deployed. The status area will show
     both the **project name** and the **name of the host device** launching it.


@Image(source: "RemoteSyncComplete.png",
       alt: "A paired iPhone and iPad preparing to launch a synced project")
---

## Running and Debugging

Once the game starts, both devices provide context-appropriate tools:

### On the Remote (Play) Device

A floating toolbar appears with several controls:

* **Stop** — End the running session from the target device.
* **Show Console** — Display the output log directly on the device.
* **Avoid Safe Areas** — Toggle whether the game fills the entire screen
  edge-to-edge.
* **Show Status Bar** — Show or hide the iPhone’s system status bar (time,
  Wi-Fi, cellular, battery).

@Image(source: "RemoteBreakpoint.png",
       alt: "A paired iPhone and iPad stopped at a breakpoint")

### On the Host (Build) Device

The **Debugger Pad** will automatically break at any active breakpoints in your
code. From there you can:

* Step through code, view the call stack, and inspect variables.
* Switch the **Scene Tree** to the **Remote** tab to browse the live scene
  running on the target device.
* Use the **Inspector** to view and modify properties of nodes selected in the
  remote scene tree.
* Changes you make in the Inspector are applied immediately to the running game,
  just as they would in the <doc:Embedded-Game-View>.

---

## Subsequent Runs

After you’ve successfully launched a remote session once, Xogot remembers your
connected device. Pressing **Play** again will automatically run the project on
the remote device, without needing to reconnect.

This behavior also applies to **Run Current Scene**, accessible from:

* The **long-press menu** on the Play button, or
* The **Debugger Pad** when no game is currently running.
