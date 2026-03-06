# XogotDocs

XogotDocs contains the source documentation for **Xogot**, the iPad and iPhone
port of the Godot Engine developed by [Xibbon, Inc.](https://xibbon.com).  
The documentation is published at [docs.xogot.com](https://docs.xogot.com) using
Apple’s **DocC** documentation system.

---

## Overview

This repository serves as the **authoring and build source** for the Xogot
documentation set.  It combines original Xogot content written in DocC-compatible 
Markdown with material adapted from the open-source 
[Godot Engine documentation](https://github.com/godotengine/godot-docs), 
originally written in reStructuredText (reST).

All documentation can be edited, previewed, and built in **Xcode**, using the
included `Xogot.xcodeproj` and the `Documentation.docc` bundle as the primary
workspace.

---

## Repository Structure

| Path | Description |
|------|-------------|
| `.github/workflows` | GitHub Actions used to automatically build and publish the documentation from the `main` branch. |
| `Documentation.docc/` | The main DocC bundle containing all documentation topics, resources, and metadata. |
| `Xogot.xcodeproj` | The Xcode project used to open, edit, and preview the documentation locally. |
| `Xogot/` | A minimal Swift target that hosts the DocC catalog for Xcode previews. |
| `scripts/` | Conversion and utility scripts for transforming upstream Godot reST files into DocC Markdown. |

---

## Documentation Bundle Layout

Within `Documentation.docc`, the following directories and files are
particularly important:

| Folder | Description |
|---------|-------------|
| `Manual/` | Converted from `godot-docs/tutorials`. Contains adapted Godot tutorials. Files remain excluded from publication on [docs.xogot.com](https://docs.xogot.com) until the placeholder comment `<!-- Remove this line to publish to docs.xogot.com -->` is removed. |
| `Tutorials/` | Converted from `godot-docs/getting-started`. Entry-level guides for using Godot features within Xogot. |
| `Resources/` | Contains images, example projects, and other resource files referenced by the documentation. |
| `Releases/` | Includes release notes for TestFlight and App Store versions of Xogot. |
| `Documentation.md` | The top-level table of contents and navigation root for the published documentation. |

Additional articles may appear in the root of `Documentation.docc` and are
gradually being reorganized into subdirectories.

---

## Building and Previewing

You can build and preview the documentation locally in Xcode.

1. Open `Xogot.xcodeproj`.  
2. Select the **Xogot** scheme.  
3. Choose **Product → Build Documentation** or **Product → Run** to preview in
   the Documentation window.

You can also build and preview the same static site artifact used by GitHub
Pages:

```bash
./scripts/preview-pages.sh
./scripts/host-preview-pages.sh
```

Optional flags:

```bash
./scripts/preview-pages.sh --output-dir docs-local
./scripts/host-preview-pages.sh --dir docs-local --port 9000 --host 127.0.0.1
```

If you want local pages to include the same analytics IDs as production:

```bash
GOOGLE_ANALYTICS_ID=G-XXXXXXX GOOGLE_TAG_MANAGER_ID=GTM-XXXXXXX ./scripts/preview-pages.sh
```

---

## Publishing

The GitHub Actions workflow automatically rebuilds and republishes the site from
the `main` branch after each commit.

---

## Contributing

Contributions are welcome!  
You can help by improving existing tutorials, fixing formatting issues, or
validating converted content in Xogot.

- To contribute, fork this repository and open a pull request.  
- Join the discussion in the `#docs` channel on the [Xogot
  Discord](https://discord.gg/xogot).  
- Share feedback or report documentation issues through the [XogotDocs issue
  tracker](https://github.com/xibbon/XogotDocs/issues).  
- For questions or errors, email [docs@xogot.com](mailto:docs@xogot.com).

When adapting Godot content, please **retain the original attribution** and
follow the conversion conventions used in the `scripts/` folder.

---

## License

Unless otherwise noted, all files in this repository are licensed under the [MIT
License](https://opensource.org/licenses/MIT) © 2024-present Xibbon, Inc.

The following directories contain material adapted from the [Godot Engine
documentation](https://github.com/godotengine/godot-docs):

- `Documentation.docc/Manual`  
- `Documentation.docc/Tutorials`

Those directories are licensed under a combined structure:

- © 2014-present Juan Linietsky, Ariel Manzur and the Godot community  
  — licensed under the [Creative Commons Attribution 3.0 Unported License (CC BY
  3.0)](https://creativecommons.org/licenses/by/3.0/)  
- Modifications and additional content © 2024-present Xibbon, Inc.  
  — licensed under the [MIT License](https://opensource.org/licenses/MIT)

See the [LICENSE](./LICENSE) file for full details.

---

## Related Resources

- [Xogot Website](https://xogot.com)  
- [Xogot Blog](https://blog.xogot.com)  
- [Xogot Discord](https://discord.gg/xogot)
- [Godot Engine Documentation](https://docs.godotengine.org/en/stable/)  

---

_© 2024-present Xibbon, Inc. – Documentation built with DocC_
