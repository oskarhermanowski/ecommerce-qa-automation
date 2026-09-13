# 🛒 E-Commerce QA Automation

![API & UI Tests](https://github.com/oskarhermanowski/ecommerce-qa-automation/actions/workflows/api-tests.yml/badge.svg)

End-to-end QA Automation portfolio project demonstrating practical test automation skills across **API and UI testing**.

The project combines **Python, Pytest, Requests, Playwright, Postman, Newman and GitHub Actions** to test REST API endpoints and real e-commerce user flows.

API tests are based on the public [DummyJSON API](https://dummyjson.com/), while UI tests automate the [SauceDemo](https://www.saucedemo.com/) e-commerce application.

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

### Authentication

- Successful login
- Invalid credentials
- Missing password
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

The Python API automation suite currently contains **19 automated test cases**.

---

## 🌐 UI Test Coverage

The Playwright UI automation suite covers key SauceDemo e-commerce user flows.

### Login

- Successful user login
- URL validation after login
- Inventory page validation

### Inventory

- Product inventory page verification
- Adding a product to the cart

### Cart

- Product visibility in cart
- Product name validation

### Checkout

- Checkout flow
- Customer information
- Order completion validation

### Homepage

- Application availability
- Basic page validation

The UI automation suite currently contains **5 automated Playwright tests**.

---

## 🧠 Testing Techniques

The project demonstrates:

- Positive testing
- Negative testing
- Functional testing
- API testing
- UI testing
- Smoke testing
- Regression testing
- Parameterized testing
- HTTP status code validation
- Response body validation
- Data type validation
- Response time assertions
- End-to-end workflow validation
- Failure diagnostics

---

## 🏗 Page Object Model

The UI automation framework uses the **Page Object Model (POM)** design pattern.

Page-specific selectors and actions are separated from test logic.

```text
ui-tests/
│
├── pages/
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

This improves:

- Code maintainability
- Reusability
- Readability
- Separation of test logic from page interactions

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
│   └── ui-report.html
│
├── pytest.ini
├── package.json
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

### 5. Install Playwright browser

```bash
playwright install chromium
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

## 🎭 Running Playwright UI Tests

Run all UI tests:

```bash
pytest ui-tests/tests -v
```

Run tests with the browser visible:

```bash
pytest ui-tests/tests -v --headed
```

Generate the UI HTML report:

```bash
pytest ui-tests/tests -v --html=reports/ui-report.html --self-contained-html
```

---

## 🏷 Test Markers

The project supports Pytest markers for separating test suites.

Run smoke tests:

```bash
pytest -m smoke -v
```

Run regression tests:

```bash
pytest -m regression -v
```

---

## 📸 Automatic Failure Screenshots

The Playwright test framework automatically captures a screenshot when a UI test fails.

Screenshots are stored in:

```text
ui-tests/screenshots/
```

Example:

```text
test_successful_login[chromium].png
```

When tests fail in GitHub Actions, screenshots are uploaded as CI artifacts to help diagnose failures.

---

## 📊 Automated Test Reports

Separate HTML reports are generated for API and UI automation.

```text
reports/
├── api-report.html
└── ui-report.html
```

The reports include information such as:

- Test name
- Passed / failed status
- Execution duration
- Environment information
- Failure details

Reports are also uploaded as **GitHub Actions artifacts**.

---

## 📮 Postman / Newman

The project also contains a Postman API test collection executed automatically using Newman.

Install Node.js dependencies:

```bash
npm install
```

Run the collection:

```bash
npx newman run "api-tests/E-Commerce API Tests.postman_collection.json" \
-e "api-tests/DummyJSON - QA.postman_environment.json"
```

---

## ⚙️ CI/CD Pipeline

The project uses **GitHub Actions** for Continuous Integration.

The workflow is automatically triggered on pushes and pull requests.

The CI pipeline:

1. Checks out the repository
2. Sets up Node.js
3. Installs Node dependencies
4. Runs Postman API tests with Newman
5. Sets up Python
6. Installs Python dependencies
7. Installs the Chromium browser for Playwright
8. Runs Python API tests
9. Runs Playwright UI tests
10. Generates separate API and UI HTML reports
11. Uploads test reports as GitHub Actions artifacts
12. Uploads Playwright screenshots when UI tests fail

This ensures that the automated regression suite is executed consistently after code changes.

---

## 📈 Current Automation Suite

The project currently contains:

| Test layer | Technology | Automated tests |
|---|---|---:|
| API | Python + Requests + Pytest | 19 |
| UI | Playwright + Pytest | 5 |
| API | Postman + Newman | Automated collection |
| **Total Python tests** | **Pytest** | **24** |

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
- Test design
- CI/CD pipelines
- Automated reporting
- Failure diagnostics
- Git and GitHub workflows

---

## 👤 Author

**Oskar Hermanowski**

QA / Software Tester developing practical skills in test automation with Python, Pytest, Playwright and API testing.