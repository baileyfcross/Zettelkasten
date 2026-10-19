2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Web Cloud and Data Applications]]

# JavaFX WebView and WebEngine

`WebView` displays HTML5 content inside a JavaFX scene, while its `WebEngine` loads and manages local files or remote pages. The implementation is based on WebKit and can range from showing documentation to embedding an existing web application. Because it is a JavaFX node, the view can be composed with ordinary controls and layouts.

JavaScript and Java can communicate through a bridge, allowing the host application to modify a page or react to web interactions. That can expose device or client capabilities unavailable in an ordinary browser. Embedding a site is convenient, but it does not automatically use the richer control model or service boundaries of a native client; those needs lead to [[JavaFX REST Service Integration]] and [[JavaFX Cloud Client Architecture]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
