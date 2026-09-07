2026-09-06 20:34

Status: #baby

Tags: [[Web Data Query and Presentation]]

# Data Sorting

Data sorting arranges query results by a selected field and direction. In a paged Web API, sorting must occur before the requested page is selected or records can appear in inconsistent positions between pages.

An Angular Material sort control can send the selected column and direction to the server. The server should accept only recognized fields rather than inserting arbitrary client text into a [[Dynamic LINQ]] expression.

# References

[[aspnetcore3andangular9_3ed.pdf]]
