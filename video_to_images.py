import cv2
import os
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image

window = tk.Tk()
window.title("Video to Frames")
window.geometry('1000x700')
start1 = tk.Label(text = "VIDEO  TO  FRAMES", font=("Arial", 55,"underline"), fg="red") # same way bg
start1.place(x = 140, y = 10)


def start_fun():
    window.destroy()


startb = Button(window, text="START",command=start_fun,font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =130 , y =550 )


path = "Images/front.jpg"
img1 = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(window, image = img1)
panel.place(x = 170, y = 150)


def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()


exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =730 , y = 550 )
window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()

window1 = tk.Tk()
window1.title("Video to Images")
window1.geometry('1000x700')

path_list = []
clip_list = []


def open_file():
    global filename
    filename = filedialog.askopenfilename(title="Select file")

    path_text.delete("1.0", "end")
    path_text.insert(END, filename)


def get_fun():
    global filename
    cam = cv2.VideoCapture(filename)
    info1.config(text = "Frame Rate  :  " + str(cam.get(cv2.CAP_PROP_FPS)))
    x = int(cam.get(cv2.CAP_PROP_FPS))
    try:
        if not os.path.exists('Video Images'):
            os.makedirs('Video Images')
    except OSError:
        print('Error: Creating directory of data')

    currentframe = 0
    x2=0
    while True:
        ret, frame = cam.read()
        if ret:
            if currentframe % x == 0:
                x1 = int(currentframe / x)
                name = './Video Images/frame' + str(x1) + '.jpg'
                x2 = x2 + 1
                cv2.imwrite(name, frame)
            currentframe += 1
        else:
            break
    info2.config(text="No. of frame/Images  :  " + str(x2))
    cam.release()
    cv2.destroyAllWindows()
    mbox.showinfo("Success","Images extracted successfully.\n\nSaved to Video Images folder.")


start1 = tk.Label(text = "VIDEO  TO  IMAGES", font=("Arial", 55, "underline"), fg="red") # same way bg
start1.place(x = 140, y = 10)

lbl1 = tk.Label(text="Select Video to convert into Frames", font=("Arial", 40),fg="green")
lbl1.place(x=80, y=100)

lbl2 = tk.Label(text="SELECTED VIDEO", font=("Arial", 30),fg="brown")  # same way bg
lbl2.place(x=80, y=260)

path_text = tk.Text(window1, height=1, width=37, font=("Arial", 30), bg="light yellow", fg="orange",borderwidth=2, relief="solid")
path_text.place(x=80, y = 310)

info1 = tk.Label(font=("Arial", 30),fg="gray")
info1.place(x=80, y=400)

info2 = tk.Label(font=("Arial", 30),fg="gray")
info2.place(x=80, y=480)


selectb=Button(window1, text="SELECT",command=open_file,  font=("Arial", 25), bg = "light green", fg = "blue")
selectb.place(x = 80, y = 580)


getb=Button(window1, text="GET IMAGES",command=get_fun,  font=("Arial", 25), bg = "orange", fg = "blue")
getb.place(x = 390, y = 580)


def exit_win1():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window1.destroy()


getb=Button(window1, text="EXIT",command=exit_win1,  font=("Arial", 25), bg = "red", fg = "blue")
getb.place(x = 780, y = 580)

window1.protocol("WM_DELETE_WINDOW", exit_win1)
window1.mainloop()

