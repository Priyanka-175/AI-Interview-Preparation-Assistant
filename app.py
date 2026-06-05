import streamlit as st
import pandas as pd
import pytesseract
from pdf2image import convert_from_bytes
pytesseract.pytesseract.tesseract_cmd = r"C:\program Files\Tesseract-OCR\tesseract.exe"

# Load dataset
data = pd.read_csv("interview_questions.csv")

# Title
st.title("AI Interview Preparation Assistant")

# Skills List
skills_list = [
    "Python",
    "Machine Learning",
    "Deep Learning",
    "HTML",
    "CSS",
    "JavaScript",
    "Bootstrap",
    "jQuery",
    "TensorFlow",
    "SQL",
    "CNN",
    "RNN",
    "PyTorch",
    "Flask",
    "Streamlit"
]

# Extract text from resume PDF
def extract_text(pdf_file):

    text = ""

    images = convert_from_bytes(
        pdf_file.read(),
        poppler_path=r"C:\poppler\Library\bin"
    )

    for image in images:
        text += pytesseract.image_to_string(image)

    return text


# Detect Skills
def detect_skills(text):

    found_skills = []

    for skill in skills_list:

        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills


# Upload Resume
uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    st.success("Resume Uploaded Successfully!")

    # Resume text
    resume_text = extract_text(uploaded_file)

    # Detect skills
    detected_skills = detect_skills(resume_text)

    st.subheader("Detected Skills")
    st.write(detected_skills)

    st.subheader("Suggested Interview Questions")

    # Questions based on skills
    for skill in detected_skills:

        filtered = data[
            data["Skill"].str.lower()
            == skill.lower()
        ]

        st.write(f"### {skill}")

        for q in filtered["Question"]:
            st.write("•", q)