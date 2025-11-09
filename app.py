from flask import Flask, request, jsonify
from flask_cors import CORS
import PyPDF2
import io

app = Flask(__name__)
CORS(app)

@app.route('/process', methods=['POST'])
def process_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    filename = file.filename.lower()

    stage1 = f"Received file: {filename}"

    extracted_text = ""
    if filename.endswith('.pdf'):
        try:
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(file.read()))
            for page in pdf_reader.pages:
                extracted_text += page.extract_text() or ""
        except Exception as e:
            extracted_text = f"Error reading PDF: {str(e)}"
    else:
        extracted_text = "(Only PDF supported in this demo)"

    response = {
        "stage1": stage1,
        "stage2": f"Extracted text (truncated): {extracted_text[:500]}",
        "stage3": "Static placeholder for PO data segregation",
        "stage4": "Static placeholder for search string extraction",
        "stage5": "Static placeholder for fuzzy matching records",
        "stage6": "Static placeholder for closest matching values"
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
