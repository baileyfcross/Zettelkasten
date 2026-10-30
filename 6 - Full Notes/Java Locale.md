2026-10-30 15:57

Status: #baby

Tags: [[Java Application Interaction and Internationalization]]

# Java Locale

A Java `Locale` identifies a language and, optionally, region and variant conventions used to select localized resources and formats. It is not itself a translation; it is a key that helps an application choose suitable messages, number formats, dates, and other cultural conventions.

The default locale comes from the execution environment and can differ between machines. An application that requires stable machine-readable data should specify a locale-independent format, while user-facing presentation can use the user's selected locale and fall back through available resource bundles.

Java 21 added `Locale.availableLocales()` as a stream-oriented alternative to the array returned by `getAvailableLocales()`. The stream can be filtered and transformed directly without first treating the complete locale set as an array, fitting locale discovery into the ordinary Stream API.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
[[java25andbeyond_modernjavamadeeasy.epub]]
