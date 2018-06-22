# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'restart.ui'
#
# Created: Thu Dec 14 21:01:37 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 40, 211, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 100, 211, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 150, 211, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 40, 91, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 91, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 91, 20))
        self.label_3.setObjectName("label_3")
        self.complete = QtWidgets.QPushButton(Form)
        self.complete.setGeometry(QtCore.QRect(30, 210, 111, 31))
        self.complete.setObjectName("complete")
        self.return_2 = QtWidgets.QPushButton(Form)
        self.return_2.setGeometry(QtCore.QRect(200, 210, 111, 31))
        self.return_2.setObjectName("return_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 270, 321, 20))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "注册/忘记密码？"))
        self.label.setText(_translate("Form", "请输入电话号码："))
        self.label_2.setText(_translate("Form", "请输入验证码："))
        self.label_3.setText(_translate("Form", "填写密码："))
        self.complete.setText(_translate("Form", "完成"))
        self.return_2.setText(_translate("Form", "返回"))
        self.label_4.setText(_translate("Form", "友情提示：点击完成按钮后，将于2秒后自动进入系统"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())