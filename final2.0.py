# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final1.ui'
#
# Created: Wed Jan  3 16:01:17 2018
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_E(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.send = QtWidgets.QPushButton(Form)
        self.send.setGeometry(QtCore.QRect(260, 140, 111, 41))
        self.send.setObjectName("send")
        self.user = QtWidgets.QLineEdit(Form)
        self.user.setGeometry(QtCore.QRect(40, 60, 151, 20))
        self.user.setPlaceholderText("只能使用新浪邮箱")
        self.user.setObjectName("user")
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(40, 110, 151, 20))
        self.password.setObjectName("password")
        self.to = QtWidgets.QLineEdit(Form)
        self.to.setGeometry(QtCore.QRect(40, 160, 151, 20))
        self.to.setObjectName("to")
        self.retranslateUi(Form)
        self.send.clicked.connect(self.send1)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "邮件发送"))
        self.send.setText(_translate("Form", "发送"))
        self.password.setPlaceholderText(_translate("Form", "新浪邮箱密码"))
        self.to.setPlaceholderText(_translate("Form", "收件人邮箱"))
    def send1(self):
        textcontent=self.user.text()
        if textcontent!='':
            from_addr = self.user.text()#发送者邮箱地址
            password = self.password.text() #发送者邮箱密码,不告诉你密码
            to_addr = self.to.text()  #接收者邮箱地址
            msg = MIMEMultipart()
            msg.attach(MIMEText('附件中的二维码直接扫描即可！', 'plain', 'utf-8'))
            #发送带附件邮件对象:
            msg['Subject'] = Header('这是你要查的信息', 'utf-8').encode() #邮件标题
            msg['From'] = from_addr#邮件头部，发送者本人名字
            image = MIMEApplication(open('Qrcode.png', 'rb').read())
            image.add_header('Content-Disposition', 'attachment', filename='Qrcode.png')
            msg.attach(image)
            #服务器端
            smtp_server = 'smtp.sina.cn'  #发送者所在的邮箱供应商的MTA地址
            server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
            # server.set_debuglevel(1) #打印出和SMTP服务器交互的所有信息
            try:
                server.login(from_addr, password) #登录SMTP服务器
                server.sendmail(from_addr, [to_addr], msg.as_string()) #发送邮件
                reply = QMessageBox.information(self, "提示","发送成功")
            except smtplib.SMTPException as e:
                reply = QMessageBox.information(self, "提示","发送失败，请确认发送者是否为新浪邮箱")
            server.quit()
        else:
            reply = QMessageBox.warning(self, "提示","请输入信息后再点击该按钮")


