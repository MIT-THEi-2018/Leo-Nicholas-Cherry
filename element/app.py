import tkinter as tk
from tkinter import filedialog
from clarifai.rest import ClarifaiApp
from clarifai.rest.client import Image as ClImg
import pprint
from PIL import Image, ImageTk
from tkinter import font  as tkfont # python 3

string_filename = ''
obj = ''
app = ClarifaiApp(api_key='9d1135521f834d35969e93e8b94fb624')
model = app.models.get('general-v1.3')
def action01():
	hit_me()
	call_api()
	information(string_filename)

def hit_me():
	global string_filename
	string_filename = filedialog.askopenfilename(initialdir = "/",
	        title = "Select file",
	        filetypes = (("jpeg files",".jpg"),("all files",".*")))
	path = tk.Label(text = string_filename,    # 标签的文字
			font=('Arial', 7),     # 字体和字体大小
		)
	path.pack()

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
    global obj 
    obj = target['name']

def information(string_filename):
	win=tk.Tk()
	win.title("The GUI")
	win.geometry("400x650")
	win.wm_attributes('-topmost',1)
	basewidth = 300
	tk.Label().pack()
	tk.Label().pack()	
	img_open = Image.open(string_filename)
	img_open.save(string_filename)
	img_png = ImageTk.PhotoImage(img_open)
	label_img = tk.Label(image = img_png).pack(side="top")
	tk.Label().pack()
	tk.Label().pack()
	frm = tk.Frame(win)
	frm.pack()
	frm_left = tk.Frame(frm,)
	frm_right = tk.Frame(frm)
	tk.Label(frm_left,font=('Arial',12),width=15,height=3,text="Item Name:").pack()
	tk.Label(frm_left,font=('Arial',12),width=15,height=3,text="Height:").pack()
	tk.Label(frm_left,font=('Arial',12),width=15,height=3,text="Width:").pack()
	tk.Label(frm_right,font=('Arial',12),width=15,height=3,text="Item Name here").pack()
	tk.Label(frm_right,font=('Arial',12),width=15,height=3,text="Height here").pack()
	tk.Label(frm_right,font=('Arial',12),width=15,height=3,text="Width here").pack()
	win.mainloop()

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text='Hello! Welcome to here!',bg='White',font=('Arial', 12),width=30, height=13)
        label.pack(side="top", fill="x", pady=10)
        input_button = tk.Button(self,text='Select',width=15, height=2,command=action01)
        button1 = tk.Button(self, text="Submit",width=15, height=2,
                            command=lambda: controller.show_frame("PageOne"))
        input_button.pack()
        button1.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=obj, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()