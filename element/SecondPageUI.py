import tkinter as tk
from PIL import Image, ImageTk

win=tk.Tk()
win.title("The GUI")
win.geometry("400x650")
win.wm_attributes('-topmost',1)
basewidth = 300
img_open = Image.open('C:/Users/Nicholas/Desktop/Desk_tmp/1920x1080-Wallpaper-1.jpg')
img_open.save('1920x1080-Wallpaper-1.jpg') 
img_png = ImageTk.PhotoImage(img_open)
tk.Label().pack()
tk.Label().pack()
label_img = tk.Label(image = img_png).pack(side="top")
tk.Label().pack()
tk.Label().pack()
frm = tk.Frame(win)
frm.pack()
frm_left = tk.Frame(frm,)
frm_right = tk.Frame(frm)
frm_left.pack(side="left")
frm_right.pack(side="right")
tk.Label(frm_left,font=('Arial',12),width=15,height=3,text="Item Name:").pack()
tk.Label(frm_left,font=('Arial',12),width=15,height=3,text="Height:").pack()
tk.Label(frm_left,font=('Arial',12),width=15,height=3,text="Width:").pack()
tk.Label(frm_right,font=('Arial',12),width=15,height=3,text="Item Name here").pack()
tk.Label(frm_right,font=('Arial',12),width=15,height=3,text="Height here").pack()
tk.Label(frm_right,font=('Arial',12),width=15,height=3,text="Width here").pack()
win.mainloop()