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
│   ├── report.html
│   ├── Checkout_report.html
│   └── assets/
│       └── style.css
│
├── Practicse_file/       # SKIP THIS FOLDER - Contains practice files not part of the main framework
│
├── conftest.py           # Global pytest fixtures
├── requirements.txt      # Python dependencies
├── pytest.ini            # Pytest configuration
└── README.md             # Project documentation
```

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Google Chrome browser (latest version recommended)
- An internet connection (to access Sauce Demo)

### Step-by-Step Setup and Execution Guide

#### Step 1: Clone the Repository
1. Open your terminal or command prompt.
2. Navigate to the directory where you want to clone the project.
3. Run the following command to clone the repository:
   ```sh
   git clone <your-repo-url>
   ```
   Replace `<your-repo-url>` with the actual URL of your repository.
4. Navigate into the project directory:
   ```sh
   cd selenium-sauce-automation
   ```

#### Step 2: Set Up a Virtual Environment
1. It's best practice to use a virtual environment to manage dependencies.
2. Create a virtual environment by running:
   ```sh
   python -m venv .venv
   ```
3. Activate the virtual environment:
   - **On Windows:**
     ```sh
     .\.venv\Scripts\activate
     ```
   - **On macOS/Linux:**
     ```sh
     source .venv/bin/activate
     ```
   You'll know it's active because your command prompt will be prefixed with `(.venv)`.

#### Step 3: Install Dependencies
1. Once the virtual environment is active, install the required Python packages.
2. The dependencies are listed in `requirements.txt`. Install them using pip:
   ```sh
   pip install -r requirements.txt
   ```
   This command will install all necessary packages like Selenium, Pytest, etc.

#### Step 4: Verify Installation
You can verify that Selenium is installed correctly by running a simple Python command:
```sh
python -c "import selenium; print(selenium.__version__)"
```
This should print the installed version of Selenium without any errors.

#### Step 5: Running the Tests
You can now run the automated tests using Pytest. There are several ways to run the tests:

**Option A: Run All Tests**
To execute all test files in the `tests/` directory:
```sh
pytest
```
This will discover and run all `pytest` compatible test files.

**Option B: Run All Tests with HTML Report**
To run all tests and generate a detailed HTML report:
```sh
pytest --html=report/report.html --self-contained-html
```
- `--html=report/report.html`: Specifies the name and location of the report file.
- `--self-contained-html`: Makes the report self-contained (includes CSS and images in the HTML file).

The report will be saved in the `report/` directory. You can open `report/report.html` in your web browser to view the results.

**Option C: Run a Specific Test File**
To run only a specific test file, for example, the checkout tests:
```sh
pytest tests/test_checkout.py
```

**Option D: Run a Specific Test Function**
To run a specific test function within a file:
```sh
pytest tests/test_checkout.py::test_checkout_complete
```
Replace `test_checkout_complete` with the actual name of the test function.

**Option E: Run Tests with Verbose Output**
To see a more detailed output during test execution, add the `-v` or `-s` flag:
- `-v` (verbose): Shows a detailed test name output.
  ```sh
  pytest -v
  ```
- `-s` (capture=no): Shows print statements and other output from your code.
  ```sh
  pytest -s
  ```

#### Step 6: Viewing the Test Reports
After running the tests with the `--html` option, a report file will be generated.
- The default report location is `report/report.html`.
- For specific test runs like checkout, you might find reports such as `report/Checkout_report.html`.
- To view the report:
  1. Navigate to the `report/` directory in your file explorer.
  2. Open the `.html` file with your web browser (e.g., Chrome, Firefox).
  3. The report will provide details on passed, failed, and skipped tests, along with error messages and screenshots if configured.

#### Step 7: Understanding Test Output
When you run the tests, your terminal will show:
- A dot (`.`) for each passed test.
- An `F` for each failed test.
- An `S` for each skipped test.
- A summary of the test run at the end, including the number of tests passed, failed, and skipped, and the total time taken.

If a test fails, Pytest will display:
- The file and line number of the failure.
- The error message (`AssertionError` or other exceptions).
- A traceback showing the sequence of calls that led to the error.

## Key Files and Their Roles
- **`pages/login_page.py`**: Defines the Page Object for the login page. Contains methods to interact with login elements (e.g., entering username/password, clicking login).
- **`pages/checkout_page.py`**: Defines the Page Object for the checkout process. Includes methods for adding items, validating prices, and completing checkout.
- **`pages/logout_page.py`**: Defines the Page Object for logout functionality.
- **`utils/driver_factory.py`**: A utility class to set up and manage the Selenium WebDriver (e.g., initializing ChromeDriver).
- **`conftest.py`**: Contains Pytest fixtures used across tests. Common fixtures include setting up the browser driver (`driver`) and initializing page objects (e.g., `login_page`).
- **`tests/test_login.py`**: Contains test cases for the login functionality (e.g., successful login, invalid credentials).
- **`tests/test_checkout.py`**: Contains the main end-to-end checkout test. It typically includes logging in, adding products to the cart, proceeding to checkout, filling in shipping info, and verifying the order completion.
- **`tests/test_logout.py`**: Contains tests for ensuring the user can successfully log out.
- **`requirements.txt`**: Lists all Python dependencies (Selenium, Pytest, etc.) needed for the project.
- **`pytest.ini`**: Configuration file for Pytest, used to set default options (e.g., test discovery paths, addopts).

## How the Automation Works
1. **Test Initialization (`conftest.py`)**:
   - When Pytest runs, it looks for `conftest.py` to load fixtures.
   - The `driver` fixture initializes a new Chrome browser instance for each test.
   - Page object fixtures (e.g., `login_page`) create instances of the respective Page Object classes, passing the driver to them.

2. **Test Execution (e.g., `tests/test_checkout.py`)**:
   - A test function like `test_checkout_complete` is called.
   - It uses the page object fixtures to interact with the web application.
   - Example flow:
     - `login_page.login(username, password)`: Enters credentials and clicks login.
     - `checkout_page.add_to_cart()`: Adds items to the shopping cart.
     - `checkout_page.go_to_checkout()`: Navigates to the checkout page.
     - `checkout_page.fill_shipping_info(...)`: Enters shipping details.
     - `checkout_page.finish_checkout()`: Clicks the finish button.
     - Assertions are made to verify expected outcomes (e.g., URL change, success message).

3. **Test Teardown**:
   - After each test, the browser is closed automatically by the `driver` fixture's teardown (`driver.quit()`).
   - If a test fails, Pytest captures a screenshot (if configured) and includes it in the HTML report.

4. **Reporting**:
   - The `pytest-html` plugin generates an HTML report after test execution.
   - The report includes:
     - A summary of all tests run.
     - Detailed results for each test (duration, status, output).
     - Tracebacks for failed tests.
     - Screenshots embedded directly in the report for easy debugging.

## Detailed Breakdown of a Sample Test (`test_checkout.py`)
Let's assume `tests/test_checkout.py` contains a `test_checkout_complete` test:

```python
def test_checkout_complete(login_page, checkout_page):
    # Step 1: Login
    login_page.login("standard_user", "secret_sauce")
    
    # Step 2: Add items to cart and go to checkout
    checkout_page.add_to_cart("Sauce Labs Backpack")
    checkout_page.add_to_cart("Sauce Labs Bike Light")
    checkout_page.go_to_cart()
    checkout_page.go_to_checkout()
    
    # Step 3: Fill in checkout information
    checkout_page.fill_form("John", "Doe", "12345")
    
    # Step 4: Finish checkout and verify
    checkout_page.finish_checkout()
    assert "CHECKOUT: COMPLETE!" in checkout_page.get_page_title()
    assert checkout_page.is_order_complete_displayed()
