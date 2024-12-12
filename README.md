# Sauce Demo Selenium Test Automation Project

## 🚀 Project Overview

This is a comprehensive Selenium-based test automation project for the Sauce Demo web application, designed to ensure robust test coverage and reliable web application testing.

## 🧪 Test Scenarios

Our test suite covers critical functionality:
- ✅ Successful Login and Purchase Workflow
- ✅ Invalid Login Validation
- ✅ Add to Cart Functionality

## 🛠️ Technologies Used

- **Language:** Python
- **Testing Framework:** pytest
- **Automation Tool:** Selenium WebDriver
- **WebDriver Management:** WebDriver Manager
- **Reporting:** pytest-html

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/sauce_demo_tests.git
cd sauce_demo_tests
```

### 2. Create Virtual Environment

#### Windows
```powershell
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🧪 Running Tests

### Run All Tests
```bash
pytest tests/ --html=report.html
```

### Run Specific Test
```bash
pytest tests/test_e2e_flow.py::test_valid_purchase_flow
```

## 📊 Reporting

Test reports are generated in HTML format. After running tests, check `report.html` for detailed test results and insights.

## 🔄 Continuous Integration

GitHub Actions workflow is configured for automated testing on:
- Push events
- Pull request creation

## 🛠️ Troubleshooting

- Ensure Chrome browser is installed
- Check WebDriver compatibility
- Verify Python and pip versions

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🔗 Quick Links

- [Repository](https://github.com/yourusername/sauce_demo_tests)
- [Issues](https://github.com/yourusername/sauce_demo_tests/issues)

---

**Happy Testing! 🚀**
