#!/usr/bin/env python3
import sys
from pathlib import Path
from typing import Literal, get_args

TemplateName = Literal[
    'add.preview',
    'add.result',
    'add.script',
    'delete.preview',
    'delete.result',
    'error',
    'update.preview',
    'update.result',
]

if sys.argv[1] not in get_args(TemplateName):
    sys.exit(f'Template not found: {sys.argv[1]}. Available: {", ".join(get_args(TemplateName))}')

sys.stdout.write(
    (Path(__file__).parent / f'{sys.argv[1]}.md').read_text(),
)
