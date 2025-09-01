Change Log
===

> Here's our record of all notable changes made to to this project

v1.3.2
---

* Add additional fallback for Workspace Detection ( Thanks @bjrmatos )
* Move Missing Workspace Message to Panel rather than show alert ( Thanks @colas31 )
* Revert Glob Pattern Change that used OS Path Separator

v1.3.1
---

* Fixed Naming Issue in PackageJSON

v1.3.0
---

* Added system indicator to VS Code File Excludes that cannot be removed
* Add the ability to not show picker and directly exclude selected file ( Thanks @rw3iss )
* Updated Workspace Detection to handle a few more unique use cases
* Updated default null settings to {} vs null ( Thanks @Himadu2000 )
* Added JSON Settings Linter Fix ( Thanks @MatthewTh0 )

v1.2.0
---

* Added new Hidden Items Pane Menu

![pane-menu](https://explorer-exclude.s3.amazonaws.com/pane-menu.gif?v=1.2.0)

v1.1.0
---

* Add Language Translations for [VS Code Supported Locales](https://code.visualstudio.com/docs/getstarted/locales#_available-locales)
* Fix bug with Command Pallet showing Explorer Exclude as available commands when it should not

v1.0.1
---

* Extensions like Prophet Debugger were creating virtual folders in / for accessing log files, and this created a weird bug in the logic that tried to detect project paths
* Added .github folder to help automate issue reporting
* Updated logo with dark background for search results Marketplace page

v1.0.0
---

* Initial Release
