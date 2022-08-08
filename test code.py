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

    num="Enter your mobile number"

    if x==60:
        x=1
        y=y+1
    pywhatkit.sendwhatmsg(num,'Thanks for using this tool designed by Harshit'*x,y,x)












    # browserExe = "firefox.exe"
    # os.system("taskkill /f /im " + browserExe)


