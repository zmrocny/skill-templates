<!-- The template script of the target skill: `<skill>/templates/template.py`. Not a reply.
     Copy it as is; add one name to `TemplateName` for each template file, using `<mode>.<template>`. -->
#!/usr/bin/env python3
import sys
from pathlib import Path
from typing import Literal, get_args

TemplateName = Literal[
    '<mode>.<template>',
]

if sys.argv[1] not in get_args(TemplateName):
    sys.exit(f'Template not found: {sys.argv[1]}. Available: {", ".join(get_args(TemplateName))}')

sys.stdout.write(
    (Path(__file__).parent / f'{sys.argv[1]}.md').read_text(),
)
