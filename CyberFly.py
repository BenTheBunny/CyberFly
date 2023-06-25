import os
from pypdf import PdfReader
import streamlit as st
import pandas as pd
import numpy as np


uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    with os.scandir(uploaded_file) as files:
        for file in files:
            reader = PdfReader(file.path)
            number_of_pages = len(reader.pages)
            for i in range(number_of_pages): #number_of_pages ):
                page = reader.pages[i]
                text = page.extract_text()
                st.write(text)
