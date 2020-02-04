from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel,QPushButton,QHBoxLayout,QLineEdit, QDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sys
from functools import partial

class BodyLayout:

    def __init__(self):
        super().__init__()
        self._create_numbers()
        self._create_operators()

        self.numbers = {
            '0':self.btn_zero,
            '1':self.btn_one,
            '2':self.btn_two,
            '3':self.btn_three,
            '4':self.btn_four,
            '5':self.btn_five,
            '6':self.btn_six,
            '7':self.btn_seven,
            '8':self.btn_eight,
            '9':self.btn_nine
        }

        self.special_numbers = {
            'pi':self.btn_pi,
            'e':self.btn_e
        }

        self.operators = {
            '+':self.btn_add,
            '-':self.btn_sub,
            'x':self.btn_multip,
            '/':self.btn_divide,
            '(':self.btn_start_paranthesis,
            ')':self.btn_end_paranthesis,
            '+/-':self.btn_negative,
            '.':self.btn_dot,
            '=':self.btn_equal,
            'CE':self.btn_clear,
            '<-':self.btn_backspace
        }

       

    def _create_numbers(self):
        # @Numbers
        self.btn_zero = QPushButton("0")
        self.btn_one = QPushButton("1")
        self.btn_two = QPushButton("2")
        self.btn_three = QPushButton("3")
        self.btn_four = QPushButton("4")
        self.btn_five = QPushButton("5")
        self.btn_six = QPushButton("6")
        self.btn_seven = QPushButton("7")
        self.btn_eight = QPushButton("8")
        self.btn_nine = QPushButton("9")

        # @Special Numbers
        self.btn_pi = QPushButton("pi")
        self.btn_e = QPushButton('e')

    def _create_operators(self):
        # @Operators
        self.btn_add = QPushButton('+')
        self.btn_sub = QPushButton('-')
        self.btn_multip = QPushButton('*')
        self.btn_divide = QPushButton('/')
        self.btn_start_paranthesis = QPushButton("(")
        self.btn_end_paranthesis = QPushButton(")")
        self.btn_negative = QPushButton('+/-')
        self.btn_dot = QPushButton(".")
        self.btn_equal = QPushButton("=")
        self.btn_clear = QPushButton('CE')
        self.btn_backspace = QPushButton('<-')


    def _create_buttons(self):
        pass

    def _set_layout(self):
        pass

class VectorCalculatorBody(QVBoxLayout, BodyLayout):
    def __init__(self):
        super().__init__()
        
        self._create_buttons()

        self.basic_functions = {
            'sum':self.sum,
            'median':self.median,
            'mod':self.mod,
            'max':self.max,
            'min':self.min
        }

        self._set_layout()


    def _create_buttons(self):
        self.create_vector = QPushButton("Create Vector")
        self.create_vector.clicked.connect(self._open_dialog)


        self.sum = QPushButton("sum")
        self.median = QPushButton("median")
        self.mod = QPushButton("mod")
        self.max = QPushButton('max')
        self.min = QPushButton('min')
 
        
        return super()._create_buttons()

    def _set_layout(self):

        first_two_buttons = QHBoxLayout()
        first_two_buttons.addWidget(self.operators['CE'])
        first_two_buttons.addWidget(self.operators['<-'])

        second_four_buttons = QHBoxLayout()
        second_four_buttons.addWidget(self.basic_functions['median'])
        second_four_buttons.addWidget(self.basic_functions['mod'])
        second_four_buttons.addWidget(self.basic_functions['max'])
        second_four_buttons.addWidget(self.basic_functions['min'])

        third_four_buttons = QHBoxLayout()
        third_four_buttons.addWidget(self.operators['('])
        third_four_buttons.addWidget(self.operators[')'])
        third_four_buttons.addWidget(self.basic_functions['sum'])
        third_four_buttons.addWidget(self.operators['/'])

        fourth_four_buttons = QHBoxLayout()
        fourth_four_buttons.addWidget(self.numbers['7'])
        fourth_four_buttons.addWidget(self.numbers['8'])
        fourth_four_buttons.addWidget(self.numbers['9'])
        fourth_four_buttons.addWidget(self.operators['x'])

        fifth_four_buttons = QHBoxLayout()
        fifth_four_buttons.addWidget(self.numbers['4'])
        fifth_four_buttons.addWidget(self.numbers['5'])
        fifth_four_buttons.addWidget(self.numbers['6'])
        fifth_four_buttons.addWidget(self.operators['-'])

        sixth_four_buttons = QHBoxLayout()
        sixth_four_buttons.addWidget(self.numbers['1'])
        sixth_four_buttons.addWidget(self.numbers['2'])
        sixth_four_buttons.addWidget(self.numbers['3'])
        sixth_four_buttons.addWidget(self.operators['+'])

        seventh_four_buttons = QHBoxLayout()
        seventh_four_buttons.addWidget(self.operators['+/-'])
        seventh_four_buttons.addWidget(self.numbers['0'])
        seventh_four_buttons.addWidget(self.operators['.'])
        seventh_four_buttons.addWidget(self.operators['='])

        self.addWidget(self.create_vector)
        self.addLayout(first_two_buttons)
        self.addLayout(second_four_buttons)
        self.addLayout(third_four_buttons)
        self.addLayout(fourth_four_buttons)
        self.addLayout(fifth_four_buttons)
        self.addLayout(sixth_four_buttons)
        self.addLayout(seventh_four_buttons)


    def _open_dialog(self):
        self.dialog = Dialog(isVector1d=True)
        self.dialog.show()
        self.dialog.closeEvent = self.dialog_return

    def setto(self,func):
        self.func = func

    def dialog_return(self,event):
        try:
            self.func(self.dialog.vec)
        except:
            # Just close
            pass
    
