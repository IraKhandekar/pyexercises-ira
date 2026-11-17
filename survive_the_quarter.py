# Ira Khandekar, Group A
#
# FEATURE I CHOSE (Mandatory 2): (d) Difficulty.
# Why: the player picks easy (15,000 EUR) or hard (6,000 EUR) at the start.
# It only changes the starting budget, so it is simple to add and it cannot
# break the rest of the game. It also changes how risky each choice feels.
#
# MANDATORY 1: I added three scenarios of my own at the end of
# scenarios_A.csv (numbers 31, 32 and 33), in the same format as the others.
#
# 1. WHAT GOES IN?
#    scenarios_A.csv: comma-separated, one header row, then the scenarios.
#    14 columns: ID, Scenario, OptionA, OptionB, OptionC,
#    BudgetA, BudgetB, BudgetC, ReputationA, ReputationB, ReputationC,
#    FeedbackA, FeedbackB, FeedbackC.
#    Numbers are whole integers, with a minus sign for losses (e.g. -1500),
#    and no thousand separators. But everything is read as text, so I must
#    convert budget and reputation with int() before doing maths.
#    Text that contains a comma or a quote is wrapped in double quotes
#    (inner quotes are doubled), so splitting on commas would break rows.
#    I use the csv module instead.
#    The player also types a name, a difficulty, and A, B or C each day.
#
# 2. WHAT HAPPENS?
#    Ask the name. Load and convert every scenario. Ask the difficulty.
#    Shuffle the scenarios and play 10 days. Each day: show the day, both
#    gauges, the situation and options A/B/C. Ask until the answer is valid
#    (a, b, c or upper case). Apply the budget and reputation change, cap
#    reputation at 100, show the feedback line. If budget or reputation is
#    0 or less, the game stops at once. Each day is saved as one tuple in a
#    history list. At the end: show the result, find the best and worst
#    move from the history, and append one line to results.csv.
#
# 3. WHAT COMES OUT?
#    On screen: either "fired" with the reason, or the final score
#    (reputation + budget // 200), the title, and the best and worst move.
#    In results.csv, one line per game: name, budget, reputation, title, date.
#
# 4. WHAT COULD GO WRONG?
#    - The player types something invalid (d, empty, "ab"): I keep asking
#      until the answer is a, b or c, and I strip spaces first.
#    - A gauge reaches 0 or below, or reputation goes over 100: I check after
#      every day and stop at once; I cap reputation with min(100, ...).
#    - scenarios_A.csv is missing or a number cell is not a number: I catch
#      FileNotFoundError and ValueError, show a clear message, and exit
#      without a crash.
#    - results.csv does not exist yet: opening in append mode creates it.
#    - The player presses Ctrl+D or Ctrl+C: I catch EOFError and
#      KeyboardInterrupt so the game ends cleanly.

import csv
import random
from datetime import date

SCENARIO_FILE = "scenarios_A.csv"
RESULTS_FILE = "results.csv"
DAYS_PER_GAME = 10
START_REPUTATION = 50
MAX_REPUTATION = 100
EASY_BUDGET = 15000
HARD_BUDGET = 6000


# Asks for the player's name; an empty answer becomes "Player".
def ask_player_name():
    name = input("What is your name? ").strip()
    if name == "":
        return "Player"
    return name


# Asks easy or hard until the answer is valid; returns the starting budget.
def ask_difficulty():
    while True:
        answer = input("Difficulty: easy (15000 EUR) or hard (6000 EUR)? (E/H): ")
        answer = answer.strip().lower()
        if answer in ("e", "easy"):
            return EASY_BUDGET
        if answer in ("h", "hard"):
            return HARD_BUDGET
        print("Please type E or H.")


# Reads the CSV with the csv module and turns the numbers into ints.
def load_scenarios(filename):
    scenarios = []
    with open(filename, newline="", encoding="utf-8-sig") as file:
        for row in csv.DictReader(file):
            options = []
            for letter in "ABC":
                option = (
                    row["Option" + letter],
                    int(row["Budget" + letter]),
                    int(row["Reputation" + letter]),
                    row["Feedback" + letter],
                )
                options.append(option)
            scenarios.append((row["Scenario"], options))
    return scenarios


# Prints one day: the day number, both gauges, the situation and the options.
def show_day(day, budget, reputation, scenario):
    situation, options = scenario
    print(f"\n--- Day {day} ---")
    print(f"[Budget: {budget} EUR | Reputation: {reputation}/{MAX_REPUTATION}]")
    print(situation)
    for letter, option in zip("ABC", options):
        print(f"  {letter}: {option[0]}")


