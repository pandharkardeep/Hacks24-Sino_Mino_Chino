import streamlit as st
import pdfplumber
import re
import os
import requests
openaikey = ''
chatgpt_url = "https://api.openai.com/v1/chat/completions"
chatgpt_headers = {
    "content-type": "application/json",
    "Authorization":"Bearer {}".format(openaikey)}

with open('pdf.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
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


def json_to_dataframe(json_data):
    data = []
    for item in json_data:
        values = []
        for subitem in item.values():
            if isinstance(subitem, list):
                values.extend([nested_subitem['value'] for nested_subitem in subitem])
        data.append(values)
    
    df = pd.DataFrame(data).transpose()
    return df

def main():
    st.title("PDF to JSON Converter")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
    if uploaded_file is not None:
        with st.spinner("Extracting text from PDF..."):
            text = extract_text_from_pdf(uploaded_file)
        st.write("Text is Extracted successfully!")
        #st.write(text)
        prompt_prefix = f"""{text}
        --------------------------
        Generate basic Blood Report from Given Text. Generate the value to be key value pair. The JSON should have the following format:"""

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
        output_directory = "config"
        #os.makedirs(output_directory, exist_ok=True)
        output_file_path = os.path.join(output_directory, "output.json")

        with open(output_file_path, "w") as output_file:
            json.dump(response['choices'][0]['message']['content'], output_file, indent=2)

        st.write(response['choices'][0]['message']['content'])
        st.success(f"JSON output saved to {output_file_path}")
        


if __name__ == "__main__":
    main()
