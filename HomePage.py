# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:07:17 2022

@author: SUWARNA
"""

from tkinter import *
import sys
import os
import Pmw
import warnings
warnings.filterwarnings("ignore")
#import AImouse
def page2():
    # destroy current window
    root.destroy()
    # open page2 window
    import ImageEdit

def page3():
    # destroy current window
    root.destroy()
    # open page2 window
    import VideoEdit

def page4():
    # destroy current window
    #root.destroy()
    # open page2 window
    import AImouse
root = Tk()

root.title('ARTIFY BY HANDS')
root.geometry("600x900") 
Pmw.initialise(root) #initializing it in the root window
bg = PhotoImage(master=root,file = "colour.png")

label1 = Label( root, image = bg)
label1.place(x = 0,y = 0)
label2 = Label( root, image = bg)
label2.place(x = 0,y = 450)

#label=Label(root,text='ARTIFY BY HANDS',background='#CDCDCD', font=('calibri',20,'bold'))
l1=Label(root, text = "ARTIFY BY HANDS",font=('calibri',40,'bold')).place(x = 150,y = 5) 

img1 = PhotoImage(master=root,file='ImageEditing.png')
b = Button(root,
image=img1,
command=page2)
b.pack(pady=80)

tooltip_1 = Pmw.Balloon(root) #Calling the tooltip
tooltip_1.bind(b,'Image Editing features are going to be opened shortly.') #binding it and assigning a text to it

img2 = PhotoImage(master=root,file='VideoEdit.png')
b1 = Button(root,
image=img2,
command=page3)
b1.pack(pady=10)

tooltip_2 = Pmw.Balloon(root) #Calling the tooltip
tooltip_2.bind(b1,'Video Editing features are going to be opened shortly.') 
               
               
img3 = PhotoImage(master=root,file='AImouse.png')
b2 = Button(root,
image=img3,
command=page4)
b2.pack(pady=20)

tooltip_3 = Pmw.Balloon(root) #Calling the tooltip
tooltip_3.bind(b2,'IThis feature will help to navigate software with your hand signals.') #binding it and assigning a text to it





root.mainloop()