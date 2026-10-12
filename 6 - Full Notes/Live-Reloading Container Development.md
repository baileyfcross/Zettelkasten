2026-10-11 21:26

Status: #baby

Tags: [[Docker Development and Testing]]

# Live-Reloading Container Development

Live-reloading container development combines a source mount with a language-specific watcher that reloads or restarts the application when files change. Tools such as nodemon, framework development servers, Spring Boot DevTools, or `dotnet watch` restore a short feedback loop while the program still runs inside its declared dependency environment.

The watcher, development flags, and broad filesystem access should be confined to a development image or Compose profile. Production should use a stable startup command and immutable application content so an unreviewed file change cannot redefine the running service.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]
