import tkinter as tk
from tkinter import filedialog
import os

string_filename = ''

window = tk.Tk()
window.title('my window')
window.geometry('350x550')

next1 = tk.Label()
next1.pack() 
next2 = tk.Label()
next2.pack() 
next3 = tk.Label()
next3.pack() 

l = tk.Label(window, 
    text='Hello! Welcome to here!',    # 标签的文字
    bg='White',     # 背景颜色
    font=('Arial', 12),     # 字体和字体大小
    width=30, height=13  # 标签长宽
    )
l.pack()    # 固定窗口位置

next4 = tk.Label()
next4.pack() 
next5 = tk.Label()
next5.pack() 
next6 = tk.Label()
next6.pack() 
next7 = tk.Label()
next7.pack() 



root = None
on_hit = False  # 默认初始状态为 False
def hit_me():
    global on_hit
    global string_filename
    if on_hit == False:     # 从 False 状态变成 True 状态
        on_hit = True
        string_filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        print(1,string_filename)
        path = tk.Label(
		    text = string_filename,    # 标签的文字
		    font=('Arial', 12),     # 字体和字体大小
		    )
        path.pack() 
        print(2,string_filename)
        return string_filename

        #file_path = filedialog.askopenfilename()
  		#设置标签的文字为 'you hit me'
print(3,string_filename)
b = tk.Button(window, 
    text='hit me',      # 显示在按钮上的文字
    width=15, height=2, 
    command=hit_me)     # 点击按钮式执行的命令
b.pack()    # 按钮位置
print(4,string_filename)
window.mainloop()
print(5,string_filename)
