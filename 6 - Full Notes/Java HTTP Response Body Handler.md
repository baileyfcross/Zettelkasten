2026-10-30 16:54

Status: #baby

Tags: [[Java Platform API Evolution]]

# Java HTTP Response Body Handler

A Java HTTP response body handler tells `HttpClient` how to materialize response content. Predefined handlers produce a string, stream of lines, byte array, or file, allowing the representation to match the caller's intended consumption.

The handler is selected before sending the request, while the returned response separately exposes the status code, headers, and typed body. A file handler can therefore stream a download to a chosen path without first holding the entire page as a string.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
