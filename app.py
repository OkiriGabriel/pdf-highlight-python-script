import fitz  # PyMuPDF

def highlight_keywords(input_path, output_path, password=None):
    try:
        pdf = fitz.open(input_path)
    except fitz.fitz.FileDataError:
        print("Error opening PDF file. The file may be corrupted or not a valid PDF.")
        return
    
    if pdf.needs_pass:
        if not password:
            print("The PDF is encrypted and a password is required.")
            return
        if not pdf.authenticate(password):
            print("The provided password is incorrect.")
            return

    # Keywords to search for (case sensitive)
    keywords = ["Name1", "Fuel", "Name2", "Name3", "Name4", "Also", "Name5", "Facebook", "Name6"]

    # Iterate through the pages
    for page in pdf:
        text = page.get_text("dict")  # Get text in dict format for structured analysis
        blocks = text["blocks"]

        columns_to_highlight = set()
        rows_to_highlight = set()

        # First pass: identify the columns and rows to highlight
        for block in blocks:
            if block["type"] == 0:  # Text block
                for line in block["lines"]:
                    for span in line["spans"]:
                        for keyword in keywords:
                            if keyword in span["text"]:
                                if keyword == "Name1":
                                    columns_to_highlight.add(span["origin"][0])  # X-coordinate of Name1 column
                                elif keyword == "Fuel":
                                    columns_to_highlight.add(span["origin"][0])  # X-coordinate of Fuel column
                                rows_to_highlight.add(span["origin"][1])  # Y-coordinate of row

        # Second pass: highlight rows and columns
        for block in blocks:
            if block["type"] == 0:  # Text block
                for line in block["lines"]:
                    for span in line["spans"]:
                        # Highlight rows
                        if span["origin"][1] in rows_to_highlight:
                            rect = fitz.Rect(0, span["bbox"][1], page.rect.width, span["bbox"][3])
                            highlight_area(page, rect, (1, 1, 0))  # Yellow for rows

                        # Highlight columns
                        for col in columns_to_highlight:
                            if abs(span["origin"][0] - col) < 5:  # Allow small tolerance
                                rect = fitz.Rect(span["bbox"][0], 0, span["bbox"][2], page.rect.height)
                                highlight_area(page, rect, (0, 1, 1))  # Cyan for columns

    pdf.save(output_path)
    pdf.close()

def highlight_area(page, rect, color):
    highlight = page.add_highlight_annot(rect)
    highlight.set_colors(stroke=color)
    highlight.update()

# Example usage
input_file = "sample.pdf"
output_file = "output_highlighted.pdf"
password = "your_password_here"  # Replace with actual password if the PDF is encrypted

highlight_keywords(input_file, output_file, password)
