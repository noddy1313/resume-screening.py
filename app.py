from flask import Flask, request, jsonify
from flask_cors import CORS
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
CORS(app)

def extract_text_from_pdf(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text() or ""
    return text

def rank_resumes(job_description, resumes):
    documents = [job_description] + resumes
    vectorizer = TfidfVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()
    job_vector = vectors[0]
    resume_vectors = vectors[1:]
    similarities = cosine_similarity([job_vector], resume_vectors).flatten()
    return similarities

@app.route("/rank", methods=["POST"])
def rank():
    job_description = request.form.get("job_description")
    files = request.files.getlist("files")

    resumes_text = [extract_text_from_pdf(file) for file in files]
    scores = rank_resumes(job_description, resumes_text)

    results = [{"name": file.filename, "score": float(score)} for file, score in zip(files, scores)]
    results = sorted(results, key=lambda x: x["score"], reverse=True)
    return jsonify({"results": results})

if __name__ == "__main__":
    app.run(debug=True)

