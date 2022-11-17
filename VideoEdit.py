# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 14:26:12 2022

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
    import CartoonVideo

def page3():
    # destroy current window
    root.destroy()
    # open page2 window
    import VideoBlack
    
root = Tk()

root.title('VIDEO EDITTING')
root.geometry("600x900") 
Pmw.initialise(root) #initializing it in the root window
bg = PhotoImage(master=root,file = "videocolour.png")

label1 = Label( root, image = bg)
label1.place(x = 0,y = 0)
label2 = Label( root, image = bg)
label2.place(x = 0,y = 450)

#label=Label(root,text='ARTIFY BY HANDS',background='#CDCDCD', font=('calibri',20,'bold'))
l1=Label(root, text = "VIDEO EDITING",font=('calibri',40,'bold')).place(x = 100,y = 5) 

img1 = PhotoImage(master=root,file='Cartoonify (2).png')
b = Button(root,
image=img1,
command=page2)
b.pack(pady=80)

tooltip_1 = Pmw.Balloon(root) #Calling the tooltip
tooltip_1.bind(b,'Cartoonify option is going to be inintiated') #binding it and assigning a text to it

img2 = PhotoImage(master=root,file='convertgreyscale.png')
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
