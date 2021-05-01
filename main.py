import PyQt5.QtWidgets as qwd
import PyQt5.QtGui as qtg

class CreateWindow(qwd.QWidget):
    # create window
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('calculator')
        self.setWindowIcon(qtg.QIcon('calculator.png'))
        self.setStyleSheet('background: #FAEBD7;')
        self.setFixedWidth(300)
        self.setFixedHeight(170)

        # show result
        self.res = '' # i will use this to reset the text if the user pressed the equal sign
        self.text = '0'
        self.show_oper = True

        self.UIcomponents()

        self.show()

    def UIcomponents(self):
        # layout

        grid = qwd.QGridLayout()
        

        # show numbers
        self.resultText = qwd.QLineEdit(self.text)
        self.resultText.setReadOnly(True)
        self.resultText.setStyleSheet('background: #FFFAFA;')

        # buttons
        self.but9 = qwd.QPushButton('9')
        self.but8 = qwd.QPushButton('8')
        self.but7 = qwd.QPushButton('7')
        self.but6 = qwd.QPushButton('6')
        self.but5 = qwd.QPushButton('5')
        self.but4 = qwd.QPushButton('4')
        self.but3 = qwd.QPushButton('3')
        self.but2 = qwd.QPushButton('2')
        self.but1 = qwd.QPushButton('1')
        self.but0 = qwd.QPushButton('0')
        self.but_add = qwd.QPushButton('+')
        self.but_decreas = qwd.QPushButton('-')
        self.but_multiply = qwd.QPushButton('*')
        self.but_devide = qwd.QPushButton('/')     
        self.but_equal = qwd.QPushButton('=')
        self.but_clear = qwd.QPushButton('clear')

        # positionate the buttons
        grid.addWidget(self.resultText, 0, 0, 1, 5)
        grid.addWidget(self.but9, 1, 2)
        grid.addWidget(self.but8, 1, 1)
        grid.addWidget(self.but7, 1, 0)
        grid.addWidget(self.but6, 2, 2)
        grid.addWidget(self.but5, 2, 1)
        grid.addWidget(self.but4, 2, 0)
        grid.addWidget(self.but3, 3, 2)
        grid.addWidget(self.but2, 3, 1)
        grid.addWidget(self.but1, 3, 0)
        grid.addWidget(self.but0, 4, 0)

        # buttons for operation
        self.but_devide.setStyleSheet('background: #7FFFD4')
        grid.addWidget(self.but_devide, 1, 4)
        self.but_multiply.setStyleSheet('background: #7FFFD4')
        grid.addWidget(self.but_multiply, 2, 4)
        self.but_add.setStyleSheet('background: #7FFFD4')
        grid.addWidget(self.but_add, 3, 4)
        self.but_decreas.setStyleSheet('background: #7FFFD4')
        grid.addWidget(self.but_decreas, 4, 4)
        self.but_equal.setStyleSheet('background: #008B8B')
        grid.addWidget(self.but_equal, 4, 2)
        self.but_clear.setStyleSheet('background: #008B8B')
        grid.addWidget(self.but_clear, 4, 1)
        # connect buttons
        self.but9.clicked.connect(lambda state, number = '9': self.show_num(number))
        self.but8.clicked.connect(lambda state, number = '8': self.show_num(number))
        self.but7.clicked.connect(lambda state, number = '7': self.show_num(number))
        self.but6.clicked.connect(lambda state, number = '6': self.show_num(number))
        self.but5.clicked.connect(lambda state, number = '5': self.show_num(number))
        self.but4.clicked.connect(lambda state, number = '4': self.show_num(number))
        self.but3.clicked.connect(lambda state, number = '3': self.show_num(number))
        self.but2.clicked.connect(lambda state, number = '2': self.show_num(number))
        self.but1.clicked.connect(lambda state, number = '1': self.show_num(number))
        self.but0.clicked.connect(lambda state, number = '0': self.show_num(number))
        self.but_decreas.clicked.connect(lambda state, oper = ' - ': self.chose_oper(oper))
        self.but_add.clicked.connect(lambda state, oper = ' + ': self.chose_oper(oper))
        self.but_multiply.clicked.connect(lambda state, oper = ' * ': self.chose_oper(oper))
        self.but_devide.clicked.connect(lambda state, oper = ' / ': self.chose_oper(oper))
        
        # equal button and clear button
        self.but_equal.clicked.connect(self.show_res)
        self.but_clear.clicked.connect(self.clear_text)

        self.setLayout(grid)

    def show_num(self, number):
        self.show_oper = True
        if self.text == self.res:
            self.text = '0'

        if len(self.text) != 20:
            if self.text == '0':
                self.text = ''
            self.text += number
            self.resultText.setText(str(self.text))

    def chose_oper(self, oper):
        if self.show_oper == True:
            self.text += oper

        self.resultText.setText(str(self.text))
        self.show_oper = False

    def show_res(self):
        try:
            self.result = eval(self.text)
            self.res = str(self.result)
            self.text = str(self.result)
            self.resultText.setText(str(self.text))
        except:
            print('error')
        
    def clear_text(self):
        self.text = '0'
        self.resultText.setText(str(self.text))

def create_app():
    app = qwd.QApplication([])
    wind = CreateWindow()
    # set app style
    app.setStyle('Fusion')

    app.exec_()

create_app()