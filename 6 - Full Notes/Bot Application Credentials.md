2026-09-08 22:09

Status: #baby

Tags: [[Microsoft Bot Framework Applications]]

# Bot Application Credentials

Bot application credentials consist of the Microsoft application identifier and secret associated with a bot channel registration. The Bot Framework uses them to authenticate communication involving the deployed bot.

The secret is shown only when created and must be recorded or regenerated. The project places these values in Azure App Service settings so deployment configuration can override empty development-file values without committing the secret to source.

# References

[[c8andnetcore30projectsusingazure.pdf]]
