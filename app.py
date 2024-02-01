from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables
GOOGLE_API_KEY = ""
import streamlit as st
import os
import google.generativeai as genai
import json
st.set_page_config(page_title="Q&A Demo")
with open('llm.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
genai.configure(api_key=GOOGLE_API_KEY)

## function to load Gemini Pro model and get repsonses
model=genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])
def get_gemini_response(question):
    
    response=chat.send_message(question,stream=True)
    return response

##initialize our streamlit app



st.header("AI Report Parser")
localhost_link = "http://localhost:8501"
st.markdown(f"[Click here to upload pdf File]({localhost_link})")
# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

if submit and input:
    output_data = {}
    try:
        with open('D:/OSC/config/output.json', 'r') as json_file:
            output_data = json.load(json_file)
    except FileNotFoundError:
        # If the file doesn't exist yet, initialize with an empty dictionary
        output_data = {}
    input +=  f"{input}\n{json.dumps(output_data)}"
    print(input)
    response = get_gemini_response(input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))
st.subheader("The Chat History is")
    
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
