2026-10-30 15:57

Status: #baby

Tags: [[Java Control Flow and Exceptions]]

# Java Exception Wrapping and Custom Exceptions

A custom Java exception names a failure in the vocabulary of an application or API. It extends an appropriate checked or unchecked base and commonly provides constructors for a message and an underlying cause.

Wrapping translates a low-level failure while preserving the original throwable as the cause. This lets a higher layer expose a stable abstraction without discarding the diagnostic chain. Catching an exception only to print it or replace it with an unrelated message loses context unless that location can actually recover or add meaningful information.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
