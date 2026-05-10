"""Ensure ``python/code`` is on ``sys.path`` for tests under ``python/test/``."""

from __future__ import annotations

import sys
from pathlib import Path

_CODE = Path(__file__).resolve().parent.parent / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))
