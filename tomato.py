#!/usr/bin/env python3

# 原作者：https://blog.csdn.net/qq_38190111/article/details/89044299

from PIL import Image, ImageTk
import tkinter as tk
import time,os
current_dir = os.path.dirname(os.path.abspath(__file__))

def dialog():
    window = tk.Tk()
    window.title('休息一下吧!')
    window.geometry('1200x900')
    global img_png
    Img = Image.open(current_dir + "./dialog.jpg")
    img_png = ImageTk.PhotoImage(Img)
    label_Img = tk.Label(window, image=img_png)
    label_Img.pack()
    window.mainloop()

def study():
    print('''             __                      __            __
            /  |                    /  |          /  |
  _______  _$$ |_    __    __   ____$$ | __    __ $$/  _______    ______
 /       |/ $$   |  /  |  /  | /    $$ |/  |  /  |/  |/       \  /      \
/$$$$$$$/ $$$$$$/   $$ |  $$ |/$$$$$$$ |$$ |  $$ |$$ |$$$$$$$  |/$$$$$$  |
$$      \   $$ | __ $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |
 $$$$$$  |  $$ |/  |$$ \__$$ |$$ \__$$ |$$ \__$$ |$$ |$$ |  $$ |$$ \__$$ |
/     $$/   $$  $$/ $$    $$/ $$    $$ |$$    $$ |$$ |$$ |  $$ |$$    $$ |
$$$$$$$/     $$$$/   $$$$$$/   $$$$$$$/  $$$$$$$ |$$/ $$/   $$/  $$$$$$$ |
                                        /  \__$$ |              /  \__$$ |
                                        $$    $$/               $$    $$/
                                         $$$$$$/                 $$$$$$/ ''')
def rest():
    print('''                                 __
                                /  |
  ______    ______    _______  _$$ |_
 /      \  /      \  /       |/ $$   |
/$$$$$$  |/$$$$$$  |/$$$$$$$/ $$$$$$/
$$ |  $$/ $$    $$ |$$      \   $$ | __
$$ |      $$$$$$$$/  $$$$$$  |  $$ |/  |
$$ |      $$       |/     $$/   $$  $$/
$$/        $$$$$$$/ $$$$$$$/     $$$$/  ''')

#按分钟计时
def run(studyTime,interval):
    while True:
        try:
            study()
            time.sleep(studyTime*60) #就是睡指定时间
            dialog()
            print("学习暂停,进入5分钟休息时间")
            rest()
            time.sleep(interval*60)#回到循环开头
        except Exception as e:
            print(e)

if __name__ == "__main__":
    studyTime = 45
    interval = 5
    run(studyTime,interval)
