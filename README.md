# Playwright Automation Project

This project contains automated UI tests using [Playwright](https://playwright.dev/python/) with Python.

## Setup

1. Clone the repository:
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo

2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate   # for Linux/macOS
   venv\Scripts\activate      # for Windows

3. Install dependencies:
   pip install -r requirements.txt

4. Install Playwright browsers:
   playwright install

5. Run tests:
   pytest            # run all tests in headless mode
   pytest --headed   # run tests with visible browser

## Project Structure

- pages/ — Page Object classes  
- tests/ — Test cases  
- README.md — This file  
- requirements.txt — Python dependencies

## Notes

- Make sure your virtual environment is activated before running tests.  
- Customize test data and locators as needed.  
- Use a .gitignore file to exclude folders like venv/, .pytest_cache/, and __pycache__/ from being tracked by Git.

