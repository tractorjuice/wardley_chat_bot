<div align="center">
  <img src="images/wardley-gpt-1.png" alt="Wardley GPT-2 Chatbot">
</div>

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://wardleygpt.streamlit.app/)

# Wardley Chat Bot

This is a Streamlit web app utilizing GPT-4 model of OpenAI to enable interactive chat with an assistant trained to provide responses with examples from Wardley Mapping. The responses are designed to be at the comprehension level of a 12-year-old and the assistant can communicate both in technical and colloquial UK English.

This code supports the blog post on creating a ChatBot using OpenAI. To learn more, check out the blog on [Prompt Engineering](https://medium.com/prompt-engineering/how-to-create-a-powerful-chatbot-in-minutes-with-streamlit-and-openai-gpt-3-5-7954e8e05db0).


## Features
- This chatbot utilizes the GPT-4 API from OpenAI.
- It is designed to provide responses in the context of a strategy researcher based in the UK, incorporating Wardley Mapping examples.
- All interactions are kept in a session state, ensuring conversation continuity during the user's session.
- A simple user interface built with Streamlit.

## How to Run
1. Clone the repository.\
2. Set the OpenAI API key in the Streamlit secrets manager.\
3. Run the streamlit app using the command streamlit run WardleyGPT.py.\

## Dependencies
To run this code, you need the following Python packages:

- os
- re
- openai
- streamlit

### API Keys
The application uses the OpenAI API. You will need to obtain an API key from OpenAI and set it in the Streamlit secrets manager.

## Using the Application
Once the application is running, you can use the input box labeled "Question for the book?" to ask your question. After entering your question, the application will generate an answer and display it on the screen.

## Developer Info
This application is developed by Mark Craddock. You can follow him on Twitter at https://twitter.com/mcraddock.

## Version Info
The current version of this application is 0.1.4.

## Disclaimer
This application is not optimized and may run out of OpenAI credits. Also, Wardley Mapping is provided courtesy of Simon Wardley and is licensed under Creative Commons Attribution Share-Alike.

Please use responsibly and in accordance with OpenAI's use-case policy.

## License
This project is licensed under Creative Commons Attribution Share-Alike.
