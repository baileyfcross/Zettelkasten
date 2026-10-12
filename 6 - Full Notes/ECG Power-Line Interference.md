2026-09-28 03:19

Status: #baby

Tags: [[Clinical Sensor and Signal Analytics]]

# ECG Power-Line Interference

ECG power-line interference is periodic contamination induced by the electrical supply, commonly appearing near the local mains frequency. It can mask small waveform details and distort measurements derived from an [[Electrocardiogram Signal]].

A notch filter can suppress the narrow frequency band, while adaptive filtering or empirical mode decomposition can address variation. The filter must be selective because aggressive removal can alter cardiac components that overlap the interference. Evaluation should compare noise reduction with preservation of waveform shape, not merely the reduction of spectral power at one frequency.

# References

[[healthcaredataanalytics.pdf]]
