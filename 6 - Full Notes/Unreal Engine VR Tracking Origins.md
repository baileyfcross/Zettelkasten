2026-10-12 23:13

Status: #baby

Tags: [[Unreal Engine VR Development]]

# Unreal Engine VR Tracking Origins

A VR tracking origin defines the [[Reference Frame]] from which a headset and its controllers report their tracked transforms. Unreal Engine's Eye Level origin is suited to a seated experience because the calibrated eye position acts as the baseline, while Floor Level places the origin on the calibrated physical floor for standing or room-scale use.

The pawn, camera root, and Player Start must agree with that choice. With a floor origin, placing the virtual spawn point on the level floor lets the tracked headset supply the user's actual standing height. With an eye origin, the application supplies the expected seated eye position. Changing the engine origin without reconciling the pawn hierarchy can create an unexplained height or horizontal offset.

The book describes device defaults from its Unreal Engine 4.13 era - Rift used Eye Level and Vive used Floor Level - so those defaults should be treated as version-specific. The durable rule is to select the origin explicitly for the intended posture and make every gameplay transform relative to the same calibrated frame.

# References

[[unrealenginevrcookbook.pdf]]