# Asks for A, B or C and keeps asking until the answer is valid.
def ask_choice():
    answer = input("Your choice (A, B or C): ").strip().upper()
    while answer not in ("A", "B", "C"):
        answer = input("Please type A, B or C: ").strip().upper()
    return answer


# Applies one option to both gauges and returns them as a tuple.
def apply_choice(budget, reputation, option):
    text, budget_change, reputation_change, feedback = option
    new_budget = budget + budget_change
    new_reputation = min(MAX_REPUTATION, reputation + reputation_change)
    return new_budget, new_reputation


# Returns the reason the player is fired, or "" if they are still safe.
def get_fired_reason(budget, reputation):
    if budget <= 0 and reputation <= 0:
        return "Your budget and your reputation both hit zero."
    if budget <= 0:
        return "Your budget ran out."
    if reputation <= 0:
        return "Your reputation hit zero."
    return ""


# Final score, only used when the player survives.
def calculate_score(budget, reputation):
    return reputation + budget // 200


# Turns the score into a title.
def get_title(score):
    if score < 95:
        return "Eternal Intern"
    if score < 120:
        return "Growth Hacker"
    if score < 140:
        return "CMO Material"
    return "Viral Legend"


# Returns best and worst moves based on history tuples.
def find_best_and_worst_moves(history):
    if not history:
        return None, None
    return max(history), min(history)


# Appends one line to results.csv.
def save_result(name, budget, reputation, title):
    with open(RESULTS_FILE, "a", newline="", encoding="utf-8") as file:
        csv.writer(file).writerow(
            [name, budget, reputation, title, date.today().isoformat()]
        )


# Prints the end of the game.
def show_ending(name, budget, reputation, title, fired_reason, history):
    print("\n" + "=" * 32)
    if fired_reason:
        print("You are FIRED!")
        print(fired_reason)
        print(f"Budget: {budget} EUR, reputation: {reputation}/{MAX_REPUTATION}")
    else:
        print("Quarter survived!")
        print(f"Budget left: {budget} EUR, reputation: {reputation}/{MAX_REPUTATION}")
        print(f"Final score: {calculate_score(budget, reputation)}")
        print(f"{name}, your title: {title}")
    best, worst = find_best_and_worst_moves(history)
    if best is not None:
        print()
        print(f'Best move:  day {best[1]}, "{best[2]}" ({best[0]:+d})')
        print(f'Worst move: day {worst[1]}, "{worst[2]}" ({worst[0]:+d})')


# Plays one full game from the name to the saved result.
def play_game():
    name = ask_player_name()

    try:
        scenarios = load_scenarios(SCENARIO_FILE)
    except FileNotFoundError:
        print(f"I cannot find {SCENARIO_FILE}. Put it in the same folder as this file.")
        return
    except (KeyError, ValueError, TypeError) as e:
        print(f"{SCENARIO_FILE} has a row I cannot read ({e}). Check the columns and numbers.")
        return
    if not scenarios:
        print(f"{SCENARIO_FILE} has no scenarios.")
        return

    budget = ask_difficulty()
    reputation = START_REPUTATION
    random.shuffle(scenarios)
    days_to_play = min(DAYS_PER_GAME, len(scenarios))

    history = []
    fired_reason = ""
    for day in range(1, days_to_play + 1):
        scenario = scenarios[day - 1]
        show_day(day, budget, reputation, scenario)
        letter = ask_choice()
        option = scenario[1]["ABC".index(letter)]
        budget, reputation = apply_choice(budget, reputation, option)
        print(option[3])
        print(f"Budget {option[1]:+d} EUR, Reputation {option[2]:+d}")
        history.append((option[2], day, option[0]))
        fired_reason = get_fired_reason(budget, reputation)
        if fired_reason:
            break

    if fired_reason:
        title = "Fired"
    else:
        title = get_title(calculate_score(budget, reputation))
    show_ending(name, budget, reputation, title, fired_reason, history)

    try:
        save_result(name, budget, reputation, title)
        print(f"Saved in {RESULTS_FILE}")
    except OSError:
        print(f"I could not write to {RESULTS_FILE}.")


if __name__ == "__main__":
    try:
        # Runs the game 10 times consecutively as requested
        for i in range(10):
            print(f"\n================================")
            print(f"       GAME RUN {i+1} OF 10     ")
            print(f"================================")
            play_game()
    except (EOFError, KeyboardInterrupt):
        print("\nGame stopped. See you next quarter!")