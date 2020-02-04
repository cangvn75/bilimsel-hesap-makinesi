from .base import BaseOperator
import numpy as np

class Vector2dOperator(BaseOperator):
    def __init__(self):
        pass
    def add(self,val1,val2):
        if len(val1)==len(val2) and len(val1[0])==len(val2[0]):
            return np.add(val1,val2)
    def substract(self,val1,val2):
        if len(val1)==len(val2) and len(val1[0])==len(val2[0]):
            return np.subtract(val1,val2)
    def divide(self,val1,val2):
        if not isinstance(val1,list) or not isinstance(val2,list):
            return np.divide(val1,val2)
    def multiply(self,val1,val2):
        if not isinstance(val1,list) or not isinstance(val2,list):
            return np.multiply(val1,val2)
        elif(len(val1)==len(val2[0]) or len(val2)==len(val1[0])):
            return np.dot(val1,val2)
class Vector2dFunctions:
    def __init__(self):
        self.functions = {
            "mean":self.mean,
            "std":self.std,
            "median":self.median,
            "max":self.maxOfMatrix,
            "min":self.minOfMatrix,
            "sum":self.sumOfElements,
            "inv":self.inv,
            "T":self.transpoz,
            "det":self.determinant
        }
    def mean(self,val):
        return np.mean(val)
    def std(self,val):
        return np.std(val)
    def median(self,val):
        return np.median(val)
    def maxOfMatrix(self,val):
        return np.amax(val)
    def minOfMatrix(self,val):
        return np.amin(val)
    def sumOfElements(self,val):
        return np.sum(val)
    def inv(self,val):
        return np.linalg.inv(val)
    def transpoz(self,val):
        return np.transpose(val)
    def determinant(self,val):
        return np.linalg.det((val))