# Selenium Sauce Automation Project

## Overview
This project is a robust end-to-end test automation framework for the [Sauce Demo](https://www.saucedemo.com/) web application, built using Python, Selenium WebDriver, and Pytest. It follows the Page Object Model (POM) design pattern for maintainability and scalability.

## Features
- Automated login, add-to-cart, checkout, and logout flows
- Page Object Model for clean separation of test logic and UI interactions
- Pytest fixtures for driver and page object management
- Price validation between inventory and checkout
- Modular structure for easy extension
- HTML reporting support

## Project Structure
```
Selenium Project/
│
├── pages/                # Page Object classes
│   ├── __init__.py
│   ├── login_page.py
│   ├── checkout_page.py
│   └── logout_page.py
│
├── tests/                # Test scripts
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_checkout.py
│   └── test_logout.py
│
├── utils/                # Utility modules
│   ├── __init__.py
│   └── driver_factory.py
│
├── report/               # Test reports
│   └── report.html
│
├── conftest.py           # Global pytest fixtures
├── requirements.txt      # Python dependencies
├── pytest.ini            # Pytest configuration
└── README.md             # Project documentation
```

## Getting Started

### Prerequisites
- Python 3.8+
- Google Chrome browser
- ChromeDriver (auto-managed by Selenium)

### Installation
1. Clone the repository:
   ```sh
   git clone <your-repo-url>
   cd "Selenium Project"
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running Tests
To run all tests:
```sh
pytest --html=report/report.html
```
To run a specific test file:
```sh
pytest tests/test_checkout.py
```

## Key Files
- `pages/login_page.py`: Page object for login functionality
- `pages/checkout_page.py`: Page object for cart and checkout
- `pages/logout_page.py`: Page object for logout
- `utils/driver_factory.py`: WebDriver setup utility
- `conftest.py`: Centralized pytest fixtures
- `tests/test_checkout.py`: Main checkout journey test

## How It Works
- Tests use fixtures to initialize the browser and page objects
- Page objects encapsulate UI interactions and assertions
- The checkout test adds products, validates prices, completes checkout, and logs out
- Results are reported in HTML format

## Best Practices
- Use the Page Object Model for maintainable tests
- Keep locators and UI logic in page classes
- Use fixtures for driver and page object management
- Validate business logic (e.g., price matching) in tests

## Troubleshooting
- Ensure Chrome and ChromeDriver versions are compatible
- If tests fail to find elements, check for UI changes or slow page loads
- Use `pytest -s` for debug output

## License
MIT

---
**Note:** The `Practicse_file/` directory is for learning and is not part of the main automation framework.
