\# E-Commerce QA Automation



QA automation portfolio project focused on testing an e-commerce REST API using Postman and Newman, with automated test execution through GitHub Actions.



The project demonstrates API testing, test scenario design, response validation, environment variables, end-to-end testing and CI integration.



\## 🛠 Technologies



\- Postman

\- Newman

\- JavaScript (Postman test scripts)

\- REST API

\- JSON

\- Git

\- GitHub

\- GitHub Actions

\- Node.js / npm



API used for testing: DummyJSON



\## 🧪 API Test Coverage



The Postman collection currently contains \*\*25 API requests and 166 automated assertions\*\*.



\### Health Checks

\- API availability

\- HTTP status validation

\- JSON response validation

\- Response time validation



\### Authentication

\- Successful login

\- Invalid credentials

\- Missing password

\- Access token validation

\- Refresh token validation



\### Products

\- Get all products

\- Get product by ID

\- Product not found

\- Search products

\- Response schema and data type validation



\### Users

\- Get all users

\- Get user by ID

\- User not found

\- Create user

\- Update user

\- Delete user

\- Email format validation



\### Carts

\- Get all carts

\- Get cart by ID

\- Cart not found

\- Create cart

\- Update cart

\- Delete cart

\- Product and quantity validation



\## 🔄 End-to-End Scenario



The project contains an automated E2E API scenario simulating a basic e-commerce flow:



1\. Authenticate user

2\. Get selected product

3\. Create shopping cart

4\. Update shopping cart

5\. Delete shopping cart



Variables such as user ID, product ID and cart ID are reused between requests.



\## ▶️ Running Tests Locally



Install dependencies:



```bash

npm install

