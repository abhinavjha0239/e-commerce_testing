# Sauce Demo Selenium Test Automation Project  

## Overview  
This is a comprehensive Selenium test automation project for testing the Sauce Demo website (https://www.saucedemo.com/). The project demonstrates end-to-end testing using Python, Selenium WebDriver, and pytest.  

## Project Structure  
sauce_demo_tests/
├── tests/
│ ├── init.py
│ └── test_e2e_flow.py
├── pages/
│ ├── init.py
│ ├── login_page.py
│ ├── inventory_page.py
│ ├── cart_page.py
│ └── checkout_page.py
├── conftest.py
└── requirements.txt



## Features  
- Page Object Model implementation  
- Automated web testing for e-commerce workflow  
- Multiple test scenarios  
- HTML reporting  
- Cross-browser support  

## Prerequisites  
- Python 3.8+  
- pip  
- Chrome Browser  

## Setup Instructions  

### 1. Clone the Repository  
```bash  
git clone https://github.com/yourusername/sauce_demo_tests.git  
cd sauce_demo_tests  
2. Create Virtual Environment
bash
# Windows  
python -m venv venv  
venv\Scripts\activate  

# Mac/Linux  
python3 -m venv venv  
source venv/bin/activate  
3. Install Dependencies
bash
pip install -r requirements.txt  
Running Tests
Run All Tests
bash
pytest tests/ --html=report.html  
Run Specific Test
bash
pytest tests/test_e2e_flow.py::test_valid_purchase_flow  
Test Scenarios Covered
Successful Login and Purchase Workflow
Invalid Login Validation
Add to Cart Functionality
Technologies Used
Python
Selenium WebDriver
pytest
WebDriver Manager
pytest-html
Reporting
Test reports are generated in HTML format. After running tests, check report.html for detailed test results.

Continuous Integration
GitHub Actions workflow is configured for automated testing on push and pull requests.

Troubleshooting
Ensure Chrome browser is installed
Check WebDriver compatibility
Verify Python and pip versions
Contributing
Fork the repository
Create your feature branch
Commit your changes
Push to the branch
Create a Pull Request
License
This project is open-source and available under the MIT License.

