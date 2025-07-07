def resume_matches(text, university, gpa, field, degree):
    return (
        university.lower() in text and
        field.lower() in text and
        degree.lower() in text and
        f"gpa" in text and float(gpa) <= extract_gpa(text)
    )

def extract_gpa(text):
    import re
    match = re.search(r"gpa[:\s]*([0-9]\.\d+)", text)
    if match:
        return float(match.group(1))
    return 0.0
