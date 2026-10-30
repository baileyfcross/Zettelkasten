2026-10-30 16:54

Status: #baby

Tags: [[Java Collection and Stream Evolution]]

# Java Stream mapMulti

Java's `mapMulti` intermediate operation lets one input emit zero, one, or many output elements through a supplied consumer. It covers many flattening tasks without creating a temporary stream for each source element as [[Java Stream map and flatMap|flatMap]] normally does.

The operation is useful for conditional emission and expanding small iterables. Its callback controls exactly which values enter the downstream pipeline, so it can combine filtering and one-to-many mapping while preserving the lazy [[Java Stream Pipeline]].

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
