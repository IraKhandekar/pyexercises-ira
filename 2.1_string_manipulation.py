"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. My four transformations, and when each is useful:


# Your code below
WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.


# 1. In: A single sentence (string) entered by the user.
# 2. Process: The program applies four unique built-in string transformations to the input.
# 3. Out: The four transformed versions of the original sentence printed to the screen.
# 4. My four transformations, and when each is useful:
#    - strip(): Useful for cleaning up user inputs by removing accidental leading/trailing whitespaces.
#    - upper(): Useful for standardized case-insensitive string comparisons (e.g., matching "YES" or "NO").
#    - title(): Useful for formatting names, book titles, or headers where each word needs a capital letter.
#    - replace(' ', '_'): Useful for generating URL slugs, file names, or database keys from a human-readable string.



# Get user input
user_sentence = input("Please enter a sentence: ")

# Transformation 1: Strip leading and trailing whitespace
transformed_1 = user_sentence.strip()
print(f"1. Stripped whitespace: '{transformed_1}'")

# Transformation 2: Convert to all uppercase
transformed_2 = user_sentence.upper()
print(f"2. Uppercase version: '{transformed_2}'")

# Transformation 3: Convert to title case
transformed_3 = user_sentence.title()
print(f"3. Title case version: '{transformed_3}'")

# Transformation 4: Replace spaces with underscores
transformed_4 = user_sentence.replace(' ', '_')
print(f"4. Spaces to underscores: '{transformed_4}'")

# RESULTS:
# Input tested: " i want to attend skema business school " (spaces at both ends and a capital 'S')
# Results:
# 1. Stripped whitespace: 'i want to attend skema business school'
# 2. Uppercase version: ' I WANT TO ATTEND SKEMA BUSINESS SCHOOL '
# 3. Title case version: ' I Want To Attend Skema Business School ' 
# 4. Spaces to underscores: '_i_want_to_attend_skema_business_school_'