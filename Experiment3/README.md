# LLM Monitoring using MongoDB
**Objective** : The main objective of this experiment is to check the LLM API usage and monitoring the details in MongoDB atlas.
## Project Folder Structure
  1. **.env** -> used to keep the gemini API key and MongoDB URL
  2. **.gitignore** -> used to avoid the pushing of .env file into the repository.
  3. **llm_client.py** -> provides different AI models and monitor there usage.
  4. **test_client.py** -> Tests the common LLM client without calling a real AI API or MongoDB.
  5. **requirements.txt** -> install the required packages.
  6. **usage_logger.py** -> connects to MongoDB and stores LLM Information.
  7. **main.py** -> The actual runnable python code.
## How to run it??
  1. Activate the virtual environment.
  2. Install the required packages using Python -m pip install -r requirements.txt
  3. Create the cluster in MongoDB.
  4. Connect that cluster and paste the url in .env file.
  5. Run the test_client .py for unit test
  6. Run the main programm
  7. Choose the provider gemini/ollama
  8. it will ask the user to enter the prompt. The AI will give the response.
## Expected output:
In mongodb atlas we will see the api_usage for every response. like we will see the provider name, model name, input tokens, output tokens, total tokens, estimated cost in USD.
