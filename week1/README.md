
     #LLM_API_CALL USING PYTHON

The main objective of this experiment is to **use AI models through an API key**.

First, we want to create the required files for the experiment:

1. **`.env`** → Used to store our API key. Don't share your API key with others.
2. **`.gitignore`** → Used to avoid pushing unwanted or important files into the repository.
3. **`requirements.txt`** → Used to install the required packages.
4. **`main.py`** → The main Python program.

Before running the code, activate the virtual environment. Without activating it, the program won't run.

Then, install the required packages using:

**`python -m pip install -r requirements.txt`**

Use the **Gemini API key** because it offers a free plan. If we use the **OpenAI API key**, it require billing or credits depending on the account and usage. So, for this experiment, use the **Gemini API key**.

### In the `main.py` program:

1. **Loads the API key.**
2. **Creates the Gemini client.**
3. **Sends the prompt.**
4. **Receives and prints the AI's answer.**
