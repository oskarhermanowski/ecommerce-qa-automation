import sys
from pathlib import Path

import pytest

UI_TESTS_DIR = Path(__file__).resolve().parent
sys.path.append(str(UI_TESTS_DIR))


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            screenshots_dir = UI_TESTS_DIR / "screenshots"
            screenshots_dir.mkdir(exist_ok=True)

            screenshot_path = screenshots_dir / f"{item.name}.png"

            page.screenshot(
                path=str(screenshot_path),
                full_page=True
            )