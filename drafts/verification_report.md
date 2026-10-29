# Verification report: Hebrew and Arabic texts against the English

Verifier: independent back-translation check. No file under `final/` was edited, and nothing was committed.
Back-translations: `drafts/backtranslation_he.md`, `drafts/backtranslation_ar.md`.

## 0. Method and caveats

1. **Step 1 was not fully blind for TV (a).** A heading grep on `tv_statement.md` printed the English block of (a) before I translated it. `statement_en.md` and the English of (b) and (c) were opened only after both back-translations were saved.
2. **A commit landed mid-task.** Commit 89e8134 (06:42) changed the clause 1 footnote, the reservations table, Part B §1 and Part D in all three languages. Both back-translations were updated for it, and this report covers the committed state.
3. **The "original" label does not match how the text was made.** The status note says "The Hebrew text is the original". `drafts/he_drafting_notes.md` shows the Hebrew was drafted *from* `statement_en.md`. Where Hebrew and English differ below, the Hebrew is the declared master, but the English is the actual source. The parties should be told which text governs.
4. **Documented differences are still listed.** Several differences were made on purpose and recorded in the drafting notes or accepted in `reviews/run2/lock_check/`. They are still listed, because they differ in meaning, with a **Doc** column:
   - **D**: documented in the drafting notes;
   - **A**: accepted by the named party in a lock check;
   - **–**: undocumented.

Severity: **HIGH** changes a negotiated commitment or a party's sensitive term. **MEDIUM** is a noticeable shift. **LOW** is a nuance.

## 1. HIGH items

| # | File / clause | Original wording | Back-translation | English master | Doc | Note |
|---|---|---|---|---|---|---|
| H1 | AR A16 and B7 | «المسجد الأقصى المبارك / الحرم القدسي الشريف» | "the Blessed al-Aqsa Mosque / al-Haram al-Sharif" | A16: "on the Temple Mount (al-Aqsa)"; B7: "including al-Aqsa" | D; A by Ra'am and Ta'al | "Temple Mount" disappears from the Arabic government text. "The Mosque" is also narrower than the Mount/compound. Yashar, Yisrael Beiteinu, Bennett and Yesh Atid locked "הר הבית" but checked only the Hebrew. |
| H2 | **EN** B7 against HE B7 (master) | HE «לרבות בהר הבית (אל-אקצא)» | "including on the Temple Mount (al-Aqsa)" | "including al-Aqsa" | D (HE notes §2, flagged) | The English master drops Temple Mount from the government's own letter. That is inconsistent with EN A16 and with Yisrael Beiteinu's lock. |
| H3 | AR A13c | «لا تُقام مستوطنات جديدة… البناء في المستوطنات القائمة» | "no new settlements… construction in the existing settlements" | "No new communities… existing communities" | D (AR notes §4.3, flagged as a risk) | The listed term communities→settlements. The signatories (Yashar, Yesh Atid, Democrats) have not approved it. Fallback offered in the notes: «بلدات». |
| H4 | AR A13d, A14 (×2), Democrats reservation, D-Balad | «البؤر الاستيطانية غير القانونية»; «لن تُشرعَن»; «الشرعنة» | "illegal settlement outposts"; "will not be legalized"; "legalization" | "unauthorized outposts"; "regularized"; "regularization" | D; A by Ta'al ("the gap favours us") | "Unauthorized" (under Israeli law) became "illegal". "Regularize" became "legalize". In A14 the Arabic now says that some *illegal* outposts already in the pipeline will be *legalized*, which is a sharper statement than the English. The signatories have not approved it. Fallback in the notes: «غير المرخّصة». |
| H5 | HE A12 (master) against EN and AR | HE «בתוך 14 ימים מיום השבעתה תחליט הממשלה, לפי חוק ועדות חקירה, התשכ"ט–1968, על הקמת ועדת חקירה ממלכתית»; AR «تقيم الحكومة، خلال 14 يومًا… لجنة تحقيق رسمية» | HE: "will *decide*, under the Commissions of Inquiry Law 1968, on establishing…"; AR: "the government *establishes* within 14 days… an official commission" | "Within 14 days… the government will establish a state commission of inquiry" | D (HE notes §3, marked "same meaning") | It is not the same meaning. The English and Arabic promise that a commission exists within 14 days, while the Hebrew promises a government decision. The English and Arabic also drop the statutory anchor (the 1968 Law), which is what separates a state commission from a governmental one. The Arabic «رسمية» ("official") is weaker still. Recommendation: put "decide… under the Commissions of Inquiry Law, 1968" into the English and Arabic. |
| H6 | EN D, Hadash and Ta'al against HE and AR | HE «בגבולות 1967»; «זכותו של העם הפלסטיני להגדרה עצמית»; AR «على حدود 1967»; «حق الشعب الفلسطيني في تقرير المصير» | "on the 1967 *borders*"; "the *right* of the Palestinian people to self-determination" | "on the 1967 *lines*"; "self-determination for the Palestinian people" | – | "Lines" against "borders" is a contested term. Ta'al's locked Arabic and TV (c) both say "borders". For Hadash the English also drops "right". |
| H7 | HE and EN D, Joint List bullet 2, against AR | AR «تبقى القائمة شبكة أمان **لشعبنا**»; HE «רשת ביטחון **לחברה הערבית**» | AR: "a safety net for *our people*"; HE: "for *Arab society*" | "a safety net for Arab society" | A by Hadash (it proposed the Hebrew wording); Balad checked only the Arabic | In Joint List usage "our people" (شعبنا) means the Palestinian people. "Arab society" is the Israeli-civic framing. TV (c) says "a safety net for our people, not for the government". Confirm with Balad and Ta'al, or use "for our people" in all three languages. |

