2026-09-08 22:09

Status: #baby

Tags: [[Microsoft Bot Framework Applications]]

# Bot Channel Registration

A bot channel registration connects a published bot endpoint to clients and communication channels managed through Azure. It names the bot, identifies the `/api/messages` endpoint, and supplies application credentials used by the deployed bot.

Registration is distinct from publishing the ASP.NET Core service: one makes the bot code reachable, while the other tells the channel infrastructure where and how to reach it. Configuration values can be stored as App Service settings instead of embedded in application files.

# References

[[c8andnetcore30projectsusingazure.pdf]]
