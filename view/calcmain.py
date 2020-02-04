import sys
"""
I use this function sys.path.append because 
I have an import issue and i can't solve it without 
sys.path hack.. 
I wanted to use from ..utils.component import <stufff>
But because of the problems that i've writed at the top,
with sys hack issue solved as : from utils.component import <stuff>
"""
sys.path.append("..")

from PyQt5.QtWidgets import (QStyle,
QWidget,
QApplication,
QVBoxLayout,
QGridLayout,
QHBoxLayout,
QPushButton,
QLabel,
QLineEdit,
QTabWidget,
QListWidget,
QMenuBar)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QIcon,
QColor,
QPalette,
QFont)

from functools import partial
from body import (ScientificCalculatorBody,
VectorCalculatorBody,
Vector2DCalculatorBody)
from controls import CalculatorController
from utils.component import *
from utils.tokenizer import Tokenizer
# from utils.dbconnector import CalculatorDBManager


class CalculatorView(QWidget):
    
    def __init__(self, ctype, parent=None, flags=Qt.WindowFlags() ):
        super().__init__(parent=parent, flags=flags)
        self.__set_window_config()
        self.CTYPE = {
            "SCIENTIFIC":ScientificCalculatorBody(),
            "VECTOR 1D":VectorCalculatorBody(),
            "VECTOR 2D":Vector2DCalculatorBody()
        }
        
        self.tab_result = ctype
        self.__configuration()

    def updateExpression(self,expression):
        self.expression.setText(expression)
    def updateResult(self,result):
        self.result.setText(str(result))
    def updateHistory(self,expression):
        self.history.addItem(expression)

    def __configuration(self):
        self.main = QHBoxLayout()
        self.left = QVBoxLayout()
        self.right= QVBoxLayout()
        self.head = QVBoxLayout()
        self.body = self.CTYPE[self.tab_result.upper()]

        self.__set_head()
        self.__set_right()
        self.__set_left()

        self.main.addLayout(self.left)
        self.main.addLayout(self.right)
        self.setLayout(self.main)

    def __set_window_config(self):
        # self.setFont(QFont("default",  9))
        pass
    
    def __set_head(self):
        self.expression = QLineEdit("0")
        self.expression.setReadOnly(True)
        self.expression.setAlignment(Qt.AlignRight)
        # self.expression.setFont(QFont("default",10,QFont.ExtraLight))
        
        self.result = QLabel('0')
        self.result.setAlignment(Qt.AlignRight)
        # self.result.setFont(QFont("default",10,QFont.Bold))

        self.head.addWidget(self.expression)
        self.head.addWidget(self.result)

    def __set_right(self):
        rtab = QTabWidget()

        self.history = QListWidget()
        self.formula = QListWidget()

        rtab.addTab(self.history,"History")
        rtab.addTab(self.formula,"Formulas")

        self.right.addWidget(rtab)

    def __set_left(self):
        label = QLabel(self.tab_result)
        # label.setFont(QFont("default",10))
        self.left.addWidget(label)
        self.left.addLayout(self.head)
        self.left.addLayout(self.body)
 

class GeneralCalcView(QTabWidget):

    _scientific = "Scientific"
    _vector1d = "Vector 1d"
    _vector2d = "Vector 2d"

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # self.setFont(QFont("default", 9))
        self.setWindowOpacity(1)
        self.setWindowIcon(QIcon("assets/calculator.png"))
        self.setWindowTitle("Calculator")
        
        sci = CalculatorView(ctype=GeneralCalcView._scientific)
        vec1 = CalculatorView(ctype=GeneralCalcView._vector1d)
        vec2 = CalculatorView(ctype=GeneralCalcView._vector2d)

        sci_controller  = CalculatorController(sci, InputController(GeneralCalcView._scientific), Tokenizer("real"))
        vec1_controller = CalculatorController(vec1, InputController(GeneralCalcView._vector1d), Tokenizer("vec1"))
        vec2_controller = CalculatorController(vec2, InputController(GeneralCalcView._vector2d), Tokenizer("vec2"))


        self.addTab(sci, QIcon("assets/calculator.png"), GeneralCalcView._scientific)
        self.addTab(vec1, QIcon("assets/vector1d.png"), GeneralCalcView._vector1d)
        self.addTab(vec2, QIcon("assets/vector2d.png"), GeneralCalcView._vector2d)
   
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)
    view = GeneralCalcView()
    view.show()
    sys.exit(app.exec_())