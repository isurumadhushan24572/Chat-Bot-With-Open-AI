# Chatbot with openai

This repository contains the code how to create a Chatbot using  Python, streamlit, LangChain and LLM models with Open AI and Llama.


# Architecture
![Architecture](Architecture/Simple%20chatbot%20Flow%20chart.png)
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

## Key Notes
- This project is a simple implementation to get started with AI-powered chatbots.
- The chatbot uses OpenAI’s model with a **temperature variable set to 0.5** for balanced responses.
- Chat history (user inputs and chatbot responses) is maintained to provide better quality answers based on context.

---

## Troubleshooting

### Common Issue: OpenAI API Key Credits
If you encounter an error related to insufficient OpenAI API Key credits, ensure your key has enough credits by adding funds to your OpenAI account.

### Also If you don't have money use free open source llms like Llama, Mistral, etc...

for that you can use Groq to acesss free LLMS. As an example:

  ```
  from langchain_groq import ChatGroq  

  llm = ChatGroq(model="llama3-8b-8192",temperature = 0.5)
  ```

Also to access these free open source LLMS you need to generate GROQ_API_KEY

Save GROQ_API_KEY inside .env file
  ```
  GROQ_API_KEY = your_GROQ_API_KEY
  ```

---

## Linkedin Profile

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Isuru%20Madhushan-blue?logo=linkedin&style=for-the-badge)](https://www.linkedin.com/in/isuru-madhushan-096878273/)


---

Feel free to contribute or report any issues you encounter. Let's build smarter AI together!

#AI #Chatbot #OpenAI #Streamlit #Python #LangChain
