import os
from PyPDF2 import PdfMerger

def merge_pdfs():
    print("Enter paths to PDF files to merge (enter 'done' when finished):")
    pdf_files = []
    while True:
        path = input("PDF path: ").strip()
        if path.lower() == 'done':
            break
        if os.path.exists(path) and path.lower().endswith('.pdf'):
            pdf_files.append(path)
        else:
            print("Invalid file. Try again.")

    if len(pdf_files) < 2:
        print("Need at least two PDF files to merge.")
        return

    output_dir = os.path.dirname(pdf_files[0])
    output_file = os.path.join(output_dir, "merged_output.pdf")

    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)

    merger.write(output_file)
    merger.close()
    print(f"Merged PDF saved as: {output_file}")

if __name__ == "__main__":
    merge_pdfs() 