from pathlib import Path
from typing import List

REF_FOLDER_PATH = Path("ref")


def get_file_lines(path: Path) -> List[str]:
    with open(path, "r") as fp:
        return fp.readlines()
