# Experiment 7 - Next-Token Probabilities Using Hugging Face Transformers

**Objective:** Next-token probabilities: inspect logits and top-k candidates from a small open model with Hugging Face Transformers.

## Project Structure
  1. **.env** -> Used to store the Hugging Face access token and model ID for connecting to the Hugging Face Inference API.
  2. **.gitignore** -> Used to avoid uploading unwanted files and important information such as API tokens to GitHub.
  3. **requirements.txt** -> Used to install the required libraries.
  4. **main.py** -> Loads the GPT-2 model using Hugging Face Transformers. It converts the input sentence into token IDs, extracts output             logits, converts them into probabilities using Softmax, and displays the top 5 next-token candidates.
  5. **huggingface.py** -> Connects to the Hugging Face Inference API using the access token stored in the `.env` file. It sends a prompt to           the selected model and generates text.
  6. **local_model.py** -> Used to work with the language model locally without depending on the Hugging Face Inference API.

## How to Run

**Method 1: Using GPT-2 Locally**

1. Open the experiment7 folder in VS Code.
2. Create and activate a virtual environment if required.
3. Install the required packages using:

   `python -m pip install -r requirements.txt`

4. Run the main Python file:

   `python main.py`

5. The program loads the GPT-2 model and processes the input sentence.
6. It displays the output logits, probabilities, and top 5 candidate tokens.

**Method 2: Using Hugging Face Inference API**

1. Create an account on Hugging Face.
2. Generate an access token from your Hugging Face account.
3. Add the following details to the `.env` file:

   - HF_TOKEN = Your Hugging Face access token
   - HF_MODEL_ID = Your selected model ID

4. Install the required packages using:

   `python -m pip install -r requirements.txt`

5. Run the Python file:

   `python huggingface.py`

6. The program connects to the Hugging Face Inference API and generates text based on the given prompt.
