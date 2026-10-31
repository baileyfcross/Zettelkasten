2026-10-31 13:15

Status: #baby

Tags: [[Java Object Construction and Class Members]]

# Java Method Call Chaining

Method-call chaining lets one invocation's returned object become the receiver of the next invocation. An instance method can return `this` so several operations on the same object can be written as one left-to-right chain.

The chain works only when each intermediate return type exposes the following method. Returning the current object is therefore an API design choice: it supports fluent mutation or configuration, while a method with `void` return type ends the chain.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
