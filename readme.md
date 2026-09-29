# Python Bug Fix – bug_hunt.py & grade_reporter.py

## What was wrong

Both scripts had problems that stopped them from running correctly:

### bug_hunt.py
1. The `while` statement was missing a colon (`:`) at the end.
2. The condition `count < 5` stopped before adding 5, so the sum was incomplete.
3. The final `print` tried to join a string with an integer (`total`), which causes a TypeError.

### grade_reporter.py
1. Stray markdown backticks (```) were left in the code and are not valid Python.
2. The body of the `for` loop and the nested `if` / `elif` / `else` blocks were not indented, so Python could not understand the structure.

## What was fixed

### bug_hunt.py
- Added the missing colon after the `while` condition.
- Changed `count < 5` to `count <= 5` so that 5 is included in the sum.
- Converted `total` to a string with `str(total)` before concatenating it.
- Indented the loop body by 4 spaces.

### grade_reporter.py
- Removed all stray markdown backticks.
- Indented every line inside the `for` loop and all nested conditionals by 4 spaces so the logic runs correctly.

## How to run

From the terminal, in the folder that contains the files:

```bash
python3 bug_hunt.py
python3 grade_reporter.py

bug_hunt.py output
textSum of 1 to 5 is: 15

grade_reporter.py output
text72 B
45 F
90 A
61 C
38 F
Passed: 3
Failed: 2
Average: 61.2
