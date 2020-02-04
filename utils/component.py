
"""
---------------------
[3, +, sin(120)]
[<class ComponentValue>, <class ComponentOperator>, <class ComponentFunction>]
if isinstance(ComponentValue):
    a = comp.value -> ([1,2,3,4],53,[[1,2],[2,3]],5+3i)
    Operator(comp.type).compute(val1,val2) -> 'complex','vector','real'

ComponentFunction('sin','3+5*20') -> basic
    comp.expression = comp.resolve(comp.expression)
    funcManager.solve(comp.func,comp.expression)
ComponentFunction('mod',['5','7']) -> advanced
ComponentFunction('x^y',[5,3]) -> advanced = 125

"""

class ComponentFunction:
    
    def __init__(self,fun,val):
        self.fun = fun
        self.expression = []

        self.finito = False
        # One param functions 
        # example : sin(x), cos(x), abs(x)
        self.type = "basic"

        # Multi param functions
        # example : x^y, modx,y ..
        if type(self.expression) == list: self.type = "advanced"

   
    def update(self,val):
        self.expression.append(val)

    def close(self):
        self.finito = True

    def __str__(self):
        ex = ""
        for i in self.expression: ex+=str(i)
        if not self.finito:
            return "{0}({1}".format(self.fun,ex)
        else:
            return "{0}({1})".format(self.fun,ex)
        # if self.type =="basic": return "{0}({1})".format(self.fun,self.expression)

class ComponentParanthesis:

    _start = '('
    _end = ')'

    def __init__(self,paranthesis):
        self.paranthesis = paranthesis

    def __str__(self):
        return self.paranthesis
            

class ComponentOperator:

    _add = '+'
    _mul = '*'
    _sub = '-'
    _div = '/'
    
    def __init__(self,op):
        self.op = op
    
    def precedence(self):
        if self.op == ComponentOperator._add or self.op == ComponentOperator._sub:
            return 1
        elif self.op == ComponentOperator._mul or self.op == ComponentOperator._div:
            return 2
        return 0

    def __len__(self):
        return 1

    def __str__(self):
        return self.op

def conversion(val):
    if str(val).find(",")!=-1:
        return list(val) 
    elif str(val).find(".")==-1:
        return int(val)
    return float(val)

class ComponentValue:

    _pi = (22/7)
    _e = (10) 
    
    def __init__(self,val):

        # Get value as integer or float.
        # You have to declare it here.

        self.val = conversion(val)
        self.special_val = [ComponentValue._pi,ComponentValue._e]

        self.type = "basic"
        if val in self.special_val: self.type = "special"

    def update(self,val):
        self.val = val


    def __len__(self):
        return len(str(self.val))

    def __str__(self):
        return str(self.val)

class ComponentController:

    def createFunctionComponent(self,fun,val):
        return ComponentFunction(fun,val)

    def createOperatorComponent(self,op):
        return ComponentOperator(op)

    def createValueComponent(self,val):
        return ComponentValue(val)

    def createParanthesisComponent(self,paranthesis):
        return ComponentParanthesis(paranthesis)
    

