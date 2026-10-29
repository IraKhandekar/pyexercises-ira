"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. What my list is about, and what I computed from it:


# Your code below
#DELIVERABLE


# 1. In: A list of 8 monthly marketing channel budgets (floats/integers).
# 2. Process: Sorting the list, selecting a single element by index, and computing the average budget using sum() and len().
# 3. Out: The printed representation of the raw list, one chosen budget, the sorted list, and the computed average marketing budget.
# 4. What my list is about, and what I computed from it: 
#    The list represents monthly advertising budgets (in USD) for different digital acquisition channels (e.g., Search, Social, Affiliate, Display, Email, SEO, Influencer, Video).
#    I computed the average monthly budget across all channels ($4,837.5). 
#    This number is interesting because it represents the baseline benchmark spend per channel, helping us allocate marketing resources more evenly.

# Your code below

# 1. Define the list of at least eight marketing channel budgets
budgets = [6500, 3200, 1500, 4800, 1200, 8500, 3500, 9500]

# 2. Display the whole list
print("Whole list of budgets:", budgets)

# 3. Display one item of choice (e.g., the 5th item, which is index 4)
chosen_budget = budgets[4]
print("Chosen budget (index 4):", chosen_budget)

# 4. Display the sorted list
sorted_budgets = sorted(budgets)
print("Sorted budgets:", sorted_budgets)

# 5. Display something computed from it (the average budget)
total_budget = sum(budgets)
average_budget = total_budget / len(budgets)
print(f"Computed Average Budget: ${average_budget:,.2f}")

