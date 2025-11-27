# Lab 3: Create Your Own GitHub Actions Workflow

## Objective
Automate a simple CI check for your repository using GitHub Actions to run tests and linting on every push and pull request.

## Scenario
You will set up a continuous integration (CI) pipeline that automatically checks code quality and runs tests whenever code is pushed to the repository. This demonstrates how GitHub Actions can help maintain code quality and catch issues early.

---

## Prerequisites

Ensure your repository has the following structure:

```
demo-app/
├── app.py
├── requirements.txt
├── tests/
│   └── test_app.py
└── README.md
```

---

## Instructions

### Part 1: Prepare Your Repository

1. Open your repository in GitHub
2. Verify you have the following files:
   - `app.py` (your main application file)
   - `test_app.py` (your test file in the `tests/` directory)
   - `requirements.txt` (list dependencies: `flask`, `pytest`)

### Part 2: Create the Workflow

1. Navigate to the **Actions** tab in your repository
2. Click **New workflow**
3. Choose **Set up a workflow yourself**
4. Create the file `.github/workflows/ci.yml` with the following content:

```yaml
name: Python CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest flake8

      - name: Run Linter
        run: flake8 .

      - name: Run Tests
        run: PYTHONPATH=. pytest
```

### Part 3: Push the Workflow

1. Commit the workflow file with a descriptive message:
   ```
   Add CI workflow for automated testing
   ```
2. Push the changes to your repository

### Part 4: Trigger and Monitor the Action

1. **Make a small code change** in your repository (e.g., update a comment in `app.py`)
2. **Push the change** to trigger the workflow
3. Navigate to the **Actions** tab to watch the jobs run live
4. **Optional test:** Add a lint error (e.g., remove a space) and observe the job fail

---

## Expected Outcome

You should have:
- ✅ A working GitHub Actions workflow file in `.github/workflows/ci.yml`
- ✅ Automated CI checks running on every push and pull request
- ✅ Linting performed with flake8
- ✅ Tests executed with pytest
- ✅ Visible workflow runs in the Actions tab

## Understanding the Workflow

**Triggers:**
- Runs on pushes to the `main` branch
- Runs on pull requests targeting `main`

**Steps:**
1. **Checkout code** - Retrieves your repository code
2. **Set up Python** - Installs Python 3.x
3. **Install dependencies** - Installs required packages from `requirements.txt` and flake8
4. **Run Linter** - Checks code style with flake8
5. **Run Tests** - Executes tests with pytest

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Workflow doesn't trigger | Ensure the workflow file is in `.github/workflows/` directory |
| Tests fail | Check that `requirements.txt` includes all dependencies |
| Linter errors | Review flake8 output and fix code style issues |
| Import errors | Verify the test file paths match your repository structure |

---