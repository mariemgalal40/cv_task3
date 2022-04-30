from Harris import *
from SIFT import *
from PyQt5.QtWidgets import QWidget,QDialog, QApplication

class welcome_page(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)
        MainWindow.setStyleSheet("background-color:rgb(38, 38, 38);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 901, 341))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.widget.setFont(font)
        self.widget.setStyleSheet("backgroud-color: rgb(34, 34, 34);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(280, 112, 371, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(72)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: italic 72pt \"Times New Roman\";\n" "color:rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(210, 220, 501, 81))
        self.label_2.setStyleSheet("font: italic 36pt \"Times New Roman\";\n" "color:rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(0, 350, 891, 311))
        self.widget_2.setObjectName("widget_2")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(200, 30, 221, 131))
        self.pushButton.setStyleSheet("font: italic 20pt \"Times New Roman\";\n" "color:rgb(255, 255, 255);\n" "border-radius:20px;\n" "background-color:rgb(255, 170, 127);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 30, 231, 131))
        self.pushButton_2.setStyleSheet("font: italic 20pt \"Times New Roman\";\n" "color:rgb(255, 255, 255);\n" "border-radius:20px;\n" "background-color:rgb(255, 170, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Welcome"))
        self.label_2.setText(_translate("MainWindow", "Choose The Methodology"))
        self.pushButton.setText(_translate("MainWindow", "Harris Operator "))
        self.pushButton.clicked.connect(self.harris_navigate)
        self.pushButton_2.setText(_translate("MainWindow", "SIFT"))
        self.pushButton_2.clicked.connect(self.sift_navigate)

    def harris_navigate(self):
        self.other_window = QtWidgets.QMainWindow()
        self.ui = Harris_operator()
        self.ui.setupUi(self.other_window)
        self.other_window.show()

    def sift_navigate(self):
        self.other_window = QtWidgets.QMainWindow()
        self.ui = SIFT()
        self.ui.setupUi(self.other_window)
        self.other_window.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = welcome_page()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
