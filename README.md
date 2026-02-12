# Professional CLI Calculator

A modular, professional-grade command-line calculator application built in Python.  
This project demonstrates clean architecture, modular design, error handling strategies, testing best practices, and continuous integration using GitHub Actions.

---

## 📌 Project Overview

This calculator application is implemented using:

- Object-Oriented Programming principles
- Factory design pattern
- DRY (Don't Repeat Yourself) principle
- LBYL and EAFP error handling paradigms
- Unit testing with pytest
- Parameterized tests
- 100% test coverage enforcement
- Continuous Integration (CI) using GitHub Actions

---

## 🚀 Features

### ✔ REPL Interface
Implements a Read–Eval–Print Loop for continuous user interaction.

### ✔ Arithmetic Operations
- Addition
- Subtraction
- Multiplication
- Division

### ✔ Input Validation
Ensures correct input format:
add 4 5

### ✔ Error Handling
- Division by zero handling
- Invalid operation handling
- Invalid input format handling
- Demonstrates:
  - LBYL (Look Before You Leap)
  - EAFP (Easier to Ask Forgiveness than Permission)

### ✔ Calculation History
Maintains session history of all performed calculations.

### ✔ Special Commands
- `help`
- `history`
- `exit`

### ✔ Testing & Coverage
- Unit tests using pytest
- Parameterized tests
- 100% code coverage required
- Coverage enforcement in CI pipeline

---

## 📂 Project Structure
professional-cli-calculator/
│
├── app/
│ ├── calculator/
│ │ └── calculator.py
│ ├── calculation/
│ │ └── calculation.py
│ ├── operation/
│ │ └── operations.py
│
├── tests/
│ ├── test_calculations.py
│ └── test_operations.py
│
├── main.py
├── README.md
└── .github/workflows/python-app.yml

---

## ⚙ Installation & Setup

### 1️⃣ Clone Repository


### 2️⃣ Create Virtual Environment


### 3️⃣ Activate Virtual Environment

Windows:
venv\Scripts\activate


Mac/Linux:
source venv/bin/activate


### 4️⃣ Install Dependencies
pip install pytest pytest-cov


---

## ▶ Running the Application
python main.py


### Example Usage:
add 4 5
Result: 9

divide 10 2
Result: 5

history
(4.0, 5.0, 'add', 9.0)
(10.0, 2.0, 'divide', 5.0)

exit
Goodbye!


---

## 🧪 Running Tests

Expected Output:
- All tests passing
- 100% coverage

---

## 🔍 Coverage Enforcement

The project enforces:
coverage report --fail-under=100


If coverage drops below 100%, the CI pipeline fails.

Lines intentionally excluded from coverage use:

```python
# pragma: no cover

🔄 Continuous Integration (CI)

GitHub Actions automatically:

Runs all tests on every push

Measures coverage

Fails the build if coverage is below 100%

Workflow file location:
.github/workflows/python-app.yml