from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from gaussian_filter import *
import time
import cv2
from sobel import *


class Harris_operator(object):
    def setupUi(self, second_window):
        second_window.setObjectName("MainWindow")
        second_window.resize(910, 700)
        second_window.setStyleSheet("background-color:rgb(38, 38, 38);")
        self.centralwidget = QtWidgets.QWidget(second_window)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, -20, 241, 721))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.widget.setFont(font)
        self.widget.setStyleSheet("backgroud-color: rgb(34, 34, 34);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 60, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: italic 16pt \"Times New Roman\";\n" "color:rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(10, 110, 231, 41))
        self.pushButton.setStyleSheet("font: italic 20pt \"Times New Roman\";\n" "color:rgb(255, 255, 255);\n" "border-radius:20px;\n" "background-color:rgb(255, 170, 127);")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 190, 141, 31))
        self.label_2.setStyleSheet("font: italic 16pt \"Times New Roman\";\n" "color:rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 260, 191, 31))
        self.lineEdit.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 340, 191, 31))
        self.lineEdit_3.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(20, 230, 141, 31))
        self.label_3.setStyleSheet("font: italic 14pt \"Times New Roman\";\n" "color:rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(20, 300, 141, 31))
        self.label_4.setStyleSheet("font: italic 14pt \"Times New Roman\";\n" "color:rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 410, 231, 41))
        self.pushButton_2.setStyleSheet("font: italic 20pt \"Times New Roman\";\n" "color:rgb(255, 255, 255);\n" "border-radius:20px;\n" "background-color:rgb(255, 170, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(250, -10, 661, 691))
        self.widget_2.setStyleSheet("background-color:rgb(85, 85, 85);")
        self.widget_2.setObjectName("widget_2")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(0, 35, 651, 321))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(0, 370, 661, 331))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(30, 480, 141, 31))
        self.label_7.setStyleSheet("font: italic 14pt \"Times New Roman\";\n" "color:rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(50, 510, 181, 31))
        self.label_8.setStyleSheet("font: italic 14pt \"Times New Roman\";\n" "color:rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setGeometry(QtCore.QRect(0, 12, 200, 30))
        self.label_9.setStyleSheet("font: italic 14pt \"Times New Roman\";\n" "color:rgb(255, 255, 255);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget_2)
        self.label_10.setGeometry(QtCore.QRect(0, 350, 200, 30))
        self.label_10.setStyleSheet("font: italic 14pt \"Times New Roman\";\n" "color:rgb(255, 255, 255);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")

        second_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(second_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 21))
        self.menubar.setObjectName("menubar")
        second_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(second_window)
        self.statusbar.setObjectName("statusbar")
        second_window.setStatusBar(self.statusbar)

        self.retranslateUi(second_window)
        QtCore.QMetaObject.connectSlotsByName(second_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Insert Image"))
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.pushButton.clicked.connect(self.browse_image)
        self.label_2.setText(_translate("MainWindow", "Set Parameters"))
        self.label_3.setText(_translate("MainWindow", "Threshold"))
        self.label_4.setText(_translate("MainWindow", "Sensitivity factor"))
        self.label_7.setText(_translate("MainWindow", "Computation time"))
        self.label_9.setText(_translate("MainWindow", "Input_image"))
        self.label_10.setText(_translate("MainWindow", "output_image"))
        self.pushButton_2.setText(_translate("MainWindow", "Show Result"))
        self.pushButton_2.clicked.connect(self.apply_harris)

    def browse_image(self):
        print('browse button is clicked')
        image = QFileDialog.getOpenFileName(None, 'OpenFile', '', "Image file(*.png)")
        self. imagePath = image[0]
        pixmap = QPixmap(self.imagePath)
        self.label_5.setPixmap(pixmap.scaled(450, 300))

    def apply_harris(self):
        self.start_time = time.time()
        img = cv2.imread(self. imagePath)
        # imggray = convert_to_grayScale(img)
        imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # I_x = SobelFilter(imggray, 3, kernel_type="x")
        # I_y = SobelFilter(imggray, 3, kernel_type="y")
        I_x = cv.Sobel(imggray, cv.CV_64F, 1, 0, ksize=3)
        I_y = cv.Sobel(imggray, cv.CV_64F, 0, 1, ksize=3)
        self.applying_gaussian(I_x, I_y, img)

    def applying_gaussian(self,I_x, I_y,img):
        # Ixx = gaussian_fitler(np.multiply(I_x, I_x), 3, 1)
        # Ixy = gaussian_fitler(np.multiply(I_x, I_y), 3, 1)
        # Iyy = gaussian_fitler(np.multiply(I_y, I_y), 3, 1)
        Ixx = cv2.GaussianBlur(np.multiply(I_x, I_x), (3, 3), 1)
        Ixy = cv2.GaussianBlur(np.multiply(I_x, I_y), (3, 3), 1)
        Iyy = cv2.GaussianBlur(np.multiply(I_y, I_y), (3, 3), 1)
        self.getting_response(Ixx, Ixy, Iyy, img)

    def getting_response(self,Ixx, Ixy, Iyy, img):
        k = self.lineEdit_3.text()
        # determinante
        detA = np.multiply(Ixx, Iyy) - np.multiply(Ixy, Ixy)
        # trace
        traceA = np.add(Ixx, Iyy)
        harris_response = detA - float(k) * traceA ** 2
        self.get_EdgesAndCorners(img, harris_response)

    def get_EdgesAndCorners(self, img, R):
        threshold = self.lineEdit.text()
        img_corners = np.copy(img)
        R = cv.dilate(R, None)
        for rowindex, response in enumerate(R):
            for colindex, r in enumerate(response):
                if r > (np.max(R) * float(threshold)):
                      # this is a corner
                    img_corners[rowindex, colindex] = [0, 0, 255]
        cv2.imwrite('saved.png',img_corners)
        pixmap = QPixmap('saved.png')
        self.end_time =time.time()
        com_time = self.end_time -self.start_time
        print(com_time)
        self.label_8.setText(str(com_time)+"seconds")
        self.label_6.setPixmap(pixmap.scaled(450, 300))

















if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    second_window = QtWidgets.QMainWindow()
    ui = Harris_operator()
    ui.setupUi(second_window)
    second_window.show()
    sys.exit(app.exec_())
