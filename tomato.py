<<<<<<< HEAD
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
    print('''
                                 _oo0oo_
                                088888880
                                88" . "88
                                (| -_- |)
                                 0\ = /0
                              ___/'---'\___
                            .' \\\\|     |// '.
                           / \\\\|||  :  |||// \\
                          /_ ||||| -:- |||||- \\
                         |   | \\\\\\  -  /// |   |
                          | \_|  ''\---/''  |_/ |
                          \  .-\__  '-'  __/-.  /
                         ___'. .'  /--.--\  '. .'___
                      ."" '<  '.___\_<|>_/___.' >'  "".
                     | | : '-  \'.;'\ _ /';.'/ - ' : | |
                     \  \ '_.   \_ __\ /__ _/   .-' /  /
                 ====='-.____'.___ \_____/___.-'____.-'=====
                                   '=---='

               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                        闭关修炼    iii    法力无边
    ''')
def rest():
    print('''
                                                 __
                                                /  |
                  ______    ______    _______  _$$ |_
                 /      \  /      \  /       |/ $$   |
                /$$$$$$  |/$$$$$$  |/$$$$$$$/ $$$$$$/
                $$ |  $$/ $$    $$ |$$      \   $$ | __
                $$ |      $$$$$$$$/  $$$$$$  |  $$ |/  |
                $$ |      $$       |/     $$/   $$  $$/
                $$/        $$$$$$$/ $$$$$$$/     $$$$/

    ''')

=======
#!/usr/bin/python
#encoding:utf-8
import tkinter as tk
import tkinter.messagebox
import time
import sys

def dialog(studyTime, interval):
    studyTime = str(studyTime)
    interval  = str(interval)
    root = tk.Tk()
    root.withdraw()
    confirm = tk.messagebox.showinfo(title = '番茄时钟提示', message = studyTime + '分钟过去了，休息' + interval + '分钟一下吧！')
    if (confirm == "ok"):
        root.destroy()	

def study():
    print(''' 
                   | |  (_)             
__      _____  _ __| | ___ _ __   __ _  
\ \ /\ / / _ \| '__| |/ / | '_ \ / _` | 
 \ V  V / (_) | |  |   <| | | | | (_| | 
  \_/\_/ \___/|_|  |_|\_\_|_| |_|\__, | 
                                  __/ | 
                                 |___/  
 ''')
def rest():
    print(''' 
               | |  
  _ __ ___  ___| |_ 
 | '__/ _ \/ __| __|
 | | |  __/\__ \ |_ 
 |_|  \___||___/\__|
 
 ''')
 
>>>>>>> 6057d1cd499376b1ef1d4b808e8c455bffb27991
#按分钟计时
def run(studyTime,interval):
    if len(sys.argv) == 3:
        studyTime = float(sys.argv[1])
        interval  = float(sys.argv[2])
    while True:
        try:
            study()
            time.sleep(studyTime*60) #就是睡指定时间
            dialog(studyTime,interval)
            print("工作暂停,进入休息时间")
            rest()
            time.sleep(interval*60)#回到循环开头
        except Exception as e:
            print(e)

if __name__ == "__main__":
<<<<<<< HEAD
    studyTime = 45
=======
    for i in sys.argv:
        print(i)
    studyTime = 25
>>>>>>> 6057d1cd499376b1ef1d4b808e8c455bffb27991
    interval = 5
    run(studyTime,interval)
