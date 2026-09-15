2026-09-15 02:14

Status: #baby

Tags: [[Convolutional Visual Architecture]]

# CNN Filter Bank

One [[Convolutional Kernel]] detects one kind of local pattern. A convolutional network therefore trains multiple kernels, or filters, in parallel when it needs to detect different visual features. Each filter produces its own [[Convolutional Feature Map]], and the maps can be assembled into a multifilter representation.

A later convolutional layer may analyze that combined representation, or a [[CNN Dense Layer Integration|dense layer]] may combine all filter outputs to make a final decision. The bank expands what the network can represent without abandoning [[Convolutional Weight Sharing]] within each individual filter.

# References

[[deeplearning_mit.epub]]