class Ui_Form(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(400, 611)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(308, 91, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(113, 91, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(16, 91, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(80, 30, 291, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(16, 120, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(210, 90, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(113, 120, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(308, 120, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(210, 120, 75, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 32, 60, 16))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(16, 220, 271, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(17, 150, 75, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(210, 150, 75, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(113, 150, 75, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(Form)
        self.pushButton_12.setGeometry(QtCore.QRect(307, 220, 75, 20))
        self.pushButton_12.setObjectName("pushButton_12")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(14, 250, 371, 311))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(13, 10, 341, 301))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_13 = QtWidgets.QPushButton(Form)
        self.pushButton_13.setGeometry(QtCore.QRect(323, 590, 75, 20))
        self.pushButton_13.setObjectName("pushButton_13")

        self.retranslateUi(Form)
        self.pushButton_6.clicked.connect(self.slot1)
        self.pushButton_3.clicked.connect(self.slot2)
        self.pushButton_7.clicked.connect(self.slot3)
        self.pushButton_2.clicked.connect(self.slot4)
        self.pushButton.clicked.connect(self.slot5)
        self.pushButton_5.clicked.connect(self.slot6)
        self.pushButton_8.clicked.connect(self.slot7)
        self.pushButton_4.clicked.connect(self.slot8)
        self.pushButton_9.clicked.connect(self.slot9)
        self.pushButton_11.clicked.connect(self.slot10)
        self.pushButton_10.clicked.connect(self.slot11)
        self.pushButton_12.clicked.connect(self.sou)
        self.pushButton_13.clicked.connect(self.show)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "我的VIP视频助手"))
        self.pushButton_2.setText(_translate("Form", "通道4"))
        self.pushButton_3.setText(_translate("Form", "通道2"))
        self.pushButton_6.setText(_translate("Form", "通道1"))
        self.lineEdit.setPlaceholderText(_translate("Form", "直接粘贴视频地址，然后选中通道即可"))
        self.pushButton.setText(_translate("Form", "通道5"))
        self.pushButton_7.setText(_translate("Form", "通道3"))
        self.pushButton_5.setText(_translate("Form", "通道6"))
        self.pushButton_4.setText(_translate("Form", "通道8"))
        self.pushButton_8.setText(_translate("Form", "通道7"))
        self.label.setText(_translate("Form", "输入地址："))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "直接输入您想搜索的内容，点击搜索"))
        self.pushButton_9.setText(_translate("Form", "通道9"))
        self.pushButton_10.setText(_translate("Form", "通道11"))
        self.pushButton_11.setText(_translate("Form", "通道10"))
        self.pushButton_12.setText(_translate("Form", "开始搜索"))
        self.groupBox.setTitle(_translate("Form", "微信扫描二维码即可同步观看"))
        self.pushButton_13.setText(_translate("Form", "远程观看"))


    def slot1(self):
        url=self.lineEdit.text()
        if re.match(r'^https?:/{2}\w.+$',url):
            url=parse.quote_plus(url)
            logurl='http://wwwhe41.177kdy.cn/1.php?url=http://api.baiyug.cn/vip/index.php?url=%s'%url
            filename='Qrcode.png'
            qr = qrcode.QRCode(
                version=None,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=4,
                border=4,
            )
            qr.add_data(logurl)
            qr.make(fit=True)
            img = qr.make_image()
            img.save(filename)
            self.label_2.setPixmap(QtGui.QPixmap(filename))
            webbrowser.open(logurl)
        else:
            reply = QMessageBox.warning(self, "提示","请输入网址后再点击该按钮")
    def slot2(self):
        url=self.lineEdit.text()
        if re.match(r'^https?:/{2}\w.+$',url):
            url=parse.quote_plus(url)
            logurl='http://api.baiyug.cn/vip/index.php?url=%s'%url

            filename='Qrcode.png'
            qr = qrcode.QRCode(
                version=None,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=4,
                border=4,
            )
            qr.add_data(logurl)
            qr.make(fit=True)
            img = qr.make_image()
            img.save(filename)
            self.label_2.setPixmap(QtGui.QPixmap(filename))
            webbrowser.open(logurl)
        else:
            reply = QMessageBox.warning(self, "提示","请输入网址后再点击该按钮")
    def slot3(self):
        url=self.lineEdit.text()
        if re.match(r'^https?:/{2}\w.+$',url):
            url=parse.quote_plus(url)
            logurl='http://vip.jlsprh.com/index.php?url=%s'%url
            filename='Qrcode.png'
            qr = qrcode.QRCode(
                version=None,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=4,
                border=4,
            )
            qr.add_data(logurl)
            qr.make(fit=True)
            img = qr.make_image()
            img.save(filename)
            self.label_2.setPixmap(QtGui.QPixmap(filename))
            webbrowser.open(logurl)
        else:
            reply = QMessageBox.warning(self, "提示","请输入网址后再点击该按钮")
    def slot4(self):
        url=self.lineEdit.text()
        if re.match(r'^https?:/{2}\w.+$',url):
            url=parse.quote_plus(url)
            logurl='http://v.72du.com/api/?url=%s'%url
            filename='Qrcode.png'
            qr = qrcode.QRCode(
                version=None,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=4,
                border=4,
            )
            qr.add_data(logurl)
            qr.make(fit=True)
            img = qr.make_image()
            img.save(filename)
            self.label_2.setPixmap(QtGui.QPixmap(filename))
            webbrowser.open(logurl)
        else:
            reply = QMessageBox.warning(self, "提示","请输入网址后再点击该按钮")
    def slot5(self):
        url=self.lineEdit.text()
        if re.match(r'^https?:/{2}\w.+$',url):
            url=parse.quote_plus(url)
            logurl='http://api.xfsub.com/index.php?url=%s'%url
            filename='Qrcode.png'
            qr = qrcode.QRCode(
                version=None,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=4,
                border=4,
            )
            qr.add_data(logurl)
            qr.make(fit=True)
            img = qr.make_image()
            img.save(filename)
            self.label_2.setPixmap(QtGui.QPixmap(filename))
            webbrowser.open_new(logurl)
        else:
            reply = QMessageBox.warning(self, "提示","请输入网址后再点击该按钮")
    def slot6(self):
        url=self.lineEdit.text()
        if re.match(r'^https?:/{2}\w.+$',url):
            url=parse.quote_plus(url)
            logurl='http://www.wmxz.wang/video.php?url=%s'%url
            filename='Qrcode.png'
            qr = qrcode.QRCode(
                version=None,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=4,
                border=4,
            )
            qr.add_data(logurl)
            qr.make(fit=True)
            img = qr.make_image()
            img.save(filename)
            self.label_2.setPixmap(QtGui.QPixmap(filename))
            webbrowser.open_new(logurl)
        else:
            reply = QMessageBox.warning(self, "提示","请输入网址后再点击该按钮")
    def slot7(self):
        url=self.lineEdit.text()
        if re.match(r'^https?:/{2}\w.+$',url):
            url=parse.quote_plus(url)
            logurl='http://yun.mt2t.com/yun?url=%s'%url
            filename='Qrcode.png'
            qr = qrcode.QRCode(
                version=None,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=4,
                border=4,
            )
            qr.add_data(logurl)
            qr.make(fit=True)
            img = qr.make_image()
            img.save(filename)
            self.label_2.setPixmap(QtGui.QPixmap(filename))
            webbrowser.open_new(logurl)
        else:
            reply = QMessageBox.warning(self, "提示","请输入网址后再点击该按钮")
    def slot8(self):
        url=self.lineEdit.text()
        if re.match(r'^https?:/{2}\w.+$',url):
            url=parse.quote_plus(url)
            logurl='http://www.0335haibo.com/tong.php?url=%s'%url
            filename='Qrcode.png'
            qr = qrcode.QRCode(
                version=None,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=4,
                border=4,
            )
            qr.add_data(logurl)
            qr.make(fit=True)
            img = qr.make_image()
            img.save(filename)
            self.label_2.setPixmap(QtGui.QPixmap(filename))
            webbrowser.open_new(logurl)
        else:
            reply = QMessageBox.warning(self, "提示","请输入网址后再点击该按钮")
    def slot9(self):
        url=self.lineEdit.text()
        if re.match(r'^https?:/{2}\w.+$',url):
            url=parse.quote_plus(url)
            logurl='http://jqaaa.com/jx.php?url=%s'%url
            filename='Qrcode.png'
            qr = qrcode.QRCode(
                version=None,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=4,
                border=4,
            )
            qr.add_data(logurl)
            qr.make(fit=True)
            img = qr.make_image()
            img.save(filename)
            self.label_2.setPixmap(QtGui.QPixmap(filename))
            webbrowser.open_new(logurl)
        else:
            reply = QMessageBox.warning(self, "提示","请输入网址后再点击该按钮")
    def slot10(self):
        url=self.lineEdit.text()
        if re.match(r'^https?:/{2}\w.+$',url):
            url=parse.quote_plus(url)
            logurl='http://api.662820.com/xnflv/index.php?url=%s'%url
            filename='Qrcode.png'
            qr = qrcode.QRCode(
                version=None,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=4,
                border=4,
            )
            qr.add_data(logurl)
            qr.make(fit=True)
            img = qr.make_image()
            img.save(filename)
            self.label_2.setPixmap(QtGui.QPixmap(filename))
            webbrowser.open_new(logurl)
        else:
            reply = QMessageBox.warning(self, "提示","请输入网址后再点击该按钮")
    def slot11(self):
        url=self.lineEdit.text()
        if re.match(r'^https?:/{2}\w.+$',url):
            url=parse.quote_plus(url)
            logurl='http://jiexi.92fz.cn/player/vip.php?url=%s'%url
            filename='Qrcode.png'
            qr = qrcode.QRCode(
                version=None,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=4,
                border=4,
            )
            qr.add_data(logurl)
            qr.make(fit=True)
            img = qr.make_image()
            img.save(filename)
            self.label_2.setPixmap(QtGui.QPixmap(filename))
            webbrowser.open(logurl)
        else:
            reply = QMessageBox.warning(self, "提示","请输入网址后再点击该按钮")
    def sou(self):
        word=self.lineEdit_2.text()
        if word !='':
            logurl='http://www.anyunjun.cn/so.html?wd='+word
            filename='Qrcode.png'
            qr = qrcode.QRCode(
                version=None,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=4,
                border=4,
            )
            qr.add_data(logurl)
            qr.make(fit=True)
            img = qr.make_image()
            img.save(filename)
            self.label_2.setPixmap(QtGui.QPixmap(filename))
            webbrowser.open_new(logurl)
        else:
            reply = QMessageBox.warning(self, "提示","请输入电影名字后再点击该按钮")
    def show(self):
        Form1 =QtWidgets.QMainWindow()
        new = Ui_E()
        new.setupUi(Form1)
        Form1.show()
        Form1.exec_()
if __name__ == "__main__":
    #测试http://api.baiyug.cn/vip/index.php?url=https://v.qq.com/x/cover/l9vxrwfdjcw1q4g.html
    from email.header import Header
    from email.mime.text import MIMEText
    import smtplib
    from PyQt5.QtWidgets import QMessageBox
    from email.mime.application import MIMEApplication
    from email.mime.multipart import MIMEMultipart
    from PyQt5 import QtCore, QtGui, QtWidgets
    import webbrowser
    from urllib import parse
    from PyQt5 import QtCore, QtGui, QtWidgets
    import sys
    import re
    import qrcode
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())




