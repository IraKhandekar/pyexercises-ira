"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. My stop condition, my attempt limit, my summary:


# Your code below


# 1. In: The user's typed answers to the question "Has the client approved the
#        campaign brief? (yes/no)", one answer per attempt.
# 2. Process: A while loop asks the question again and again. Each answer is
#             saved as typed, then cleaned with .strip().lower() before it is
#             compared with "yes". The loop stops as soon as the cleaned answer
#             is "yes", or after 5 attempts, whichever comes first.
# 3. Out: A summary with the number of attempts used, every answer exactly as
#         typed, and the result (approved, or limit reached).
# 4. My stop condition, my attempt limit, my summary:
#    - Stop condition: the cleaned answer equals "yes".
#    - Attempt limit: 5. When it is reached, the program stops asking and
#      reports that the brief was not approved. It never loops for ever.
#    - Accepted forms of "yes": "Yes", "yes", " yes ", "YES" and "  YES  " all
#      count as the same answer, because I remove spaces at both ends with
#      .strip() and ignore capitals with .lower(). Anything else ("y", "yes!",
#      "yeah") is NOT accepted. That is my decision.
#    - Summary: attempts used out of 5, the list of answers as typed, and the result.
#
#    CHECK YOURSELF:
#    - Never giving the expected answer: the program stops after attempt 5.
#    - Answering "  YES  " (capitals and extra spaces): accepted at once.

MAX_ATTEMPTS = 5
STOP_ANSWER = "yes"

attempts = 0
answers = []
approved = False

print("--- 5.2 While Loop ---")

while attempts < MAX_ATTEMPTS and not approved:
    raw_answer = input(
        f"Attempt {attempts + 1} of {MAX_ATTEMPTS} - "
        "Has the client approved the campaign brief? (yes/no): "
    )
    attempts += 1
    answers.append(raw_answer)

    cleaned_answer = raw_answer.strip().lower()

    if cleaned_answer == STOP_ANSWER:
        approved = True
    else:
        print("Not approved yet.")

print("\n--- Summary ---")
print(f"Attempts used: {attempts} of {MAX_ATTEMPTS}")
print(f"Answers typed: {answers!r}")

if approved:
    print("Result: approved (stop condition met).")
else:
    print(f"Result: limit reached, brief not approved after {MAX_ATTEMPTS} attempts.")