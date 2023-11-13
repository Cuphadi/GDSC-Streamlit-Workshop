import streamlit as st
import openai

#Simple configuration of the page
st.set_page_config(page_title="Chatbot Maker", layout="wide", initial_sidebar_state="expanded")

#Hiding header & footer
hide_streamlit_style = """
            <style>
            header {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

#This creates the prompt in which the bot will behave as
def createBot(personality,character,profession,nationality,phrase,short,emoji):
    st.session_state["bot"] = True
    st.session_state.messages = []
    full_response = ""
    if len(personality) != 0:
        full_response += "You are a " + " and ".join(personality) + " Person. "
    if character:
        full_response += "You imitate the character " + character + ". "
    if profession:
        full_response += "Your profession is " + profession + ". "
    if nationality:
        full_response += "Speak English but with " + nationality + " accent. "
    if phrase.strip():
        full_response += "Your catchphrase is " + phrase.strip() + ". "
    if short:
        full_response += "Always provide a short response which is less than 40 words. "
    if emoji:
        full_response += "Use emojis excessively. "
    st.session_state.messages.append({"role": "system", "content": full_response})

#All parameters of bot creation
with st.sidebar:
    personality = st.multiselect("Personality", options=["Sassy","Sarcastic","Enthusiastic","Rude"])
    character = st.selectbox("Character Imitation", options=["", "Mario from Super Mario", "Pikachu from Pokemon", "Richter Belmont from Castlevania"])
    profession = st.selectbox("Profession", options=["","Mathematician","Rapper","Computer Scientist"])
    nationality = st.selectbox("Nationality", options=["", "Italian", "French"])
    phrase = st.text_input("Catchphrase")
    short = st.toggle("Make responses short", value=False)
    emoji = st.toggle("Make assistant emoji fanatic")
    st.button("Unleash Assistant Chatbot!", args=(personality,character,profession,nationality,phrase,short,emoji), on_click=createBot)

st.header("Assistant Chatbot Maker 🤖")

if "bot" not in st.session_state:
    st.session_state["bot"] = False

if not st.session_state["bot"]:
    st.markdown("<h6>Fill out the necessary fields in the sidebar and click generate to make your own assistant chatbot!</h6>", unsafe_allow_html=True)
else:
    openai.api_key = "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"

    # Set a default model
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages[1:]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    try:
    # Accept user input
        if prompt := st.chat_input():
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(prompt)
            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                for response in openai.ChatCompletion.create(
                    model=st.session_state["openai_model"],
                    messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                    stream=True,
                ):
                    full_response += response.choices[0].delta.get("content", "")
                    message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
    except:
        st.warning("Rate Limit Reached! Wait for 1 minute then try again.")