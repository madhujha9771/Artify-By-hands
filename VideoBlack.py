# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:18:16 2022

@author: SUWARNA
"""
import tkinter as tk
import cv2
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

# create the root window
root = tk.Tk()
root.title('Upload File By selecting')
root.resizable(False, False)
root.geometry('500x300')
#my_str=tk.StringVar()
#my_str.set("")


def select_file():
    filetypes = (
        ('Video filex', '*.mp4'),
        ('All files', '.')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    #my_str.set(filename)
    

    showinfo(
        title='Selected File',
        message=filename
    )
    source = cv2.VideoCapture(filename) 

    # We need to set resolutions. 
    # so, convert them from float to integer. 
    frame_width = int(source.get(3)) 
    frame_height = int(source.get(4)) 
       
    size = (frame_width, frame_height) 

    result = cv2.VideoWriter('gray.avi',  
                cv2.VideoWriter_fourcc(*'MJPG'), 
                10, size, 0) 
      
    # running the loop 
    while True: 
      
        # extracting the frames 
        ret, img = source.read() 
          
        # converting to gray-scale 
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

        # write to gray-scale 
        result.write(gray)

        # displaying the video 
        cv2.imshow("Live", gray) 
      
        # exiting the loop 
        key = cv2.waitKey(1) 
        if key == ord("q"): 
            break
          
    # closing the window 
    cv2.destroyAllWindows()
  

# open button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file
)

open_button.pack(expand=True)




# run the application
root.mainloop()