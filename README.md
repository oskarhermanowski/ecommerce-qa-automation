# 🛒 E-Commerce QA Automation

![API Tests](https://github.com/oskarhermanowski/ecommerce-qa-automation/actions/workflows/api-tests.yml/badge.svg)

Automated API testing project created to demonstrate practical QA Automation skills using **Python, Pytest, Requests, Postman, Newman and GitHub Actions**.

The project tests the public [DummyJSON API](https://dummyjson.com/) and includes automated validation of authentication and product endpoints.

---

## 🛠 Tech Stack

- Python
- Pytest
- Requests
- Postman
- Newman
- GitHub Actions
- pytest-html
- Git / GitHub

---

## 🧪 Test Coverage

The automated test suite covers:

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

---

## 🧠 Testing Techniques

The project demonstrates:

- Positive testing
- Negative testing
- API response validation
- HTTP status code validation
- Data type validation
- Parameterized testing
- Smoke testing
- Regression testing
- Response time assertions

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
│   ├── postman/
│   ├── test-cases/
│   ├── DummyJSON - QA.postman_environment.json
│   └── E-Commerce API Tests.postman_collection.json
│
├── python-api-tests/
│   ├── tests/
│   │   ├── conftest.py
│   │   ├── test_auth.py
│   │   ├── test_health.py
│   │   └── test_products.py
│   ├── pytest.ini
│   └── requirements.txt
│
└── README.md
```

---

## ▶️ Running Python Tests

### 1. Clone the repository

```bash
git clone https://github.com/oskarhermanowski/ecommerce-qa-automation.git
cd ecommerce-qa-automation
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r python-api-tests/requirements.txt
```

### 5. Run all tests

```bash
cd python-api-tests
pytest
```

---

## 🏷 Running Test Suites

Run smoke tests:

```bash
pytest -m smoke -v
```

Run regression tests:

```bash
pytest -m regression -v
```

Run the complete test suite:

```bash
pytest -v
```

---

## 📊 HTML Test Report

Pytest automatically generates an HTML report after test execution.

```text
python-api-tests/report.html
```

The report contains:

- Test names
- Passed/failed status
- Execution duration
- Environment information

In GitHub Actions, the report is automatically uploaded as the:

```text
pytest-html-report
```

artifact after every CI run.

---

## 📮 Postman / Newman

The project also contains a Postman API test collection.

Postman tests can be executed from the command line using Newman.

```bash
npm install
```

Then run the collection:

```bash
npx newman run "api-tests/E-Commerce API Tests.postman_collection.json" \
-e "api-tests/DummyJSON - QA.postman_environment.json"
```

---

## ⚙️ Continuous Integration

The project uses **GitHub Actions** for Continuous Integration.

The CI pipeline is automatically triggered on:

- Push to `main`
- Pull requests to `main`

The pipeline:

1. Checks out the repository
2. Sets up Node.js
3. Installs Newman dependencies
4. Runs Postman API tests
5. Sets up Python
6. Installs Python dependencies
7. Runs Pytest API tests
8. Generates an HTML test report
9. Uploads the report as a GitHub Actions artifact

This ensures that automated API tests are executed after every code change.

---

## ✅ Current Test Suite

The Python automation suite currently contains **19 automated test cases** covering authentication, API health and product operations.

Tests include both positive and negative scenarios as well as parameterized test execution.

---

## 🎯 Project Purpose

This project was created as a QA Automation portfolio project to demonstrate practical experience with:

- API test automation
- Python test development
- Pytest
- REST API testing
- Postman and Newman
- Test design
- CI/CD pipelines
- Automated test reporting
- Git and GitHub workflows

---

## 👤 Author

**Oskar Hermanowski**

QA / Software Tester developing skills in test automation with Python.