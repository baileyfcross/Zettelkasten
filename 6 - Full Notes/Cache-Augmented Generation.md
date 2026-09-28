2026-09-27 21:45

Status: #baby

Tags: [[Azure AI Application Architecture]]

# Cache-Augmented Generation

Cache-augmented generation places a bounded knowledge set directly in the model context and reuses the prepared context when the platform supports prompt caching. It can avoid a retrieval stage for compact, relatively stable corpora, reducing retrieval variability and simplifying the request path. The tradeoff is that context size, refresh cost, token limits, and stale material become central constraints, so the pattern is less suitable when knowledge is large, rapidly changing, or individually permissioned.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]
