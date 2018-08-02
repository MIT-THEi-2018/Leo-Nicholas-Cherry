import tkinter as tk
from PIL import Image, ImageTk

win=tk.Tk()
win.title("The GUI")
windowWidth = 400
windowHeight = 700
win.geometry(geometryParam)
win.wm_attributes('-topmost',1)
img_open = Image.open('Anthem.jpg')
img_png = ImageTk.PhotoImage(img_open)
label_img = tk.Label(image = img_png)
labe2_word= tk.Label(win, text='Hello World!')

label_img.pack()
labe2_word.pack() 
win.mainloop()