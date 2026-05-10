# Proposal: initialize_project_workflow

## Goal

Match this repository to `.cursor/rules/project-workflow.mdc`: create `conversation_cursor/`, `to-do/`, `task_summary/`, `progress/`, `structure/`, and root `IMPLEMENTATION_PLAN.md`. Remove nonessential upstream files while keeping `streamlit_app.py` and `.cursor/`.

## Approach

- Use dated folders `202605/20260510/` for the first task set (same basename across the three task locations).
- Delete upstream `README.md`, `requirements*.txt`, `.gitignore`, and decorative PNGs; keep git history and remotes.
- Make header images in `streamlit_app.py` conditional on file presence so the UI runs without those assets.

## Rationale

Workflow rules require consistent paths for proposals, to-dos, and summaries. Trimming the repo focuses the project on Streamlit + future SQL work without losing version control.
