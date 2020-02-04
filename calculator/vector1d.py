from .base import BaseOperator
import numpy as np

class Vector1dOperator(BaseOperator):
    def __init__(self):
        super().__init__()
    def add(self,val1,val2):
        if(len(val1)==len(val2)):
            return np.add(val1,val2)
    def substract(self,val1,val2):
        if(len(val1)==len(val2)):
            return np.subtract(val1,val2)
    def divide(self,val1,val2):
        if not isinstance(val1,list) or not isinstance(val2,list):
            return np.divide(val1,val2)
    def multiply(self,val1,val2):
        if not isinstance(val1,list) or not isinstance(val2,list):
            return np.multiply(val1,val2)
        elif (len(val1)==1 or len(val2)==1) or (len(val1)==len(val2)):
            return np.multiply(val1,val2)

class Vector1dFunctions:
    def __init__(self):
        self.functions = {
            "median":self.median,
            "mod":self.mod,
            "max":self.maxOfMatrix,
            "min":self.minOfMatrix,
            "sum":self.sumOfElements,
        }
    def median(self,val):
        return np.median(val)
    def mod(self,val):
        bincount = np.bincount(val)
        return np.argmax(bincount)
    def maxOfMatrix(self,val):
        return np.amax(val)
    def minOfMatrix(self,val):
        return np.amin(val)
    def sumOfElements(self,val):
        return np.sum(val)