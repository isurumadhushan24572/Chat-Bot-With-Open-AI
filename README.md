# Chatbot with openai

This repository contains the code how to create a Chatbot using  Python, streamlit and LangChain.

## Steps Should Follow

create Virtual env

  ```
  python -m venv chatbot-env
  ```
activate Virtual env

  ```
  cd chatbot-env\Scripts\activate
  ```
creating .gitignore file , .env file and chatbot.py

  ```
  echo "# Files to ignore" > .gitignore && echo "OPENAI_API_KEY=your_api_key_here" > .env && echo "# Chatbot script" > chatbot.py
  ```
Insatalling Required dependencies

  ```
  pip install -r requirements.txt
  ```

Save OpenAI API Key inside .env file
  ```
  OPENAI_API_KEY=your_openai_api_key
  ```

Run Chatbot.py file

  ```
  streamlit run Chatbot.py
  ```

## Note

* This is a very simple project of AI. 
* Here when importing openai model I gave tempreature variable as 0.5
* tempreature variable is used for change the radomness of the output(response)
* Also here append all the chat history of the user input and chatbot output to get Quality response for the user input 


## Issues

some times you will get error due to the your OpenAI API Key Credit is equal to Zero.
To solve this issue you need to add credit doing the payement



