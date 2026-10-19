2026-10-18 22:56

Status: #baby

Tags: [[Java Social Platform SDKs]]

# BigBone Mastodon Client

BigBone is a Java client library for the Mastodon API. It exposes Mastodon resources and operations through Java-friendly calls, allowing an application to work with accounts, statuses, timelines, notifications, and other server capabilities without hand-building every HTTP exchange.

A Mastodon client connects to a chosen server rather than to one universal central host. Server version, enabled features, and moderation policy can therefore affect behavior, and the application must not assume that every instance exposes an identical environment. BigBone addresses the platform API; cross-server delivery is governed by [[ActivityPub Federation Model]]. That distinction makes [[Social Platform Java Client Selection|client-version compatibility]] and graceful handling of instance differences important.

# References

[[enterprisesocialforthejavaplatform_sharesmashupslikesandwaystointe.epub]]
