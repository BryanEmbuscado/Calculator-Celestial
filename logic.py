class Logic():
    def __init__(self):
    # Frame of the calculator
        self.textbox = ""

    def Calculate(self):
        try:
            self.textbox = self.textbox.replace('÷', '/')
            self.textbox = self.textbox.replace('x', '*')
            self.textbox = self.textbox.replace('%', '/100')
            self.answer = eval(self.textbox)
            return self.answer

        except SyntaxError as e:
            
            return "Syntax Error"

        except ZeroDivisionError:
            return "Zero Division Error"
            
        except OverflowError:
            return "Math Error"       
    def special1(self):
        self.answer =((float(eval(self.textbox)))**0.5)
        return self.answer

    def special2(self):
        self.answer =((float(eval(self.textbox)))**2)
        return self.answer
