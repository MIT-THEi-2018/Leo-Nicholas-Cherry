import tkinter as tk
from tkinter import filedialog
from tkinter import *
from clarifai.rest import ClarifaiApp
from clarifai.rest.client import Image as ClImg
import pprint
from PIL import Image, ImageTk

app = ClarifaiApp(api_key='c0da642111c24a63b1988e0d14f30c71')
model = app.models.get('general-v1.3')
string_filename = ''
# Call WIndow
window = tk.Tk()
window.title('Tidy Home')
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
    text='Hello! Welcome to Tidy Home !',    # 标签的文字
    bg='White',     # 背景颜色
    font=('Arial', 12),     # 字体和字体大小
    width=30, height=13  # 标签长宽
    )
l.pack()    # 固定窗口位置

# Onclick Function
def hit_me():
    global string_filename  #Call Global Var
    # Get file path
    string_filename = filedialog.askopenfilename(initialdir = "/",
        title = "Select file",
        filetypes = (("jpeg files",".jpg"),("all files",".*")))
    # show path
    path = tk.Label(
    text = string_filename,    # 标签的文字
    font=('Arial', 7),     # 字体和字体大小
    )
    path.pack()
  
b = tk.Button(window, 
    text='Select Image',      # 显示在按钮上的文字
    width=15, height=2, 
    command=hit_me)     # 点击按钮式执行的命令
b.pack()    # 按钮位置

def call_api():
    image = ClImg(file_obj=open(string_filename, 'rb'))
    #output is a dictionary
    result = model.predict([image])
    #data is a list
    datas = result['outputs']
    outputs = datas[0]
    concepts = outputs['data']
    data = concepts['concepts']
    target = data[0]
    #
    win=tk.Toplevel(window)
    win.title("Information")
    win.geometry("400x650")
    win.wm_attributes('-topmost',1)
    basewidth = 300
    frm = tk.Frame(win)
    frm.pack(side="top")
    frm_left = tk.Frame(frm,)
    frm_right = tk.Frame(frm)
    frm_left.pack(side="left")
    frm_right.pack(side="right")
    img_open = Image.open(string_filename)
    img_open= img_open.resize((400,300), Image.ANTIALIAS)
    img_open.save(string_filename) 
    img_png = ImageTk.PhotoImage(img_open)
    tk.Label(frm_left,image = img_png,width=400,height=300).pack()
    tk.Label(frm_left,font=('Arial',12),width=15,height=3,text="Item Name:  "+target['name']).pack()
    tk.Label(frm_left,font=('Arial',12),width=15,height=3,text="Height:"+"").pack()
    tk.Label(frm_left,font=('Arial',12),width=15,height=3,text="Width:"+"").pack()
    tk.Label(frm_left,font=('Arial',12),width=15,height=3,text="Place:"+"").pack()

    win.mainloop()

c = tk.Button(window,
    text='submit',
    width=15, height=2,
    command=call_api)
c.pack()

window.mainloop()
