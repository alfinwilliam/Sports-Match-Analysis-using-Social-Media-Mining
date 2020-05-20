from PyQt5 import QtWidgets, uic
import sys
	
	
	
	class Ui(QtWidgets.QMainWindow):
	    def __init__(self):
	        super(Ui, self).__init__()
	        uic.loadUi('mainwindow.ui', self)
	
	        self.button = self.findChild(QtWidgets.QPushButton, 'pbStartVideoCapture')
	        self.button.clicked.connect(self.openCaptureWindow)
	
	        self.exitButton = self.findChild(QtWidgets.QPushButton,'pbExit')
	        self.exitButton.clicked.connect(self.close)
	        self.show()
	    

	
	
	app = QtWidgets.QApplication(sys.argv)
	window = Ui()
	app.exec_()