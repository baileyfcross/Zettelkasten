2026-09-06 20:52

Status: #baby

Tags: [[Web Performance and Scalability]]

# Cache Entry

A cache entry associates a key with a stored value and expiration behavior. An endpoint or repository first checks for the key, computes and stores the value when absent, and reuses it while the entry remains valid.

Entry lifetime determines the balance between reuse and freshness. Keys must also distinguish every input that can change the result, or unrelated requests may receive the same cached representation.

# References

[[aspnetcore3andreact.pdf]]
