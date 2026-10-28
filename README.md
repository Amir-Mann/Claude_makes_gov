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

## Process
- A: `research/<slug>.md` — per-movement dossiers (quotes kept in original language)
- B: `drafts/statement_vN.md` — consolidated statement + reasoning
- C/D: `reviews/round_N/<slug>.md` — per-movement reviews, `reviews/round_N/consolidation.md`
- E: `final/` — statement in Hebrew, English, Arabic