```

**Explanation**:
- `login_page` and `checkout_page` are fixtures providing instances of those page objects.
- `login_page.login(...)`: Calls the login method on the login page.
- `checkout_page.add_to_cart(...)`: Adds a specific item to the cart.
- `checkout_page.go_to_cart()` and `checkout_page.go_to_checkout()`: Navigate through the cart and checkout flow.
- `checkout_page.fill_form(...)`: Enters shipping details.
- `checkout_page.finish_checkout()`: Submits the checkout.
- `assert` statements verify that the checkout was successful by checking page elements.

## Best Practices
- **Page Object Model (POM)**: Always use POM to separate page-specific logic from test scripts. This makes tests easier to read and maintain.
- **Locators**: Store element locators (e.g., IDs, XPath) within the Page Object classes. Use descriptive names for locators.
- **Fixtures**: Use Pytest fixtures for setup and teardown operations (e.g., driver initialization). This keeps tests DRY (Don't Repeat Yourself).
- **Assertions**: Place assertions in tests to verify expected behavior. Use clear and specific assertion messages.
- **Explicit Waits**: Instead of `time.sleep()`, use Selenium's `WebDriverWait` to wait for elements to be clickable or visible. This makes tests more reliable.
- **Reporting**: Always generate HTML reports for detailed insights into test execution. Store reports in a dedicated directory (`report/`).
- **Error Handling**: Implement try-except blocks in test methods to handle potential exceptions gracefully and log meaningful error messages.
- **Modularity**: Keep tests small, focused, and independent. One test should verify one specific scenario.
- **Version Control**: Commit your code and reports to version control (e.g., Git) for tracking changes and history.

## Troubleshooting Common Issues

### Issue 1: ChromeDriver Version Mismatch
**Problem**: Tests fail with `SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version X`.
**Solution**:
- Ensure that your Google Chrome browser is updated to the latest version.
- `selenium-manager` (included in Selenium 4.6.0+) automatically handles ChromeDriver. If you're using an older version, download the correct ChromeDriver from the [official site](https://googlechromelabs.github.io/chrome-for-driving/) and ensure it's in your PATH or specify the path in `driver_factory.py`.

### Issue 2: Elements Not Found (StaleElementReferenceException or NoSuchElementException)
**Problem**: Tests fail because elements cannot be found on the page.
**Causes**:
- Page loads slowly.
- Elements are dynamically generated.
- Incorrect locators.
**Solutions**:
- Use explicit waits instead of implicit waits:
  ```python
  from selenium.webdriver.support.ui import WebDriverWait
  from selenium.webdriver.support import expected_conditions as EC

  element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "element_id"))
  )
  ```
- Verify your locators by manually inspecting the web page using browser developer tools (F12).
- Ensure the page is fully loaded before interacting with elements.

### Issue 3: Tests Faking Intermittently (Flakiness)
**Problem**: Tests sometimes pass and sometimes fail without any changes to the code.
**Causes**:
- Network latency.
- Race conditions where test actions are faster than page load.
**Solutions**:
- Increase explicit wait times where necessary.
- Add small, strategic delays (`time.sleep(1)`) only if absolutely needed, but prefer explicit waits.
- Ensure that one test does not depend on the state left by another test. Each test should be independent.

### Issue 4: HTML Report Not Generated
**Problem**: The `--html` report is not created or is empty.
**Solution**:
- Ensure that the `pytest-html` plugin is installed (it should be in `requirements.txt`).
- Check the file path where you're saving the report. Ensure the directory exists or create it:
  ```sh
  mkdir report
  pytest --html=report/report.html
  ```
- Run Pytest from the correct directory (root of the project).

### Issue 5: Virtual Environment Not Activating
**Problem**: Commands like `pip` or `python` are not using the virtual environment.
**Solution**:
- Make sure you've activated the virtual environment correctly:
  - **Windows**: `.venv\Scripts\activate`
  - **macOS/Linux**: `source .venv/bin/activate`
- You can check if it's active by seeing `(.venv)` at the start of your command prompt.

### Issue 6: Skipping the `Practicse_file/` Folder
**Problem**: Tests are failing or behaving unexpectedly because files from `Practicse_file/` are being included.
**Solution**:
- The `Practicse_file/` directory is intended for learning purposes and is not part of the main automation framework.
- Ensure that your test discovery is configured correctly in `pytest.ini` to exclude this folder:
  ```ini
  [pytest]
  testpaths = tests
  python_files = test_*.py
  python_classes = Test*
  python_functions = test_*
  ```
- If you run `pytest` from the project root, it will automatically discover tests only in the `tests/` directory.

## Additional Commands and Tips

### Running Tests in Parallel (Optional)
To speed up test execution, you can run tests in parallel using the `pytest-xdist` plugin:
1. Install the plugin:
   ```sh
   pip install pytest-xdist
   ```
2. Run tests with multiple workers:
   ```sh
   pytest -n 4
   ```
   Replace `4` with the number of CPU cores you want to use.

### Debugging Tests
- Use `pytest --pdb` to drop into a PDB debugger on test failure.
- Use `pytest -s -v` to see print statements and verbose output.
- For debugging element locators, use the browser's developer tools to inspect elements and find reliable selectors.

### Cleaning Up
- To remove the virtual environment, simply delete the `.venv` folder.
- To clean up generated reports, delete the contents of the `report/` directory.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

---

**Final Note:**
Always ensure that you have the latest versions of dependencies to avoid compatibility issues. Regularly update your packages using:
```sh
pip list --outdated
pip install --upgrade package-name
```

Happy testing!
