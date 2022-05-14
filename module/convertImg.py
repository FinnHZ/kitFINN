from tkinter import *
import pyautogui
from PIL import Image, ImageTk  #pip install pillow
from tkinter import filedialog
import os


def convertInterface(event=None):
    newWin_c = Toplevel()

    Btn_Img = Button(newWin_c, text="Choose Img",  command=lambda:convertImgChoose())
    Btn_Img.grid(row=0, column=0, padx=5, pady=5)

    imgPathStr = StringVar()
    imgPathStr.set("")
    imgPathLab = Label(newWin_c, textvariable=imgPathStr)
    imgPathLab.grid(row=0, column=1, padx=5, pady=5)

    imgOptions = ["jpg", "png", "bmp", "ico"]
    imgVar = StringVar()
    imgVar.set(imgOptions[0])
    imgTypeList = OptionMenu(newWin_c, imgVar, *imgOptions)
    imgTypeList.grid(row=1, column=0, padx=5, pady=5)
    
    uploadImgBtn = Button(newWin_c, text="Convert", state=DISABLED, command=lambda: convertImgUpload())
    uploadImgBtn.grid(row=1, column=1, padx=5, pady=5)


    def convertImgChoose():
        curent_directory = os.getcwd()
        file_path = filedialog.askopenfilename(initialdir=curent_directory, title="Select Image")  #, filetypes=[('Image Files', '*.jpg')]
        if file_path != "" and file_path != "Convert Successfully!":
            imgPathStr.set(file_path)
            uploadImgBtn["state"] = NORMAL
        else:
            pass
    
    def convertImgUpload():
        
        imSavePath = filedialog.asksaveasfilename(initialdir='/', title='Save Image') #, filetypes=(('JPEG', ('*.jpg', '*.jpeg', '*.jpe')), ('PNG', '*.png'), ('BMP', ('*.bmp', '*.jdib')), ('ICON', '*.ico'))
        # imSavePath = filedialog.askdirectory(initialdir='/', title='Save Image') 
        if imSavePath != "":
            originalImgPath = imgPathStr.get()
            # directoryStr = originalImgPath.rsplit('/', 1)
            imgType = imgVar.get()
            img_o = Image.open(r'{}'.format(originalImgPath))
            imgPathNew = imSavePath + '.' + imgType
            img_o.save(r'{}'.format(imgPathNew))
            imgPathStr.set("Convert Successfully!")
            uploadImgBtn["state"] = DISABLED
        else:
            pass