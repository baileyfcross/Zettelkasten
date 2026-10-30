2026-10-30 16:54

Status: #baby

Tags: [[Java Platform API Evolution]]

# Java Bounded String Search

A bounded Java string search looks for a character or substring only between supplied begin and end indexes. It reports the first match in that range rather than forcing the caller to allocate a substring or search the entire original text.

The range makes a parsing phase explicit—for example, locating a marker only inside one header or record segment. Index boundaries still require the same care as other string indexing operations so that the search window describes the intended portion.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
