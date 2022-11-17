# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 10:36:32 2022

@author: SUWARNA
"""

from tkinter import *
import sys
import os
import Pmw
def page1():
    # destroy current window
    root.destroy()
    # open page2 window
    import HomePage

def page2():
    # destroy current window
    root.destroy()
    # open page2 window
    import cartoonifierPythonProject

def page3():
    # destroy current window
    root.destroy()
    # open page2 window
    import ColouredImageToGreyScaleImage
    
root = Tk()
 
root.title('IMAGE EDITTING')
root.geometry("600x900") 
Pmw.initialise(root) #initializing it in the root window
bg = PhotoImage(master=root,file = "imageEDBack .png")

label1 = Label( root, image = bg)
label1.place(x = 0,y = 0)
label2 = Label( root, image = bg)
label2.place(x = 0,y = 450)

#label=Label(root,text='ARTIFY BY HANDS',background='#CDCDCD', font=('calibri',20,'bold'))
l1=Label(root, text = "IMAGE EDITTING",font=('calibri',30,'bold')).place(x = 140,y = 5) 

img1 = PhotoImage(master=root,file='Cartoon.png')
b = Button(root,
image=img1,
command=page2)
b.pack(pady=70)

tooltip_1 = Pmw.Balloon(root) #Calling the tooltip
tooltip_1.bind(b,'Cartoonify option is going to be inintiated') #binding it and assigning a text to it

img2 = PhotoImage(master=root,file='grey.png')
b1 = Button(root,
image=img2,
command=page3)
b1.pack(pady=10)

tooltip_2 = Pmw.Balloon(root) #Calling the tooltip
tooltip_2.bind(b1,'Grey Scaling option is going to be inintiated.') 

img3 = PhotoImage(master=root,file='HomeButton.png')
b = Button(root,
image=img3,
command=page1)
b.pack(pady=10)

tooltip_3 = Pmw.Balloon(root) #Calling the tooltip
tooltip_3.bind(b,'HOME PAGE.') #binding it and assigning a text to it             

root.mainloop()