import cv2    #openCV use as cv2 in python
import easygui #to open the filebox
import numpy as np #to store image
import imageio #to read image stored at particular path

import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

top=tk.Tk()
top.geometry('400x400')
top.title('Cartoonify Your Image !')
top.configure(background='white')
label=Label(top,background='#CDCDCD', font=('calibri',20,'bold'))

def upload():
    #ImagePath=easygui.fileopenbox()
    ImagePath = filedialog.askopenfilename()
    grey(ImagePath)

def grey(ImagePath):
    # read the image
    originalmage = cv2.imread(ImagePath)
    originalmage = cv2.cvtColor(originalmage, cv2.COLOR_BGR2RGB)
    #print(image)  # image is stored in form of numbers

    # confirm that image is chosen
    if originalmage is None:
        print("Can not find any image. Choose appropriate file")
        sys.exit()

    ReSized1 = cv2.resize(originalmage, (500, 540))
    #plt.imshow(ReSized1, cmap='gray')


    #converting an image to grayscale
    grayScaleImage= cv2.cvtColor(originalmage, cv2.COLOR_BGR2GRAY)
    ReSized2 = cv2.resize(grayScaleImage, (500, 540))
    #plt.imshow(ReSized2, cmap='gray')
    images=[ReSized1, ReSized2]
    fig, axes = plt.subplots(2,1, figsize=(10,10), subplot_kw={'xticks':[], 'yticks':[]}, gridspec_kw=dict(hspace=0.1, wspace=0.1))
    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap='gray')

    save1=Button(top,text="Save grayscale image",command=lambda: save(ReSized2, ImagePath),padx=30,pady=5)
    save1.configure(background='#364156', foreground='white',font=('calibri',15,'bold'))
    save1.pack(side=TOP,pady=50)
    
    plt.show()

def save(ReSized2, ImagePath):
    #saving an image using imwrite()
    newName="Grey_Scale_Image"
    path1 = os.path.dirname(ImagePath)
    extension=os.path.splitext(ImagePath)[1]
    path = os.path.join(path1, newName+extension)
    cv2.imwrite(path, cv2.cvtColor(ReSized2, cv2.COLOR_RGB2BGR))
    I= "Image saved by name " + newName +" at "+ path
    tk.messagebox.showinfo(title=None, message=I)

upload=Button(top,text="Grayscaling of Images",command=upload,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('calibri',15,'bold'))
upload.pack(side=TOP,pady=50)

top.mainloop()

#----------------------------------------------
# #Loads a color image. Any transparency of image will be neglected. It is the default flag.
# #this function is used to read the image from location
# img1 = cv2.imread(ImagePath,1)  
# img1 = cv2.resize(img1,(1280,700))#width ,height
# cv2.imshow("Colored Image",img1)  #It accept two parameters 1)- Name of screen ,2) -  Image
# print("Give image with color==\n",img1)

# #cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
# img2 = cv2.imread('H:\\Data\\avengers.jpg',0)
# img2 = cv2.resize(img2,(1280,700))#width ,height
# cv2.imshow("Gray Scale Image",img2)
# print("Image in gray scale==\n",img2)

# #cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
# img3 = cv2.imread('H:\\Data\\avengers.jpg',-1)
# img3 = cv2.resize(img3,(1280,700))#width ,height
# cv2.imshow("Original Image",img3)
# print("Image in original value==\n",img3)

# cv2.waitKey(0)  #here parameter inside waitkey handle the life duration of an image
# cv2.destroyAllWindows()


# #Image conversion project colored image into grayscale.

# #path = input("Enter the Path and name of an image===")
# #print("You Enter this===",path)

# #Now read image 
# img1 = cv2.imread("H:\\Data\\thor.jpg",0) #convert image into grayscale
# img1 = cv2.resize(img1,(560,700))
# img1 = cv2.flip(img1,0)#it accept 3 parameters 0,-1,1
# cv2.imshow("converted image==",img1)
# k = cv2.waitKey(0) & 0xFF
# if k == ord("q"):
#     cv2.destroyAllWindows()
    
# elif k == ord("s"):
#     cv2.imwrite("H:\\ouput.png",img1)  #it accept name of image and data
#     cv2.destroyAllWindows()