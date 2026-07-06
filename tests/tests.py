import pytest
import os
from pathlib import Path
import sys
import shutil

# Add the parent directory (one level up) to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from generateTestData import main

# Run this in testDataGenerator, not
def test_generation():
    sys.argv[1] = "tests/test_settings_1.json"
    #with pytest.raises(SystemExit) as wrapped_error:
    main()
    directory_path = Path('output/output/output1')

    # rglob('*') finds all items recursively; item.is_file() excludes folders
    file_count = sum(1 for item in directory_path.rglob('*') if item.is_file())
    assert file_count == 100

    filesInSizeRange = True
    for file in directory_path.rglob('*'):
        if file.is_file():
            if (os.path.getsize(file) > 1999999) or (os.path.getsize(file) < 10000):
                filesInSizeRange = False
    assert filesInSizeRange

    # Clear out output1 for later test
    shutil.rmtree(Path('output/output'))