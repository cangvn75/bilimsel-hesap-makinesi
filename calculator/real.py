from .base import BaseOperator
import math

class RealOperator(BaseOperator):
    def __init__(self):
        super().__init__()
        
    def add(self,val1,val2):
        return val1+val2
    def substract(self,val1,val2):
        return val1-val2
    def divide(self,val1,val2):
        return val1/val2
    def multiply(self,val1,val2):
        return val1*val2
   
class RealFunctions:
    def __init__(self):
        self.functions = {
            "sin":self.sin,
            "cos":self.cos,
            "tan":self.tan,
            "cot":self.cot,
            "n!":self.factorial,
            "ln":self.ln,
            "|x|":self.fabs,
            "2^x":self.xPowerOfTwo,
            "x^2":self.twoPowerOfx,
            "1/x":self.oneDivideToX,
            "exp":self.exp,
            "x^3":self.threePowerOfx,
            "10^x":self.xPowerOfTen,
        }
    def sin(self,val):
        return math.sin(val)
    def cos(self,val):
        return math.cos(val)
    def tan(self,val):
        return math.tan(val)
    def cot(self,val):
        return math.cos(val)/math.sin(val)
    def factorial(self,val):
        return math.factorial(val)
    def ln(self,val):
        return math.log1p(val)
    def fabs(self,val):
        return math.fabs(val)
    def xPowerOfTwo(self,val):
        return math.pow(2,val)
    def twoPowerOfx(self,val):
        return math.pow(val,2)
    def oneDivideToX(self,val):
        return 1/val
    def exp(self,val):
        return math.exp(val)
    def threePowerOfx(self,val):
        return math.pow(val,3)
    def xPowerOfTen(self,val):
        return math.pow(10,val)