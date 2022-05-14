import tkinter
from tkinter import *
from turtle import width
from PIL import Image, ImageTk
from pyautogui import ImageNotFoundException  #pip install pillow
import time
#from pynput import keyboard
import pyautogui
from PIL import Image, ImageTk  #pip install pillow
import win32clipboard as clip   #pip install pywin32 and restart
from io import BytesIO
from tkinter import filedialog
import os
import pytesseract
import googletrans
from googletrans import Translator
# from google_trans_new import google_translator 
import win32com.client
from tkinter import scrolledtext


def translateText(event=None, rootname=None):
    rootname.attributes("-alpha", 0)
    
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'./img/screenshotTest.png')
    rootname.attributes("-alpha", 1)
    newWin = Toplevel()  #create a new pop window
    newWin.overrideredirect(True)  # remove the title of the window
    screen_width, screen_height = newWin.maxsize()  # get the size of whole screen
    #newWin.state("zoomed")   # this is just work for windows system, can make window max

    newWin.geometry("%dx%d+0+0" %(screen_width, screen_height))  # get the size of whole screen
    

    ## create the canvas
    canvas_new = tkinter.Canvas(newWin, width=screen_width, height=screen_height, bd=0, highlightthickness=0)
    img_path = './img/screenshotTest.png'
    img = Image.open(img_path)
    photo = ImageTk.PhotoImage(img)
    canvas_new.create_image(screen_width/2,screen_height/2, image=photo)
    canvas_new.pack()


    def downmouse(event): 
        global left_data, top_data, coverWin
        left_data = event.x
        top_data = event.y
        coverWin = Toplevel()
        coverWin.overrideredirect(True)
        coverWin.attributes('-alpha', 0.5)

        coverWin.geometry("1x1+%d+%d"%(left_data,top_data))

    def upmouse(event):
        
        ## remove the drag cover gray area and use 4 lines to form a rectangle to represent the screenshot area.
        coverWin.destroy()
        left_top_x = left_data
        left_top_y = top_data
        right_top_x = left_data + move_left
        right_top_y = top_data
        left_bottom_x = left_data
        left_bottom_y = top_data + move_top
        right_bottom_x = left_data + move_left
        right_bottom_y = top_data + move_top
        canvas_new.create_line(left_top_x,left_top_y,left_bottom_x,left_bottom_y, fill="cyan", width=2)
        canvas_new.create_line(left_bottom_x,left_bottom_y,right_bottom_x,right_bottom_y, fill="cyan", width=2)
        canvas_new.create_line(right_bottom_x,right_bottom_y,right_top_x,right_top_y, fill="cyan", width=2)
        canvas_new.create_line(right_top_x,right_top_y,left_top_x,left_top_y, fill="cyan", width=2)

        ## save the temporary screenshot picture
        left_data1 = event.x
        top_data1 = event.y

        left_int = left_data
        top_int = top_data
        
        width_int = left_data1 - left_int
        height_int = top_data1 - top_int
        part_ss = pyautogui.screenshot(region=(left_int, top_int, width_int , height_int))

        part_ss.save(r'./img/screenShot_tem_translate.png')
        
        #### take text from picture part  ###
        # You should download the Tesseract-OCR from https://github.com/UB-Mannheim/tesseract/wiki, install that and record the location.
        # this address should be changed as your location of  Tesseract-OCR
        pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract' 
        string_picture = pytesseract.image_to_string(r'./img/screenShot_tem_translate.png')
        #！！！！！！！   string_picture = pytesseract.image_to_string(Image.open('图片路径'), lang='chi_sim', config='-psm 6')
        translator = Translator()

        result_translate = translator.translate(string_picture, src='en', dest='zh-cn')
        print(result_translate)

        os.remove('./img/screenShot_tem_translate.png')
        os.remove('./img/screenshotTest.png')
        newWin.destroy()

        newWin_t = Toplevel()
        scrollbox = scrolledtext.ScrolledText(newWin_t, width=100, height=20)  #, font=('黑体'， 10)
        scrollbox.pack()
        scrollbox.insert(tkinter.END, "Original:")
        scrollbox.insert(tkinter.END, string_picture)
        scrollbox.insert(tkinter.END, "Translation:")
        scrollbox.insert(tkinter.END, result_translate.text)

    def dragrectangel(event):   
        start_left = left_data
        start_top = top_data 
        global move_left, move_top
        move_left = event.x_root - left_data
        move_top = event.y_root - top_data
        coverWin.geometry('%dx%d+%d+%d' % (move_left+1, move_top+1, start_left, start_top))

    def closeTop(event=None):
        os.remove('./img/screenshotTest.png')
        os.remove('./img/screenShot_tem_translate.png')
        newWin.destroy()

    newWin.bind('<Button-1>', downmouse)
    newWin.bind('<ButtonRelease-1>', upmouse)
    newWin.bind('<B1-Motion>', dragrectangel)
    newWin.bind('<Double-Button-3>',closeTop)

    newWin.mainloop()