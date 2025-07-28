# PDF Outline Extractor (Round 1A)

## Functionality
Extracts structured outlines including the document title and hierarchical headings (H1, H2, H3 with page numbers) from PDF files.

## Methodology
Utilizes PyMuPDF for parsing and analyzing PDF content, identifying headings through font-size heuristics, and exporting structured JSON.

## Build and Execution

### Docker Build:
```bash
docker build --platform linux/amd64 -t mysolutionname:somerandomid .
```

### Docker Run:
```bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none mysolutionname:somerandomid
```

## Output Format Example:
```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
```

## Compliance
- Fully Dockerized for AMD64 systems
- Offline-only with no external dependencies
- Execution under 10 seconds for 50-page PDFs
- Model-free and lightweight (no GPU or internet required)