# BDD Framework with Behave, Selenium, and Allure

This repository contains a Behavior-Driven Development (BDD) framework using Python, Behave, Selenium WebDriver, and Allure for reporting.

## Getting Started

These instructions will help you set up and run the BDD framework on your local machine.

## Prerequisites
Before running the tests, ensure you have the following installed:
- PyCharm (preferred IDE)
- Python (version 3.x recommended)
- Install dependencies using `pip install -r requirements.txt`

## Running Tests
To execute the tests, follow these commands:

1. **Run all feature files and scenarios:**
   ```bash
   behave
   ```

2. **Run scenarios with a specific tag:**
   ```bash
   behave --tags=@tag_name
   ```

## Run Tests and Generate Test Cases Report
To generate a report, use the following command:

```bash
behave -f allure_behave.formatter:AllureFormatter -o allure-results
allure serve allure-results
```

---