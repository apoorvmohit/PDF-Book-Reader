# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 23:24:17 2021

@author: Apoorv
"""

from tkinter import *
from tkinter import filedialog
import pyttsx3
import PyPDF2

Window=Tk()
Window.geometry('500x350')
Window.config(bg="orange")
Window.title("PDF Audio Book")

startingpagenumber = Entry(Window)
page1=Label(Window,text= "Enter starting page number")
page1.place(relx=0.02,rely=0.1)
startingpagenumber.place(relx=0.6,rely=0.1)
label = Label(Window, text="select a book.")
label.place(relx=0.3,rely=0.2)

def file():
    path = filedialog.askopenfilename()
    book = open(path, 'rb')
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages
    speaker = pyttsx3.init("sapi5")
    
    for i in range(int(startingpagenumber.get()), pages):
        page = pdfreader.getPage(i) 
        txt = page.extractText()
        speaker.say(txt)
        speaker.runAndWait()
 
B=Button(Window, text="Choose  the Book", command=file)
B.place(relx=0.4,rely=0.3)
 
mainloop()