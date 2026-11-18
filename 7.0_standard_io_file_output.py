"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In:
#    Five values typed by the user, one entry per run: the brand, the campaign
#    name, the launch year, the budget in euros, and the main channel.
# 2. Process:
#    Each value is checked as it is typed. Text must not be empty, the year
#    must be a whole number between 1990 and next year, the budget must be a
#    positive number, and the channel must be one from a fixed list. If a
#    value is not acceptable, the program says why and asks again until it is.
#    Then the program opens the file in append mode ("a") so earlier entries
#    are never overwritten. If the file does not exist yet, or is empty, it
#    writes the header line first, then the entry.
# 3. Out, file name and columns:
#    campaigns.csv (semicolon-separated, like 7.0_student_data.csv), with the
#    columns: brand;campaign_name;launch_year;budget_eur;main_channel
# 4. Why these columns, and what this file is for:
#    The purpose is to build my own small database of luxury fashion campaigns
#    so I can compare them. With two hundred rows I would filter by brand to
#    see how each house spends, group by main_channel to compare the average
#    budget per channel, and sort by launch_year to see how channel choices
#    changed over time. Brand and campaign_name identify the entry, and the
#    other three are the numbers and categories I would actually compare.

import csv
import os
from datetime import date

FILE_NAME = "campaigns.csv"
COLUMNS = ["brand", "campaign_name", "launch_year", "budget_eur", "main_channel"]
CHANNELS = ["social", "tv", "print", "outdoor", "events"]
FIRST_YEAR = 1990


def ask_text(prompt):
    """Ask until the user types something that is not empty."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  This cannot be empty. Please try again.")


def ask_year(prompt):
    """Ask until the user types a whole number between FIRST_YEAR and next year."""
    last_year = date.today().year + 1
    while True:
        raw = input(prompt).strip()
        if not raw.isdigit():
            print("  Please type the year as digits, for example 2024.")
            continue
        year = int(raw)
        if year < FIRST_YEAR or year > last_year:
            print(f"  The year must be between {FIRST_YEAR} and {last_year}.")
            continue
        return year


def ask_budget(prompt):
    """Ask until the user types a positive number. A comma decimal is accepted."""
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            amount = float(raw)
        except ValueError:
            print("  Please type a number, for example 250000.")
            continue
        if amount <= 0:
            print("  The budget must be greater than zero.")
            continue
        return amount


def ask_choice(prompt, options):
    """Ask until the user types one of the options (case does not matter)."""
    while True:
        value = input(prompt).strip().lower()
        if value in options:
            return value
        print(f"  Please choose one of: {', '.join(options)}.")


def file_needs_header(path):
    """True if the file does not exist yet or is empty."""
    return not os.path.exists(path) or os.path.getsize(path) == 0


def save_entry(path, row):
    """Append one row to the CSV, writing the header first if the file is new."""
    needs_header = file_needs_header(path)
    with open(path, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        if needs_header:
            writer.writerow(COLUMNS)
        writer.writerow(row)


def main():
    print("Record one campaign. Type the values below.\n")
    brand = ask_text("Brand (e.g. Gucci): ")
    campaign_name = ask_text("Campaign name (e.g. Gucci Ancora): ")
    launch_year = ask_year("Launch year: ")
    budget_eur = ask_budget("Budget in euros: ")
    main_channel = ask_choice(f"Main channel ({'/'.join(CHANNELS)}): ", CHANNELS)

    save_entry(FILE_NAME, [brand, campaign_name, launch_year, budget_eur, main_channel])
    print(f"\nSaved to {FILE_NAME}.")


main()