class InputController:

    """
    write wrapper class for controlling display bigger than length > 0 otherwise it shows error.

    @control_display
    """
    
    def __init__(self,ttype = "Scientific"):

        self.open_paranthesis = 0
        self.display = []
        self.compController = ComponentController()
        self.ttype = ttype
        self.isFunction = False

    def typeFunction(self,func, expression):
        if len(self.display)>0 and (isinstance(self.display[-1],ComponentOperator) or str(self.display[-1]) == ComponentParanthesis._start) : 
            self.display.append(self.compController.createFunctionComponent(func, expression))
            self.isFunction = True
        elif len(self.display)==0:
            self.display.append(self.compController.createFunctionComponent(func,expression))
            self.isFunction = True
    def negatiate(self):
        if len(self.display)>0 and isinstance(self.display[-1],ComponentValue):
            return self.display[-1].update(conversion(str(self.display[-1]))*-1)

    def typeValue(self,val):
        """
        Right now this method needs to control stack.
        if last add element is a ComponentValue, delete last element frorm stack.
        After deleting update the value of it then add to stack.
        """
        if self.isFunction:
            if len(self.display[-1].expression)>0 and isinstance(self.display[-1].expression[-1],ComponentValue):            
                curr_value = self.display[-1].expression[-1] # Takes object reference
                if not isinstance(curr_value.val,list):
                    curr_value.update(conversion(str(curr_value)+val))
                # self.display[-1].update(int(str(self.display[-1])+val))
            else: self.display[-1].expression.append(self.compController.createValueComponent(val))
        else:
            if len(self.display)>0 and isinstance(self.display[-1],ComponentValue):            
                curr_value = self.display[-1] # Takes object reference
                if not isinstance(curr_value.val,list):
                    curr_value.update(conversion(str(curr_value)+val))
                # self.display[-1].update(int(str(self.display[-1])+val))
            elif len(self.display)>0 and str(self.display[-1])==ComponentParanthesis._end: pass
            else: self.display.append(self.compController.createValueComponent(val))
        
    def typeDot(self):
        if self.isFunction:
            if len(self.display[-1].expression)>0 and isinstance(self.display[-1].expression[-1],ComponentValue):
                checkval = self.display[-1].expression[-1]
                if isinstance(conversion(checkval),int):
                    val = str(self.display[-1].expression[-1]+".")
                    self.display[-1].expression[-1].update(val)

        else:
            if len(self.display)>0 and isinstance(self.display[-1],ComponentValue):
                checkval = str(self.display[-1])
                if isinstance(conversion(checkval),int):
                    self.display[-1].update(str(self.display[-1])+".")

    def typeOperator(self,op):
        if self.isFunction:
            if len(self.display[-1].expression)>0 and not isinstance(self.display[-1].expression[-1],ComponentOperator): 
                self.display[-1].expression.append(self.compController.createOperatorComponent(op))
        else:
            if len(self.display)>0 and not isinstance(self.display[-1],ComponentOperator) and str(self.display[-1])!=ComponentParanthesis._start: self.display.append(self.compController.createOperatorComponent(op))
        
    def typeParanthesis(self,paranthesis):
        if self.isFunction:
            if paranthesis == ')': 
                self.display[-1].close()
                self.isFunction = False
        else:
            if paranthesis == ComponentParanthesis._start and len(self.display) ==0: 
                self.open_paranthesis += 1
                self.display.append(self.compController.createParanthesisComponent(paranthesis))
            elif paranthesis == ComponentParanthesis._start and len(self.display)>0 and isinstance(self.display[-1],ComponentOperator):
                self.open_paranthesis += 1
                self.display.append(self.compController.createParanthesisComponent(paranthesis))
            elif paranthesis == ComponentParanthesis._end and len(self.display)>0 and self.open_paranthesis>0 and not isinstance(self.display[-1],ComponentOperator):
                self.open_paranthesis -= 1
                self.display.append(self.compController.createParanthesisComponent(paranthesis))


    def getDisplayValue(self):
        display_val = ""
        for i in self.display: display_val+= str(i)
        return display_val

    def typeBackspace(self):
        """
        If you are deleting a number wwith backspace
        321 -> it doesnt matter 32->3 -- you can delete like this
        but if you are deleting a function, that means you have to delete all
        """
        if self.isFunction:
            if len(self.display[-1].expression)>0 and isinstance(self.display[-1].expression[-1],ComponentValue):
                if len(str(self.display[-1].expression[-1]))>1:
                    val = str(self.display[-1].expression[-1])
                    val = val[:len(val)-1]
                    self.display[-1].expression[-1].update(val)
                else:
                    self.display[-1].expression.pop()
            elif len(self.display[-1].expression) == 0:
                self.display.pop()
                self.isFunction = False
            else:
                self.display[-1].expression.pop()

        elif len(self.display) >0 and not self.isFunction:
            if isinstance(self.display[-1],ComponentValue):
                if len(str(self.display[-1]))>1:
                    val = str(self.display[-1])
                    val = val[:len(val)-1]
                    self.display[-1].update(val)
                else:
                    self.display.pop()

            elif isinstance(self.display[-1],ComponentParanthesis):
                val = self.display.pop()
                if str(val) == ComponentParanthesis._start:
                    self.open_paranthesis -= 1
                else:
                    self.open_paranthesis += 1

            else:
                self.display.pop()

    def cls(self):
        self.display.clear()


