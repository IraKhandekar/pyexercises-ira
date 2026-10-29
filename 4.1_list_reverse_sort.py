"""Exercise 4.1 — Reordering without losing the original (homework)"""

# 1. In: The list of 8 fashion campaigns from exercise 4.0 (copied here so this
#        file runs on its own).
# 2. Process: Build four different orders of the list. Three use functions or
#             slicing that return a NEW list. The fourth uses an in-place method
#             (.sort), but only on a separate copy made with .copy().
# 3. Out: The four orders, then the original list printed last to prove it is
#         unchanged.
# 4. My four orders, and which ones modify the original:
#    - Order 1: Reversed with slicing [::-1]        -> returns a copy; original safe
#    - Order 2: Alphabetical with sorted()          -> returns a copy; original safe
#    - Order 3: By name length with sorted(key=len) -> returns a copy; original safe
#    - Order 4: Z to A with .sort(reverse=True)     -> modifies the list it is called
#               on IN PLACE (and returns None). I call it on a copy, so the
#               original is still safe.
#    Key difference: sorted() and slicing build a new list; .sort() and .reverse()
#    change the existing list. If I had called campaigns.sort() or
#    campaigns.reverse() directly, the original would have been damaged.

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

# Snapshot used only to verify at the end that nothing changed
original_snapshot = campaigns.copy()

print("--- 4.1 Reordering Output ---")

# Order 1: reversed with slicing (new list)
order_1 = campaigns[::-1]
print("\nOrder 1 (reversed, slicing):", order_1)

# Order 2: alphabetical with sorted() (new list)
order_2 = sorted(campaigns)
print("\nOrder 2 (alphabetical, sorted()):", order_2)

# Order 3: shortest to longest name with sorted(key=len) (new list)
order_3 = sorted(campaigns, key=len)
print("\nOrder 3 (by name length, sorted(key=len)):", order_3)

# Order 4: Z to A with .sort(), an in-place method, used on a COPY
order_4 = campaigns.copy()
order_4.sort(reverse=True)
print("\nOrder 4 (Z to A, .sort() on a copy):", order_4)

# Proof that the original survived
print("\nOriginal list after all four orders:")
print(campaigns)
print("Original unchanged?", campaigns == original_snapshot)