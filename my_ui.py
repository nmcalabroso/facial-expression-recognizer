from Tkinter import Tk,BOTH
from Tkinter import Frame
from ttk import Button, Style
from PIL import Image
import tkFileDialog

class FacialExpressionApp(Frame):

	def __init__(self,parent):
		Frame.__init__(self,parent,background = "white")
		self.parent = parent
		self.center_window()
		self.initUI()
		
	def center_window(self):
		w,h = 400,300
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
		
		loadButton = Button(self, text="Load",command=self.load_image)
		loadButton.place(x=215, y=265)

		runButton = Button(self, text="Run",command=self.classify)
		runButton.place(x=305, y=265)

	def load_image(self):
		img = tkFileDialog.askopenfile(mode='r', **self.file_opt)
		print img.tell()
		#img = img.convert("L")
		"""pixels = img.load()
		pixel_list = []
		for i in range(48):
			for j in range(48):
				pixel_list.append(pixels[i,j])

		return pixel_list #returns a list of pixels with size 2304(or 48*48)

		photo = ImageTk.PhotoImage(image)"""

	def classify(self):
		pass

if __name__ == "__main__":
	#main()
    root = Tk()
    app = FacialExpressionApp(root)
    root.mainloop()


