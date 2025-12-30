from flask import Flask, render_template, request
from pdf2image import convert_from_bytes
import pytesseract
from PIL import Image
import io
import fitz  # PyMuPDF

app = Flask(__name__)

# ---------- Tesseract OCR Path ----------
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# ---------- Allowed Upload Types ----------
ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# ---------- Text Extraction ----------
def extract_text(file_bytes, filename):
    text = ""
    try:
        if filename.lower().endswith(".pdf"):
            doc = fitz.open(stream=file_bytes, filetype="pdf")
            for page in doc:
                page_text = page.get_text()
                if page_text:
                    text += page_text
            if len(text.strip()) > 30:
                return text
            images = convert_from_bytes(file_bytes)
            for img in images:
                text += pytesseract.image_to_string(img)
        else:
            img = Image.open(io.BytesIO(file_bytes))
            text = pytesseract.image_to_string(img)
    except Exception as e:
        print("Error extracting text:", e)
    return text

# ---------- Upload Page ----------
@app.route("/", methods=["GET", "POST"])
@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files.get("resume")
        if not file or file.filename == "":
            return render_template("upload.html", msg="Please upload a file")
        if not allowed_file(file.filename):
            return render_template("upload.html", msg="Only PDF or Image files allowed")

        file_bytes = file.read()
        text = extract_text(file_bytes, file.filename)

        # Simple skill scoring
        skills = ["python", "machine learning", "ai", "flask", "data"]
        score = sum(s.lower() in text.lower() for s in skills)
        status = "Shortlisted" if score >= 2 else "Rejected"

        return render_template("result.html",
                               text=text[:1000],
                               score=score,
                               status=status)

    return render_template("upload.html")

# ---------- Run App ----------
if __name__ == "__main__":
    app.run(debug=True)
