<!-- Remove this line to publish to docs.xogot.com -->
# HTML5 shell class reference

Projects exported for the Web expose the :js:class:`Engine` class to the JavaScript environment, that allows
fine control over the engine's start-up process.

This API is built in an asynchronous manner and requires basic understanding
of Promises.

## Engine

The Engine class provides methods for loading and starting exported projects on the Web. For default export
settings, this is already part of the exported HTML page. To understand practical use of the Engine class,
see <doc:customizing_html5_shell>.

### Static Methods

Promise | :js:attr:`load <Engine.load>`**(**string basePath**)**
------- | ------------------------------------------------------
void | :js:attr:`unload <Engine.unload>`**(****)**
boolean | :js:attr:`isWebGLAvailable <Engine.isWebGLAvailable>`**(**[ number majorVersion=1 ]**)**

### Instance Methods

Promise | :js:attr:`init <Engine.prototype.init>`**(**[ string basePath ]**)**
------- | --------------------------------------------------------------------
Promise | :js:attr:`preloadFile <Engine.prototype.preloadFile>`**(**string|ArrayBuffer file[, string path ]**)**
Promise | :js:attr:`start <Engine.prototype.start>`**(**EngineConfig override**)**
Promise | :js:attr:`startGame <Engine.prototype.startGame>`**(**EngineConfig override**)**
void | :js:attr:`copyToFS <Engine.prototype.copyToFS>`**(**string path, ArrayBuffer buffer**)**
void | :js:attr:`requestQuit <Engine.prototype.requestQuit>`**(****)**

## Engine configuration

An object used to configure the Engine instance based on godot export options, and to override those in custom HTML
templates if needed.

### Properties

type | name
---- | ----
boolean | :js:attr:`unloadAfterInit`
HTMLCanvasElement | :js:attr:`canvas`
string | :js:attr:`executable`
string | :js:attr:`mainPack`
string | :js:attr:`locale`
number | :js:attr:`canvasResizePolicy`
Array.<string> | :js:attr:`args`
function | :js:attr:`onExecute`
function | :js:attr:`onExit`
function | :js:attr:`onProgress`
function | :js:attr:`onPrint`
function | :js:attr:`onPrintError`