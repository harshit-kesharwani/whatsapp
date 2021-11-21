import tkinter
from tkinter import *
from tkinter import  filedialog
from PIL import ImageTk, Image
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
import pywhatkit
import os


x=56
y=21

for number in range(10000000):
    x=x+1

    num="+916201157459"

    if x==60:
        x=1
        y=y+1
    pywhatkit.sendwhatmsg(num,'💓'*x,y,x)












    # browserExe = "firefox.exe"
    # os.system("taskkill /f /im " + browserExe)


