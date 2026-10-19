2026-10-18 22:56

Status: #baby

Tags: [[Open Social Standards and Federation]]

# ActivityPub Federation Model

ActivityPub defines JSON-LD APIs for both client-to-server publishing and server-to-server federation. An actor exposes an outbox for activities it publishes and an inbox for activities delivered by other actors. Clients and servers use HTTP operations to create, retrieve, and distribute social objects.

The model separates a user's logical identity from the server that hosts it, allowing independently operated services to exchange posts and interactions. Common ActivityStreams types such as actor, activity, object, link, and collection provide the vocabulary carried by the protocol. Projects including Mastodon adopted it after earlier experience with [[OStatus Protocol Suite|OStatus]]. Together with other protocols, it forms a major interoperability route within [[Fediverse Protocol Diversity]].

# References

[[enterprisesocialforthejavaplatform_sharesmashupslikesandwaystointe.epub]]
