2026-09-06 20:41

Status: #baby

Tags: [[Progressive Web Application Capabilities]]

# Secure Origin

A secure origin is a web origin delivered through HTTPS without active mixed content. The encrypted and authenticated connection prevents network intermediaries from silently changing the code delivered to the browser.

Browsers require this trust boundary before enabling sensitive capabilities such as a [[Service Worker]]. Local development may receive a special exception, but a deployed progressive web application needs HTTPS.

# References

[[aspnetcore3andangular9_3ed.pdf]]
