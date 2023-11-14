import streamlit as st
import openai

#Simple configuration of the page
st.set_page_config(page_title="Chatbot Maker", layout="wide", initial_sidebar_state="expanded")

#Hiding footer
hide_streamlit_style = """
<style>
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if "bot" not in st.session_state:
    st.session_state.bot = False

#This creates the prompt in which the bot will behave as
def createBot(personality,character,profession,nationality,phrase,short,emoji):
    st.session_state.bot = True
    st.session_state.messages = []
    full_response = ""
    if len(personality) != 0:
        full_response += "You are a " + " and ".join(personality) + " Person. "
    if character:
        full_response += "You imitate the character " + character + ". "
    if profession:
        full_response += "Your profession is " + profession + ". "
    if nationality:
        full_response += "Speak English but with " + nationality + ' accent. '
    if phrase.strip():
        full_response += "Your catchphrase is " + phrase.strip() + ". "
    if short:
        full_response += "Always provide a short response which is less than 40 words. "
    if emoji:
        full_response += "Use emojis excessively. "
    st.session_state.messages.append({"role": "system", "content": full_response})
    

#All parameters of bot creation
with st.sidebar:
    personality = st.multiselect("Personality", options=["Sassy" , "Sarcastic", "Enthusiastic", "Rude"])
    character = st.selectbox("Character Imitation", options=["", "Mario from Super Mario", "Pikachu from Pokemon", "Richer Belmont from Castlevania"])
    profession = st.selectbox("Profession", options=["", "Mathematician","Rapper","Computer Scientist"])
    nationality = st.selectbox("Nationality", options=["", "Italian", "Egyptian"])
    phrase = st.text_input("Catchphrase")
    short = st.toggle("Make responses short", value=False)
    emoji = st.toggle("Make assistant emoji fanatic", value=False)
    st.button("Unleash Assistant Chatbot!", on_click=createBot, args=(personality,character,profession,nationality,phrase,short,emoji))

st.header("Assistant Chatbot Maker")

if not st.session_state.bot:
    st.markdown("<h6>Fill out the necessary fields in the sidebar and click generate to make your own asisstant chatbot</h6>", unsafe_allow_html=True)
else:

    # Set a default model
    if "openai_model" not in st.session_state:
        st.session_state.openai_model = "gpt-3.5-turbo"

    # Display chat messages from history on app rerun
    for message in st.session_state.messages[1:]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    try:
        # Accept user input
        if prompt := st.chat_input():
            # Add user message to chat history
            st.session_state.messages.append({"role":"user", "content":prompt})

            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(prompt)

            client = openai.OpenAI(api_key="YOUR_API_KEY")

            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                for response in client.chat.completions.create(
                    model=st.session_state["openai_model"],
                    messages = [{"role": m["role"], "content":m["content"]} for m in st.session_state.messages],
                    stream=True
                ):
                    full_response += response.choices[0].delta.content or ""
                    message_placeholder.markdown(full_response + " ")
                message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role":"assistant","content":full_response})
    except:
        st.warning("Rate Limit Reached! Wait for 1 mintue then try again.")