---
name: compile-latex
description: Handles LaTeX compilation workflow including auxiliary file cleanup and proper citation compilation. Use when compiling LaTeX documents, fixing missing citations, or cleaning up auxiliary files.
---

# Compile LaTeX

## Rule: Always Delete Auxiliary Files After Compiling

**Whenever you compile a `.tex` file, delete the resulting auxiliary files in that directory immediately after compilation.** Do not leave `.aux`, `.log`, `.out`, `.fls`, `.fdb_latexmk`, or `.synctex.gz` in the folder. Keep only `.tex` and `.pdf` (and `.bib`/`.bst` if present).

---

## Skill: LaTeX Compilation Workflow

### Compilation Process for Citations

To ensure all citations and references appear correctly, run the full compilation cycle:

```
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

**Important**: In PowerShell, run these as separate commands (do NOT use `&&` which is not supported).

#### When to Use Full Compilation

- After adding new `\cite{}` commands
- After modifying `library.bib`
- When citations show as "?" in the PDF
- After deleting auxiliary files

#### Quick Compilation (No Citation Changes)

If no bibliography changes, a single run suffices:

```
pdflatex -interaction=nonstopmode main.tex
```

### Auxiliary Files

#### Common Auxiliary File Extensions

| Extension | Purpose |
|-----------|---------|
| `.aux` | Cross-references and citations |
| `.log` | Compilation log |
| `.out` | Hyperref bookmarks |
| `.bbl` | Processed bibliography |
| `.blg` | BibTeX log |
| `.toc` | Table of contents |
| `.lof` | List of figures |
| `.lot` | List of tables |
| `.fls` | File list (latexmk) |
| `.fdb_latexmk` | Latexmk database |
| `.synctex.gz` | SyncTeX data |

#### Cleaning Auxiliary Files

Before committing or when troubleshooting, delete auxiliary files:

**PowerShell** (e.g. in the draft folder):

```powershell
Remove-Item main.aux, main.log, main.out, main.bbl, main.blg, main.fls, main.fdb_latexmk -ErrorAction SilentlyContinue
```

Or use the Delete tool to remove each file individually.

#### Files to Keep

- `.tex` - Source files
- `.pdf` - Compiled output
- `.bib` - Bibliography database
- `.bst` - Bibliography style

#### Files to Delete Before Commit

- All auxiliary files listed above
- Temporary/standalone compilation files (e.g. `*_standalone.tex`, `*_standalone.pdf`)

### Project-Specific Notes

- Main document: `draft/main.tex`
- Bibliography: `draft/library.bib`
- Bibliography style: `draft/ecta.bst` (Econometrica style)
- The estimation section is in `draft/estimation_gmm.tex` (included via `\input{estimation_gmm}`)

### Troubleshooting

**Citations Show as "?"**

1. Delete all auxiliary files
2. Run the full compilation cycle (pdflatex → bibtex → pdflatex → pdflatex)

**Undefined References**

1. Run pdflatex twice to resolve cross-references
2. Check that all `\label{}` commands are defined before `\ref{}` calls

**BibTeX Errors**

1. Check `main.blg` for error messages
2. Verify bibliography entries in `library.bib` are correctly formatted

---

## Examples

### Example 1: First compile after adding citations

User added `\cite{smith2020}` to `draft/main.tex` and a new entry to `draft/library.bib`.

**Steps:**

1. From project root (or `draft/`), run full cycle. In Bash:
   ```bash
   cd draft && pdflatex -interaction=nonstopmode main.tex && bibtex main && pdflatex -interaction=nonstopmode main.tex && pdflatex -interaction=nonstopmode main.tex
   ```
2. In PowerShell, run each of the four commands separately in `draft/`.

### Example 2: Citations show as "?" in PDF

**Steps:**

1. Delete auxiliary files in `draft/`:
   - `main.aux`, `main.log`, `main.out`, `main.bbl`, `main.blg`, `main.fls`, `main.fdb_latexmk`
2. Run full compilation cycle (pdflatex → bibtex → pdflatex → pdflatex).

### Example 3: Quick compile (no .bib changes)

User only changed body text in `main.tex` or `estimation_gmm.tex`.

**Step:**

- Run once: `pdflatex -interaction=nonstopmode main.tex` (from `draft/` or with path to `main.tex`).

### Example 4: Clean before commit

**Steps:**

1. Delete all auxiliary files in `draft/` (see table and cleanup commands above).
2. Optionally remove any `*_standalone.tex` / `*_standalone.pdf` if present.
3. Keep: `main.tex`, `estimation_gmm.tex`, `library.bib`, `ecta.bst`, and the final `main.pdf`.

### Example 5: Compiling a different document (e.g. resume)

For a document with no bibliography (e.g. `Resume_HSU_Ke_Cheng.tex`):

**Steps:**

1. Run once: `pdflatex -interaction=nonstopmode Resume_HSU_Ke_Cheng.tex` (from the directory containing the `.tex`).
2. **Delete auxiliary files** in that directory: `Resume_HSU_Ke_Cheng.aux`, `Resume_HSU_Ke_Cheng.log`, and any `.out`, `.fls`, `.fdb_latexmk`, `.synctex.gz`. Keep only the `.tex` and `.pdf`.
