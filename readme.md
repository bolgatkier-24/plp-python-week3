# Grade Reporter & Bug Hunt

`grade_reporter.py` calculates grades, pass/fail counts, and the average for a list of learner scores.

`bug_hunt.py` fixes three bugs in a while loop so that it correctly calculates the sum of 1 to 5.

# The hardest bug to find was the `while` loop condition because the program ran without an error message, but it stopped before adding 5. I knew something was wrong because the program printed the wrong answer instead of the expected `15`, so I checked the loop condition and changed `< 5` to `<= 5`.
The expected grade_reporter.py results are:

72 B
45 F
90 A
61 C
38 F
Passed: 3
Failed: 2
Average: 61.2

# And bug_hunt.py should print:

Sum of 1 to 5 is: 15
