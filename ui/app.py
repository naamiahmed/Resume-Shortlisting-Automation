import streamlit as st
from backend.main import process_resumes

st.title("📄 Resume Shortlisting Automation")

uploaded_files = st.file_uploader("Upload CVs (PDF/DOCX)", type=["pdf", "docx"], accept_multiple_files=True)

university = st.text_input("Preferred University")
gpa = st.number_input("Minimum GPA", min_value=0.0, max_value=4.0, step=0.1)
field = st.text_input("Field (e.g., Software, DevOps)")
degree = st.text_input("Degree or Diploma")

if st.button("Start Shortlisting"):
    if uploaded_files:
        count = process_resumes(uploaded_files, university, gpa, field, degree)
        st.success(f"{count} CVs matched and saved in 'shortlisted/' folder!")
    else:
        st.warning("Please upload at least one CV file.")
