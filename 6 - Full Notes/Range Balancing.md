2026-09-28 23:03

Status: #baby

Tags: [[Game Balance and Progression]]

# Range Balancing

Range balancing separates an attribute's player-facing scale from a normalized internal scale. A designer chooses meaningful minimum and maximum values, represents each object as a percentage within that range, and translates it with `((maximum - minimum) × percentage) + minimum`.

The normalized scale makes relative placement easy to compare while the displayed scale can preserve familiar units such as speed or height. Changing the endpoints updates every dependent object without changing their relative ordering. This reduces ripple-effect balancing and separates systemic tuning of the range from individual tuning of each object's percentage.

# References

[[introductiontogamesystemdesign.pdf]]
