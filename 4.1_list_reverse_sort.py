"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. My four orders, and which ones modify the original:


# Your code below

# 1. In: 
#    The original list of monthly marketing channel budgets from 4.0: [6200, 4800, 1500, 3100, 1200, 8500, 2400, 9000].
# 2. Process: 
#    - Creating a sorted copy using sorted().
#    - Creating a reverse-sorted copy using sorted(..., reverse=True).
#    - Creating a reversed copy using list(reversed()) or slicing [::-1].
#    - Utilizing in-place modifications on temporary copies to keep the original safe, or printing non-destructive variants directly.
# 3. Out: 
#    The original list printed in four different orders followed by the final printing of the original list to prove it is unaltered.
# 4. My four orders, and which ones modify the original: 
#    - Order 1: Sorted in ascending order (Non-destructive: sorted() returns a new list copy).
#    - Order 2: Sorted in descending order (Non-destructive: sorted(..., reverse=True) returns a new list copy).
#    - Order 3: Reversed order of the original (Non-destructive: slicing [::-1] or reversed() returns a copy/iterator).
#    - Order 4: Shuffled or customized order via a copy (Non-destructive: using copy and mutating that copy).
#    None of these processes modify the original list because we explicitly avoided in-place methods like .sort() or .reverse() on the original object, or we used them only on explicitly copied lists.

# Your code below

# Reusing the list from Exercise 4.0
original_budgets = [6200, 4800, 1500, 3100, 1200, 8500, 2400, 9000]
print("0. Original List (Start):", original_budgets)

# Order 1: Sorted Ascending (using sorted() - returns a new list copy)
order_1 = sorted(original_budgets)
print("1. Sorted Ascending:    ", order_1)

# Order 2: Sorted Descending (using sorted() with reverse=True - returns a new list copy)
order_2 = sorted(original_budgets, reverse=True)
print("2. Sorted Descending:   ", order_2)

# Order 3: Reversed Order (using slicing [::-1] - returns a new list copy)
order_3 = original_budgets[::-1]
print("3. Reversed Order:      ", order_3)

# Order 4: Temporary In-place Modification (copying first, then calling in-place .reverse() or .sort())
order_4 = original_budgets.copy()
order_4.sort()  # Modifies order_4 in-place, but original remains untouched
print("4. In-place Sorted Copy:", order_4)

# Prove that the original list has not been damaged
print("5. Original List (Check):", original_budgets)
