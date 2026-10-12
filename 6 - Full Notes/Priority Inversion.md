2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Locking]]

# Priority Inversion

Priority inversion occurs when a high-priority task waits for a lock held by a lower-priority task, while medium-priority work prevents the holder from running and releasing it. The effective delay can violate real-time assumptions even though the high-priority task remains logically most urgent.

Priority inheritance mitigates the inversion by temporarily boosting the lock owner to the highest relevant waiter priority. Linux implements this behavior with the [[RT-Mutex]], while correct lock scope and bounded critical-section work remain essential for predictable latency.

# References

[[linuxkernelprogramming_secondedition.pdf]]
