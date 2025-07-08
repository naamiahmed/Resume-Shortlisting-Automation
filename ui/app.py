import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from BE.main import process_resumes

st.title("📄 Resume Shortlisting Automation")

uploaded_files = st.file_uploader("Upload CVs (PDF/DOCX)", type=["pdf", "docx"], accept_multiple_files=True)

job_description = st.text_area("Paste the Job Description Here", height=200)

if st.button("Start Shortlisting"):
    if uploaded_files and job_description.strip():
        result = process_resumes(uploaded_files, job_description)
        st.success(f"{result['above_50']} CVs scored above 50 and saved in 'shortlisted/above_50/'!\n{result['below_50']} CVs scored 50 or below and saved in 'shortlisted/below_50/'!")
        if result['details']:
            st.write("### Resume Scores and Folders:")
            st.table([
                {'Filename': r['filename'], 'Score': r['score'], 'Folder': r['folder']} for r in result['details']
            ])
    else:
        st.warning("Please upload at least one CV file and paste the job description.")
