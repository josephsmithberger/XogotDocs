<!-- Remove this line to publish to docs.xogot.com -->
# Recording with microphone

Godot supports in-game audio recording for Windows, macOS, Linux, Android and
iOS.

On iOS and iPadOS, it is important for your application to set the proper flags
for the audio session.  Visit the Project Settings in Xogot, and then tap "Show
Advanced", and then select Audio/General on the settings and look for "Session
Category".   Make sure that you set the category to "Record" or "Play and
Record", as this will inform the operating system of your intended use of the
audio system.

It is possible that you get an error like `AudioOutputUnitStart failed, code
2003329396`, this indicates that your Audio Session Category is not correctly set.

A simple demo is included in the official demo projects and will be used as
support for this tutorial:
https://github.com/godotengine/godot-demo-projects/tree/master/audio/mic_record.

You will need to enable audio input in the [Audio > Driver > Enable Input](https://docs.godotengine.org/en/stable/classes/class_projectsettings_property_audio/driver/enable_input.html#class-projectsettings_property_audio/driver/enable_input) project setting, or you'll just get empty audio files.

## The structure of the demo

The demo consists of a single scene. This scene includes two major parts: the
GUI and the audio.

We will focus on the audio part. In this demo, a bus named Record with the
effect Record is created to handle the audio recording.
An AudioStreamPlayer named AudioStreamRecord is used for recording.

@Image(source: "record_bus.png")

@Image(source: "record_stream_player.png")

The audio recording is handled by the [AudioEffectRecord](https://docs.godotengine.org/en/stable/classes/class_audioeffectrecord.html#class-audioeffectrecord) resource
which has three methods:
[get_recording()](https://docs.godotengine.org/en/stable/classes/class_audioeffectrecord_method_get_recording.html#class-audioeffectrecord_method_get_recording),
[is_recording_active()](https://docs.godotengine.org/en/stable/classes/class_audioeffectrecord_method_is_recording_active.html#class-audioeffectrecord_method_is_recording_active),
and [set_recording_active()](https://docs.godotengine.org/en/stable/classes/class_audioeffectrecord_method_set_recording_active.html#class-audioeffectrecord_method_set_recording_active).

At the start of the demo, the recording effect is not active. When the user
presses the RecordButton, the effect is enabled with
set_recording_active(true).

On the next button press, as effect.is_recording_active() is true,
the recorded stream can be stored into the recording variable by calling
effect.get_recording().

To playback the recording, you assign the recording as the stream of the
AudioStreamPlayer and call play().

To save the recording, you call save_to_wav() with the path to a file.
In this demo, the path is defined by the user via a LineEdit input box.