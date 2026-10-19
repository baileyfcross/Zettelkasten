2026-10-18 22:56

Status: #baby

Tags: [[Java Social Platform SDKs]]

# Java Discord Client Libraries

Discord4J, JDA, and Javacord are Java libraries for building clients and bots against Discord. They expose entities such as guilds, channels, members, messages, and events, but differ in API design, asynchronous programming model, and ecosystem.

Selection should begin with the application's event and concurrency needs rather than superficial method-count comparisons. A bot must also declare the intents needed to receive particular event classes, protect its token, and respect platform permissions and rate limits. Because community libraries can track API changes at different speeds, the client should be hidden behind a small integration boundary. These considerations apply the general criteria in [[Social Platform Java Client Selection]] to the community-centered messaging described by [[Social Messaging Services]].

# References

[[enterprisesocialforthejavaplatform_sharesmashupslikesandwaystointe.epub]]
