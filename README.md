# 🛒 E-Commerce QA Automation

[![QA Automation Tests](https://github.com/oskarhermanowski/ecommerce-qa-automation/actions/workflows/api-tests.yml/badge.svg)](https://github.com/oskarhermanowski/ecommerce-qa-automation/actions/workflows/api-tests.yml)

End-to-end **QA Automation portfolio project** demonstrating practical test automation skills across **API and UI testing**.

The project combines **Python, Pytest, Requests, Playwright, Postman, Newman and GitHub Actions** to test REST API endpoints and real e-commerce user flows.

API tests are based on the public [DummyJSON API](https://dummyjson.com/), while UI tests automate the [SauceDemo](https://www.saucedemo.com/) e-commerce application.

The project includes automated **smoke and regression test suites**, Page Object Model architecture, parameterized tests, HTML reporting, automatic failure screenshots and a CI pipeline executed with GitHub Actions.

---

## 🛠 Tech Stack

- Python
- Pytest
- Requests
- Playwright
- Page Object Model (POM)
- Postman
- Newman
- GitHub Actions
- pytest-html
- Git
- GitHub

---

## 🧪 API Test Automation

API automation is implemented using **Python, Requests and Pytest**.

The automated API suite currently contains **19 tests**.

### Authentication

Tests cover:

- Successful login
- Invalid credentials
- Missing required credentials
- Multiple invalid credential combinations
- Access token validation
- Refresh token validation
- HTTP status code validation
- Response body validation
- Response time validation

### Products

Tests cover:

- Get product by ID
- Get nonexistent product
- Create product
- Update product
- Delete product
- Search products
- Parameterized product ID tests
- Response schema and data type validation
- HTTP status code validation
- Response time validation

### API Health

Tests cover:

- API availability
- HTTP status validation
- Basic response validation
- Response time validation

### Parameterized API Testing

Pytest parameterization is used to execute the same test logic against multiple datasets.

Example scenarios include retrieving multiple products using different product IDs.

This reduces duplicated test code and improves test coverage.

---

## 🌐 UI Test Automation

UI automation is implemented using **Playwright with Python and Pytest**.

The automated UI suite currently contains **22 tests** covering important SauceDemo user flows.

### 🔐 Login

Tests cover:

- Successful login
- Invalid password
- Locked-out user
- Required username validation
- Required password validation
- Login error message validation

### 📦 Inventory

Tests cover:

- Inventory page verification
- Product visibility
- Adding products to the cart
- Product sorting by name A → Z
- Product sorting by name Z → A
- Product sorting by price
- Inventory interactions

### 🛒 Cart

Tests cover:

- Adding products to the cart
- Adding multiple products
- Removing products from the cart
- Product visibility in the cart
- Product name validation
- Continuing shopping from the cart
- Cart state verification

### 💳 Checkout

Tests cover:

- Complete checkout flow
- Customer information
- Required field validation
- First name validation
- Last name validation
- Postal code validation
- Order completion verification

### 🏠 Homepage

Tests cover:

- Application availability
- Basic page validation
- Initial application state

---

## 🔄 End-to-End Test Scenarios

The project includes automated user journeys that simulate real e-commerce behavior.

Example workflow:

```text
Login
  ↓
Browse products
  ↓
Add product to cart
  ↓
Open cart
  ↓
Proceed to checkout
  ↓
Enter customer information
  ↓
Complete order
  ↓
Verify successful purchase
```

These scenarios validate interactions between multiple application pages instead of testing individual elements in isolation.

---

## 🧠 Testing Techniques

The project demonstrates practical use of:

- Positive testing
- Negative testing
- Functional testing
- API testing
- UI testing
- End-to-end testing
- Smoke testing
- Regression testing
- Parameterized testing
- Data-driven testing
- HTTP status code validation
- Response body validation
- Data type validation
- Response time assertions
- Form validation testing
- Error message validation
- Failure diagnostics

---

## 🏗 Page Object Model

The UI automation framework uses the **Page Object Model (POM)** design pattern.

Page-specific selectors and actions are separated from the test logic.

```text
ui-tests/
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
└── tests/
    ├── test_login.py
    ├── test_homepage.py
    ├── test_inventory.py
    ├── test_cart.py
    └── test_checkout.py
```

Using Page Object Model improves:

- Code maintainability
- Reusability
- Readability
- Separation of test logic from page interactions
- Scalability of the automation framework

---

## 📁 Project Structure

```text
ecommerce-qa-automation/
│
├── .github/
│   └── workflows/
│       └── api-tests.yml
│
├── api-tests/
│   ├── DummyJSON - QA.postman_environment.json
│   └── E-Commerce API Tests.postman_collection.json
│
├── python-api-tests/
│   ├── tests/
│   │   ├── conftest.py
│   │   ├── test_auth.py
│   │   ├── test_health.py
│   │   └── test_products.py
│   │
│   └── requirements.txt
│
├── ui-tests/
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── login_page.py
│   │   ├── inventory_page.py
│   │   ├── cart_page.py
│   │   └── checkout_page.py
│   │
│   ├── tests/
│   │   ├── test_login.py
│   │   ├── test_homepage.py
│   │   ├── test_inventory.py
│   │   ├── test_cart.py
│   │   └── test_checkout.py
│   │
│   ├── screenshots/
│   └── conftest.py
│
├── reports/
│
├── .gitignore
├── pytest.ini
├── package.json
├── package-lock.json
└── README.md
```

Generated HTML reports and failure screenshots are excluded from Git version control and are generated automatically when the tests are executed.

---

## ▶️ Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/oskarhermanowski/ecommerce-qa-automation.git
cd ecommerce-qa-automation
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### 4. Install Python dependencies

```bash
pip install -r python-api-tests/requirements.txt
```

### 5. Install the Playwright Chromium browser

```bash
playwright install chromium
```

---

## 🐍 Running Python API Tests

Run all Python API tests:

```bash
pytest python-api-tests/tests -v
```

Generate an HTML report:

```bash
pytest python-api-tests/tests -v --html=reports/api-report.html --self-contained-html
```

Collect API tests without executing them:

```bash
pytest python-api-tests/tests --collect-only -q
```

Current API suite:

```text
19 tests
```

---

## 📮 Running Postman / Newman API Tests

The project also contains a Postman API collection that can be executed using Newman.

Install Node.js dependencies:

```bash
npm install
```

Run the Postman collection:

```bash
npx newman run "api-tests/E-Commerce API Tests.postman_collection.json" -e "api-tests/DummyJSON - QA.postman_environment.json"
```

The Postman collection is also executed automatically in GitHub Actions.

---

## 🎭 Running Playwright UI Tests

Run all UI tests:

```bash
pytest ui-tests/tests -v
```

Run UI tests with the browser visible:

```bash
pytest ui-tests/tests -v --headed
```

Generate an HTML report:

```bash
pytest ui-tests/tests -v --html=reports/ui-report.html --self-contained-html
```

Collect UI tests without executing them:

```bash
pytest ui-tests/tests --collect-only -q
```

Current UI suite:

```text
22 tests
```

---

## 🚦 Smoke and Regression Tests

Pytest markers are used to separate UI automation into different test suites.

### Smoke Tests

Smoke tests verify the most critical application functionality.

Run locally:

```bash
pytest ui-tests/tests -m smoke -v
```

Generate a smoke test report:

```bash
pytest ui-tests/tests -m smoke -v --html=reports/ui-smoke-report.html --self-contained-html
```

Smoke tests are executed as a separate job in GitHub Actions.

### Regression Tests

Regression tests execute the broader UI automation suite.

Run locally:

```bash
pytest ui-tests/tests -m regression -v
```

Generate a regression test report:

```bash
pytest ui-tests/tests -m regression -v --html=reports/ui-regression-report.html --self-contained-html
```

Regression tests are also executed as a separate CI job.

---

## 📸 Automatic Failure Screenshots

The Playwright test framework automatically captures screenshots when UI tests fail.

Screenshots are stored locally in:

```text
ui-tests/screenshots/
```

Example:

```text
test_successful_login[chromium].png
```

Failure screenshots are excluded from Git version control.

When a UI test fails in GitHub Actions, screenshots are uploaded as CI artifacts for easier failure investigation.

This provides additional diagnostic information without requiring the test to be reproduced locally first.

---

## 📊 Automated Test Reports

HTML reports are generated using **pytest-html**.

Reports can be generated for:

- Python API tests
- UI smoke tests
- UI regression tests

Example report files:

```text
reports/
├── api-report.html
├── ui-smoke-report.html
└── ui-regression-report.html
```

Reports include information such as:

- Test name
- Passed / failed status
- Execution duration
- Environment information
- Failure details
- Traceback information

Generated reports are excluded from Git version control.

During CI execution, reports are uploaded as **GitHub Actions artifacts**, allowing test results to be downloaded and inspected after each workflow run.

---

## ⚙️ Continuous Integration

The project uses **GitHub Actions** to automatically execute the automation suites on:

- Pushes to `main`
- Pull requests targeting `main`

The CI workflow contains three independent test jobs:

```text
GitHub Actions
│
├── API Tests
│
├── UI Smoke Tests
│
└── UI Regression Tests
```

### API Tests

The API job:

1. Checks out the repository
2. Sets up Node.js
3. Installs Node dependencies
4. Executes the Postman collection using Newman
5. Sets up Python
6. Installs Python dependencies
7. Executes Python API tests
8. Generates an API HTML report
9. Uploads the report as a GitHub Actions artifact

### UI Smoke Tests

The smoke job:

1. Checks out the repository
2. Sets up Python
3. Installs Python dependencies
4. Installs Chromium for Playwright
5. Executes tests marked as `smoke`
6. Generates an HTML report
7. Uploads failure screenshots when necessary
8. Uploads the smoke HTML report as an artifact

### UI Regression Tests

The regression job:

1. Checks out the repository
2. Sets up Python
3. Installs Python dependencies
4. Installs Chromium for Playwright
5. Executes tests marked as `regression`
6. Generates an HTML report
7. Uploads failure screenshots when necessary
8. Uploads the regression HTML report as an artifact

Separating the suites into independent jobs makes CI results easier to understand and allows the test suites to execute independently.

---

## 📦 GitHub Actions Artifacts

After a CI run, GitHub Actions provides test artifacts containing generated reports.

Depending on the executed workflow, artifacts can include:

```text
api-test-report
ui-smoke-report
ui-regression-report
smoke-failure-screenshots
regression-failure-screenshots
```

Failure screenshot artifacts are created only when corresponding UI tests fail.

---

## 📈 Current Automation Suite

The project currently contains:

| Test Layer | Technology | Automated Tests |
|---|---|---:|
| API | Python + Requests + Pytest | 19 |
| UI | Playwright + Pytest | 22 |
| API | Postman + Newman | Automated collection |
| **Total Pytest tests** | **Python + Pytest** | **41** |

The project demonstrates automation across multiple testing layers rather than focusing only on individual test cases.

---

## 🔍 Example CI Execution

A successful GitHub Actions workflow executes three independent jobs:

```text
✓ API Tests
✓ UI Smoke Tests
✓ UI Regression Tests
```

Each job provides an independent result, making it easier to identify whether a failure occurred in the API, smoke or regression automation layer.

---

## 🎯 Project Purpose

This project was created as a **QA Automation portfolio project** to demonstrate practical experience with:

- Python test automation
- REST API automation
- UI automation
- Pytest
- Requests
- Playwright
- Postman
- Newman
- Page Object Model
- Positive and negative testing
- Parameterized testing
- Smoke testing
- Regression testing
- End-to-end test scenarios
- Test data validation
- Automated HTML reporting
- Failure diagnostics
- GitHub Actions
- Continuous Integration
- Git and GitHub workflows

The goal of the project is to demonstrate the structure and practices used in a real automation testing project rather than only presenting isolated automation scripts.

---

## 🚀 Skills Demonstrated

Through this project, the following QA Automation skills are demonstrated:

**Test Automation**
- Designing automated test cases
- Creating reusable test code
- Building API and UI automation suites
- Organizing smoke and regression suites

**Python**
- Pytest fixtures
- Assertions
- Parameterization
- HTTP requests
- Test organization

**API Testing**
- REST API testing
- HTTP methods
- Status code validation
- JSON response validation
- Authentication testing
- Negative API testing

**UI Testing**
- Browser automation with Playwright
- Page Object Model
- Form validation
- User flow automation
- Product and cart interactions
- Checkout automation

**CI/CD**
- GitHub Actions workflows
- Automated test execution
- Independent CI jobs
- HTML report generation
- Artifact management
- Failure screenshot collection

---

## 👤 Author

**Oskar Hermanowski**

QA / Software Tester developing practical skills in test automation with **Python, Pytest, Playwright, Requests, API testing and CI/CD**.

GitHub: [oskarhermanowski](https://github.com/oskarhermanowski)