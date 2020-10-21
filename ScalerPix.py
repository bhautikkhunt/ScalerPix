import cv2
from cv2 import dnn_superres
import datetime
import time
from tkinter import *
#from tkinter.ttk import Style
import numpy as np
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile

# Create an SR object
sr = dnn_superres.DnnSuperResImpl_create()
#-----Tinkter--------

now = datetime.datetime.now()
seconds = now.second


a = Tk()
toolbar = Frame(a)
toolbar2 = Frame(a)
toolbar3 = Frame(a)
text = Text(a)
a.title("Scaler Pix")





a.geometry("1500x1000+200+5")
#1500x930+200+40
#a.title("wm min/max")
a.resizable(0,0)



#---Opening A File--------

def mFileopen():
    global file_path
    global panel
    file_path = filedialog.askopenfilename(filetypes=(("Image files", "*.jpg;*.jpeg;*.png;*.tif;*.gif;*.bmp;*.tiff;*.jfif;*.eps;*.raw;*.cr2;*.nef;*.orf;*.sr2;"),
                                       ("All files", "*.*") ))
    print(file_path)
    img = Image.open(file_path)
    img = img.resize((450, 450), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(a, image=img,borderwidth=2, relief="solid")
    panel.image = img
    panel.pack(side=LEFT,anchor=NW,padx=200)
    toolbar.pack(side=TOP)
    btn1.configure(state="disable")
    btn2.configure(state="active")
    btn3.configure(state="active")
    btn4.configure(state="active")
    btn5.configure(state="disable")
    btn6.configure(state="active")

    #, anchor = S
    #panel.pack()

#label = Label(text=file_path).pack()

#----Opening End-----------------------

#------Image Processing------

def mProcess_two():
    global final_img
    global panel2
    print("File path outside the function")
    print(file_path)
    img = cv2.imread(file_path)
    start_time = time.time()
    path = "EDSR_x2.pb"
    sr.readModel(path)
    sr.setModel("edsr", 3)
    result = sr.upsample(img)
    b, g, r = cv2.split(result)
    conv_img = cv2.merge((r, g, b))
    #print(result.shape)
    #array = np.reshape(result, (1024, 720))
    #print(type(result))
    final_img = Image.fromarray(conv_img)
    #print(type(final_image))
    #print(final_image.mode)
    #print(final_image.size)
  # final_image = cv2.resize(result, (450, 450))
    img = final_img.resize((450, 450), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img)
    panel2 = Label(a, image=img_1,borderwidth=2, relief="solid")
    panel2.image = img_1
    end_time = time.time()
    print("Excution Time: ", (end_time - start_time))
    panel2.pack(side=LEFT, padx=0)
    toolbar.pack(side=TOP)
    btn1.configure(state="disable")
    btn2.configure(state="disable")
    btn3.configure(state="disable")
    btn4.configure(state="disable")
    btn5.configure(state="active")
    btn6.configure(state="active")

def mProcess_three():
    global final_img
    global panel2
    print("File path outside the function")
    print(file_path)
    img = cv2.imread(file_path)
    start_time_3 = time.time()
    path = "EDSR_x3.pb"
    sr.readModel(path)
    sr.setModel("edsr", 3)
    result = sr.upsample(img)
    b, g, r = cv2.split(result)
    conv_img = cv2.merge((r, g, b))
    #print(result.shape)
    #array = np.reshape(result, (1024, 720))
    #print(type(result))
    final_img = Image.fromarray(conv_img)
    #print(type(final_image))
    #print(final_image.mode)
    #print(final_image.size)
  # final_image = cv2.resize(result, (450, 450))
    img = final_img.resize((450, 450), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img)
    panel2 = Label(a, image=img_1,borderwidth=2, relief="solid")
    panel2.image = img_1
    end_time_3 = time.time()
    print("Excution Time: ", (end_time_3 - start_time_3))
    panel2.pack(side=LEFT, padx=0)
    toolbar.pack(side=TOP)
    btn1.configure(state="disable")
    btn2.configure(state="disable")
    btn3.configure(state="disable")
    btn4.configure(state="disable")
    btn5.configure(state="active")
    btn6.configure(state="active")


def mProcess_four():
    global final_img
    global panel2
    print("File path outside the function")
    print(file_path)
    img = cv2.imread(file_path)
    start_time_4 = time.time()
    path = "EDSR_x4.pb"
    sr.readModel(path)
    sr.setModel("edsr", 3)
    result = sr.upsample(img)
    b, g, r = cv2.split(result)
    conv_img = cv2.merge((r, g, b))
    #print(result.shape)
    #array = np.reshape(result, (1024, 720))
    #print(type(result))
    final_img = Image.fromarray(conv_img)
    #print(type(final_image))
    #print(final_image.mode)
    #print(final_image.size)
  # final_image = cv2.resize(result, (450, 450))
    img = final_img.resize((450, 450), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img)
    panel2 = Label(a, image=img_1,borderwidth=2, relief="solid")
    panel2.image = img_1
    end_time_4 = time.time()
    print("Excution Time: ", (end_time_4 - start_time_4))
    panel2.pack(side=LEFT, padx=0)
    toolbar.pack(side=TOP)
    btn1.configure(state="disable")
    btn2.configure(state="disable")
    btn3.configure(state="disable")
    btn4.configure(state="disable")
    btn5.configure(state="active")
    btn6.configure(state="active")

def save():
    files = [("Image files", "*.jpg;*.jpeg;*.png;*.tif;*.gif;*.bmp;*.tiff;*.eps;*.raw;*.cr2;*.nef;*.orf;*.sr2"),
                                       ("All files", "*.*")]
    file = asksaveasfile(filetypes=files, defaultextension=files)
    final_img.save(file)
    btn6.configure(state="active")
    #cv2.imwrite(file,img)

def mRefresh():
    #btn5.configure(image="")
    #btn1 = upload
    #btn2 = Run with 2x
    #btn3 = Run with 3x
    #btn4 = Run with 4x
    #btn5 = save
    #btn6 = Refresh
    btn1.configure(state="active")
    btn2.configure(state="disable")
    btn3.configure(state="disable")
    btn4.configure(state="disable")
    btn5.configure(state="disable")
    btn6.configure(state="disable")
    panel.destroy()
    panel2.destroy()


#-------------Default Layout-------------

btn1 = Button(toolbar,text="Upload your file",fg = "black",font = ("SF Pro Text",16),height=2,width=120,command= mFileopen)
btn1.pack(side=TOP,padx = 120,pady = 150,fill=X)
toolbar.pack(side=TOP,padx = 50,pady = 0)
"""
btn5 = Button(toolbar3,text="Download",fg = "black",font = ("SF Pro Text",16),height=2,width=30,command=save)
btn5.pack(anchor=SE,padx=190,pady=20)
toolbar3.pack(side=BOTTOM,fill=X,padx=50,pady=10)

btn6 = Button(toolbar3,text="Cancel",fg = "black",font = ("SF Pro Text",16),height=2,width=30,command=save)
btn6.pack(anchor=SE,side=LEFT,padx=190,pady=20)
toolbar3.pack(side=BOTTOM,fill=X)
"""


btn5 = Button(toolbar3,text="Download",fg = "black",font = ("SF Pro Text",16),height=2,width=30,command= save)
btn5.configure(state="disable")
btn5.pack(anchor=SW,side=LEFT,padx = 190,pady = 20)
toolbar3.pack(side=BOTTOM,fill=X)



btn6 = Button(toolbar3,text="Refresh",fg = "black",font = ("SF Pro Text",16),height=2,width=30,command= mRefresh)
btn6.configure(state="disable")
btn6.pack(anchor=SE,side=LEFT,padx = 190,pady = 20)
toolbar3.pack(side=BOTTOM,fill=X)

#side=TOP,fill=X,padx = 50,pady = 10

btn2 = Button(toolbar2,text="Run With 2x",fg = "black",font = ("SF Pro Text",10),height=3,width=25,command= mProcess_two)
btn2.configure(state="disable")
btn2.pack(anchor=SW,side=LEFT,padx = 190,pady = 20)
toolbar2.pack(side=BOTTOM,fill=X)


btn3 = Button(toolbar2,text="Run With 3x",fg = "black",font = ("SF Pro Text",10),height=3,width=25,command= mProcess_three)
btn3.configure(state="disable")
btn3.pack(anchor=S,side=LEFT,padx = 60,pady = 20)
toolbar2.pack(side=BOTTOM,fill=X)

btn4 = Button(toolbar2,text="Run With 4x",fg = "black",font = ("SF Pro Text",10),height=3,width=25,command= mProcess_four)
btn4.configure(state="disable")
btn4.pack(anchor=SE,side=TOP,padx = 190,pady = 20)
toolbar2.pack(side=BOTTOM,fill=X)
#btn3 = Button(toolbar2,text="Note:Choose Only Image",bg="yellow",height=2,width=20)
#btn3.pack(side=LEFT,padx=190,pady=10)
#btn3.configure(state="disable",font = ('Sans','11','bold'))
#toolbar2.pack(side=BOTTOM,fill=X,padx = 30,pady = 10)


#----------------------------------------------------------------------

uname = Label(a,anchor=N, text = "Scaler Pix",fg = "black",font = ("SF Pro Text Bold",35)).place(x = 650,y = 50)

#50
#abel(a, text="Blue Text in Verdana bold",fg = "black",font = "SF Pro Text 16").pack()
a.mainloop()