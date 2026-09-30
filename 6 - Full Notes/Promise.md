2026-09-06 20:37

Status: #baby

Tags: [[Front-End Service Design]] [[Modern JavaScript Language Features]]

# Promise

A promise represents the eventual success or failure of one asynchronous operation. Consumers attach handlers that run when the operation settles instead of blocking while the result is unavailable.

The [[Fetch API]] uses promises. Angular HttpClient instead returns an [[Observable]], which supports stream-oriented composition and framework operators in addition to delivering an HTTP result.

A promise is constructed around an asynchronous operation with functions for fulfillment and rejection. Consumers attach success and failure handlers with `then`, allowing later work to be described without blocking while a request, timer, or other delayed result completes.

# References

[[aspnetcore3andangular9_3ed.pdf]]

[[learningreact1.pdf]]
