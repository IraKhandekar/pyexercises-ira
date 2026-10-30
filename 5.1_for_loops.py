"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. What I compute for each item, and why it is worth showing:


# Your code below
"""Exercise 5.1 — Doing the same thing to every item"""

# 1. In: A list of 8 fashion campaigns, written directly in the code so this
#        file runs on its own.
# 2. Process: Loop over the list with enumerate(). For each campaign, take its
#             position (starting at 1), measure the length of its name, and compare
#             that length with a threshold of 15 characters.
# 3. Out: One line per campaign: position, name, length, and "compact" or "long".
#         At the end, a check that the number of lines printed equals the number
#         of items in the list.
# 4. What I compute for each item, and why it is worth showing:
#    I compute the number of characters in each campaign name and whether it is
#    within 15 characters. I chose 15 myself: it is close to the typical length
#    of the names in my list and works as a limit for short placements such as a
#    mobile notification title or a small ad headline. The reader sees at a glance
#    which names are compact enough to use as they are and which would need
#    shortening.
#    Hand check on 3 items: "Gucci Ancora" = 12 (compact),
#    "Versace La Vacanza" = 18 (long), "Louis Vuitton Voyager" = 21 (long).
#    The program agrees on all three.

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

THRESHOLD = 15  # my own choice: maximum characters for a "compact" name

print("--- 5.1 For Loop Output ---")

lines_printed = 0

for position, campaign in enumerate(campaigns, start=1):
    length = len(campaign)

    if length <= THRESHOLD:
        verdict = "compact"
    else:
        verdict = "long"

    print(f"{position}. {campaign}: {length} characters ({verdict})")
    lines_printed += 1

# CHECK YOURSELF: exactly one line per item, no off-by-one
print(f"\nLines printed: {lines_printed}")
print(f"Items in list: {len(campaigns)}")
print("Same number?", lines_printed == len(campaigns))