import os
import re
from pypdf import PdfReader

example_dir = 'C:\\Python\\Nado\\pd'
with os.scandir(example_dir) as files:
    for file in files:
        reader = PdfReader(file.path)
        number_of_pages = len(reader.pages)
        for i in range(number_of_pages):
            page = reader.pages[0]
            text = page.extract_text()
            print(text)