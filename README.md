Sauce Demo Selenium Test Automation Project
🚀 Setup Instructions
1. Clone the Repository
bash
git clone https://github.com/yourusername/sauce_demo_tests.git  
cd sauce_demo_tests  
2. Create Virtual Environment
Windows
powershell
python -m venv venv  
venv\Scripts\activate  
Mac/Linux
bash
python3 -m venv venv  
source venv/bin/activate  
3. Install Dependencies
bash
pip install -r requirements.txt  
🧪 Running Tests
Run All Tests
bash
pytest tests/ --html=report.html  
Run Specific Test
bash
pytest tests/test_e2e_flow.py::test_valid_purchase_flow  
📋 Test Scenarios Covered
✅ Successful Login and Purchase Workflow
✅ Invalid Login Validation
✅ Add to Cart Functionality
🛠️ Technologies Used
Python
Selenium WebDriver
pytest
WebDriver Manager
pytest-html
📊 Reporting
Test reports are generated in HTML format. After running tests, check report.html for detailed test results.

🔄 Continuous Integration
GitHub Actions workflow is configured for automated testing on push and pull requests.

🛠 Troubleshooting
Ensure Chrome browser is installed
Check WebDriver compatibility
Verify Python and pip versions
🤝 Contributing
Fork the repository
Create your feature branch
Commit your changes
Push to the branch
Create a Pull Request
📄 License
This project is open-source and available under the MIT License.
