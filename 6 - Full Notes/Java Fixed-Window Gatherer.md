2026-10-30 16:54

Status: #baby

Tags: [[Java Collection and Stream Evolution]]

# Java Fixed-Window Gatherer

The predefined Java `windowFixed(m)` gatherer partitions a stream into consecutive, non-overlapping lists of up to `m` elements. It changes many individual inputs into fewer grouped outputs while remaining an intermediate stream operation.

If the input ends before the final window is full, that last list contains the remaining elements rather than being discarded. Fixed windows can group time-series observations into intervals or form batches that later stream stages process as units.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
