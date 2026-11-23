# WEEK-2 Gemini and Ollama
**Objective** : The main objective of this project is to provide a single LLM Client interface that can work with gemini and Ollama.
To implement this we need to create the files:
  1. **.env** -> Used to keep the API key .
  2. **.gitignore** -> Used to avoid pushing unwanted or important files into the repository.
  3. **requirements.txt** -> Install the required packages using
     **python -m pip install -r requirements.txt**
  4. **llm_client.py** -> provides a common interface for AI models.
  5. **test_client.py** -> it will check whether the LLM client is working or not
  6. **main.py** -> The actual runnable python code.
## How to run
Download ollama on your computer and check the version of ollama in **cmd**. Pull the llamma3.2 on your computer.  

Activate the virtual environment in VS code if not.  

run the main.py and it will ask the user to choose the model gemini or ollama. Select any one give the prompt, AI will give the response.  

**If you got the server error change the gemini model to other model, Better use gemini-3.5-flash-lite.**

