2026-09-06 20:52

Status: #baby

Tags: [[Dapper Data Access]]

# Dapper Multiple Results

Dapper can execute several SQL result sets in one database command and expose a reader for consuming them in order. A repository can retrieve parent records and related child records in one round trip, then associate them in memory.

This avoids the duplicated columns of a large join while still controlling round-trip count. The code must keep the result-set order and mapping contract synchronized with the SQL batch.

# References

[[aspnetcore3andreact.pdf]]
