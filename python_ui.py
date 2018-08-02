import tkinter as tk
from tkinter import filedialog
string_filename = ''
# Call WIndow
window = tk.Tk()
window.title('my window')
window.geometry('350x550')

# Create Space
next1 = tk.Label()
next1.pack() 
next2 = tk.Label()
next2.pack() 
next3 = tk.Label()
next3.pack() 

#Title
l = tk.Label(window, 
    text='Hello! Welcome to here!',    # 标签的文字
    bg='White',     # 背景颜色
    font=('Arial', 12),     # 字体和字体大小
    width=30, height=13  # 标签长宽
    )
l.pack()    # 固定窗口位置

# Onclick Function
def hit_me():
    global string_filename  #Call Global Var
    # Get file path
    string_filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    # show path
  

b = tk.Button(window, 
    text='hit me',      # 显示在按钮上的文字
    width=15, height=2, 
    command=hit_me)     # 点击按钮式执行的命令
b.pack()    # 按钮位置

path = tk.Label(
    text = string_filename,    # 标签的文字
    font=('Arial', 12),     # 字体和字体大小
    )
path.pack() 

def call_api():
    pass
c = tk.Button(window,
    text='submit',
    width=15, height=2,
    command=call_api)
c.pack()

window.mainloop()
