# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 09:28:12 2022

@author: SUWARNA
"""

from tkinter import *

def page2():
    # destroy current window
    root.destroy()
    # open page2 window
    import VideoManupulation

root=Tk()

#s1=Tk.Button(root,text='Submit',command=page2)
s1 = Button(root,
text='Submit',
command=page2)
s1.pack(pady=10)

mainloop()