class Vector2DCalculatorBody(QVBoxLayout, BodyLayout):
    def __init__(self):
        super().__init__()
        self._create_buttons()

        self.basic_functions = {
            'mean':self.mean,
            'std':self.std,
            'mod':self.mod,
            'median':self.median,
            'max':self.max,
            'min':self.min,
            'inv':self.inv,
            'T':self.transpoze,
            'det':self.det,
            'sum':self.sum
        }

        self._set_layout()


    def _create_buttons(self):
        self.create_vector = QPushButton("Create Vector")
        self.create_vector.clicked.connect(self._open_dialog)

        self.mean = QPushButton("mean")
        self.std = QPushButton("std")
        self.mod = QPushButton("mod")
        self.median = QPushButton("median")
        self.max = QPushButton("max")
        self.min = QPushButton("min")
        self.inv = QPushButton("inv")
        self.transpoze = QPushButton("T")
        self.det = QPushButton("det")
        self.sum = QPushButton("sum")
        return super()._create_buttons()

    def _set_layout(self):

        

        first_four_buttons = QHBoxLayout()
        first_four_buttons.addWidget(self.basic_functions['mean'])
        first_four_buttons.addWidget(self.basic_functions['std'])
        first_four_buttons.addWidget(self.basic_functions['mod'])
        first_four_buttons.addWidget(self.basic_functions['median'])

        eighth_third_buttons = QHBoxLayout()
        eighth_third_buttons.addWidget(self.basic_functions['sum'])
        eighth_third_buttons.addWidget(self.operators["CE"])
        eighth_third_buttons.addWidget(self.operators["<-"])


        second_four_buttons = QHBoxLayout()
        second_four_buttons.addWidget(self.basic_functions['max'])
        second_four_buttons.addWidget(self.basic_functions['min'])
        second_four_buttons.addWidget(self.basic_functions['inv'])
        second_four_buttons.addWidget(self.basic_functions['T'])

        third_four_buttons = QHBoxLayout()
        third_four_buttons.addWidget(self.operators['('])
        third_four_buttons.addWidget(self.operators[')'])
        third_four_buttons.addWidget(self.basic_functions['det'])
        third_four_buttons.addWidget(self.operators['/'])

        fourth_four_buttons = QHBoxLayout()
        fourth_four_buttons.addWidget(self.numbers['7'])
        fourth_four_buttons.addWidget(self.numbers['8'])
        fourth_four_buttons.addWidget(self.numbers['9'])
        fourth_four_buttons.addWidget(self.operators['x'])

        fifth_four_buttons = QHBoxLayout()
        fifth_four_buttons.addWidget(self.numbers['4'])
        fifth_four_buttons.addWidget(self.numbers['5'])
        fifth_four_buttons.addWidget(self.numbers['6'])
        fifth_four_buttons.addWidget(self.operators['-'])

        sixth_four_buttons = QHBoxLayout()
        sixth_four_buttons.addWidget(self.numbers['1'])
        sixth_four_buttons.addWidget(self.numbers['2'])
        sixth_four_buttons.addWidget(self.numbers['3'])
        sixth_four_buttons.addWidget(self.operators['+'])

        seventh_four_buttons = QHBoxLayout()
        seventh_four_buttons.addWidget(self.operators['+/-'])
        seventh_four_buttons.addWidget(self.numbers['0'])
        seventh_four_buttons.addWidget(self.operators['.'])
        seventh_four_buttons.addWidget(self.operators['='])

        self.addWidget(self.create_vector)
        self.addLayout(first_four_buttons)
        self.addLayout(eighth_third_buttons)
        self.addLayout(second_four_buttons)
        self.addLayout(third_four_buttons)
        self.addLayout(fourth_four_buttons)
        self.addLayout(fifth_four_buttons)
        self.addLayout(sixth_four_buttons)
        self.addLayout(seventh_four_buttons)


        return super()._set_layout()


    def _open_dialog(self):
        self.dialog = Dialog()
        self.dialog.show()
        self.dialog.closeEvent = self.dialog_return

    def setto(self,func):
        self.func = func

    def dialog_return(self,event):
        try:
            self.func(self.dialog.vec)
        except:
            # just close
            pass

