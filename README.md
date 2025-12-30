# AI Resume Ranker

A smart, real-time tool that helps recruiters screen resumes faster and smarter. Built with Python, Flask, and NLP techniques, this project demonstrates how AI can assist HR teams by automatically analyzing resumes, extracting key skills, and ranking candidates.

---

## Overview

Manually screening resumes can be time-consuming and error-prone. **AI Resume Ranker** solves this by:

- Accepting PDF and image-based resumes  
- Extracting text using OCR if needed  
- Identifying relevant skills  
- Scoring and shortlisting candidates  

All of this happens in **real-time through a simple web interface**.

---

## Features

- **Resume Upload**: Accepts PDFs and images (JPEG/PNG).  
- **Text Extraction**: Uses PyMuPDF for text PDFs and Tesseract OCR for images.  
- **Skill Detection & Scoring**: Matches keywords like Python, AI, Machine Learning, Flask, Data, etc.  
- **Shortlisting Decision**: Automatically marks resumes as *Shortlisted* or *Rejected* based on score.  
- **Web Dashboard**: Clean interface built with Flask and Jinja2 templates.  
- **Optional Login**: Secure login with hashed passwords using bcrypt.

---

## How It Works

1. **Upload Resume** – The user selects a PDF or image.  
2. **Extract Text** – Text is extracted from PDF or OCR is applied for images/scanned PDFs.  
3. **Analyze Skills** – Keywords are matched against a predefined skill set.  
4. **Score & Shortlist** – Candidates scoring above threshold are shortlisted.  
5. **Show Results** – Extracted text (truncated), skill score, and status are displayed on the dashboard.

---

## Project Structure
resume_ranker/
├── app.py # Main Flask app
├── templates/ # HTML templates (upload.html, result.html)
├── static/ # CSS/JS assets
├── test_resumes/ # Sample PDF and image resumes
├── users.csv # Optional login credentials
└── requirements.txt # Python dependencies
Tech Stack

Python, Flask

pandas for data handling

PyMuPDF & pdf2image for PDF processing

Pillow & pytesseract for OCR

bcrypt for secure login (optional)

fpdf (optional) for generating sample resumes