## 2. MEDIUM items

| # | File / clause | Original | Back-translation | English master | Doc | Note |
|---|---|---|---|---|---|---|
| M1 | HE and AR status paragraph | HE «בקולות המפלגות הערביות או בהימנעותן»; AR «على أصوات العرب أو على امتناعهم» | HE: "the votes of the *Arab parties*"; AR: "the votes of *the Arabs*" | "Arab votes or abstention" | D (HE "Check") | The three versions name different actors. The Arabic attributes to Bennett and Yisrael Beiteinu a rejection of *Arabs'* votes, not of Arab parties' votes. Use «أصوات الأحزاب العربية» and "the Arab parties' votes". |
| M2 | AR A10 | «جثامين القتلى» | "the bodies of the dead/killed" | "the bodies of the fallen" | D (for TV (a)) | The Hebrew חללים means fallen (soldiers and victims). The Arabic neutral «القتلى» changes the term. The hostages are rendered «المخطوفين» (abductees, not detainees), which is fine. |
| M3 | A14, reporting | HE «ודיווח על ההתקדמות יפורסם מדי רבעון»; AR «ويُقدَّم تقرير… كل ربع سنة» | HE: "a progress report will be *published* quarterly"; AR: "a report will be *submitted*" | "progress will be reported every quarter" | – | The Hebrew makes a public-reporting commitment. The English does not say to whom the report goes, and the Arabic ("submitted") is weaker. |
| M4 | Part B frame: addressee and signature | HE «לכבוד יו"ר הוועד הארצי…», «שלום רב», «בכבוד רב, גדי איזנקוט, ח"כ, המועמד להרכבת הממשלה»; AR «حضرات رؤساء السلطات المحلية العربية المحترمين», with no signature | HE: addressed to the *Chairman*, signed by Eisenkot; AR: addressed to *all heads* of Arab local authorities, unsigned | No addressee, no salutation, no signature | D (HE only) | The letter's commitments are personal to its signer. The English and Arabic texts are unsigned, and each version has a different addressee. |
| M5 | Part B title and A17 | HE «המועמד להרכבת הממשלה»; AR «رئيس الحكومة المكلَّف» | HE: "the *candidate* to form the government"; AR: "Prime Minister-*designate*" | "Prime Minister-designate" | – | "Designate" implies a formal presidential mandate, which the status note says does not exist. Minor legally, but it overstates. |
| M6 | TV (c) HE and EN against the Arabic original | «وقف هدم البيوت» | "*halting* house demolitions" | EN "an *end* to house demolitions"; HE «סוף להריסת בתים» | – | Both translations harden the original. Even "halting" overclaims against Part B, which promises only that enforcement against existing inhabited homes is frozen and that no inhabited home in the Negev process is demolished. |
| M7 | TV (c) EN | «وفق قرارات الشرعية الدولية» | "according to the resolutions of *international legitimacy*" | "in line with international resolutions" | – | «الشرعية الدولية» is a fixed Palestinian political term (UN resolutions, including 194). The English drops it; the Hebrew keeps it. |
| M8 | TV (a) in all languages against the statement | HE «מאחזים בלתי חוקיים»; AR «غير القانونية» | "illegal outposts" | TV "illegal outposts"; statement "unauthorized outposts" | A by Yesh Atid only | The Zionist leaders' spoken text uses the stronger term the legal text avoids. It is also the main argument in the Arabic drafting notes for H4. Confirm with Yashar, Bennett and Yisrael Beiteinu. |
| M9 | TV (b) and (c), all languages, against Part B §3 | «تجميد قانون كامينيتس» | "freezing the Kaminitz Law" | "the Kaminitz Law frozen" | – | Part B freezes only *enforcement against existing inhabited homes*. The TV lines claim more than the letter gives. These are the parties' own originals, so this is a consistency flag, not a translation error. |
| M10 | AR D, Ta'al | «وعدم شرعية المستوطنات» | "the *illegitimacy* of the settlements" | "the illegality of the settlements" | A by Ta'al (its own Arabic) | Hadash's line in the same list uses «عدم قانونية» (illegality), so the distinction looks deliberate. The Hebrew and English should then say "illegitimacy", or Ta'al should confirm "illegality". |

