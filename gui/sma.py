# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sma.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 70, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.redditbtn = QtWidgets.QPushButton(self.centralwidget)
        self.redditbtn.setGeometry(QtCore.QRect(240, 80, 89, 25))
        self.redditbtn.setObjectName("redditbtn")
        self.redditbtn.setIcon(QtGui.QIcon('reddit.jpg'))
        self.redditbtn.setIconSize(QtCore.QSize(24,24))
        self.twitterbtn = QtWidgets.QPushButton(self.centralwidget)
        self.twitterbtn.setGeometry(QtCore.QRect(470, 80, 89, 25))
        self.twitterbtn.setObjectName("twitterbtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuData_Collection = QtWidgets.QMenu(self.menubar)
        self.menuData_Collection.setObjectName("menuData_Collection")
        self.menuView_Data = QtWidgets.QMenu(self.menubar)
        self.menuView_Data.setObjectName("menuView_Data")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuData_Collection.menuAction())
        self.menubar.addAction(self.menuView_Data.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sports Match Analyser"))
        self.label.setText(_translate("MainWindow", "Collect Data From :"))
        self.redditbtn.setText(_translate("MainWindow", "Reddit"))
        self.twitterbtn.setText(_translate("MainWindow", "Twitter"))
        self.menuData_Collection.setTitle(_translate("MainWindow", "Data Collection"))
        self.menuView_Data.setTitle(_translate("MainWindow", "View Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
