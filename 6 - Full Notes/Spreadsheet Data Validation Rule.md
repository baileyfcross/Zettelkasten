2026-09-28 23:03

Status: #baby

Tags: [[Game Design Spreadsheets]] [[Excel Formula Analysis and Automation]]

# Spreadsheet Data Validation Rule

A spreadsheet data validation rule restricts a game-data cell to technically acceptable inputs. A name column may require text, an attribute column may permit only numbers within its designed range, and an equipment cell may draw from a controlled list of weapon names.

Validation communicates expectations at the point of entry and reduces misspellings, inconsistent labels, and out-of-range values that later analysis or game imports cannot interpret. It becomes especially important when several people edit the same workbook. Validation cannot eliminate every bad value, but it prevents many errors before they spread through calculations or reach the game.

Excel can base a custom validation rule on a formula. COUNTIF can reject a duplicate by requiring the proposed value to occur only once, EXACT can enforce case-sensitive agreement, and a reference to a separate criterion cell can keep the rule configurable. An input message explains the expectation before entry, while an error alert determines how Excel responds after invalid data is attempted.

# References

[[introductiontogamesystemdesign.pdf]]

[[microsoftexcelfunctionsandformulaswithexcel2019andoffice365.pdf]]
