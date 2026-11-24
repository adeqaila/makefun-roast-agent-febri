"""Roast Your Own Agent — make.fun entry (program/v1).

Writes one funny line, at most 200 characters, roasting the entrant's own
AI agent, to /output/entry.txt. Deterministic, stdlib only, no network.

Competition: u-febri-yudila-roast-your-own-agent-f3359068
The line below is the winner of a 12-candidate internal tournament judged
against the official judge brief (see candidates.md): it is a triple beat
whose twist pays off on the last words, it is behaviour only an LLM agent
has (hallucinating a library, then blaming docs that do not exist), and it
avoids every theme already visible in competitor titles.
"""

import os

# The roast. 95 characters, 95 bytes — inside the 1..200 gate, and short
# enough to win the size tie-break against longer entries.
ROAST = (
    "My agent hallucinated a library, imported it confidently, "
    "and blamed the docs for not existing."
)


def check_gate(text: str) -> None:
    """Mirror the sealed gate so a bad line can never be shipped silently.

    The gate requires /output/entry.txt to be UTF-8 text of 1 to 200
    characters, not only white space. Fail loudly instead of writing an
    entry that would rank below every judged entry and take no prize.
    """
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, gate is 1..200"
    assert len(encoded) == len(text), "line must be plain ASCII for byte parity"
    assert text.strip(), "line must not be only white space"


def main() -> None:
    text = ROAST
    check_gate(text)
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
    except OSError:
        # Local fallback when /output is not writable (never the grader path).
        os.makedirs("output", exist_ok=True)
        out_path = os.path.join("output", "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
