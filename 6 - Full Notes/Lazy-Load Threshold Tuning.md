2026-09-28 04:01

Status: #baby

Tags: [[Image Lazy Loading]]

# Lazy-Load Threshold Tuning

A lazy-load threshold controls how far before visibility an image request begins. The correct buffer must cover network latency, transfer time, and decode time under expected scrolling, without preloading so far ahead that most savings disappear.

Thresholds may be tuned by image size, connection quality, or placement. Measurement should include visible blank time and unused downloads, because optimizing only one metric pushes the system toward either excessive eagerness or disruptive lateness.

# References

[[highperformanceimages.pdf]]
