import PyPDF2
import requests
import os
from playsound import playsound
from tkinter import *
from tkinter.filedialog import askopenfilename


def start():
    filetypes = (
        ('pdf', '*.pdf'),
        ('All files', '*.*')
    )
    f = askopenfilename(filetypes=filetypes)
    url = "https://api.voicerss.org/"
    Key = os.environ.get("Key")
    pdf = PyPDF2.PdfReader(f)
    page = pdf.pages[0]
    string = str(page.extract_text())

    parameter = {
        'key': Key,
        'src': string,
        'hl': 'en-us'
    }

    response = requests.get(url, params=parameter)
    response.raise_for_status()
    with open("audio.wav", mode="wb") as binary_file:
        binary_file.write(response.content)

    playsound('audio.wav')
    os.remove("audio.wav")


window = Tk()
window.title("Pdf to Audio Convertor")
window.config(width=400, height=400, background="#C1ECE4")

label1 = Label(text="Please Select a file", background="#FF9EAA", font=("Arial", 14, "normal"), width=20, fg="#FFFFFF")
label1.place(x=90, y=140)
button = Button(text="Start", command=start, background="#5A96E3", font=("Arial", 12, "normal"), width=8)
button.place(x=160, y=180)

window.mainloop()
