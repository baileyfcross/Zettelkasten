2026-09-05 16:28

Status: #baby

Tags: [[Virtual Assistant Architecture]]

# Wake Word

A wake word is a short activation phrase that tells a listening device to begin processing a request. Detection can run locally so that continuous ambient audio does not need to be sent to a remote [[Speech-to-Text Service]].

A device can maintain only a short rolling audio buffer and transmit speech after a likely activation. This design reduces unnecessary network processing, although false activations and privacy expectations still require care.

# References

[[aiassistants.epub]]
