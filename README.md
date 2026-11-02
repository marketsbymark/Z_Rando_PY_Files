# PDF chunk splitter

A small Python desktop utility that splits a selected PDF into numbered files.
The repository currently contains one script, [`PDF_Kutta.py`](PDF_Kutta.py).

## Requirements

- Python 3 with Tkinter available and a graphical desktop session.
- The `PyPDF2` package:

```sh
python -m pip install PyPDF2
```

Tkinter is supplied by the Python installation or operating system rather than
by this repository. If the file picker cannot open, check that Tkinter and a
display are available. There is no dependency lockfile in this repository.

## Run

From the repository directory:

```sh
python PDF_Kutta.py
```

Choose a PDF in the file picker. The script splits it into **40-page chunks** by
default, with a shorter final chunk if necessary. Canceling the picker exits
without splitting a file. Progress and output paths are printed to the terminal.

For example, selecting a 95-page `report.pdf` produces these files beside it:

| Output | Pages from the original |
|---|---|
| `report-1.pdf` | 1–40 |
| `report-2.pdf` | 41–80 |
| `report-3.pdf` | 81–95 |

The original PDF is not modified. **Existing chunk files with the same names
are overwritten without a confirmation prompt.** Work on a copy or move old
outputs before running the script again.

## Use a different chunk size

The graphical entry point always uses the default of 40 pages. To select a
different positive integer size, call the function from Python:

```python
from PDF_Kutta import split_pdf_into_chunks

split_pdf_into_chunks("report.pdf", chunk_size=50)
```

Use a positive integer; the function does not validate the chunk size. Output
files are still saved beside the input PDF.

## Limitations

This is a local utility, not a batch-processing service. It copies PDF pages
into new files; it does not perform OCR or reduce file size to a target limit.
There is no password prompt, error-recovery workflow, or automated test suite.
Unreadable PDFs and output-permission errors can stop a run. Check the page
counts and contents of generated files before relying on them.
