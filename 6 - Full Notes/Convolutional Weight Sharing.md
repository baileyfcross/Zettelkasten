2026-09-15 02:14

Status: #baby

Tags: [[Convolutional Visual Architecture]]

# Convolutional Weight Sharing

Convolutional weight sharing means that neurons inspecting different image locations use the same learned weights. Because the weights define a detector, those neurons search for the same pattern in different [[CNN Receptive Field|receptive fields]]. A feature can be found wherever a member of the shared group responds, rather than requiring a separately learned detector at each position.

Sharing also reduces the number of trainable parameters compared with assigning independent weights to every local neuron. It supplies a useful spatial assumption to a [[Convolutional Neural Network]]: the local pattern worth detecting may recur at multiple locations. Pooling can add tolerance to location, but it can also discard information about the arrangement of parts.

# References

[[deeplearning_mit.epub]]
