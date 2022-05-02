# pycache 삭제하는 코드

import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]
import pathlib; [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]

