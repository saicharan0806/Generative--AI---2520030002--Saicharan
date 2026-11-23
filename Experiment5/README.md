# Token Economics cost and rate limit budgeting
**Objective** : The main objective of this experiment is to estimate the token usage, API cost, and rate-limit before building an LLM application.

## Project folder structure
  1. **.env** -> used to store the all budget values such as input price per million, RPM limits, TPM limits etc..
  2. **.gitignore** -> used to avoid the pushing of important information in to the repository.
  3. **requirements.txt** -> used to install the required libraries / packages.
  4. **budget.py** -> it will tells us whether the AI feature is affordable or not.
  5. **test_budget.py** -> it will check whether budget.py is working correctly or not.
## how it works??
  1. Activate the virtual environment.
  2. install the required libraries using python -m pip install -r requirements.txt.
  3. Read all values from .env
  4. calculate token usage, monthly cost. and check RPM, TPM limits.
  5. then after calculating and checking all values it will give recommendation that within limit or exceeding the limit.
