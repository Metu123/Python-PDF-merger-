
Interactive file selection (manual input)

File existence and format validation

Optional reordering of PDFs before merging

Custom output filename

Automatic output directory selection

Error handling during merge process



---

Requirements

Python Version

Python 3.7+


Dependencies

Install required library:

pip install PyPDF2


---

How It Works

1. File Selection

Function: get_pdf_files

The script prompts the user to input PDF file paths one by one:

User enters file path manually

Special keyword done ends input session


Validation checks:

File must exist

File must have .pdf extension


Example:

PDF path: file1.pdf
PDF path: file2.pdf
PDF path: done


---

2. Display Selected Files

Function: display_files

Once files are collected, they are displayed with indexes:

Example:

Files selected:
1. file1.pdf
2. file2.pdf
3. file3.pdf

This helps the user visually confirm selection before merging.


---

3. Reordering PDFs

Function: reorder_files

The user is asked if they want to change the order:

Do you want to reorder files? (y/n):

If yes:

User inputs new order using numbers


Example:

New order: 2,1,3

This means:

Second file becomes first

First file becomes second

Third stays in place


If invalid input is provided:

Original order is kept



---

4. Output File Name

Function: get_output_path

The user is prompted to name the output file:

Enter output file name (without .pdf):

Rules:

If empty input → defaults to merged_output.pdf

File is saved in the same directory as the first selected PDF


Example output path:

/home/user/documents/merged_output.pdf


---

5. PDF Merging Process

Function: merge_pdfs

This is the main function that controls the workflow.

Steps:

1. Collect PDF files


2. Validate minimum requirement (at least 2 files)


3. Display selected files


4. Allow optional reordering


5. Define output path


6. Merge files using PdfMerger




---

6. Merging Engine

The script uses:

PdfMerger()

For each file:

merger.append(pdf)

Then final output is written:

merger.write(output_file)

Finally:

merger.close()

This ensures proper resource cleanup.


---

7. Error Handling

The script handles:

Invalid Files

Non-existent files

Non-PDF files


Merge Errors

Corrupted PDF files

Read/write failures


Example output:

Error during merge: [error message]


---

Example Usage

Start Program

python script.py


---

Input Files

PDF path: doc1.pdf
PDF path: doc2.pdf
PDF path: done


---

Display

Files selected:
1. doc1.pdf
2. doc2.pdf


---

Reorder Option

Do you want to reorder files? (y/n): y
New order: 2,1


---

Output Name

Enter output file name (without .pdf): final_report


---

Final Output

Merged PDF saved as:
/home/user/documents/final_report.pdf


---

Code Structure

Core Functions

Function	Purpose

get_pdf_files()	Collects PDF file paths
display_files()	Shows selected files
reorder_files()	Changes file order
get_output_path()	Sets output filename
merge_pdfs()	Main merge logic



---

Workflow Summary

User Input → File Validation → Display → Optional Reorder → Output Name → Merge → Save PDF


---

Design Decisions

1. Manual Input Approach

The script uses interactive input instead of CLI arguments to make it beginner-friendly.


---

2. Safe Validation

Each file is checked before being added:

Exists on disk

Has .pdf extension



---

3. Flexible Ordering

Users can reorder files without reselecting them.


---

4. Output Control

Output filename is customizable, but directory is automatically derived from input files.


---

Limitations

No drag-and-drop support

No GUI interface

No recursive folder scanning

No password-protected PDF support

No preview of PDFs before merging

No parallel processing



---

Possible Improvements

CLI Enhancements

Use argparse for automation

Support direct folder merging


Feature Enhancements

Add PDF splitting

Add page range selection (e.g., pages 1–5 only)

Add duplicate detection

Add PDF preview (metadata, page count)


UX Improvements

GUI version (Tkinter / Electron / Web UI)

Progress bar during merge

Drag-and-drop file selection



---

Security Notes

The tool does not modify original PDFs

Output is a new file only

No network activity involved

Safe for offline use



---

License

This script is free to use, modify, and distribute for personal or commercial purposes.
