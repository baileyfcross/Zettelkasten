2026-10-07 17:18

Status: #baby

Tags: [[Abstract Data Structures]]

# Linear Probing Hash Table

A linear probing hash table keeps all entries in one array. When the hashed slot is occupied, it checks subsequent slots in a fixed cyclic order until it finds the key or an available position.

Lookup must follow the same probe sequence used for insertion. Deletion cannot simply create an ordinary empty slot inside a cluster because that could prematurely stop later searches; the implementation must mark the slot specially or repair the affected probe chain.

# References

[[statisticalcomputingincplusplusandr.pdf]]
