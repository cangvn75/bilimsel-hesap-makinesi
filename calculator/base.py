class FunctionManager:
    
    def __init__(self,solver):
        self.solver = solver
    def solve(self, val, func):
        return self.solver.functions[func](val)


class OperatorManager:
    
    def __init__(self,solver):

        self.operators = {
            # how to fill those operators
            '+':solver.add,
            '-':solver.substract,
            '*':solver.multiply,
            '/':solver.divide
        }

    def solve(self, val1, val2, op):
        # assert (not op in self.operators.keys()), "You can't solve anything with paranthesis !"
        return self.operators[op](val1,val2)


class BaseOperator:

    def __init__(self):
        # configure operators
        self.name = "Operator"


    def add(self,*args):
        raise NotImplementedError

    def substract(self,*args):
        raise NotImplementedError

    def multiply(self,*args):
        raise NotImplementedError

    def divide(self,*args):
        raise NotImplementedError



# class Formula:
#     def __init__(self,*args):
#         super().__init__()
#         self.variables, self.operators = tokenize(*args)

#     def tokenize(self,*args):
#         pass

