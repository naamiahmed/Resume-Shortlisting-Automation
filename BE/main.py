import os
from BE.resume_parser import extract_text_from_pdf, extract_text_from_docx
from BE.file_manager import save_to_folder
import re

def score_resume(resume_text, job_description):
    # Simple keyword overlap scoring (can be improved)
    resume_words = set(resume_text.lower().split())
    job_words = set(job_description.lower().split())
    if not job_words:
        return 0
    overlap = resume_words & job_words
    score = int(100 * len(overlap) / len(job_words))
    return score

def extract_university(resume_text):
    # Simple heuristic: look for lines with 'university' in them
    for line in resume_text.split('\n'):
        if 'university' in line.lower():
            return line.strip().replace(':', '').replace('University', 'University').strip()
    return 'Unknown_University'

def process_resumes(uploaded_files, job_description):
    above_50 = 0
    below_50 = 0
    results = []
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

        score = score_resume(text, job_description)
        if score > 50:
            university = extract_university(text)
            folder_path = f"shortlisted/above_50/{university}"
            above_50 += 1
        else:
            folder_path = f"shortlisted/below_50"
            below_50 += 1
        save_to_folder(path, folder_path)
        results.append({
            'filename': filename,
            'score': score,
            'folder': folder_path
        })
    return {'above_50': above_50, 'below_50': below_50, 'details': results}