class ScientificCalculatorBody(QVBoxLayout, BodyLayout):
    
    def __init__(self):
        super().__init__()
        self._create_buttons()


        self.basic_functions = {
            '1/x':self.btn_onedivx,
            '|x|':self.btn_abs,
            'exp':self.btn_exp,
            'n!':self.btn_fact,
            'ln':self.btn_ln,
            '10^x':self.btn_tentox,
            'x^3':self.btn_cube,
            'x^2':self.btn_square,
            '2^x':self.btn_twotox,
            'sin':self.btn_sin,
            'cos':self.btn_cos,
            'tan':self.btn_tan,
            'cot':self.btn_cot
        }

        self.advanced_functions = {
            'mod':self.btn_mod,
            'log':self.btn_log,
            'x^y':self.btn_xtoy,
            'rand':self.btn_rand
        }

    
        self._set_layout()

    def _create_buttons(self):
        

        # @Basic Functions
        self.btn_onedivx = QPushButton("1/x")
        self.btn_abs = QPushButton('|x|')
        self.btn_exp = QPushButton('exp')
        self.btn_fact = QPushButton('n!')
        self.btn_ln = QPushButton('ln')
        self.btn_tentox = QPushButton('10^x')
        self.btn_cube = QPushButton('x^3')
        self.btn_square = QPushButton('x^2')
        self.btn_twotox = QPushButton('2^x')
        self.btn_sin = QPushButton('sin')
        self.btn_cos = QPushButton('cos')
        self.btn_tan = QPushButton('tan')
        self.btn_cot = QPushButton('cot')

        # @Advanced Functions
        self.btn_mod = QPushButton('mod')
        self.btn_log = QPushButton('log')
        self.btn_xtoy = QPushButton('x^y')
        self.btn_rand = QPushButton('rand')
   
    def _set_layout(self):
        
        first_five_buttons = QHBoxLayout()
        first_five_buttons.addWidget(self.basic_functions['sin'])
        first_five_buttons.addWidget(self.basic_functions['cos'])
        first_five_buttons.addWidget(self.basic_functions['tan'])
        first_five_buttons.addWidget(self.basic_functions['cot'])
        first_five_buttons.addWidget(self.advanced_functions['rand'])

        second_five_buttons = QHBoxLayout()
        second_five_buttons.addWidget(self.basic_functions['2^x'])
        second_five_buttons.addWidget(self.special_numbers['pi'])
        second_five_buttons.addWidget(self.special_numbers['e'])
        second_five_buttons.addWidget(self.operators['CE'])
        second_five_buttons.addWidget(self.operators['<-'])

        third_five_buttons = QHBoxLayout()
        third_five_buttons.addWidget(self.basic_functions['x^2'])
        third_five_buttons.addWidget(self.basic_functions['1/x'])
        third_five_buttons.addWidget(self.basic_functions['|x|'])
        third_five_buttons.addWidget(self.basic_functions['exp'])
        third_five_buttons.addWidget(self.advanced_functions['mod'])

        fourth_five_buttons = QHBoxLayout()
        fourth_five_buttons.addWidget(self.basic_functions['x^3'])
        fourth_five_buttons.addWidget(self.operators['('])
        fourth_five_buttons.addWidget(self.operators[')'])
        fourth_five_buttons.addWidget(self.basic_functions['n!'])
        fourth_five_buttons.addWidget(self.operators['/'])

        fifth_five_buttons = QHBoxLayout()
        fifth_five_buttons.addWidget(self.advanced_functions['x^y'])
        fifth_five_buttons.addWidget(self.numbers['7'])
        fifth_five_buttons.addWidget(self.numbers['8'])
        fifth_five_buttons.addWidget(self.numbers['9'])
        fifth_five_buttons.addWidget(self.operators['x'])

        sixth_five_buttons = QHBoxLayout()
        sixth_five_buttons.addWidget(self.basic_functions['10^x'])
        sixth_five_buttons.addWidget(self.numbers['4'])
        sixth_five_buttons.addWidget(self.numbers['5'])
        sixth_five_buttons.addWidget(self.numbers['6'])
        sixth_five_buttons.addWidget(self.operators['-'])

        seventh_five_buttons = QHBoxLayout()
        seventh_five_buttons.addWidget(self.advanced_functions['log'])
        seventh_five_buttons.addWidget(self.numbers['1'])
        seventh_five_buttons.addWidget(self.numbers['2'])
        seventh_five_buttons.addWidget(self.numbers['3'])
        seventh_five_buttons.addWidget(self.operators['+'])

        eighth_five_buttons = QHBoxLayout()
        eighth_five_buttons.addWidget(self.basic_functions['ln'])
        eighth_five_buttons.addWidget(self.operators['+/-'])
        eighth_five_buttons.addWidget(self.numbers['0'])
        eighth_five_buttons.addWidget(self.operators['.'])
        eighth_five_buttons.addWidget(self.operators['='])


        self.addLayout(first_five_buttons)
        self.addLayout(second_five_buttons)
        self.addLayout(third_five_buttons)
        self.addLayout(fourth_five_buttons)
        self.addLayout(fifth_five_buttons)
        self.addLayout(sixth_five_buttons)
        self.addLayout(seventh_five_buttons)
        self.addLayout(eighth_five_buttons)

