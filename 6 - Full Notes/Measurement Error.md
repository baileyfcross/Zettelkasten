2026-09-06 21:16

Status: #baby

Tags: [[Spatial Tracking and Registration]]

# Measurement Error

Measurement error is the difference between a sensor reading and the physical quantity it is intended to represent. Systematic error introduces a repeatable bias, while random error produces changing noise or jitter around repeated measurements.

Calibration can reduce modeled systematic error. Filtering can reduce random variation, but often adds computation and delay, so an augmented-reality tracker must balance smoother measurements against temporal registration.

Changing the unit in which a measured quantity is reported does not supply a more accurate observation. Pryor's conversion discussion warns against mistaking displayed numerical resolution for meaningful accuracy; the precision of the original measurement should govern the converted result's reported digits. See [[Conversion Resolution versus Accuracy]].

# References

[[augmentedreality_pearson.pdf]]
[[dimensionalanalysisforunitconversionusingmatlab.pdf]]
