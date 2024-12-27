from pathlib import Path
from typing import List


def get_file_lines(path: Path) -> List[str]:
    with open(path, "r") as fp:
        return fp.readlines()
