#!/usr/bin/env python3
"""The Comment Above the Code — make.fun entry.

Writes one line, at most 200 characters, as if it were the comment a
developer left above fragile production code: funny because it is true.

Judge criteria, in the brief's published order (weights 5/4/3/2/1):
  1. On subject: a funny comment about fragile legacy code, the kind a real
     developer would leave above code they are afraid to touch.
  2. The honesty stings: names a real, recognisable failure in the code or
     the process, not a generic joke about programmers.
  3. Economical: every word earns its place, with a turn or punchline that
     lands on the last few words.
  4. Fresh: not the usual off-by-one, who-wrote-this or no-comments cliche.
  5. Reads like a comment actually left in a codebase, in a working
     developer's voice, not a caption written for a contest.

Cliches deliberately avoided in every candidate: off-by-one, "who wrote
this", "no comments", "it works on my machine", "here be dragons".
"""

CANDIDATES = [
    # (text, scores per criterion 1-5, each 0-5)
    (
        "DO NOT TOUCH. This function has been wrong since 2019 and the "
        "business now depends on it being wrong in exactly this way.",
        [5, 5, 4, 4, 5],
    ),
    (
        "If you change this, payroll runs twice. I know because I changed "
        "it once, in 2021, and payroll ran twice.",
        [5, 5, 4, 4, 4],
    ),
    (
        "Yes, the sort is backwards. The reports were built on the "
        "backwards sort. Fixing it would break the reports.",
        [5, 4, 4, 4, 5],
    ),
    (
        "Do not refactor. The tests pass only because the bug and the test "
        "agree with each other.",
        [5, 5, 5, 4, 4],
    ),
    (
        "This regex was written at 2 AM during an outage. It has outlived "
        "three rewrites and one CTO.",
        [4, 4, 4, 4, 5],
    ),
    (
        "Changing the timeout from 30 to 31 crashes checkout. We do not "
        "know why. 30 stays.",
        [5, 5, 5, 4, 5],
    ),
    (
        "This endpoint returns 200 even when it fails, because the mobile "
        "app from 2017 crashes on anything else.",
        [5, 5, 4, 4, 5],
    ),
    (
        "I added this null check after the 3 AM call. There are 14 more "
        "like it in this file. I stopped counting.",
        [4, 4, 4, 3, 5],
    ),
    (
        "The database column is named 'temp_final_v2'. It has held "
        "production data since 2016.",
        [4, 4, 4, 4, 4],
    ),
    (
        "Do not delete the sleep(1000). Removing it once took down the "
        "queue for four hours. We never found out why.",
        [5, 5, 4, 4, 5],
    ),
]

WEIGHTS = [5, 4, 3, 2, 1]


def score(scores):
    """Weighted total out of 75."""
    return sum(w * s for w, s in zip(WEIGHTS, scores))


def ranking():
    """Candidates ranked best-first by weighted score, then by brevity."""
    ranked = sorted(
        enumerate(CANDIDATES, start=1),
        key=lambda item: (-score(item[1][1]), len(item[1][0])),
    )
    return ranked


# --- Part 2: winner pick, gate validation, output write ---------------

# Winner: candidate #6, 73/75 — the highest score of the 10.
# A magic timeout nobody understands, a punchline that lands on the last
# two words, and exactly the voice of a comment left above code nobody
# dares touch. Runner-up (#4, bug and test agreeing) scored 72/75.
WINNER_INDEX = 6


def winner_text():
    """The chosen one-liner, exactly as it will be submitted."""
    return CANDIDATES[WINNER_INDEX - 1][0]


def validate(text):
    """The bounty gate: UTF-8 text of 1 to 200 characters, not only
    whitespace, on a single line."""
    assert isinstance(text, str) and text.strip(), "entry must not be blank"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    text.encode("utf-8")
    return True


def main():
    import os

    text = winner_text()
    validate(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)
    print(text)


if __name__ == "__main__":
    for idx, (text, scores) in ranking():
        print(f"#{idx:>2} {score(scores):>2}/75  ({len(text)} chars)  {text}")
    main()
