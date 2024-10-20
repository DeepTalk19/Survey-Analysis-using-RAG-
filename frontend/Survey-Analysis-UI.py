import streamlit as st
from io import BytesIO
import pandas as pd

sys.path.append(os.path.abspath('../backend'))
from Main import SurveyAnalysis

# Define the Streamlit app
st.title('Survey Analysis - Excel File Q&A')

# File uploader for the Excel file
uploaded_file = st.sidebar.file_uploader("Upload your Excel file", type=["xlsx", "xls"])

# Text input for the question
question = st.text_input("Ask a question about the survey:")

# Placeholder for the result
if uploaded_file and question:
    # Load the Excel file into memory for processing
    excel_path = uploaded_file.name
    # print(excel_path)

    # Initialize the SurveyAnalysis object with the in-memory Excel file
    survey_analysis = SurveyAnalysis(excel_path)

    # Run the analysis with the provided question
    result = survey_analysis.analyze_survey(question)

    # Display the result
    st.subheader("Answer:")
    st.write(result)  # Display the generated answer
