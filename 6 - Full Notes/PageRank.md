2026-09-06 00:13

Status: #baby

Tags: [[PageRank and Link Analysis]] [[Scalable Social Data Processing]]

# PageRank

PageRank is an algorithm that ranks web pages by interpreting hyperlinks as weighted endorsements. A page receives importance from its [[Backlink|backlinks]], and each source page divides its own importance evenly among its outgoing links.

The method represents the web as a [[Web Graph]], forms a [[Google Matrix]], and applies the [[Power Method]] until the [[PageRank Vector]] converges. The final values are relative and sum to one, allowing pages to be ordered by structural importance.

In a distributed dataflow implementation, each iteration emits outgoing links and partial rank contributions, groups contributions by destination, and stores or exchanges the revised ranks. Caching the graph and communicating updates collectively avoids rereading the unchanged network during every round.

# References

[[algorithms.epub]]

[[bigdataincomplexandsocialnetworks.pdf]]