## 3. LOW items

| # | File / clause | Original → back-translation | English | Note |
|---|---|---|---|---|
| L1 | HE and AR status bullets | HE «יחתמו / תצביע / יאפשרו לה לקום» "will sign / will vote / will allow it to be formed"; AR «مستعدون للتوقيع / ستدعه يمرّ» "are ready to sign / will let it pass" | "would sign / would vote / would let it stand" | The English is conditional and the Hebrew is indicative. The object of "let it stand" differs between versions. |
| L2 | AR title | «إصلاح» "reform" | "Repair" | «إصلاح» can echo the "judicial reform"; «ترميم» or «تصحيح» would avoid that. |
| L3 | HE and EN A3, quotation | HE «לכל אזרחיה» "all its *citizens*" | AR and EN "all its *inhabitants*" | Each follows its own official text of the Declaration (D). "Inhabitants" is the broader word. |
| L4 | HE A3 | «מצהירות» "declare" | "affirm" (AR «تؤكد») | Nuance. |
| L5 | EN and AR A6 lead | HE «תביא הממשלה לחקיקת חוק» "will bring about enactment" | "will pass a law" (AR «تسنّ») | The government cannot pass laws (D). |
| L6 | AR A6a | «كل شاب وشابة… قانون خدمة الأمن» "every young man and woman"; the citation (1986, consolidated version) is dropped | "Every young person liable under the Security Service Law" | No change in meaning. |
| L7 | AR A6d | «وقف الامتيازات» "stopping" | "suspending" | Slightly stronger. |
| L8 | AR A7 | «ستعمل على الدفع قُدمًا» "will work to advance"; «تقريرها» "report" | "will advance"; HE «מסקנות» "conclusions" | The Arabic is weaker. "Report" and "conclusions" are a nuance. |
| L9 | EN A10 | HE «החטופים שנותרו» "the remaining hostages"; AR «من تبقّى» | "any remaining hostages" | The English hedges whether any hostages remain. |
| L10 | HE A11 and TV (a) | «קומץ אלים» "violent handful" | "small, violent minority" (AR A11 «أقلية صغيرة»; AR TV (a) «حفنة») | A locked term in each language (D). The Arabic is inconsistent between the statement and TV (a). |
| L11 | AR A11 | «لواء الشرطة في الضفة الغربية (لواء يهودا والسامرة)» | "the Judea and Samaria police district" | Name order reversed for the audience (D). |
| L12 | AR preamble, A13, A13 heading | «الضفة الغربية (يهودا والسامرة)» | EN preamble "Judea and Samaria"; heading "Judea and Samaria (the West Bank)" | Primary name inverted (D; locked by Hadash). |
| L13 | AR B3 and Part C | «تجميد تطبيق قانون كامينيتس» "freezing the *application* of the Kaminitz Law" | "enforcement… frozen" | «تطبيق القانون» usually means enforcement, but it can be read as non-application of the law. Locked by Ra'am and Hadash. |
| L14 | AR B5 | «لن تعرقل» "will not obstruct" | "will not block"; HE «לא ימנעו» "will not prevent" | Nuance. |
| L15 | B7 | HE «צעד שיש בו כדי למנוע» "liable to prevent"; AR «تحول دون» "prevents" | "precludes" | The Hebrew is slightly broader. |
| L16 | HE D, Ra'am | «שלא מסיבה מוצדקת» "not for a justified reason" | "without cause" (AR «دون سبب») | Ra'am supplied both wordings. Same intent. |
| L17 | HE D, Ra'am | «באל-אקצא» alone | "al-Aqsa" | `he_drafting_notes.md` §2 says Ra'am's Hebrew reply should read «הר הבית (אל-אקצא)». The current file does not. |
| L18 | AR D, Ra'am | adds «تجاه المجتمع العربي» "toward Arab society" | "budgets that fund Part B" | Descriptive addition (D). |
| L19 | AR D, Balad budget line | «للبؤر الاستيطانية غير القانونية» "illegal settlement outposts" | "outposts" (HE «למאחזים») | Narrows Balad's condition literally. Balad's own lock term (D). |
| L20 | TV (a) AR | «حكومة دولة يهودية وديمقراطية» "the government of a Jewish and democratic state" | "A Jewish and democratic state" | Nuance. |
| L21 | TV (b) HE and EN | «أهلنا الكرام» "our dear folk" → HE "my dear brothers and sisters"; «ثوابتنا» "our fixed principles/constants" → "principles" | "Dear people"; "principles" | Register. «ثوابت» is stronger than "principles". |
| L22 | TV (b), all languages | withdrawal "if al-Aqsa is touched or the commitments are broken" | the same | Omits Part D's 60-day cure period. This is the party's own text, so it is a consistency flag only. |
| L23 | TV (c) HE | adds «שלכם ולא של אף אחד אחר» "yours and no one else's"; «منع الضمّ» "preventing annexation" → «בלי סיפוח» "without annexation" | "This is your achievement"; "no annexation" | Small addition and softening. Hadash accepted the Hebrew. |
| L24 | All three, D, Balad budget line | HE «רק אם», AR «لن… إلا إذا», EN "only if" | – | All three say "only if". With "otherwise vote against", the intent ("if and only if") is clear enough. |

