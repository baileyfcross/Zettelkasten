2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Locking]]

# Sequence Lock

A sequence lock lets readers copy a small data snapshot without taking a conventional lock, then verify whether a writer changed it during the read. Writers serialize updates and change a sequence counter before and after the critical section; a reader retries if the count was odd or changed.

Readers must tolerate retries and cannot safely follow pointers that a writer might free. Sequence locks fit compact, frequently read values such as timekeeping data, while lifetime-sensitive object graphs usually need another technique such as [[Read-Copy-Update]].

# References

[[linuxkernelprogramming_secondedition.pdf]]
