import os
import re
import tkinter as tk
from pypdf import PdfReader

window = tk.Tk()
entry = tk.Entry(width=50,fg="black",bg='white')
label = tk.Label(
    text="Вставьте путь до пдф файла", foreground="black" , background="AntiqueWhite1", width=45,height=5)
label.pack()
entry.pack(anchor="nw", padx=6,pady=6)

window.mainloop()


example_dir = 'C:\\Python\\Nado\\pd'
with os.scandir(example_dir) as files:
    for file in files:
        reader = PdfReader(file.path)
        number_of_pages = len(reader.pages)
        for i in range(number_of_pages):
            page = reader.pages[i]
            text = page.extract_text()
            print(text)
            