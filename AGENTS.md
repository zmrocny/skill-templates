# AGENTS.md

This repo ships Agent Skills for defining interaction templates.

## Layout

| Path | Purpose |
|---|---|
| `skills/skill-templates/SKILL.md` | The skill's main file. |
| `skills/skill-templates/templates/` | The skill's own templates, named `<mode>.<template>.md`, and `template.py` that prints them. |
| `apm.yml` | APM package manifest. |
| `.claude-plugin/` | Claude Code plugin metadata, marketplace listing and icon. |
| `README.md` | User-facing description and install instructions. |
| `LICENSE` | MIT. |

## Rules

- Never commit, tag or push for the maintainer.
- Keep the skill in `skills/skill-templates/`.

## Release

Versions follow semver. Each release gets a git tag `vX.Y.Z`.

1. Bump `version` in `apm.yml` and `.claude-plugin/plugin.json`; both must match.
2. Run `claude plugin validate . --strict` and `apm pack --dry-run`.
3. Give the maintainer the release commands:
   ```sh
   git add -A
   git commit -m "Release vX.Y.Z"
   git tag vX.Y.Z
   git push origin main vX.Y.Z
   ```
