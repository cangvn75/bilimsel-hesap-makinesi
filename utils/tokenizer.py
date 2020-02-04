from .component import *
import sys
sys.path.append("..")
from calculator.real import RealOperator,RealFunctions
from calculator.vector1d import Vector1dOperator,Vector1dFunctions
from calculator.vector2d import Vector2dOperator,Vector2dFunctions
from calculator.base import OperatorManager,FunctionManager

def xxsolver(content,op_solver, fun_solver):
    valStack = []
    opStack = []
    op_manager = OperatorManager(op_solver)
    fun_manager = FunctionManager(fun_solver)
    for item in content:
        if(isinstance(item,ComponentValue)):
            valStack.append(item.val)
        elif(isinstance(item,ComponentFunction)):
            funcVal = xxsolver(item.expression,op_solver,fun_solver)
            valStack.append(fun_manager.solve(funcVal,item.fun))
        elif(isinstance(item,ComponentParanthesis)):
            if(item.paranthesis== ComponentParanthesis._start):
                opStack.append(item.paranthesis)
            else:
                while opStack[-1]!=ComponentParanthesis._start:
                    op = opStack.pop()
                    rightVal = valStack.pop()
                    leftVal = valStack.pop()
                    valStack.append(op_manager.solve(leftVal,rightVal,op))
                opStack.pop()
        elif(isinstance(item,ComponentOperator)):
            while len(opStack)>0 and ComponentOperator(opStack[-1]).precedence()>=item.precedence():
                op = opStack.pop()
                rightVal = valStack.pop()
                leftVal = valStack.pop()
                valStack.append(op_manager.solve(leftVal,rightVal,op))
            opStack.append(item.op)
        
    while len(opStack)>0:
        op = opStack.pop()
        rightVal = valStack.pop()
        leftVal = valStack.pop()
        valStack.append(op_manager.solve(leftVal,rightVal,op))
    return valStack.pop()

class Tokenizer:
    
    def __init__(self,tType):

        self.tokenizer_type = tType

        self.solvers = {
            "real":RealOperator(),
            "vec1":Vector1dOperator(),
            "vec2":Vector2dOperator()
        }
        self.fun_solvers = {
            "real":RealFunctions(),
            "vec1":Vector1dFunctions(),
            "vec2":Vector2dFunctions()
        }

    def tokenize(self,content):
        # Maybe do some controls here.
        solver = self.solvers[self.tokenizer_type]
        fun_solver = self.fun_solvers[self.tokenizer_type]
        func = xxsolver
        return func(content,solver,fun_solver)
