# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 18:22:38 2022

@author: SUWARNA
"""
'''
import sys
import os
import  tkinter

top=tkinter.Tk()
top.geometry('400x400')
def helloCallBack():
    os.system('cartoonifier-python-project.py')

B=tkinter.Button(top,text="hello",command= helloCallBack)
B.pack()
top.mainloop()

## isko tum direct button per hi chalana tab hi chalega'''
# importing tkinter and tkinter.ttk
# and all their functions and classes
from tkinter import *
from tkinter.ttk import *

# importing askopenfile function
# from class filedialog
from tkinter.filedialog import askopenfile

root = Tk()
root.geometry('200x100')

# This function will be used to open
# file in read mode and only Python files
# will be opened
def open_file():
	file = askopenfile(mode ='r', filetypes =[('Python Files', '*.py')])
	if file is not None:
		content = file.read()
		print(content)

btn = Button(root, text ='Open', command = lambda:open_file())
btn.pack(side = TOP, pady = 10)

mainloop()

