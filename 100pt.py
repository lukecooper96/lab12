#########################################
#
#         100pt - Working with Canvas
#
#########################################



from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=480,height=320, background='white')
oval = drawpad.create_oval(160,160,320,320, fill="red")

class MyApp:
	def __init__(self, parent):
	
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="Left", background= "green")
		self.button1.grid(row=0,column=0)
		self.button1.bind("<Button-1>", self.button1Click)
	     
	        #button 2
		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="Right", background= "yellow")
		self.button2.grid(row=0,column=1)
		self.button2.bind("<Button-1>", self.button2Click)
		
		#button 3
		self.button3 = Button(self.myContainer1)
		self.button3.configure(text="up", background= "blue")
		self.button3.grid(row=0,column=2)
		self.button3.bind("<Button-1>", self.button3Click)	
		
		#button 4
		self.button4 = Button(self.myContainer1)
		self.button4.configure(text="down", background= "magenta")
		self.button4.grid(row=0,column=3)
		self.button4.bind("<Button-1>", self.button4Click)			
		
																
		self.button1.bind("<Button-1>", self.button1Click)
	
	
		drawpad.pack()
		

		
	def button1Click(self, event):   
		global oval
		global drawpad
		drawpad.move(oval,-25,0)
	#button 2	
	def button2Click(self, event):
	    global oval
	    global drawpad
	    drawpad.move(oval,25,0)
	#button 3
	def button3Click(self, event):
	    global oval
	    global drawpad
	    drawpad.move(oval,0,-10)
	#button 4
	def button4Click(self, event):
	    global oval
	    global drawpad
	    drawpad.move(oval,0,10)
	
	
	
		
myapp = MyApp(root)
root.mainloop()


	
	



	
	
		
myapp = MyApp(root)
root.mainloop()