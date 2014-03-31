from Tkinter import Tk,BOTH,Frame,Canvas,PhotoImage,NW,NO
from ttk import Button, Style
from PIL import Image
from fer import FER
import tkFileDialog
import os

class FacialExpressionApp(Frame):

	def __init__(self,parent):
		Frame.__init__(self,parent,background = "white")
		self.reference = None
		self.parent = parent
		self.pixel_list = []
		self.recognizer = FER()
		self.center_window()
		self.initUI()
		
	def center_window(self):
		w,h = 300,200
		sw,sh = self.parent.winfo_screenwidth(),self.parent.winfo_screenheight()

		x = (sw - w)/2
		y = (sh - h)/2
		self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

	def initUI(self):
		self.parent.title("Facial Expression Recognizer")
		self.style = Style()
		self.style.theme_use("default")
		self.pack(fill=BOTH, expand=1)

		self.file_opt = options = {}
		options['defaultextension'] = '.txt'
		options['filetypes'] = [('all files', '.*'),('JPG', '.jpg'),('GIF','.gif'),('PNG','.png')]
		options['initialdir'] = ''
		options['initialfile'] = ''
		options['parent'] = self.parent
		options['title'] = 'Choose 48x48 Grayscale Image...'

		mycolor = '#f7f7f7'

		self.canvas = Canvas(self,width = 50, height = 150, bd = 3,bg = mycolor)
		self.canvas.pack(expand = NO, fill = BOTH)

		self.canvas_id1 = self.canvas.create_text(10, 10, anchor="nw")
		self.canvas.itemconfig(self.canvas_id1, text="Hello, Are you happy?")

		self.canvas_id2 = self.canvas.create_text(145, 100, anchor="nw")
		self.canvas.itemconfig(self.canvas_id2, text="...")

		x = Image.open('default.png')
		self.draw_image(x)

		loadButton = Button(self, text="Load",command=self.load_image)
		loadButton.place(x=115, y=165)

		runButton = Button(self, text="Run",command=self.classify)
		runButton.place(x=205, y=165)

	def draw_image(self,img):
		img.save('default.gif')
		photo = PhotoImage(file = "default.gif")
		self.reference = photo
		self.photo_id = self.canvas.create_image(125, 45, image = photo, anchor = NW) 

	def load_image(self):
		img_file = tkFileDialog.askopenfile(mode='r', **self.file_opt)
		abs_path = os.path.abspath(img_file.name)
		img = Image.open(abs_path)
		self.pixel_list = []

		self.draw_image(img)

		img = img.convert("L")
		pixels = img.load()

		for i in range(48):
			for j in range(48):
				self.pixel_list.append(pixels[j,i])

	def classify(self):
		if len(self.pixel_list) == 0 or self.pixel_list is None:
			strng = "Not sure. Load your image."
			x = 80
		else:
			if self.recognizer.predict(self.pixel_list) == 1:
				strng = "Indeed, you are happy!"
				x = 90
			else:
				strng = "Nope. You are not."
				x = 100

		self.canvas.coords(self.canvas_id2,(x,100))
		self.canvas.itemconfig(self.canvas_id2, text = strng)


if __name__ == "__main__":
    root = Tk()
    app = FacialExpressionApp(root)
    root.mainloop()


