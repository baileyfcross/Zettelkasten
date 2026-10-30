2026-10-30 15:57

Status: #baby

Tags: [[Java Collections and Date-Time]]

# Java Instant and Zoned Date-Time

`Instant` represents a point on the UTC timeline, making it appropriate for timestamps and elapsed ordering. `ZonedDateTime` combines local date-time fields with a `ZoneId`, allowing zone rules and daylight-saving transitions to determine the corresponding instant.

An offset alone records displacement from UTC but not the region's future and historical rules. Converting between an instant and a zone changes the displayed local fields without changing the moment; attaching a zone to an existing local time instead interprets that local value under zone rules and can encounter gaps or overlaps.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
