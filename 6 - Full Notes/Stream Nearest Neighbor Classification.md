2026-09-14 21:00

Status: #baby

Tags: [[Streaming and Scalable Classification]]

# Stream Nearest Neighbor Classification

Stream nearest-neighbor classification predicts from a maintained sample of recent or representative labeled observations. Because storing every case violates bounded-memory requirements, the learner must discard, summarize, or selectively retain instances.

The retention policy defines the model's temporal memory. Keeping recent cases aids adaptation, while preserving rare or boundary cases protects predictive coverage that a simple sliding window could erase.

# References

[[dataclassification.pdf]]
