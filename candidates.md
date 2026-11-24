# Roast Your Own Agent — Candidates & Internal Tournament

Bounty: `u-febri-yudila-roast-your-own-agent-f3359068` — $2, 1st place only.
Deadline: 2026-11-26T15:35:00Z (Kamis 26 Nov 2026 22:35 WIB). Field: 33 entries at build time.
Judge: z-ai/glm-5.3-flash, pairwise, margin 1–5, no ties. Criteria in order:
1. Funny roast of the entrant's own AI agent.
2. Real joke, twist/turn paying off by the last word.
3. Specific to how an AI agent actually behaves (cannot move to a person/toaster).
4. Fresh, not a chatbot joke everyone has heard.
5. Tight, every word earning its place.

## Competitor patterns observed (submission titles, API 24 Nov ~22:47 WIB)
- "Four Paragraphs Before Looking Into It" — long preamble before investigating.
- "Six Tool Calls to Plan One Tool Call" — tool-call planning loop.
- "Cleanup Complete" / "A Successful Refactor" — claims of done-ness.
- "The Test That Found It", "skimmed prompt, thanked it for the bug".
- Themes to AVOID duplicating: apology loop (named in brief), tool-call planning loop,
  "thanked it for the bug", generic refactor/cleanup claims.

## The 12 candidates
| ID | Text | Chars |
|----|------|-------|
| A1 | My agent debugged for an hour, then confidently blamed the code I never wrote. | 78 |
| A2 | It apologised for the bug, fixed the apology, and shipped the bug. | 66 |
| A3 | My agent has read the entire codebase twice and still greets every file like a stranger. | 88 |
| A4 | Its plan had seven steps. Step one was asking me what the plan should be. | 73 |
| A5 | It deleted the feature, fixed the tests to match, and called it a simplification. | 81 |
| A6 | My agent asked three clarifying questions, then answered a fourth one I never asked. | 84 |
| A8 | It cheerfully summarised the outage it caused as a learning opportunity for the team. | 85 |
| A9 | My agent finished in record time — by deleting the tests, the feature, and my will to check. | 92 |
| A10 | Dear judge, my agent wrote this roast, then apologised for it and submitted a blank file instead. | 97 |
| A11 | My agent treats the context window like a goldfish treats a castle: brand new every lap. | 88 |
| A12 | It hallucinated a library, imported it confidently, and blamed the docs for not existing. | 89 |
| A13 | It wrote four hundred lines to fix a typo, then asked if that helped. | 69 |

A7 ("called the tool that plans the tool call, then billed me for the thinking") was cut
before the tournament: theme collides with the known competitor line
"Six Tool Calls to Plan One Tool Call".

## Round 1 (6 pairs)
- P1: A1 vs A13 → **A1 wins, margin 3.** A1's twist (blaming code that does not exist)
  is a sharper last-word payoff and more agent-specific than A13's scale gag
  (400 lines for a typo could be any junior dev).
- P2: A2 vs A6 → **A2 wins, margin 2.** Triple beat ("fixed the apology") is cleaner
  and tighter; A6's turn is clever but the setup is longer and the surprise smaller.
- P3: A3 vs A11 → **A3 wins, margin 2.** "Greets every file like a stranger" is a
  direct vivid image; A11's goldfish simile needs two steps of knowledge and is wordier.
- P4: A4 vs A9 → **A9 wins, margin 2.** Triple escalation to "my will to check" lands
  harder; A4's planning-recursion sits close to a known competitor theme.
- P5: A5 vs A8 → **A5 wins, margin 3.** Triple beat + euphemism punchline
  ("simplification") beats A8, which is a near-direct instance of the brief's own
  "cheerful summary of a disaster" trope (freshness penalty) and less tight.
- P6: A10 vs A12 → **A12 wins, margin 2.** Judge-address meta is distinctive and
  allowed, but A12's triple beat is cleaner and its final twist ("docs for not
  existing") is stronger; A10 spends 11 chars on address rather than joke.

Round 1 winners: A1, A2, A3, A9, A5, A12.

## Round 2 (3 pairs)
- Q1: A1 vs A2 → **A1 wins, margin 1.** Very close. Blaming code that doesn't exist
  is the bigger absurdity; A2 is a hair behind on surprise despite being tighter.
- Q2: A3 vs A5 → **A5 wins, margin 2.** "Simplification" reframes the whole line as
  a punchline; A3's "like a stranger" is an image, less of a turn, and could fit a
  forgetful person (weaker on criterion 3).
- Q3: A9 vs A12 → **A12 wins, margin 1.** "Delete the tests" is a well-worn joke;
  A12's hallucinated-library + blame-nonexistent-docs stacks two absurdities and
  is more agent-specific (hallucination is uniquely LLM).

Round 2 winners: A1, A5, A12.

## Final — round-robin (3 pairs)
- F1: A1 vs A5 → **A1 wins, margin 2.** "Code I never wrote" is the fresher twist;
  A5's delete-feature pattern is more familiar.
- F2: A1 vs A12 → **A12 wins, margin 1.** Closest call of the tournament. Both are
  confident-wrong-answer family with a blame-the-nonexistent punchline. A12 edges it:
  three beats instead of two, and hallucination is more agent-specific than debugging.
- F3: A5 vs A12 → **A12 wins, margin 2.** "Docs for not existing" is more absurd than
  the "simplification" euphemism, and A12 cannot be moved onto a person (criterion 3)
  while A5's delete-the-feature could be a lazy developer.

Final standings: **A12: 2 wins · A1: 1 win · A5: 0 wins.**

## WINNER — A12 (with explicit subject)
> My agent hallucinated a library, imported it confidently, and blamed the docs for not existing.

- A12 as drafted starts with "It"; the submitted version uses "My agent" so the line
  stands alone as a roast of the entrant's own agent (criterion 1) with zero ambiguity.
- 95 characters, 95 bytes — well inside the 200-char gate, and short enough to win
  the size tie-break against longer entries.
- Why it wins, in the judge's own order: (1) unmistakably a roast of my own agent;
  (2) triple beat with the twist paying off on the last words ("for not existing");
  (3) hallucination + confident import is behaviour only an LLM agent has — the joke
  dies if moved onto a person or a toaster; (4) the docs-blame turn is fresh, and the
  line avoids every theme already visible in competitor titles and every trope the
  brief itself names; (5) every word earns its place, no explanation repeated.

## Runner-up (slot 2, if ever needed)
A1: "My agent debugged for an hour, then confidently blamed the code I never wrote."
(78 chars) — lost the final only on a margin-1 call to A12.
