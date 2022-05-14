from tkinter import *
from tkinter import filedialog
import os
from pdf2docx import Converter
# import win32com





def convertInterface_Doc(event=None):
    newWin_c = Toplevel()

    Btn_Doc = Button(newWin_c, text="Choose PDF",  command=lambda:convertDocChoose_Doc())
    Btn_Doc.grid(row=0, column=0, padx=5, pady=5)

    docPathStr = StringVar()
    docPathStr.set("")
    docPathLab = Label(newWin_c, textvariable=docPathStr)
    docPathLab.grid(row=0, column=1, padx=5, pady=5)

    
    uploadDocBtn = Button(newWin_c, text="Convert", state=DISABLED, command=lambda: convertDocUpload_Doc())
    uploadDocBtn.grid(row=1, column=0, padx=5, pady=5, columnspan=2)


    def convertDocChoose_Doc():
        curent_directory = os.getcwd()
        file_path = filedialog.askopenfilename(initialdir=curent_directory, title="Select PDF", filetypes=[('PDF Files', '*.pdf')])  #
        if file_path != "" and file_path != "Convert Successfully!":
            docPathStr.set(file_path)
            uploadDocBtn["state"] = NORMAL
        else:
            pass
    
    def convertDocUpload_Doc():
        pdf_file = docPathStr.get()
        directoryStr = pdf_file.rsplit('.', 1)
        docx_file = directoryStr[0] + "." + "docx"
        cv = Converter(pdf_file)
        cv.convert(docx_file, start=0, end=None)
        cv.close()
        docPathStr.set("Convert Successfully!")
        uploadDocBtn["state"] = DISABLED




        # word = win32com.client.DispatchEx("Word.Application")
        # word.Visible = True
        # originalDocPath = docPathStr.get()
        # in_file = os.path.abspath(originalDocPath)
        # wd = word.Documents.Open(in_file)
        # directoryStr = originalDocPath.rsplit('.', 1)
        # docPathNew = directoryStr[0] + "." + "docx"
        # out_file = os.path.abspath(docPathNew)
        # wd.SaveAs(out_file, FileFormat=16)
        # wd.Close()
        # word.Quit()
        # docPathStr.set("Convert Successfully!")
        # uploadDocBtn["state"] = DISABLED
            
            
