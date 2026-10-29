# Claude makes gov — coalition consensus-statement exercise

Analytical simulation: drafting a minimal-concession 4-year coalition statement for the
Israeli "change bloc" after the 27 Oct 2026 Knesset election, based on the public positions
of 9 political movements. Agents *simulate* each movement from public sources; nothing here
speaks for any real party.

## Movements (9)
| slug | movement | list (2026) |
|---|---|---|
| yashar | Yashar (Gadi Eisenkot) | Yashar |
| bennett | Bennett's party (Bennett 2026) | Together (B'Yachad) |
| yesh-atid | Yesh Atid (Yair Lapid) | Together (B'Yachad) |
| yisrael-beiteinu | Yisrael Beiteinu (Avigdor Lieberman) | Yisrael Beiteinu |
| democrats | The Democrats (Yair Golan; Labor+Meretz) | The Democrats |
| raam | Ra'am / United Arab List (Mansour Abbas) | Ra'am |
| hadash | Hadash | Joint List |
| taal | Ta'al (Ahmad Tibi) | Joint List |
| balad | Balad | Joint List |

## Run 2 (adversarial re-run): start here
- `final/assessment.md`: honest bottom line. No government can be formed; three Knesset bills are agreed by all nine.
- `CHANGES_run2.md`: what changed from run 1 and why, and how the verification findings were resolved.
- `research/<slug>.md`: re-verified dossiers. Section 0 of each is a claim-by-claim log of run 1's dossier.
- `research/RESULTS_2026.md`: the fact base (seats, blocs, statements).
- `research/STYLE_GUIDE.md`: verbatim models of real drafting.
- `drafts/statement_v4–v6.md` and `reviews/run2/round_1–3/`: the negotiation rounds.
- `reviews/run2/lock_check/`: the parties' final wording checks.
- `final/`: the framework in Hebrew (the original), English and Arabic; the TV statements; the PDF.

## Process (run 1)
- A: `research/<slug>.md` — per-movement dossiers (quotes kept in original language)
- B: `drafts/statement_vN.md` — consolidated statement + reasoning
- C/D: `reviews/round_N/<slug>.md` — per-movement reviews, `reviews/round_N/consolidation.md`
- E: `final/` — statement in Hebrew, English, Arabic
