import os
from pypdf import PdfReader
import streamlit as st
import pandas as pd
import numpy as np



uploaded_files = st.file_uploader('uploaded_file',accept_multiple_files=True)
for uploaded_file in uploaded_files:
    reader = PdfReader(uploaded_file)
    number_of_pages = len(reader.pages)
    for i in range(number_of_pages):
        page = reader.pages[i]
        text = page.extract_text()
        st.write(text)
