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
    for i in sys.argv:
        print(i)
    studyTime = 25
    interval = 5
    run(studyTime,interval)
