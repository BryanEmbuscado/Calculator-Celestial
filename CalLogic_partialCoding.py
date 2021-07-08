from tkinter import Tk
import math

class Celestial:
    def enterVal(self, argi: object):
        self.textbox = self.op.get()
        
        if self.textbox[0] == '0':
            self.op.delete(0, 1)
        self.op.insert(END, argi)
    
    def operation(self):
        try:
            self.textbox = self.op.get()
            self.textbox = self.textboxreplace('÷', '/')
            self.textbox = self.textbox.replace('x', '*')
            self.textbox = self.textbox.replace('%', '/100')
            self.textbox = self.textbox.replace('π', '3.14')
            self.textbox = str(eval(self.textbox))

        except:
            self.textbox = ('SyntaxError')
        
        self.refresh()
        
    def pi(self):
	self.textbox = self.op.get()
	
        try:
            self.eval = math.pi(str(eval(self.textbox)))
            self.textbox = str(float(self.eval))
		
        except:
            self.textbox = ('SyntaxError')
	
	self.refresh()
        
    def op1(self):
	self.textbox = self.op.get()
	
        try:
            self.eval = self.textbox **(0.5)
            self.textbox = str(float(self.eval))
		
        except:
            self.textbox = ('Error')
	
	self.refresh() 
	
    def op2(self):
	self.textbox = self.op.get() 
	
        try:
            self.eval = self.textbox **(2) 
            self.textbox = str(float(self.eval)) 
		
        except:
            self.textbox = ('Error') 
	
	self.refresh()

root = Tk() 
root.mainloop()
