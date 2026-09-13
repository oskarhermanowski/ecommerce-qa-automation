import sys
from pathlib import Path

UI_TESTS_DIR = Path(__file__).resolve().parent
sys.path.append(str(UI_TESTS_DIR))