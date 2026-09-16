2026-09-05 16:28

Status: #baby

Tags: [[Speech and Acoustic Modeling]] · [[Feature Engineering Foundations]]

# Feature Vector

A feature vector is an ordered set of numerical measurements representing one observation. In speech recognition, it commonly summarizes the spectral properties of a short [[Speech Frame]].

A sequence of feature vectors is more compact and model-ready than the original waveform. The [[Acoustic Model]] uses the sequence to estimate which phonetic states most plausibly produced the signal.

More generally, a feature vector assigns one value to each feature selected for a data object. Using a fixed feature set places heterogeneous objects into a common coordinate representation, allowing learning algorithms to compare, partition, or predict them.

# References

[[aiassistants.epub]]

[[featureengineeringformachinelearninganddataanalytics.pdf]]
