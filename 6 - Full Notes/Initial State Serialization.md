2026-09-30 00:32

Status: #baby

Tags: [[Universal React Applications]]

# Initial State Serialization

Initial state serialization embeds the server's current application-state snapshot in the HTML response so the browser can construct its client store from the same data. The source writes JSON into a page-level variable before loading the client bundle.

Sharing the snapshot keeps the browser's first render aligned with the server-generated HTML and avoids beginning with an unrelated empty store. Serialization is a transfer boundary: the state must be converted to text in the response and parsed or consumed by client startup before later client actions diverge from that initial point.

# References

[[learningreact1.pdf]]
