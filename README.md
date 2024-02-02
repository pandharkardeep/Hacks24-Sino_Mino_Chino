# MEDSCAN - Medical Report to JSON Converter

MEDSCAN is an application built using Streamlit, pdfplumber, and OpenAI to convert medical reports into JSON format. It simplifies the extraction of relevant information from medical documents, making it easier to work with structured data.

## Getting Started

To run the MEDSCAN app, follow these steps:

### Prerequisites

- Install the required Python packages using the following command:

  ```bash
  pip install -r requirements.txt

### Configuration
1. Open main.py and update the openaiapikey field with your OpenAI API key.
2. Open app.py and update the geminikey field with your Gemini API key.
3. Update the file locations in both app.py and main.py according to your system setup.
   
### Running the App
Run the app using the following command:
```bash
streamlit run main.py
```
Open a new terminal and then use this command:
```bash
streamlit run app.py
```

