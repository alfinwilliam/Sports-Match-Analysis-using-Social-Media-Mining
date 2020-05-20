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
        self.collectdatalabel = QtWidgets.QLabel(self.centralwidget)
        self.collectdatalabel.setGeometry(QtCore.QRect(40, 70, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.collectdatalabel.setFont(font)
        self.collectdatalabel.setObjectName("collectdatalabel")
        self.redditbtn = QtWidgets.QPushButton(self.centralwidget)
        self.redditbtn.clicked.connect(self.redditbuttonclicked)
        self.redditbtn.setGeometry(QtCore.QRect(240, 80, 131, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("reddit.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.redditbtn.setIcon(icon)
        self.redditbtn.setIconSize(QtCore.QSize(18, 18))
        self.redditbtn.setObjectName("redditbtn")
        self.twitterbtn = QtWidgets.QPushButton(self.centralwidget)
        self.twitterbtn.setGeometry(QtCore.QRect(470, 80, 131, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("twitter.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.twitterbtn.setIcon(icon1)
        self.twitterbtn.setIconSize(QtCore.QSize(20, 20))
        self.twitterbtn.setObjectName("twitterbtn")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 280, 113, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 290, 161, 17))
        self.label_3.setObjectName("label_3")
        self.redditfetchbtn = QtWidgets.QPushButton(self.centralwidget)
        self.redditfetchbtn.setGeometry(QtCore.QRect(290, 420, 181, 25))
        self.redditfetchbtn.setObjectName("redditfetchbtn")
        self.twitterfetchbtn = QtWidgets.QPushButton(self.centralwidget)
        self.twitterfetchbtn.setGeometry(QtCore.QRect(290, 400, 181, 25))
        self.twitterfetchbtn.setObjectName("twitterfetchbtn")
        self.twitterhastaglabel = QtWidgets.QLabel(self.centralwidget)
        self.twitterhastaglabel.setGeometry(QtCore.QRect(70, 230, 161, 17))
        self.twitterhastaglabel.setObjectName("twitterhastaglabel")
        self.twitterhashtag = QtWidgets.QLineEdit(self.centralwidget)
        self.twitterhashtag.setGeometry(QtCore.QRect(290, 230, 113, 25))
        self.twitterhashtag.setObjectName("twitterhashtag")
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
        self.collectdatalabel.setText(_translate("MainWindow", "Collect Data From :"))
        self.redditbtn.setText(_translate("MainWindow", " Reddit"))
        self.twitterbtn.setText(_translate("MainWindow", " Twitter"))
        self.label_3.setText(_translate("MainWindow", "Enter Reddit Thread ID :"))
        self.redditfetchbtn.setText(_translate("MainWindow", "Fetch Data"))
        self.twitterfetchbtn.setText(_translate("MainWindow", "Fetch Data"))
        self.twitterhastaglabel.setText(_translate("MainWindow", "Enter Twitter Hashtag:"))
        self.menuData_Collection.setTitle(_translate("MainWindow", "Data Collection"))
        self.menuView_Data.setTitle(_translate("MainWindow", "View Data"))

    def redditbuttonclicked(self):
        self.twitterfetchbtn.hide()
        self.twitterhastaglabel.hide()
        self.twitterhashtag.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
