---
name: skill-templates
allowed-tools:
  - Bash(python3 "templates/template.py" *)
  - Bash(python3 templates/template.py *)
description: >
  Standardize agent replies with reusable templates.
license: MIT
compatibility: Requires Python 3 and an agent runtime that can run shell commands.
metadata:
    type: task
    status: draft
---

| Name | Description |
|---|---|
| Skill templates | Standardize agent replies with reusable templates. |

# Skill Templates

## Steps

Read the target skill's `SKILL.md` and `templates/` folder. Determine the operation from the request.

### Add

1. Get the templates:
   - `python3 templates/template.py add.script`
   - `python3 templates/template.py add.preview`
   - `python3 templates/template.py add.result`
2. Draft the new templates, the script and the target `SKILL.md` changes by the rules below.
3. Use `add.preview` and wait for the user's response.
4. Write the files as the plan says and use `add.result`.

### Update

1. Get the templates:
   - `python3 templates/template.py update.preview`
   - `python3 templates/template.py update.result`
2. Draft the template and target `SKILL.md` changes by the rules below.
3. Use `update.preview` and wait for the user's response.
4. Write the files as the plan says and use `update.result`.

### Delete

1. Get the templates:
   - `python3 templates/template.py delete.preview`
   - `python3 templates/template.py delete.result`
2. Use `delete.preview` and wait for the user's response.
3. Delete the files as the plan says and use `delete.result`.

### Error

1. Get the template with `python3 templates/template.py error`.
2. Use `error` when template work cannot continue.

## Templates architecture

Templates are stored in the target skill's `templates/` directory:

```text
<skill>/
└── templates/
    ├── <mode>.<template>.md
    └── <template>.md
```

- `<mode>` identifies the workflow context or operation, such as `add`, `update`, `delete` or `error`.
- `<template>` identifies the concrete purpose of the reply within that mode.
- Use `<template>.md` when the skill has no modes.

Examples:

- `add.preview.md` — a preview before adding files.
- `add.result.md` — the result after adding files.
- `update.preview.md` — a preview before updating files.
- `delete.confirmation.md` — a confirmation before deleting files.
- `error.md` — an error reply for a skill without modes.

## Template files

- Use one file for each reply, report or file format.
- Only the shape the agent fills: placeholders in `<angle brackets>`, no inline examples of real data.
- Explain how to fill the template in `<!-- -->` comments: one at the top describing what it is for and when to use it, and one above each field or section with specific filling instructions.
- Never put template markdown inline in `SKILL.md`.
- Get templates with `python3 templates/template.py <mode>.<template>`.

## User interaction

A reply template can define one of three expected interaction types:

| Type | Use when | Example |
|---|---|---|
| Question | The user needs to confirm or choose. | “Do it?” or “Commit it?” |
| Result | The user needs the requested output. | A commit name. |
| Actions | The user chooses one action. | 1) Retry<br>2) Fix<br>3) Ignore |

## Translation

- Translate all text shown to the user, including field labels such as “Files”, “Status” and “Next step”.
- Do not translate code, paths, names or placeholders. Keep them in backticks, such as `SKILL.md`, `templates/` and `<file>`.

## Script

- Create `<skill>/templates/template.py` from the `add.script` template.
- In `template.py`, `TemplateName` is the list of template names that the script accepts. Add one name for each template file without the `.md` extension. For `<mode>.<template>.md`, use `<mode>.<template>`.
- Add the Python command to `allowed-tools` in the target skill's frontmatter:
  - `Bash(python3 "templates/template.py" *)`
  - `Bash(python3 templates/template.py *)`

