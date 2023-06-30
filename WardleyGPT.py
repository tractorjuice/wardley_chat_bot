# Importing required packages
import streamlit as st
import openai
from streamlit_chat import message
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.callbacks import get_openai_callback

st.set_page_config(page_title="Chat with WardleyGPT")
st.title("Chat with WardleyGPT")
st.sidebar.markdown("Developed by Mark Craddock](https://twitter.com/mcraddock)", unsafe_allow_html=True)
st.sidebar.markdown("Current Version: 0.1.4")
st.sidebar.markdown("Using GPT-4 API")
st.sidebar.markdown("Not optimised")
st.sidebar.markdown("May run out of OpenAI credits")

# Set OpenAI API model
#MODEL = "gpt-3"
#MODEL = "gpt-3.5-turbo"
#MODEL = "gpt-3.5-turbo-0613"
#MODEL = "gpt-3.5-turbo-16k"
#MODEL = "gpt-3.5-turbo-16k-0613"
MODEL = "gpt-4"
#MODEL = "gpt-4-0613"
#MODEL = "gpt-4-32k-0613"
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

def get_initial_message():
    messages=[
            {"role": "system", "content": """
            You are SimonGPT a strategy researcher based in the UK.
            “Researcher” means in the style of a strategy researcher with well over twenty years research in strategy and cloud computing.
            You use complicated examples from Wardley Mapping in your answers, focusing on lesser-known advice to better illustrate your arguments.
            Your language should be for an 12 year old to understand.
            If you do not know the answer to a question, do not make information up - instead, ask a follow-up question in order to gain more context.
            Use a mix of technical and colloquial uk englishlanguage to create an accessible and engaging tone.
            Provide your answers using Wardley Mapping in a form of a sarcastic tweet.
            """},
            {"role": "user", "content": "I want to learn about Wardley Mapping"},
            {"role": "assistant", "content": "Thats awesome, what do you want to know aboout Wardley Mapping"}
        ]
    return messages

def get_chatgpt_response(messages, model=MODEL):
    
    # Convert messages to corresponding SystemMessage, HumanMessage, and AIMessage objects
    new_messages = []
    for message in messages:
        role = message['role']
        content = message['content']
        
        if role == 'system':
            new_messages.append(SystemMessage(content=content))
        elif role == 'user':
            new_messages.append(HumanMessage(content=content))
        elif role == 'assistant':
            new_messages.append(AIMessage(content=content))
    
    chat = ChatOpenAI(
        openai_api_key=OPENAI_API_KEY,
        model_name=model,
        temperature=0.0,
    )

    try:
        with get_openai_callback() as cb:
            response = chat(new_messages)
    except:
        st.error("OpenAI Error")
    if response is not None:
        return response.content
    else:
        st.error("Error")
        return "Error: response not found"

def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
    
if 'past' not in st.session_state:
    st.session_state['past'] = []

query = st.text_input("Question: ", "", key="input")

if 'messages' not in st.session_state:
    st.session_state['messages'] = get_initial_message()
    st.session_state.past.append("What is Wardley Mapping?")
    st.session_state.generated.append("""
    Oh, joy! 🎉 Wardley Mapping is a fab way to visualize strategy. 🗺️ Like a pirate treasure map, but for businesses. Beware of sharks! 🦈 You'll spot nifty patterns & make better decisions. It's all about "where" things are on the map. Value chains & evolution, matey! Arrr! 👨‍🎨🚀🗺️ #GetMapping
    """)

if query:
    with st.spinner("generating..."):
        messages = st.session_state['messages']
        messages = update_chat(messages, "user", query)
        response = get_chatgpt_response(messages, MODEL)
        messages = update_chat(messages, "assistant", response)
        st.session_state.past.append(query)
        st.session_state.generated.append(response)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i), avatar_style="shapes", seed=12)
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user', avatar_style="shapes", seed=20)
