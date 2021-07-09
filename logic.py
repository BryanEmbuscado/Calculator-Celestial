from tkinter import *

class Celestial:
    def __init__(self, Cal):
        self.textbox = ""
        Cal.configure(background="gray")
        Cal.title("Celestial/Calculator")
        Cal.geometry("265x175")
        Cal.resizable(width=False , height=False)
        self.field = Entry(Cal)
        self.field.grid(columnspan=4, ipadx =70)
        self.field.insert(0, '0')
        
        #row 2
        sqrts =Button(Cal, text="√",fg='black', bg='#FF6700' , command=self.special1,height=1, width = 7)
        sqrts.grid(row=2, column=0)

        power2=Button(Cal, text="x²",fg='black', bg='#FF6700' , command=self.special2,height=1, width = 7)
        power2.grid(row=2, column=1)

        clear= Button(Cal, text='AC',fg='black', bg='#FF6700',command=self.clear, height=1, width = 7)
        clear.grid(row=2,column=2)

        clear1= Button(Cal, text='C',fg='black', bg='#FF6700',command=self.clear1, height=1, width = 7)
        clear1.grid(row=2,column=3)
    
        #row 3
        button1= Button(Cal, text='1',fg='white', bg='black',command=lambda:self.press(1), height=1, width = 7)
        button1.grid(row=3,column=0)

        button2= Button(Cal, text='2',fg='white', bg='black',command=lambda:self.press(2), height=1, width = 7)
        button2.grid(row=3,column=1)

        button3= Button(Cal, text='3',fg='white', bg='black',command=lambda:self.press(3), height=1, width = 7)
        button3.grid(row=3,column=2)

        plus= Button(Cal, text='+',fg='black', bg='#FF6700',command=lambda:self.press('+'), height=1, width = 7)
        plus.grid(row=3,column=3)
    
        #row 4

        button4= Button(Cal, text='4',fg='white', bg='black',command=lambda:self.press(4), height=1, width = 7)
        button4.grid(row=4,column=0)

        button5= Button(Cal, text='5',fg='white', bg='black',command=lambda:self.press(5), height=1, width = 7)
        button5.grid(row=4,column=1)

        button6= Button(Cal, text='6',fg='white', bg='black',command=lambda:self.press(6), height=1, width = 7)
        button6.grid(row=4,column=2)

        minus= Button(Cal, text='-',fg='black', bg='#FF6700',command=lambda:self.press('-'), height=1, width = 7)
        minus.grid(row=4,column=3)

        #row 5

        button7= Button(Cal, text='7',fg='white', bg='black',command=lambda:self.press(7), height=1, width = 7)
        button7.grid(row=5,column=0)

        button8= Button(Cal, text='8',fg='white', bg='black',command=lambda:self.press(8), height=1, width = 7)
        button8.grid(row=5,column=1)

        button9= Button(Cal, text='9',fg='white', bg='black',command=lambda:self.press(9), height=1, width = 7)
        button9.grid(row=5,column=2)

        multiply= Button(Cal, text='x',fg='black', bg='#FF6700',command=lambda:self.press('x'), height=1, width = 7)
        multiply.grid(row=5,column=3)

        #row 6

        button0= Button(Cal, text='0',fg='white', bg='black',command=lambda:self.press(0), height=1, width = 7)
        button0.grid(row=6,column=0)

        decimal= Button(Cal, text='.',fg='white', bg='black',command=lambda:self.press('.'), height=1, width = 7)
        decimal.grid(row=6,column=1)

        percent=Button(Cal, text="%",fg='white', bg='black' , command=lambda:self.press('%'),height=1, width = 7)
        percent.grid(row=6, column=2)

        divide= Button(Cal, text='÷',fg='black', bg='#FF6700',command=lambda:self.press('÷'), height=1, width = 7)
        divide.grid(row=6,column=3)

        #row 7
        equal= Button(Cal, text='=',fg='black', bg='#FF6700',command=self.equalpress, height=1, width = 35)
        equal.grid(row=7,column=0,columnspan=4)
        
    def press(self, argi: object):
        self.textbox= self.field.get()
        if self.textbox[0] == '0':
            self.field.delete(0, 1)
        self.field.insert(END, argi)
    

    def equalpress(self):
        try:
            self.textbox = self.field.get()
            self.textbox = self.textbox.replace('÷', '/')
            self.textbox = self.textbox.replace('x', '*')
            self.textbox = self.textbox.replace('%', '/100')
            self.textbox = str(eval(self.textbox))

        except:
            self.textbox = ('SyntaxError')
        
        self.refresh()
        
    def special1(self):
        self.textbox = self.field.get()
        try:
            self.textbox = str((float(self.textbox))**0.5)
        except:
            self.textbox = ('ValueError')
            
        self.refresh()
        
    def special2(self):
        self.textbox = self.field.get()
        try:
            self.textbox = str((float(self.textbox))**2)
        except:
            self.textbox = ('ValueError')
        
        self.refresh()
        
    def refresh(self):  
        self.field.delete(0, END)
        self.field.insert(0, self.textbox)

    def clear(self): 
        self.field.delete(0, END)
        self.field.insert(0, '0')

    def clear1(self):
        self.textbox = self.field.get()
        self.textbox = self.textbox[:-1] 
        
        self.refresh()
class Logic():
    def __init__(self):
    # Frame of the calculator
        self.input = ""
        self.input.replace('÷', '/')
        self.input.replace('x', '*')
        self.input.replace('%', '/100')
        

    def Calculate(self):
        
        try:
            self.answer = eval(self.input)
            return self.answer

        except SyntaxError as e:
            
            return "Syntax Error"

        except ZeroDivisionError:
            return "Zero Division Error"
            
        except OverflowError:
            return "Math Error"       

Cal = Tk()
obj = Celestial(Cal)
Cal.mainloop()