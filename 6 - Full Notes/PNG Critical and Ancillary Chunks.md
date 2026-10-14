2026-09-28 04:01

Status: #baby

Tags: [[Lossless Web Image Formats]]

# PNG Critical and Ancillary Chunks

PNG chunk names distinguish data required to reconstruct the image from optional information. Critical chunks describe the image and its compressed pixels; an unknown critical type means a decoder cannot safely render the file.

Ancillary chunks can carry color, textual, physical-dimension, or other supporting information. Unknown ancillary chunks may be skipped, which makes the format extensible. Optimization can remove truly unnecessary ancillary data, but color or transparency information must not be discarded blindly. See [[Image Color Profiles]].

# References

[[highperformanceimages.pdf]]