class Dialog(QWidget):
    
    def __init__(self, parent=None, isVector1d = False):
        super().__init__(parent=parent)
        self.isVector1d = isVector1d
        self.main = QVBoxLayout()
        self.setWindowIcon(QIcon("assets/vector1d.png"))
        self.setWindowTitle("Vector")
        self.setMinimumWidth(300)
        self._configuration()

        self.setLayout(self.main)

    def _configuration(self):
        labelrow = QLabel("Row : ")
        labelcol = QLabel("Col : ")
    
        self.row = QLineEdit()
        if self.isVector1d:
            self.row.setText("1")
            self.row.setDisabled(True)
        
        self.column = QLineEdit()
        self.create_elements = QPushButton("Create Elements")
        self.create_elements.clicked.connect(self._create_elements_layout)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(labelrow)
        hbox1.addWidget(self.row)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(labelcol)
        hbox2.addWidget(self.column)

        self.main.addLayout(hbox1)
        self.main.addLayout(hbox2)
        self.main.addWidget(self.create_elements)

    def _set_elements(self):
        # Get the data from line edits
        total = 0
        row = int(self.row.text())
        col = int(self.column.text())

        self.vec = []
        for _ in range(row):
            tmp = []
            for _ in range(col):
                tmp.append(float(self.line_edits[total].text()))
                total+=1
                
            if self.isVector1d: self.vec = tmp
            else: self.vec.append(tmp)

        print(self.vec)
        
        self.close()


    
    def _create_elements_layout(self):
        # use assert here.

        row = int(self.row.text())
        col = int(self.column.text())

        self.line_edits = {}
        labels = {}

        total = 0
        for i in range(1,row+1):
            for j in range(1,col+1):
                self.line_edits[total] = QLineEdit()
                labels[total] = QLabel(str(i)+"x"+str(j)+":")
                total+=1

        total = 0
        for _ in range(row):
            hbox = QHBoxLayout()
            for _ in range(col):
                hbox.addWidget(labels[total])
                hbox.addWidget(self.line_edits[total])
                total += 1
            
            self.main.addLayout(hbox)

        self.set_elements = QPushButton("Set Elements")
        self.set_elements.clicked.connect(self._set_elements)

        self.main.addWidget(self.set_elements)

    