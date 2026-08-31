# 📚 MAKAUT Sem-3 Study Books — Master Index

**Built from:** your 8 textbook PDFs (extracted & topic-mapped) + all 15 authentic MAKAUT question papers (2022-23, 2023-24, 2024-25, UPID-verified) + your chosen YouTube playlists (topic-matched video links).

## The two-book system (per subject)

**Concept Book** — teaches from zero to mastery in syllabus order: theory with full derivations → worked examples → *Exam Focus* (which real years/groups asked it) → traps → rapid recall → 📺 topic-wise video companion.

**Q&A Book** — every real PYQ of the last 3 cycles solved at exam length, ordered Group A → B → C inside each unit so reading front-to-back builds concepts cumulatively (every answer carries a *Concept bridge*). Ends with a 3-year **pattern map** predicting 2026 weightage.

## The books

| Subject | Concept Book | Q&A Book |
|---|---|---|
| Analog & Digital Electronics (ESC-301) | `Analog_and_Digital_Electronics/ADE_Concept_Book.md` | `ADE_QA_Book.md` — 66 solved |
| Computer Organization (PCC-CS302) | `Computer_Organization/CO_Concept_Book.md` | `CO_QA_Book.md` — 62 solved |
| Mathematics-III (BSC-301) | `Mathematics-III/M3_Concept_Book.md` | `M3_QA_Book.md` — 44 solved |
| Economics for Engineers (HSMC-301) | `Economics_for_Engineers/ECO_Concept_Book.md` | `ECO_QA_Book.md` — 60 solved |
| DSA (video prep only, per your choice) | — | `DSA/DSA_Video_Guide.md` — 63 videos by topic |

## How to study (suggested)

1. **First pass:** Concept Book chapter → its videos → the matching unit in the Q&A Book.
2. **Revision pass:** Q&A Books only, front to back (they are self-sufficient by design).
3. **Last 48 hours:** each book's *Rapid recall* boxes + formula sheets + the pattern maps' "Certain" rows, Group C versions first.

## Supporting data (all in `~/Sem3`)

- `PYQ's/` — the 15 renamed authentic papers + `extracted_json/` texts
- `extracted_json/` — full textbook texts, `topicmaps/` (65 syllabus topics → book pages), `video_maps/` (playlists → topics)
- `extract_books_to_json.py`, `detect_topics.py`, `extract_playlists.py` — the pipeline that built all of this
