from PyQt5 import QtWidgets, uic
import sys


class Ui(QtWidgets.QMainWindow):

    def procbtnclicked(self):
        self.label = self.findchild(QtWidgets.QLabel, 'Label_2')
        self.label.setText("Alfin")

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('sma.ui', self)

        self.procbtn = self.findChild(
            QtWidgets.QPushButton, 'pbproceed')
        self.procbtn.clicked.connect(self.procbtnclicked)

        #self.exitButton = self.findChild(QtWidgets.QPushButton, 'pbExit')
        # self.exitButton.clicked.connect(self.close)
        self.show()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
