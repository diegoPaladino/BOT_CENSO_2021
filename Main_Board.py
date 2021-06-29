# Main_Board

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()

    def b1_clicked(self):
        self.label.setText("you pressed the button 1")
        self.update()
        
    def b2_clicked(self):
        self.label.setText("you pressed the button 2")
        self.update()
        
    def b3_clicked(self):
        self.label.setText("you pressed the button 3")
        self.update()

    def initUI(self):
        self.setGeometry(100, 100, 1200, 500)
        self.setWindowTitle("diegoPaladino")

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Login")
        self.b1.clicked.connect(self.b1_clicked)
        self.b1.move(200,200)
        
        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Pesquisa")
        self.b2.clicked.connect(self.b2_clicked)
        self.b1.move(100,100)
        
        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setText("Reset")
        self.b3.clicked.connect(self.b3_clicked)
        self.b1.move(300,300)

    def update(self):
        self.label.adjustSize()
        


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()