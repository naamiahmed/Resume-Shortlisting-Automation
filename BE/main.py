import os
from backend.resume_parser import extract_text_from_pdf, extract_text_from_docx
from backend.filter_logic import resume_matches
from backend.file_manager import save_to_folder

def process_resumes(uploaded_files, university, gpa, field, degree):
    count = 0
    for file in uploaded_files:
        filename = file.name
        path = f"uploads/{filename}"
        with open(path, "wb") as f:
            f.write(file.read())

        # Get text from file
        if filename.endswith(".pdf"):
            text = extract_text_from_pdf(path)
        elif filename.endswith(".docx"):
            text = extract_text_from_docx(path)
        else:
            continue

        # Check for match
        if resume_matches(text, university, gpa, field, degree):
            folder_path = f"shortlisted/{field}_{gpa}"
            save_to_folder(path, folder_path)
            count += 1
    return count
