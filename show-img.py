#!/usr/bin/env python3
# 原作者地：https://blog.csdn.net/qq_38190111/article/details/89044299 
#import subprocess
from PIL import Image, ImageTk
import tkinter as tk
import time,os
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)

window = tk.Tk()
window.title('休息一下吧!')
window.geometry('1200x900')
global img_png

def Show_Img():
    global img_png
    Img = Image.open(current_dir + '/dialog.jpg')
    img_png = ImageTk.PhotoImage(Img)
    label_Img = tk.Label(window, image=img_png)
    label_Img.pack()

Show_Img()
window.mainloop()
