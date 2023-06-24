import os
from pypdf import PdfReader
import tkinter as tk


window = tk.Tk()
window.geometry("700x250")


def get_data():
    label.config(text= entry.get(), font= ('Helvetica 13')) #я пытался настроить ее так чтобы использовать в os.scandir



entry = tk.Entry(window, width= 42)
entry.place(relx= .5, rely= .5, anchor= 'center')


label= tk.Label(window, text="", font=('Helvetica 13'))
label.pack()


tk.Button(window, text= "Click to Show", command= get_data).place(relx= .7, rely= .5, anchor='center')
entry.pack()
window.mainloop()

#читает пдф файл
with os.scandir(get_data()) as files:
    for file in files:
        reader = PdfReader(file.path)
        number_of_pages = len(reader.pages)
        for i in range(1): #number_of_pages ):
            page = reader.pages[i]
            text = page.extract_text()
            print(text) #заменить обработкой документа
            