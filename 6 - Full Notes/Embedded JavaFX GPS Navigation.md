2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Deployment and Platform Integration]]

# Embedded JavaFX GPS Navigation

The book's embedded proof of concept combines a Raspberry Pi 5, a small display, and a UART GPS receiver into an in-car navigation interface. A service parses NMEA readings from the sensor into latitude and longitude, while a JavaFX view centers a map on the reported location. Gluon Maps supplies a tile-based OpenStreetMap `MapView`, and a custom map layer renders the current position.

The project joins physical input, third-party dependencies, FXML-oriented UI design, and remote deployment in one application. Network access is needed to retrieve map tiles during field use, while a fixed location lets the interface be tested without connected GPS hardware. It demonstrates how [[JavaFX on Raspberry Pi]] can support a focused appliance rather than only a desktop-style sample.

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