## 4. Status tables

- **Front status table:** every cell matches in meaning across the three languages: signs/rejects/supports, "not a party; votes for investiture / abstains / absent", Part C ranges, "4 on conditions", and Part D "publishes (joint)". **No cell differs.**
- **Part C vote table:** matches in all three, including "for, while 6c stands". **No cell differs.**
- **Reservations table:** after 89e8134 the three languages match. This includes the Yashar sentence on legislation and Yesh Atid's signature condition.

## 5. Where the English master is weaker, more awkward or more ambiguous than the native texts

1. **Status: "Arab votes or abstention".** This can be read as Arab *voters*. The Hebrew ("the Arab parties' votes") is more precise and avoids a slur reading. See M1.
2. **Status: "would let it stand".** "It" can mean the text or the government. The Hebrew ("allow it to be formed") is clearer.
3. **A6: "the government will pass a law".** This is legally wrong; the Knesset passes laws. The Hebrew "bring about the enactment" is correct.
4. **A12: "will establish… within 14 days".** This is legally inaccurate and has no statutory anchor. See H5.
5. **A14: "progress will be reported".** It does not say to whom. The Hebrew says "published". See M3.
6. **A10: "any remaining hostages".** This is a hedge that neither native text has. See L9.
7. **A7: "with broad agreement".** It is unclear whether this covers the term-limit law too. The Hebrew keeps the same ambiguity on purpose (HE notes §4.2).
8. **A6d: "suspending benefits linked to service".** It does not say whose benefits. The ambiguity is shared by all three.
9. **A7 last sentence against the Yashar reservation.** A7 says a return to the pre-25th-Knesset arrangements "is not a change requiring broad agreement". Yashar's reservation now requires it to be made "by legislation, after the committee reports". This is a substantive tension in all three languages, not a translation issue, but readers will notice it.
10. **Part B has no addressee, salutation or signature.** "I ask you" has no "you", and the commitments have no named signer. The Hebrew is a proper signed letter. See M4.
11. **B7: "including al-Aqsa".** This is inconsistent with the English's own A16 ("Temple Mount (al-Aqsa)"). See H2.
12. **Part D: "1967 lines" and "self-determination for".** These are weaker than the parties' own Hebrew and Arabic. See H6.
13. **A11: "small, violent minority".** "Minority" implies a sizeable group. The Hebrew "handful" and the Arabic TV «حفنة» are tighter. This is locked, so leave it, but note the gap.

## 6. Recommended actions

- **Conform the English to the Hebrew master** on H2 (B7 Temple Mount), H5 (decide, under the 1968 Law), H6 ("borders", "the right of") and M3 ("published"). Add the Part B frame and signature to the English and Arabic (M4).
- **Put the Arabic term choices to the signatories, since they checked only the Hebrew.** These are H1 (al-Aqsa without Temple Mount), H3 («مستوطنات») and H4 («غير القانونية», «تُشرعَن»). Fallbacks are already in the Arabic drafting notes.
- **Ask Balad and Ta'al** about "Arab society" against "our people" (H7).
- **Fix the actor in the Arabic status paragraph** (M1).
