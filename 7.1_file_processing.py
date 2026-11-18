"""

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# NOTE: replace or confirm each line after opening your own names.txt. The code
# below only defends against problems that are listed here.
# - Blank lines between or after the names.
# - Extra spaces at the start or end of lines, and double spaces between words.
# - Inconsistent capitalisation (JOHN SMITH, anna meyer).
# - Mixed formats: some lines are "First Last", others are "Last, First".
# - The same person appears more than once (sometimes with different spelling
#   of capitals or spaces).
# - Junk lines that are not names (digits or symbols, for example "12345").

# 1. In:
#    The text file names.txt, one name per line, in the messy state described
#    above. The program only reads it and never changes it.
# 2. Process, problem by problem:
#    - Blank lines: dropped.
#    - Extra spaces: each line is split into words and joined with one space.
#    - Capitalisation: words that are all upper or all lower case are turned
#      into Capitalised form (also after "-" and "'"). Words that already mix
#      cases, like McDonald, are left alone.
#    - "Last, First" format: the part before the comma is the last name; the
#      line is turned into "First Last".
#    - Duplicates: compared ignoring case and accents; only the first copy
#      is kept.
#    - Junk lines: any line with a character that is not a letter, space,
#      hyphen, apostrophe, full stop or comma is dropped and counted.
#    Then the clean names are sorted by last name (then first name) and
#    written to names_clean.txt.
# 3. Out:
#    names_clean.txt: one clean name per line as "First Last", sorted by last
#    name. The terminal also shows how many lines were read, dropped for each
#    reason, and written, so the line counts can be explained.
# 4. How I decide which word is the last name:
#    In "First Last" lines the last word is the last name, so in "Anna Maria
#    Meyer" the last name is Meyer. In "Last, First" lines the words before
#    the comma are the last name. A line with one word is treated as a last
#    name only. Limitation: a surname with particles written without a comma,
#    such as "Maria de la Cruz", is sorted under "Cruz", not "de la Cruz".
#    Written as "de la Cruz, Maria" it is sorted correctly.

import os
import re
import unicodedata

INPUT_FILE = "names.txt"
OUTPUT_FILE = "names_clean.txt"
ALLOWED_PUNCTUATION = " -'.,"


def read_lines(path):
    """Return the lines of the file as a list of strings, without changing the file."""
    try:
        with open(path, "r", encoding="utf-8-sig") as file:
            return file.read().splitlines()
    except UnicodeDecodeError:
        with open(path, "r", encoding="latin-1") as file:
            return file.read().splitlines()


def looks_like_a_name(text):
    """True if every character is a letter or an allowed punctuation mark."""
    return all(char.isalpha() or char in ALLOWED_PUNCTUATION for char in text)


def fix_capitals(word):
    """Capitalise a word that is all upper or all lower case, including after - and '."""
    if not (word.isupper() or word.islower()):
        return word
    return re.sub(r"[^-']+", lambda match: match.group().capitalize(), word)


def parse_name(line):
    """Turn one raw line into (first, last), or None if the line is not a usable name."""
    text = " ".join(line.split())
    if not text or not looks_like_a_name(text):
        return None
    if "," in text:
        last_part, first_part = text.split(",", 1)
        last_words = last_part.split()
        first_words = first_part.split()
        if not last_words or not first_words:
            return None
        return (
            " ".join(fix_capitals(w) for w in first_words),
            " ".join(fix_capitals(w) for w in last_words),
        )
    words = [fix_capitals(w) for w in text.split()]
    return (" ".join(words[:-1]), words[-1])


def strip_accents(text):
    """Remove accents so that Élodie and Elodie compare as equal."""
    decomposed = unicodedata.normalize("NFD", text)
    return "".join(char for char in decomposed if not unicodedata.combining(char))


def sort_key(name):
    """Sort by last name, then first name, ignoring case and accents."""
    first, last = name
    return (strip_accents(last).lower(), strip_accents(first).lower())


def clean_names(lines):
    """Return (sorted unique names, counts of what was dropped)."""
    counts = {"blank": 0, "junk": 0, "duplicate": 0}
    seen = set()
    names = []
    for line in lines:
        if not line.strip():
            counts["blank"] += 1
            continue
        name = parse_name(line)
        if name is None:
            counts["junk"] += 1
            continue
        key = sort_key(name)
        if key in seen:
            counts["duplicate"] += 1
            continue
        seen.add(key)
        names.append(name)
    names.sort(key=sort_key)
    return names, counts


def format_name(name):
    """Turn (first, last) into the text written on one line of the output file."""
    first, last = name
    return f"{first} {last}".strip()


def write_lines(path, lines):
    """Write the lines to a new file, one per line."""
    with open(path, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")


def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Cannot find {INPUT_FILE}. Put it in the same folder as this script.")
        return

    raw_lines = read_lines(INPUT_FILE)
    names, counts = clean_names(raw_lines)
    write_lines(OUTPUT_FILE, [format_name(name) for name in names])

    print(f"Lines in {INPUT_FILE}:           {len(raw_lines)}")
    print(f"  dropped, blank:             {counts['blank']}")
    print(f"  dropped, junk (not a name): {counts['junk']}")
    print(f"  dropped, duplicates:        {counts['duplicate']}")
    print(f"Lines in {OUTPUT_FILE}:    {len(names)}")
    if names:
        print(f"First: {format_name(names[0])}")
        print(f"Last:  {format_name(names[-1])}")


main()