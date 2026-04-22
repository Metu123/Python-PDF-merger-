import os
from PyPDF2 import PdfMerger

def get_pdf_files():
    print("Enter paths to PDF files (type 'done' to finish):")
    pdf_files = []

    while True:
        path = input("PDF path: ").strip()

        if path.lower() == 'done':
            break

        if not os.path.exists(path):
            print(" File does not exist.")
            continue

        if not path.lower().endswith('.pdf'):
            print("❌ Not a PDF file.")
            continue

        pdf_files.append(path)

    return pdf_files


def display_files(pdf_files):
    print("\n📄 Files selected:")
    for i, file in enumerate(pdf_files, start=1):
        print(f"{i}. {file}")


def reorder_files(pdf_files):
    choice = input("\nDo you want to reorder files? (y/n): ").lower()

    if choice != 'y':
        return pdf_files

    display_files(pdf_files)
    print("\nEnter new order using numbers separated by commas (e.g., 2,1,3):")

    try:
        order = list(map(int, input("New order: ").split(',')))
        reordered = [pdf_files[i - 1] for i in order]
        return reordered
    except Exception:
        print("❌ Invalid order. Keeping original.")
        return pdf_files


def get_output_path(default_dir):
    name = input("\nEnter output file name (without .pdf): ").strip()

    if not name:
        name = "merged_output"

    return os.path.join(default_dir, f"{name}.pdf")


def merge_pdfs():
    pdf_files = get_pdf_files()

    if len(pdf_files) < 2:
        print("❌ Need at least two PDF files.")
        return

    display_files(pdf_files)

    pdf_files = reorder_files(pdf_files)

    output_dir = os.path.dirname(pdf_files[0])
    output_file = get_output_path(output_dir)

    merger = PdfMerger()

    try:
        for pdf in pdf_files:
            merger.append(pdf)

        merger.write(output_file)
        print(f"\n✅ Merged PDF saved as:\n{output_file}")

    except Exception as e:
        print(f"❌ Error during merge: {e}")

    finally:
        merger.close()


if __name__ == "__main__":
    merge_pdfs()
