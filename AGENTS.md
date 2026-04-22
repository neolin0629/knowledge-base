This repository is a hierarchical knowledge base rather than a traditional software repository.

## Core rule

When working on any file or task, do NOT load every CLAUDE.md in the vault.

Instead, determine the target file or target directory first, then load only the relevant CLAUDE.md files along that path from the repository root down to the nearest directory.

Priority is proximity-based:

1. The nearest CLAUDE.md to the target file has the highest priority.
2. Parent-directory CLAUDE.md files provide broader context.
3. The root CLAUDE.md provides global defaults.
4. If rules conflict, prefer the more local CLAUDE.md.

## Rule loading algorithm

For a target file, use this process:

1. Identify the target file or working directory.
2. Walk upward from the target directory to the repository root.
3. Collect every CLAUDE.md found on that path only.
4. Merge them from root to leaf.
5. Apply local rules as overrides, not as parallel equal-priority rules.

Do not load CLAUDE.md files from sibling branches or unrelated content areas.

## Scope examples

If working on:
`3-Areas/Content/xhs-dahao/drafts/some-post.md`

Load only:
- `/CLAUDE.md`
- `/3-Areas/Content/xhs-dahao/CLAUDE.md`
- and any deeper CLAUDE.md within the exact path, if present

Do NOT load:
- `/3-Areas/Content/xhs-xiaohao/CLAUDE.md`
- `/3-Areas/Content/wechat/CLAUDE.md`

## Task execution policy

Before making edits, first infer the task type:

- knowledge organization
- article drafting
- article rewriting
- publishing cleanup
- topic extraction
- asset organization
- prompt generation

Then apply the relevant rules from the active CLAUDE.md chain.

## Editing behavior

When editing content:
- preserve the folder-specific intent
- preserve account-specific tone and audience positioning
- avoid introducing rules from unrelated branches
- prefer minimal, precise edits unless broader restructuring is requested

## If ambiguity exists

If the target file or target directory is unclear, infer the most likely scope from the user's current working path, mentioned file path, or explicitly referenced folder.

If still unclear, default to the narrowest reasonable scope rather than the whole vault.

## Important restriction

Do not treat all CLAUDE.md files as globally active at the same time.
This vault uses hierarchical scoped instructions.