"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. My function name, and why return rather than print:


# Your code below
# 1. In:
#    A list of campaign names (strings), like the list built in exercise 4.0.
# 2. Process:
#    Counts the characters in each name, adds the counts up, and divides the
#    total by the number of names.
# 3. Out:
#    The average name length as a float, or None if the list is empty.
# 4. My function name, and why return rather than print:
#    average_name_length. The name says what it computes without reading the code.
#    Why return rather than print: print only shows text on screen, and the
#    function itself then gives back None, so the number is lost. A returned
#    value can be stored, compared, used in further maths or reused later,
#    e.g. average_name_length(a) > average_name_length(b) only works if the
#    function returns its result.

# CHECK IT YOURSELF (empty list):
#    average_name_length([]) returns None instead of crashing with a
#    ZeroDivisionError. That is acceptable: "no names" is not the same as
#    "average length 0", and None makes that difference visible. The caller
#    must check for None before doing maths with the result.
#
# Hand check on 3 items: "Gucci Ancora" (12), "Prada Re-Nylon" (14),
#    "Chanel Cruise" (13) -> 39 / 3 = 13.00


def average_name_length(names):
    if not names:
        return None
    total_chars = 0
    for name in names:
        total_chars += len(name)
    return total_chars / len(names)


# The list from exercise 4.0
campaigns = [
    "Gucci Ancora",
    "Prada Re-Nylon",
    "Chanel Cruise",
    "Dior Sauvage",
    "Louis Vuitton Voyager",
    "Balenciaga Mud",
    "Versace La Vacanza",
    "Jacquemus Le Chouchou",
]

# Three calls with different inputs
print(f"All 8 campaigns:   {average_name_length(campaigns):.2f}")
print(f"First 4 campaigns: {average_name_length(campaigns[:4]):.2f}")
print(f"Last 4 campaigns:  {average_name_length(campaigns[4:]):.2f}")

# Empty-list check, kept separate from the three main calls
print("Empty list:", average_name_length([]))

# Hand-check on the 3 items from the comment above
print(f"Hand check (3 items): {average_name_length(campaigns[:3]):.2f}")


