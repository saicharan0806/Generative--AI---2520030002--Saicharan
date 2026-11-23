# Tokenizer Comparison
**Objective** : The main objective of this experiment is to know the how tokenization is happening across different languages using tokenizer methods.
## Project folder structure:
  1. **.gitkeep** -> used to avoid the pushing of .env content and other important information in to the repository.
  2. **requirements.txt** -> it will install the required packages or libraries.
  3. **tokenizer_comparison.py** -> It is the actual executable file which tells us about how tokenizer methods will generate the token ID's and counts.
## How it works??
  1. Activate the virtual environment.
  2. install the requirements using python -m pip install -r requirements.txt.
  3. Load the tokenizer methods (BPE, word piece, sentence piece).
  4. give the sample input for three different languages.
  5. Convert text into tokens and tokenID's.
## Expected output
it will convert the text into tokens and token ID's . For each language it will perform three tokenizer methods.

**BPE** -> combines frequently occuring letter pairs.  

**Word piece** -> searches for the most likelihood pair.  

**sentence piece** -> splits the text into subwords without depending on spaces.
