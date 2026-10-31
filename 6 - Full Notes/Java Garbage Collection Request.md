2026-10-31 13:15

Status: #baby

Tags: [[Java System Runtime Services]]

# Java Garbage Collection Request

`System.gc()` asks the JVM to expend effort reclaiming storage from unused objects. It is a request for best effort, not an instruction that a particular object, number of objects, or amount of memory must be collected before the call returns.

An object must first become unreachable, such as after the last live reference is removed, but even eligibility does not promise a collection time. Code therefore cannot use a garbage-collection request as deterministic resource cleanup or proof that finalization will run.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
