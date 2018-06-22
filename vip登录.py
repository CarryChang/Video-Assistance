# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vip登录.ui'
#
# Created: Sun Jan  7 21:37:11 2018
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.account = QtWidgets.QLineEdit(Form)
        self.account.setGeometry(QtCore.QRect(210, 30, 113, 20))
        self.account.setObjectName("account")
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(210, 80, 113, 20))
        self.password.setObjectName("password")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 40, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 84, 54, 12))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 150, 110, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.login)
        self.pushButton.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "欢迎来到我的VIP"))
        self.label.setText(_translate("Form", "账号："))
        self.label_2.setText(_translate("Form", "密码："))
        self.pushButton.setText(_translate("Form", "登录"))

    def login(self):
        if self.account.text() =='test' and self.password.text() =='test':
            self.accept()
        else:
            reply = QMessageBox.warning(self, "提示","请重新检查检查账号和密码！")

if __name__ == "__main__":
    #测试http://api.baiyug.cn/vip/index.php?url=https://v.qq.com/x/cover/l9vxrwfdjcw1q4g.html
    from PyQt5.QtWidgets import QMessageBox
    from PyQt5 import QtCore, QtGui, QtWidgets
    import sys
    from final1 import Ui_Form1
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Ui_Form()
    if MainWindow.exec_():





        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_Form1()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

