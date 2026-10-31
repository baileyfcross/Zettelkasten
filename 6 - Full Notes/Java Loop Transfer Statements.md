2026-10-30 15:57

Status: #baby

Tags: [[Java Control Flow and Exceptions]]

# Java Loop Transfer Statements

`break` terminates the nearest loop or switch, while `continue` skips the remainder of the current loop iteration and proceeds with the next update or condition check. Labeled forms can target an enclosing loop, though deeply nested labeled control can be hard to follow.

`return` leaves the entire method and optionally supplies its result, so it has a wider effect than break. These statements are useful for exceptional paths or early completion, but a large number of exits can make the loop's normal progression difficult to reason about.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
