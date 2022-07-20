import tkinter
from tkinter import *
from tkinter import  filedialog
from PIL import ImageTk, Image
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
import pywhatkit
import os


x=48
y=18

for number in range(10000000):
    x=x+1

    num="Enter the number with country code "

    if x==60:
        x=1
        y=y+1
    pywhatkit.sendwhatmsg(num,'Happy coading'*x,y,x)












    # browserExe = "firefox.exe"
    # os.system("taskkill /f /im " + browserExe)


