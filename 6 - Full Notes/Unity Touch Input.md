2026-10-12 01:03

Status: #baby

Tags: [[Unity 2D Interface and Mobile Development]]

# Unity Touch Input

Unity touch input represents each active contact with data such as finger identity, screen position, movement since the previous update, tap count, and phase. Phases distinguish a touch that began, moved, stayed still, ended, or was canceled.

Iterating the current touches supports gestures and simultaneous controls without assuming every device accepts the same maximum count. Stable `fingerId` values help keep behavior associated with the correct contact, and `deltaPosition` expresses a drag that can be converted from screen-space movement into gameplay response.

# References

[[unitygamedevelopmentin24hourssamsteachyourself4e.pdf]]

