2026-09-06 20:34

Status: #baby

Tags: [[Web Data Query and Presentation]]

# Client-Side Paging

Client-side paging fetches a complete result set and divides it into pages inside the browser. Page changes are fast after the initial response because they do not require another server request.

The approach becomes inefficient when the dataset is large: the server still queries and transfers every row, and the client stores and processes values the user may never view. [[Server-Side Paging]] avoids that cost by requesting one slice at a time.

# References

[[aspnetcore3andangular9_3ed.pdf]]
