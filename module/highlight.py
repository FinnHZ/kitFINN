import tkinter
from tkinter import *
from PIL import Image, ImageTk
import pyautogui
from PIL import Image, ImageTk  #pip install pillow
import os



def highlight(event=None):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'./img/screenshotTest.png')

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

    #create a obj to store the position data of mouse
    positionObj = {"start_x":0,"start_y":0}
    lineList = []
    

    
    def downmouse(event): 
        positionObj["start_x"] = event.x
        positionObj["start_y"] = event.y
        global tem_lineList
        tem_lineList = [] 

    def upmouse(event=None):
        lineList.append(tem_lineList)
            
    def dragline(event):
          
        linePoint = canvas_new.create_line(positionObj["start_x"], positionObj["start_y"], event.x, event.y, fill="cyan", width=2)
        tem_lineList.append(linePoint)
        positionObj["start_x"] = event.x
        positionObj["start_y"] = event.y

    def returnlast(event=None):
        if len(lineList) != 0:
            for point2 in lineList[-1]:
                canvas_new.delete(point2) 
            lineList.pop()       
        else:
            pass
        

    def closeTop(event=None):
        os.remove('./img/screenshotTest.png')
        newWin.destroy()

    newWin.bind('<Button-1>', downmouse)
    newWin.bind('<ButtonRelease-1>', upmouse)
    newWin.bind('<B1-Motion>', dragline)
    newWin.bind('<Double-Button-3>',closeTop)
    newWin.bind('<Button-3>',returnlast)

    newWin.mainloop()