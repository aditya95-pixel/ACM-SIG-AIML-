#basic chatbot on streamlit with streamed response
import streamlit as st
import time
import google.generativeai as genai

# Configure the API key for Gemini 1.5 Flash
GOOGLE_API_KEY = '####'
genai.configure(api_key=GOOGLE_API_KEY)

# Function to simulate streaming response
def stream_data(response):
    for word in response.split(" "):
        yield word + " "
        time.sleep(0.02)

# Function to generate response using Gemini 1.5 Flash
def generate_response(prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text
# Configure the Streamlit page
st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 AI Chatbot")
# React to user input
if prompt := st.chat_input("What is your question?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Generate and display assistant response
    response_text = generate_response(prompt)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response_chunk in stream_data(response_text):
            full_response += response_chunk
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
