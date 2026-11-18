"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process, function by function:
# 3. Out:
# 4. The question my fourth function answers:


# # 1. In:
#    A list of campaign names (strings), the list from exercise 4.0, and a
#    headline limit in characters.
# 2. Process, function by function:
#    - find_names_over_limit: returns the names longer than the limit.
#    - percentage_of: returns one number as a percentage of another.
#    - find_longest_name: returns the longest name in the list.
#    - headline_limit_report (the fourth function) calls the three above in
#      that order: first finds the too-long names, then turns their count into
#      a percentage of all names, then finds the longest name.
# 3. Out:
#    A one-line sentence (string) saying how many names are over the limit,
#    what percentage that is, and which name is the longest.
# 4. The question my fourth function answers:
#    "What share of my campaign names would not fit in a headline of N
#    characters, and which name is the longest?"
#    Splitting it makes it easier to check because each small function can be
#    tested alone with a tiny input whose answer I can work out by hand. If the
#    final sentence is wrong, I can see which of the three pieces is at fault.

# TEST CASES (CHECK IT YOURSELF), one per small function:
# - find_names_over_limit(["Dior", "Chanel Cruise"], 10) -> ["Chanel Cruise"]
#   ("Dior" is 4 characters, "Chanel Cruise" is 13)
# - percentage_of(1, 4) -> 25.0
# - find_longest_name(["Dior", "Chanel Cruise", "Gucci"]) -> "Chanel Cruise"
# The asserts just below the functions run these tests every time the file runs.


def find_names_over_limit(names, limit):
    too_long = []
    for name in names:
        if len(name) > limit:
            too_long.append(name)
    return too_long


def percentage_of(part, whole):
    if whole == 0:
        return None  
    return part / whole * 100


def find_longest_name(names):
    if not names:
        return None
    return max(names, key=len)


def headline_limit_report(names, limit):
    if not names:
        return "No campaign names to check."
    too_long = find_names_over_limit(names, limit)
    share = percentage_of(len(too_long), len(names))
    longest = find_longest_name(names)
    return (f"{len(too_long)} of {len(names)} names ({share:.1f}%) are over "
            f"{limit} characters. Longest: {longest} ({len(longest)} characters).")


# Run the three test cases from the comment above
find_names_over_limit(["Dior", "Chanel Cruise"], 10) == ["Chanel Cruise"]
percentage_of(1, 4) == 25.0
find_longest_name(["Dior", "Chanel Cruise", "Gucci"]) == "Chanel Cruise"
print("All 3 small-function tests passed.\n")

# The list from exercise 4.0
campaigns = ["Gucci Ancora",
    "Prada Re-Nylon",
    "Chanel Cruise",
    "Dior Sauvage",
    "Louis Vuitton Voyager",
    "Balenciaga Mud",
    "Versace La Vacanza",
    "Jacquemus Le Chouchou",
]

print(headline_limit_report(campaigns, 30))
print(headline_limit_report(campaigns, 15))
print(headline_limit_report([], 30))
