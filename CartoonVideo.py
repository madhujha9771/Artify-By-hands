# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 13:12:04 2022

@author: SUWARNA
"""
'''
import cv2

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Check if camera opened successfully
if (webcam.isOpened() == False):
  print("Error opening video stream or file")

# Read the video
while(webcam.isOpened()):
  # Capture frame-by-frame
  ret, frame = webcam.read()
  if ret == True:
      color = cv2.bilateralFilter(frame, 9, 9, 7)
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      blur = cv2.medianBlur(gray, 7)
      edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
      frame_edge = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
      cartoon = cv2.bitwise_and(color, frame_edge)
  	  # Display the resulting frame
      cv2.imshow('Cartoonized', cartoon)
  	  # Press q on keyboard to  exit
      if cv2.waitKey(25) == ord('q'):
          break
          # Press s on keyboard to save a screenshot
      elif cv2.waitKey(25) == ord('s'):
          cv2.imwrite('screenshot.png', cartoon)

# When everything done, release the video capture object
webcam.release()

# Closes all the frames
cv2.destroyAllWindows()'''
import cv2
import tkinter as tk

from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

# create the root window
root = tk.Tk()
root.title('Upload File By selecting')
root.resizable(False, False)
root.geometry('500x300')

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
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
    webcam = cv2.VideoCapture(filename) 

    # We need to set resolutions. 
    # so, convert them from float to integer. 
    frame_width = int(webcam.get(3)) 
    frame_height = int(webcam.get(4)) 
       
    size = (frame_width, frame_height) 

    result = cv2.VideoWriter('Cartoonify.avi',  
                cv2.VideoWriter_fourcc(*'MJPG'), 
                10, size, 0) 
    if (webcam.isOpened() == False):
      print("Error opening video stream or file")

    # Read the video
    while True:
      # Capture frame-by-frame
      ret, frame = webcam.read()
      
      color = cv2.bilateralFilter(frame, 9, 9, 7)
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      blur = cv2.medianBlur(gray, 7)
      edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
      frame_edge = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
      cartoon = cv2.bitwise_and(color, frame_edge)
      result.write(cartoon)
      	  # Display the resulting frame
      cv2.imshow('Cartoonized', cartoon)
      	  # Press q on keyboard to  exit
      if cv2.waitKey(25) == ord('q'):
        break
   
              # Press s on keyboard to save a screenshot
          

    # When everything done, release the video capture object
    webcam.release()
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