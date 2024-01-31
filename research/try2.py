# import re
# import json

# def convert_medical_report_to_json(report_text):
#     sections = re.split(r'\n\n', report_text.strip())

#     medical_data = {}

#     for section in sections:
#         section_lines = section.split('\n')
#         section_name = section_lines[0].strip()

#         if section_name not in medical_data:
#             medical_data[section_name] = {}

#         for line in section_lines[1:]:
#             if line.strip() == "":
#                 continue

#             key, value_str = map(str.strip, line.split(':', 1))
#             value = value_str.split(' ', 1)[0]

#             if '.' in value or 'High' in value or 'Low' in value or 'Normal' in value or 'Non Reactive' in value:
#                 value = float(value.replace('High', '').replace('Low', '').replace('Normal', '').replace('Non Reactive', '').strip())

#             medical_data[section_name][key] = value

#     return json.dumps(medical_data, indent=2)



# json_result = convert_medical_report_to_json(report_text)
# print(json_result)

import streamlit as st
import pdfplumber
import openai
import json
from IPython.display import Markdown
import google.generativeai as genai
import g4f
import re 
import textwrap

g4f.debug.logging = True  # Enable debug logging
g4f.debug.version_check = False  # Disable automatic version checking
print(g4f.Provider.Bing.params) 
# Replace with your own OpenAI API key
#openai.api_key = "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"
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    if len(text)>2048:
        return text[0:2045]

# import openai
# import json

def generate_revised_content(content):
    content = re.sub(r'[^\x00-\x7F]+', ' ', content)
    content = content.replace('\n', ' ')

# Escape quotes
    content = content.replace('"', '\\"')
    g4f.debug.logging = True  # Enable debug logging
    g4f.debug.version_check = False  # Disable automatic version checking
    #print(g4f.Provider.Bing.params)  # Print supported args for Bing

    # Using automatic a provider for the given model
    ## Streamed completion

    

   
    response = g4f.ChatCompletion.create(
    model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": content + "\n\nconvert each pg in the above document into json format and if not possible, skip that particular part of page "}],
    )
    # Alternative model setting
    return response # Alternative model setting

def main():
    st.title("PDF to JSON Converter")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
    if uploaded_file is not None:
        with st.spinner("Extracting text from PDF..."):
            text = extract_text_from_pdf(uploaded_file)
        st.write("Extracted Text:")
        st.write(text)
        with st.spinner("Converting text to JSON..."):
            json_data = generate_revised_content(text)
        st.write("Converted JSON:")
        st.json(json_data)

if __name__ == "__main__":
    main()