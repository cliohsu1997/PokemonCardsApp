---
name: polish-cv-resume
description: Tailors a resume (and optionally cover letter) from a job description using the user's baseline resume. Use when the user provides a job description and wants a tailored resume, CV, or application materials. Resumes go in Resume/; cover letters in Cover_letter/.
---

# Polish CV and Resume

## When to Use

- User provides a **job description** (or link/paste) and wants a **tailored resume**.
- User asks to "tailor my resume for [role]", "create a resume for [job]", or "polish my CV for this position".

## Workflow

### 1. Baseline Resume

- **Source:** `Resume_HSU_Ke_Cheng.tex` in the project root (and its current layout/fonts).
- Use this as the template: same structure (Professional Summary, Education, Experience, Projects, Leadership, Skills), same LaTeX preamble and formatting.

### 2. Naming and Location

- **Folders:** Put tailored **resumes** in **`Resume/`**; put **cover letters** in **`Cover_letter/`**.
- **Filename pattern:** Everything starts with the type, then name, then job title, then year.
  - **Resumes:** `Resume_Name_Title_Year.tex` and `.pdf` in `Resume/`. Example: `Resume_HSU_Ke_Cheng_SP_Ratings_Summer_Intern_2026.tex`.
  - **Cover letters:** `Cover_letter_Name_Title_Year.tex` and `.pdf` in `Cover_letter/`. Example: `Cover_letter_HSU_Ke_Cheng_SP_Ratings_Summer_Intern_2026.tex`.
  - Use underscores; no spaces or `&`. Normalize job title to a short slug (e.g. `SP_Ratings_Summer_Intern_2026`).
- **Auxiliary files:** After compiling, **delete** LaTeX auxiliary files (`.aux`, `.log`, `.out`, `.fls`, `.fdb_latexmk`, `.synctex.gz`) in that folder. Keep only `.tex` and `.pdf`. Also delete auxiliary files for the baseline resume (`Resume_HSU_Ke_Cheng.aux`, `Resume_HSU_Ke_Cheng.log`, etc.) when cleaning.

### 3. Tailoring the Resume

- **Professional summary:** Rewrite to match the role: mention the company/industry, key requirements (e.g. credit analysis, Excel, Mandarin), and the type of position (intern, analyst). Keep length similar (about 50–100 words).
- **Experience and projects:** Keep the same roles and projects; rephrase bullets to emphasize:
  - Keywords from the job description (e.g. financial analysis, credit, research, modeling, data, reporting, presentations, collaborative, detail-oriented).
  - Skills they ask for (e.g. MS Excel, PowerPoint, Word; financial statements; fluency in English/Mandarin).
- **Skills:** Reorder or slightly rephrase to lead with what the JD asks for (e.g. Excel, PowerPoint, Word; Languages: Mandarin, English). Add an **Attributes** line if the JD stresses soft skills (e.g. detail-oriented, collaborative, works under time pressure).
- **Do not** invent jobs or qualifications; only reframe and reorder existing content.

### 4. Compilation and Cleanup

1. Compile: `pdflatex -interaction=nonstopmode Resume_Name_Title_Year.tex` from `Resume/` (or `Cover_letter_Name_Title_Year.tex` from `Cover_letter/` for cover letters).
2. **Whenever you compile any `.tex` file, delete the auxiliary files in that directory immediately after:** `.aux`, `.log`, `.out`, `.fls`, `.fdb_latexmk`, `.synctex.gz`. Keep only `.tex` and `.pdf` in the folder.

### 5. Cover Letter (Optional)

- If the user asks for a **cover letter**, create `Cover_letter_Name_Title_Year.tex` (and `.pdf`) in `Cover_letter/`.
- One page; same tone and keywords as the tailored resume; address why this role and company, and one or two concrete examples from the resume that match the JD.

## Examples

**User:** "Tailor my resume for S&P Ratings Summer Intern HK 2026."

**Actions:**

1. Read job description (or use the one provided).
2. Create `Resume/Resume_HSU_Ke_Cheng_SP_Ratings_Summer_Intern_2026.tex` from `Resume_HSU_Ke_Cheng.tex`.
3. Tailor summary to credit/corporates/HK/APAC, Excel/PowerPoint, Mandarin+English; reframe bullets for analysis, research, modeling, reporting; highlight Excel, PowerPoint, Word.
4. Compile to PDF in `Resume/`; then delete auxiliary files in that folder.
5. Cover letter (if requested): `Cover_letter/Cover_letter_HSU_Ke_Cheng_SP_Ratings_Summer_Intern_2026.tex` and `.pdf`; compile and delete aux files there too.

**Output:** Resume and cover letter filenames follow `Resume_Name_Title_Year` and `Cover_letter_Name_Title_Year`. No auxiliary files left.
