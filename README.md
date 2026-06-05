# AI Interview Preparation Assistant using OCR

## Project Overview
This project automatically detects skills from uploaded resumes and recommends relevant interview questions based on the detected skills.

The system uses OCR technology to extract text from resumes and suggests personalized interview preparation questions.

## Features
- Resume Upload (PDF)
- Automatic Skill Detection
- OCR-Based Resume Text Extraction
- Interview Question Recommendation
- Supports Multiple Skills

## Technologies Used
- Python
- Streamlit
- Pandas
- OCR (Tesseract)
- PDF2Image
- PyPDF2

## Installation

Install required libraries:

pip install -r requirements.txt

## Run the Project

streamlit run app.py

## Project Structure

AI_Interview_Assistant
│── app.py
│── interview_questions.csv
│── requirements.txt
│── README.md