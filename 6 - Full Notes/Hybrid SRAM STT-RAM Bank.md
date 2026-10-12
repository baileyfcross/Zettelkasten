2026-09-28 03:43

Status: #baby

Tags: [[Hybrid Last-Level Cache Design]]

# Hybrid SRAM STT-RAM Bank

A hybrid SRAM STT-RAM bank contains a small fast SRAM region alongside a larger dense STT-RAM region. Frequently written lines can stay in SRAM, while read-dominant lines use STT-RAM capacity.

Using a hybrid bank near each core reduces local write pressure without giving up most of the nonvolatile memory's density advantage. Placement decisions are made by [[Cache Access-Aware Placement]] using per-line access history.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

