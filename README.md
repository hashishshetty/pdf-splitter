# pdf-splitter
  - [Overview](#overview)
  - [Usage](#usage)
  - [Screenshots](#screenshots)

## Overview
The purpose of this tool is to extract pages from a PDF file without having to upload it on random websites online, which could compromise your personal details. With this tool, you can split your PDF file locally.

## Usage
If you're running a Windows OS, you can run the executable file under `dist/Windows`, without needing to install Python.

For other OSs, you need to have [Python 3](https://www.python.org/downloads/) installed before using this tool. Additionally, it also requires `PyPDF2` and `PySimpleGUI`.

```bash
pip install -r dependencies.txt
python .\src\pdf_split_ui.py
```

## Screenshots
![ui](https://github.com/hashishshetty/pdf-splitter/blob/main/screenshots/ui.jpg)
\
\
\
![ui_pdf_error](https://github.com/hashishshetty/pdf-splitter/blob/main/screenshots/ui_pdf_error.jpg)
\
\
\
![ui_page_error](https://github.com/hashishshetty/pdf-splitter/blob/main/screenshots/ui_page_error.jpg)
