# Skill Templates

Standardize agent replies with reusable templates.

## Requirements

- Agent Skills-compatible runtime.
- `python3` on `PATH`.

## Install

### Any agent (skills CLI)

Works with Claude Code, Codex, Cursor, OpenCode and other agents that support Agent Skills:

```sh
npx skills add zmrocny/skill-templates
```

The CLI detects installed agents and asks where to put the skill.

### APM

With [APM](https://github.com/microsoft/apm) (Agent Package Manager):

```sh
apm install zmrocny/skill-templates       # current project
apm install -g zmrocny/skill-templates    # user scope, all projects
```

### Claude Code (plugin)

```
/plugin marketplace add zmrocny/skill-templates
/plugin install skill-templates@skill-templates
```

### Manually

Copy `skills/skill-templates/` into your agent's skills directory, for example `~/.claude/skills/` or `.agents/skills/`.

## Privacy

Skill Templates collects no data and makes no network requests. It reads and writes files of the skill you point it at, and runs a local Python script that prints its own templates.

## License

[MIT](LICENSE)
