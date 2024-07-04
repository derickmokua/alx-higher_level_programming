HTTP and URL Basics
What a URL is
A URL (Uniform Resource Locator) is a reference to a web resource that specifies its location and how to retrieve it.
What HTTP is
HTTP (Hypertext Transfer Protocol) is the protocol used for transmitting web pages and other web resources over the internet.
How to read a URL
A URL consists of several components:
Scheme: Specifies the protocol used (e.g., HTTP, HTTPS).
Domain Name: Identifies the server hosting the resource.
Port Number: Optional; specifies the port of the server.
Path: Specifies the location of the resource on the server.
Query String: Optional; provides additional parameters for the resource.
Fragment: Optional; identifies a specific section within the resource.
The scheme for an HTTP URL
The scheme for an HTTP URL typically starts with http:// for unencrypted connections or https:// for encrypted connections.
What a domain name is
A domain name is a human-readable address that represents a server's IP address on the internet (e.g., google.com).
What a sub-domain is
A sub-domain is a division of a domain that allows for separate web addresses under the same domain name (e.g., mail.google.com).
How to define a port number in a URL
A port number can be defined in a URL by appending :<port> after the domain name (e.g., http://example.com:8080).
What a query string is
A query string is a part of a URL that follows the path and starts with ?, containing parameters for a resource (e.g., ?id=123&name=example).
What an HTTP request is
An HTTP request is a message sent from a client (e.g., a web browser) to a server, requesting a resource (e.g., a web page).
What an HTTP response is
An HTTP response is a message sent from a server back to the client in response to an HTTP request, containing the requested resource or an error message.
What HTTP headers are
HTTP headers are additional information sent in both requests and responses, providing details such as content type, caching directives, and authentication.
What the HTTP message body is
The HTTP message body is the content of a request or response, which can include data (e.g., form submissions) or the content of a web page.
What an HTTP request method is
An HTTP request method specifies the action to be performed on a resource. Common methods include GET (retrieve), POST (submit data), and DELETE (remove).
What an HTTP response status code is
An HTTP response status code indicates the outcome of an HTTP request. Examples include 200 (OK), 404 (Not Found), and 500 (Internal Server Error).
What an HTTP Cookie is
An HTTP Cookie is a small piece of data sent from a server and stored on the client's browser, often used for session management or tracking user preferences.
How to make a request with cURL
cURL is a command-line tool for transferring data with URLs
What happens when you type google.com in your browser (Application level)
When you type google.com in your browser:
The browser initiates an HTTP request to resolve the domain name google.com to an IP address.
Once resolved, the browser sends an HTTP request to the server at that IP address.
The server processes the request, typically returning an HTML page.
The browser receives the HTML content and renders it, displaying the Google homepage.


