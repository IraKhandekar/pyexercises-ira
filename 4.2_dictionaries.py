"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""



# 1. In: One fashion marketing campaign described as a dictionary with six fields,
#        written directly in the code.
# 2. Process: Read two fields, change one value (budget), add nothing, remove one
#             field (launch_month), then loop over what is left. Finally, ask for a
#             field that does not exist and handle it safely.
# 3. Out: The values I read, the dictionary after the change, the dictionary after
#         the removal, every remaining field with its value, and the result of
#         asking for a missing field.
# 4. My object, my five fields, and why those:
#    Object: a campaign for a fashion house, the thing I would have to brief,
#    budget and report on in a marketing role.
#    - brand: tells me which house the campaign belongs to
#    - campaign_name: how the team refers to it in briefs and reports
#    - channel: where it runs (Instagram, print, etc.), which decides format and cost
#    - budget_eur: the number I must track and defend
#    - target_audience: who the creative is written for
#    Sixth field, launch_month: used while planning, then removed once the
#    campaign is live, so I can show removing a field. That leaves five fields.
#
#    CHECK YOURSELF: I asked for campaign["agency"], a field that does not exist.
#    Python stopped the program with: KeyError: 'agency'.
#    Fix: use .get("agency", "not recorded"), which returns a default value instead
#    of crashing. I also show the other safe way, testing with `in` first.

campaign = {
    "brand": "Gucci",
    "campaign_name": "Gucci Ancora",
    "channel": "Instagram",
    "budget_eur": 50000,
    "target_audience": "women 25-34",
    "launch_month": "March",
}

print("--- 4.2 Dictionary Output ---")

# READ: get values by key
print("Brand:", campaign["brand"])
print("Budget (EUR):", campaign["budget_eur"])

# CHANGE: the budget is increased
campaign["budget_eur"] = 65000
print("\nAfter changing the budget:", campaign)

# REMOVE: the campaign is live, so the planning month is no longer needed
removed_value = campaign.pop("launch_month")
print("\nRemoved launch_month (was " + removed_value + "):", campaign)

# DISPLAY: every field with its value
print("\nAll fields:")
for field, value in campaign.items():
    print(f"  {field}: {value}")

# CHECK: a field that does not exist
# print(campaign["agency"])   # this line crashes with KeyError: 'agency'
print("\nAgency (using .get):", campaign.get("agency", "not recorded"))

# Second safe way: test first with `in`
if "agency" in campaign:
    print("Agency:", campaign["agency"])
else:
    print("No agency field in this campaign.")
