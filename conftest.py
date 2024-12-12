import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    # Setup Chrome WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # Configure browser
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    # Yield driver to test
    yield driver
    
    # Teardown
    driver.quit()

def pytest_terminal_summary(terminalreporter):
    with open('test_results.txt', 'w') as f:
        for outcome in ['passed', 'failed', 'skipped']:
            for test in terminalreporter.stats.get(outcome, []):
                f.write(f"{outcome.upper()}: {test.nodeid}\n")