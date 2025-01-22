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

## Key Notes
- This project is a simple implementation to get started with AI-powered chatbots.
- The chatbot uses OpenAI’s model with a **temperature variable set to 0.5** for balanced responses.
- Chat history (user inputs and chatbot responses) is maintained to provide better quality answers based on context.

---

## Troubleshooting

### Common Issue: OpenAI API Key Credits
If you encounter an error related to insufficient OpenAI API Key credits, ensure your key has enough credits by adding funds to your OpenAI account.

---

## GitHub Repository
Find the complete source code here:
🔗 [Chat-Bot-With-Open-AI](https://github.com/isurumadhushan24572/Chat-Bot-With-Open-AI)

---

Feel free to contribute or report any issues you encounter. Let's build smarter AI together!

#AI #Chatbot #OpenAI #Streamlit #Python #LangChain
