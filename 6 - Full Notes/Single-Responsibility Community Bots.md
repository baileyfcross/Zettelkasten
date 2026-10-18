2026-10-18 16:07

Status: #baby

Tags: [[AI Community Bot Engineering]]

# Single-Responsibility Community Bots

Single-responsibility community bots separate distinct platform duties into independently understandable applications. The book assigns technical Q&A to one Discord bot and server-wide content moderation to another instead of building one large bot with every permission and rule.

The separation gives each bot a narrower event scope, credential, permission set, prompt, and failure mode. A Q&A change need not alter deletion authority, and a moderator can watch all channels without making the support bot do so. Multiple bots still need coordination rules, especially [[Bot Self-Message Suppression]], because their public actions become events visible to one another. Separation reduces conceptual and privilege coupling but does not eliminate shared-channel interaction.

# References

[[chatgptforjava.epub]]
