import streamlit as st
import pdfplumber
import re

openaikey = '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'
chatgpt_url = "https://api.openai.com/v1/chat/completions"
chatgpt_headers = {
    "content-type": "application/json",
    "Authorization":"Bearer {}".format(openaikey)}


import json
def generate_revised_content(content):
    content = re.sub(r'[^\x00-\x7F]+', ' ', content)
    content = content.replace('\n', ' ')

# Escape quotes
    content = content.replace('"', '\\"')




def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    
    return text
import requests


def main():
    st.title("PDF to JSON Converter")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
    if uploaded_file is not None:
        with st.spinner("Extracting text from PDF..."):
            text = extract_text_from_pdf(uploaded_file)
        st.write("Extracted Text:")
        st.write(text)
        prompt_prefix = f"""{text}
        --------------------------
        Generate basic Blood Report from Given Text. Generate a question and a corresponding answer
        Strictly output in JSON format. The JSON should have the following format:"""

        sample_json = [
            {"HEMOGLOBIN":[{"value": '...' },{ "range":'...' }, {"unit": 'g/dL'}]},
            {"RED_BLOOD_CELL_COUNT":[{"value": '...' },{ "range":'...' }, {"unit": 'mil/µL'}]},
            {"WHITE_BLOOD_CELL_COUNT": [{"value": '...' },{ "range":'...' }, {"unit": 'thou/µL'}]},
            {"PLATELET_COUNT": [{"value": '...' },{ "range":'...' }, {"unit": 'thou/µL'}]}
        ]

        prompt = prompt_prefix + json.dumps(sample_json)
        messages = [
        {"role": "system", "content": "You are an experienced Blood Report Analyzer."},
        {"role": "user", "content": prompt}

        ]

        chatgpt_payload = {
            "model": "gpt-3.5-turbo-16k",
            "messages": messages,
            "temperature": 1.2,
            "max_tokens": 300,
            "top_p": 1,
            "stop": ["###"]
        }
        with st.spinner("Converting text to JSON..."):
            response = requests.request("POST", chatgpt_url, json=chatgpt_payload, headers=chatgpt_headers)
            response = response.json()
            print (response)
            print (response['choices'][0]['message']['content'])
            #st.write(response['choices'][0]['message']['content'])
        st.json(response['choices'][0]['message']['content'])
        

if __name__ == "__main__":
    main()