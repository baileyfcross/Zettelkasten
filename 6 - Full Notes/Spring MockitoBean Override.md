2026-11-08 16:45

Status: #baby

Tags: [[Spring Application Testing]]

# Spring MockitoBean Override

Spring's Mockito bean-override support replaces a selected bean in the test application context with a Mockito mock. The companion spy override wraps an existing bean so its real behavior remains available while calls can be observed or selectively stubbed.

The override belongs at a framework boundary whose behavior is outside the test's scope, such as replacing a service in a controller slice. A spy requires the target bean to exist, and excessive overrides can make a full-context test resemble an unclear unit test. Pure object collaboration is usually simpler to test without loading Spring at all.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
