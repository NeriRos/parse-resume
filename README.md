# Parse Resume

## Description

This is a simple script to parse a resume in PDF format and extract the text from it.

It uses the pdfminer library to extract the text from the PDF file.

Then uses openai to get certain information from the text in the required format.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
export OPENAI_API_KEY="..." && python parse_resume.py <path_to_resume>
```

Update the structure of the resume in the `structure` variable in the script.

## Requirements

- pdfminer
- openai
- langchain
