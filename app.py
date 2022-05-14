import tkinter
from tkinter import *
from PIL import Image, ImageTk  #pip install pillow
from pyautogui import ImageNotFoundException  
import time
#from pynput import keyboard
import pyautogui
import win32clipboard as clip   #pip install pywin32             and   restart
from io import BytesIO
from tkinter import filedialog
import os
import pytesseract
import googletrans
from googletrans import Translator
# from google_trans_new import google_translator 
import win32com.client
from pdf2docx import Converter


from module.screenshot import quickscreen
from module.highlight import highlight
from module.convertImg import convertInterface
from module.convertDoc import convertInterface_Doc
from module.translate import translateText

root = Tk()
root.overrideredirect(True)
root.geometry("50x50+888+444")
root.wm_attributes("-transparentcolor","white")
root.attributes("-topmost",True)

picture_dict = {0:'./img/pikaqiu.png',1:'./img/eevee.png'}

pictureList = [ImageTk.PhotoImage(file = picture_dict[0]), ImageTk.PhotoImage(file = picture_dict[1])]

label_picture = Label(root, width=50, height=50)
label_picture.pack()

label_picture.configure(image=pictureList[0])

def MouseDown(event):
    global mous_X
    global mous_Y

    mous_X = event.x
    mous_Y = event.y

def MouseMove(event):
    width_ori = 50
    height_ori = 50
    move_left = event.x_root - mous_X
    move_top = event.y_root - mous_Y
    root.geometry('%dx%d+%d+%d' % (width_ori, height_ori, move_left, move_top))
 
def ExitWin(event):
    root.destroy()

def focusOutImage(event=None):
    label_picture.configure(image=pictureList[1])

def focusInImage(event=None):
    label_picture.configure(image=pictureList[0])


# move the window
root.bind("<Button-1>", MouseDown)
root.bind("<B1-Motion>", MouseMove)
#change logo according to the focus state
root.bind('<FocusOut>', focusOutImage)
root.bind('<FocusIn>', focusInImage)
# exit the window
root.bind("<Double-Button-1>", ExitWin)



# screen shot
root.bind('<Alt-s>', lambda event=None, rootname=root:quickscreen(None, root))

#highlight
root.bind('<Alt-h>', lambda event=None :highlight(None))

#convert image
root.bind('<Alt-i>', lambda event=None: convertInterface(None))

#convert document
root.bind('<Alt-d>', lambda event=None: convertInterface_Doc(None))

#translate
root.bind('<Alt-t>', lambda event=None, rootname=root:translateText(None, root))

root.mainloop()





