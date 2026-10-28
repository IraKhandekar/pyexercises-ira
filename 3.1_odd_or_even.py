"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. What happens on 0, on a negative number, on a very large number:


# Your code below
new_code = """Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
#    An integer entered  (input variable N).
# 2. Process:
#    Convert input to integer, check bounds. If valid, loop from 1 to N, check if number % 2 == 0.
# 3. Out:
#    Prints a message for each number from 1 to N stating if it's 'even' or 'odd'.
# 4. What happens on 0, on a negative number, on a very large number:
#    - If 0: Explain that we only start counting from 1, so there's nothing to check.
#    - If negative: Show a helpful warning saying only positive integers are accepted.
#    - If >= 5000 (or other very large values like 1000+): Warn the user that printing thousands of lines
#      will flood the terminal, and suggest a smaller limit (e.g., maximum of 100).

# Your code below

 user_input = input("Enter a number (N): ").strip()
 N = int(user_input)
    
if N < 0:
     print("I can't count to negative numbers! Please enter a positive integer.")
elif N == 0:
    print("Zero is not a valid starting range. Please enter a number starting from 1.")
elif N > 1000:
    print(f"Whoa, {N} is a bit too large! Printing that many lines will flood the screen. Let's keep it under 1000.")
else:
    for i in range(1, N + 1):
         if i % 2 == 0:
             print(f"{i} is even")
         else:
             print(f"{i} is odd")

