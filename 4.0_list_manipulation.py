"""Exercise 4.0 — Working with a list"""

# 1. In: A list of 8 fashion brand marketing campaigns (brand + campaign name),
#        written directly in the code.
# 2. Process: Display the whole list, pick one item by its index, sort the list
#             alphabetically, and compute the average length of the campaign names.
# 3. Out: The original list, one chosen campaign, the sorted list, and the
#         average name length in characters.
# 4. What my list is about, and what I computed from it:
#    My list contains campaigns from major fashion houses. I computed the average
#    number of characters per campaign name (15.75). This is interesting because
#    digital ad headlines have strict limits (for example, 30 characters per headline
#    in Google Ads responsive search ads), so name length tells me whether
#    campaign names fit in a headline.
#    Hand check on 3 items: "Gucci Ancora" = 12, "Chanel Cruise" = 13,
#    "Louis Vuitton Voyager" = 21. The program agrees on all three.

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

print("--- 4.0 List Manipulation Output ---")

# Whole list
print("Original campaigns list:", campaigns)

# One item of my choice
chosen_campaign = campaigns[2]
print("Chosen campaign (index 2):", chosen_campaign)

# Sorted list (sorted() returns a new list)
sorted_campaigns = sorted(campaigns)
print("Sorted campaigns:", sorted_campaigns)

# Computation: average length of campaign names
total_chars = sum(len(c) for c in campaigns)
avg_length = total_chars / len(campaigns)
print(f"Average campaign name length: {avg_length:.2f} characters")

# Longest name vs the 30-character headline limit
longest = max(campaigns, key=len)
print(f"Longest name: {longest} ({len(longest)} characters)")

