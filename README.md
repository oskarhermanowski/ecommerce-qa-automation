# 🛒 E-Commerce QA Automation

[![QA Automation Tests](https://github.com/oskarhermanowski/ecommerce-qa-automation/actions/workflows/api-tests.yml/badge.svg)](https://github.com/oskarhermanowski/ecommerce-qa-automation/actions/workflows/api-tests.yml)

End-to-end QA automation portfolio project demonstrating practical test automation skills across **API and UI testing**.

The project combines **Python, Pytest, Requests, Playwright, Postman, Newman and GitHub Actions** to test REST API endpoints and real e-commerce user flows.

API tests are based on the public [DummyJSON API](https://dummyjson.com/), while UI tests automate the [SauceDemo](https://www.saucedemo.com/) e-commerce application.

The project includes automated **smoke and regression test suites**, Page Object Model architecture, HTML reporting, automatic failure screenshots and a CI pipeline executed with GitHub Actions.

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
- Git / GitHub

---

## 🧪 API Test Coverage

API testing is implemented using both **Postman/Newman** and **Python with Requests + Pytest**.

### Authentication

- Successful login
- Invalid credentials
- Missing credentials
- Multiple invalid credential combinations
- Access token validation
- Refresh token validation
- Response time validation

### Products

- Get all products
- Get product by ID
- Get nonexistent product
- Create product
- Update product
- Delete product
- Search products
- Parameterized product tests
- Response schema/type validation
- Response time validation

### API Health

- API availability check
- HTTP status validation
- Response time validation

The Python API automation suite currently contains **19 automated tests**.

---

## 🌐 UI Test Coverage

The UI automation framework is built using **Playwright, Python and Pytest** and tests the SauceDemo e-commerce application.

### Homepage

- Application availability
- Page title validation

### Login

- Successful login
- Invalid password
- Locked-out user
- Missing username
- Missing password
- Empty credentials
- Parameterized validation tests
- URL validation after successful login

### Inventory

- Inventory page validation
- Add product to cart
- Product sorting by price: low to high
- Product sorting by price: high to low
- Product sorting by name: A to Z
- Product sorting by name: Z to A

### Cart

- Product visibility in cart
- Product name validation
- Add multiple products to cart
- Remove product from cart
- Continue shopping from cart
- Cart badge validation

### Checkout

- Complete checkout flow
- Customer information validation
- Missing first name validation
- Missing last name validation
- Missing postal code validation
- Order completion verification

The UI automation suite currently contains **22 automated Pytest test cases**.

---

## 🧠 Testing Techniques

The project demonstrates practical usage of:

- Positive testing
- Negative testing
- Functional testing
- API testing
- UI testing
- Smoke testing
- Regression testing
- Parameterized testing
- End-to-end testing
- HTTP status code validation
- Response body validation
- Data type validation
- Response time assertions
- UI state validation
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

This approach improves:

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
│   ├── api-report.html
│   ├── ui-smoke-report.html
│   └── ui-regression-report.html
│
├── pytest.ini
├── package.json
├── package-lock.json
└── README.md
```

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

### 6. Install Node.js dependencies

```bash
npm install
```

---

## 🔌 Running Python API Tests

Run all Python API tests:

```bash
pytest python-api-tests/tests -v
```

Generate an HTML report:

```bash
pytest python-api-tests/tests -v --html=reports/api-report.html --self-contained-html
```

---

## 📮 Running Postman / Newman API Tests

The project also contains a Postman API collection that can be executed from the command line using Newman.

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

Run tests with the browser visible:

```bash
pytest ui-tests/tests -v --headed
```

---

## 🏷 Smoke and Regression Tests

Pytest markers are used to separate the UI automation suite into different testing levels.

### Smoke tests

Smoke tests verify the most critical application functionality.

Run locally:

```bash
pytest ui-tests/tests -m smoke -v
```

### Regression tests

The regression suite executes the complete UI automation test suite.

Run locally:

```bash
pytest ui-tests/tests -m regression -v
```

The regression marker is automatically applied to UI tests through the Pytest configuration.

---

## 📸 Automatic Failure Screenshots

The Playwright framework automatically captures a screenshot when a UI test fails.

Screenshots are stored in:

```text
ui-tests/screenshots/
```

Example:

```text
test_successful_login[chromium].png
```

When UI tests fail in GitHub Actions, screenshots are uploaded as artifacts to help diagnose the failure.

This provides additional debugging information without requiring the test to be reproduced locally first.

---

## 📊 Automated Test Reports

The CI pipeline generates separate HTML reports for different automation layers.

```text
reports/
├── api-report.html
├── ui-smoke-report.html
└── ui-regression-report.html
```

The reports contain information such as:

- Test name
- Passed / failed status
- Execution duration
- Environment information
- Failure details

The reports are uploaded as **GitHub Actions artifacts** after CI execution.

---

## ⚙️ Continuous Integration

The project uses **GitHub Actions** for Continuous Integration.

The workflow is automatically triggered on:

- Pushes to `main`
- Pull requests targeting `main`

The pipeline is divided into **three independent jobs**:

### 🔌 API Tests

Executes:

- Postman API tests using Newman
- Python API tests using Requests and Pytest
- API HTML report generation

### 🚬 UI Smoke Tests

Executes the most critical Playwright UI tests:

```bash
pytest ui-tests/tests -m smoke -v
```

The job also:

- Installs Chromium
- Generates a smoke HTML report
- Captures screenshots on failure
- Uploads test artifacts

### 🔄 UI Regression Tests

Executes the complete Playwright regression suite:

```bash
pytest ui-tests/tests -m regression -v
```

The job also:

- Installs Chromium
- Generates a regression HTML report
- Captures screenshots on failure
- Uploads test artifacts

The three jobs execute independently, allowing API, smoke and regression results to be analyzed separately.

---

## 🔁 CI Workflow Overview

```text
                    Git Push / Pull Request
                              │
                              ▼
                       GitHub Actions
                              │
              ┌───────────────┼───────────────┐
              │               │               │
              ▼               ▼               ▼
          API Tests       UI Smoke        UI Regression
              │               │               │
        ┌─────┴─────┐      Playwright       Playwright
        │           │          │               │
     Newman       Pytest    Smoke Tests     Full Suite
        │           │          │               │
        └─────┬─────┘          │               │
              │                │               │
              ▼                ▼               ▼
          API Report       Smoke Report    Regression Report
```

This structure simulates a real-world automation pipeline where different testing layers can execute independently.

---

## 📈 Current Automation Suite

| Test Layer | Technology | Automated Tests |
|---|---|---:|
| API | Python + Requests + Pytest | 19 |
| UI | Playwright + Python + Pytest | 22 |
| API | Postman + Newman | Automated collection |
| **Total Python tests** | **Pytest** | **41** |

The project demonstrates automation across multiple testing layers rather than focusing only on individual test cases.

---

## 🎯 Project Purpose

This project was created as a **QA Automation portfolio project** to demonstrate practical experience with:

- API test automation
- UI test automation
- Python test development
- Playwright
- Pytest
- Requests
- REST API testing
- Postman and Newman
- Page Object Model
- Positive and negative test scenarios
- Parameterized testing
- Smoke and regression testing
- CI pipelines
- Automated reporting
- Failure diagnostics
- Git and GitHub workflows

---

## 👤 Author

**Oskar Hermanowski**

QA / Software Tester developing practical skills in test automation with **Python, Pytest, Playwright and API testing**.