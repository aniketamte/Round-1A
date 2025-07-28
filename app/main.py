import os
import json
from utils import extract_headings

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def process_pdfs():
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(INPUT_DIR, filename)
            json_path = os.path.join(OUTPUT_DIR, filename.replace(".pdf", ".json"))
            data = extract_headings(pdf_path)
            with open(json_path, "w") as f:
                json.dump(data, f, indent=2)

if __name__ == "__main__":
    process_pdfs()