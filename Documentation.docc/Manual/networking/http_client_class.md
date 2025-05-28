<!-- Remove this line to publish to docs.xogot.com -->
# HTTP client class

[HTTPClient](https://docs.godotengine.org/en/stable/classes/class_httpclient.html#class-httpclient) provides low-level access to HTTP communication.
For a higher-level interface, you may want to take a look at [HTTPRequest](https://docs.godotengine.org/en/stable/classes/class_httprequest.html#class-httprequest) first,
which has a tutorial available <doc:http_request_class>.

> Warning:
>
> When exporting to Android, make sure to enable the INTERNET
> permission in the Android export preset before exporting the project or
> using one-click deploy. Otherwise, network communication of any kind will be
> blocked by Android.
>

Here's an example of using the [HTTPClient](https://docs.godotengine.org/en/stable/classes/class_httpclient.html#class-httpclient)
class. It's just a script, so it can be run by executing:

It will connect and fetch a website.