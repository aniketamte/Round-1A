import fitz  # PyMuPDF

def extract_headings(pdf_path):
    doc = fitz.open(pdf_path)
    title = doc.metadata.get("title") or "Untitled Document"
    
    headings = []
    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                text = " ".join([span["text"] for span in line["spans"]]).strip()
                if not text or len(text.split()) > 10:
                    continue
                font_size = max([span["size"] for span in line["spans"]])
                tag = classify_heading(font_size)
                if tag:
                    headings.append({
                        "level": tag,
                        "text": text,
                        "page": page_num
                    })
    return {"title": title, "outline": headings}

def classify_heading(size):
    if size >= 17:
        return "H1"
    elif size >= 14:
        return "H2"
    elif size >= 11:
        return "H3"
    return None