<!-- Remove this line to publish to docs.xogot.com -->
# What is GDExtension?

**GDExtension** is a Godot-specific technology that lets the engine interact with
native shared libraries
at runtime. You can use it to run native code without compiling it with the engine.

There are three primary methods with which this is achieved:

- gdextension_interface.h: A set of C functions that Godot and a GDExtension can use to communicate.

- extension_api.json: A list of C functions that are exposed from Godot APIs (<doc:scripting_languages#Core-Features>).

- <doc:gdextension_file>: A file format read by Godot to load a GDExtension.

Most people create GDExtensions with some existing language binding, such as <doc:index>,
or one of the <doc:what_is_gdnative_third_party_bindings>.

## Version compatibility

See <doc:what_is_gdextension#Version-Compatibility>, which applies to all GDExtensions.
