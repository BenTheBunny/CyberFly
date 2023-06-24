import os
from pypdf import PdfReader
import tkinter as tk
import streamlit as st
import pandas as pd
import numpy as np

example_dir = st.text_input('Введите путь до пдф')
with os.scandir(example_dir) as files:
    for file in files:
        reader = PdfReader(file.path)
        number_of_pages = len(reader.pages)
        for i in range(number_of_pages): #number_of_pages ):
            page = reader.pages[i]
            text = page.extract_text()
            st.write(text)
