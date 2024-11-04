import os
import ctypes
import time
import sys
import resource_rc
import random

try:
    from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox,
                                 QComboBox, QLabel, QTextEdit)
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5 import QtCore, QtGui, QtWidgets
    import requests
    from bs4 import BeautifulSoup

except ImportError:

    ctypes.windll.user32.MessageBoxW(None, "Ilk defe oldugu ucun lazimi yuklemeler olacaq,60mb+ file yuklenecek, 15-20 deq gozleyeceksiz - [Anketlere Giris hisse gelene dek gozleyin]", "Error-Elave yuklemeler olacaq", 0)
    os.system('python -m pip install requests')
    time.sleep(20)
    os.system('python -m pip install BeautifulSoup') # BeautifulSoup
    time.sleep(30)
    os.system('python -m pip install PyQt5') #PyQt5

finally:
    from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox,
                                 QComboBox, QLabel, QTextEdit)
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5 import QtCore, QtGui, QtWidgets
    import requests
    from bs4 import BeautifulSoup

basliq=[]
head = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36'}
info=[]

class Login(QtWidgets.QDialog):
    def __init__(self):
        super(Login, self).__init__()
        self.s = requests.Session()

        self.textName = QtWidgets.QLineEdit(self)
        self.textName.setPlaceholderText('Meslehetci kodu')
        self.textPass = QtWidgets.QLineEdit(self)
        self.textPass.setPlaceholderText('Sifreniz')
        self.textPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.buttonLogin = QtWidgets.QPushButton('Giris', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        self.basliq = QtWidgets.QLabel("Anketlere Giris")
        self.basliq.setAlignment(Qt.AlignCenter)
        self.basliq.setStyleSheet("font-weight: bold; color: Black; size:14")
        self.basliq.setObjectName("label")



        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.basliq)
        layout.addStretch()
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)
        layout.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(layout)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle("AytekinStat v1.2")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/test.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

    def handleLogin(self):
        url = 'https://www.azstat.org/evtesg/index.jsp'
        url2 = 'https://www.azstat.org/evtesg/body.jsp'
        ##url = 'https://0c2bdebdec3972a29c05bfd4cded89f3.m.pipedream.net' ##deneme url
        data = {'KODINTERVYUER': self.textName.text(), 'PASS': self.textPass.text()}
        self.s.post(url, data=data, headers=head) #login olur
        time.sleep(1)
        html=self.s.post(url2,data=data,headers=head).content #body.jpdan datalari alir
        soup = BeautifulSoup(html, "html.parser")
        for i in soup.find_all("input"):
            a=i.get("value")
            basliq.append(a)
        if  len(basliq) >3:
            time.sleep(0.5)
            urlad = 'https://www.azstat.org/evtesg/profile.jsp?id=' + self.textName.text()
            html = requests.post(urlad, headers=head).content
            soup = BeautifulSoup(html, "html.parser")
            ad = []
            for i in soup.find_all('input'):
                a = i.get("value")
                ad.append(a)
            msg = QMessageBox()
            msg.setText("\n{} firildaq isler gormeye gelib :)".format(ad[0]))
            msg.exec_()

            info.append(self.textName.text())
            info.append(self.textPass.text())  #diger classda login olmaq ucun , Burdaki seesionu ora ata bilmedim

            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Alinmadi', 'Meslehetci kodu ya Parol sehfdi')



class Ui_AytekinStatv12():
    liste = ["01", "02", "03", "04", "05", "06", "07", "08", "09", 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
             23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]
    #liste=["01",43]
    def __init__(self):
        super(Ui_AytekinStatv12, self).__init__()
        self.s = requests.Session()
    def setupUi(self, AytekinStatv12):
        AytekinStatv12.setObjectName("AytekinStat v1.2")
        AytekinStatv12.setEnabled(True)
        AytekinStatv12.resize(664, 690)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/test.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AytekinStatv12.setWindowIcon(icon)
        AytekinStatv12.setStyleSheet("background-color: rgb(236, 239, 240);")
        self.centralwidget = QtWidgets.QWidget(AytekinStatv12)
        self.centralwidget.setObjectName("centralwidget")

        #self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2 = QTextEdit(self.centralwidget)  # QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 150, 491, 501))
        self.textBrowser_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_2.setReadOnly(False)
        a='1  0111312    1   3.00   1.0   2.40   1 \n2  0112530    2   0.70   1.0   3.00   1\n3  0114350    2   3.00   3.0   3.60   1\n4  0118350    1   1.00   1.0   4.00   1\n\nCopy/paste edib Parcala dan sonra usteki kimi forma almalidi '
        self.textBrowser_2.setPlaceholderText(a)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_2.setAcceptRichText(False)  # copy/paste edende formatlari qebul elemesin,xam texti gotursun
        self.textBrowser_2.setUndoRedoEnabled(True)
        self.textBrowser_2.setTabStopDistance(6)

        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(512, 180, 141, 31))
        self.textEdit_4.setReadOnly(True)
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 520, 101, 51))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(616, -62, 141, 161))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/selam.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 360, 161, 161))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/yaz.png"))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 220, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 118, 61, 21))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(61, 21))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setInputMask("")
        self.lineEdit_4.setPlaceholderText("01")
        self.lineEdit_4.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_4.setClearButtonEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(204, -2, 231, 41))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(220, 130, 118, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(226, 117, 211, 21))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(10, 50, 261, 20))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.lineEdit = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit.setMaximumSize(QtCore.QSize(147, 20))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox_2 = QtWidgets.QComboBox(self.splitter)
        self.comboBox_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox = QtWidgets.QComboBox(self.splitter)
        self.comboBox.setMaximumSize(QtCore.QSize(44, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 90, 135, 48))
        self.layoutWidget.setMaximumSize(QtCore.QSize(135, 48))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(133, 20))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(133, 20))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(448, 116, 51, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(528, 118, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(500, 600, 161, 51))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setReadOnly(True)

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(510, 250, 151, 21))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Q061 = QtWidgets.QPushButton(self.widget)
        self.Q061.setObjectName("Q061")
        self.horizontalLayout.addWidget(self.Q061)
        self.Q062 = QtWidgets.QPushButton(self.widget)
        self.Q062.setObjectName("Q062")
        self.horizontalLayout.addWidget(self.Q062)
        self.Q083 = QtWidgets.QPushButton(self.widget)
        self.Q083.setObjectName("Q083")
        self.horizontalLayout.addWidget(self.Q083)
        self.Q085 = QtWidgets.QPushButton(self.widget)
        self.Q085.setObjectName("Q085")
        self.horizontalLayout.addWidget(self.Q085)

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(510, 280, 151, 21))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Q01 = QtWidgets.QPushButton(self.widget)
        self.Q01.setObjectName("Q01")
        self.horizontalLayout_2.addWidget(self.Q01)
        self.Q04 = QtWidgets.QPushButton(self.widget)
        self.Q04.setObjectName("Q04")
        self.horizontalLayout_2.addWidget(self.Q04)
        self.Q071 = QtWidgets.QPushButton(self.widget)
        self.Q071.setObjectName("Q071")
        self.horizontalLayout_2.addWidget(self.Q071)
        self.Q10= QtWidgets.QPushButton(self.widget)
        self.Q10.setObjectName("Q10")
        self.horizontalLayout_2.addWidget(self.Q10)
        self.layoutWidget.raise_()

        self.splitter.raise_()
        self.layoutWidget.raise_()
        self.textBrowser_2.raise_()
        self.textEdit_4.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton_2.raise_()
        self.lineEdit_4.raise_()
        self.textEdit.raise_()
        self.line.raise_()
        self.lineEdit_5.raise_()
        self.pushButton_3.raise_()
        self.lineEdit_6.raise_()
        self.textEdit_2.raise_()
        self.Q085.raise_()
        self.Q061.raise_()
        self.Q062.raise_()
        self.Q083.raise_()
        self.Q04.raise_()
        self.Q071.raise_()
        self.Q01.raise_()
        self.Q10.raise_()

        AytekinStatv12.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AytekinStatv12)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 664, 21))
        self.menubar.setObjectName("menubar")
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        AytekinStatv12.setMenuBar(self.menubar)
        self.actionMursudden_Sevgilerle = QtWidgets.QAction(AytekinStatv12)
        self.actionMursudden_Sevgilerle.setObjectName("actionMursudden_Sevgilerle")
        self.menuMain.addAction(self.actionMursudden_Sevgilerle)
        self.menubar.addAction(self.menuMain.menuAction())

        self.retranslateUi(AytekinStatv12)
        QtCore.QMetaObject.connectSlotsByName(AytekinStatv12)
    def retranslateUi(self, AytekinStatv12):
        _translate = QtCore.QCoreApplication.translate
        AytekinStatv12.setWindowTitle(_translate("AytekinStatv12", "Aytekin Stat v1.2"))
        self.textEdit_4.setHtml(_translate("AytekinStatv12", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sola copy/paste edecen</p></body></html>"))
        self.pushButton.setText(_translate("AytekinStatv12", "Yazmaga Basla"))
        self.pushButton_2.setText(_translate("AytekinStatv12", "Parcala"))
        self.textEdit.setHtml(_translate("AytekinStatv12", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Aytekin Stat v1.2 Bot :)</span></p></body></html>"))
        self.lineEdit_5.setText(_translate("AytekinStatv12", "1-9  arasindaki aileleri 0\'la yaz misal: 07"))
        self.lineEdit.setText(_translate("AytekinStatv12", "Hesabat Dovru -il, rub"))
        self.comboBox_2.setItemText(0, _translate("AytekinStatv12", "2020"))
        self.comboBox_2.setItemText(1, _translate("AytekinStatv12", "2021"))
        self.comboBox_2.setItemText(2, _translate("AytekinStatv12", "2022"))
        self.comboBox_2.setItemText(3, _translate("AytekinStatv12", "2023"))
        self.comboBox.setItemText(0, _translate("AytekinStatv12", "1"))
        self.comboBox.setItemText(1, _translate("AytekinStatv12", "2"))
        self.comboBox.setItemText(2, _translate("AytekinStatv12", "3"))
        self.comboBox.setItemText(3, _translate("AytekinStatv12", "4"))

        self.comboBox.activated[str].connect(self.onChanged)
        self.lineEdit_4.text()

        self.lineEdit_2.setText(_translate("AytekinStatv12", "Meslehetci kodu  :"))
        self.lineEdit_3.setText(_translate("AytekinStatv12", "Aile nomresi  :"))
        self.pushButton_3.setText(_translate("AytekinStatv12", "D2"))
        self.Q061.setText(_translate("AytekinStatv12", "Q061"))
        self.Q062.setText(_translate("AytekinStatv12", "Q062"))
        self.Q083.setText(_translate("AytekinStatv12", "Q083"))
        self.Q085.setText(_translate("AytekinStatv12", "Q085"))
        self.Q04.setText(_translate("AytekinStatv12", "Q04"))
        self.Q071.setText(_translate("AytekinStatv12", "Q071"))
        self.Q01.setText(_translate("AytekinStatv12", "Q01"))
        self.Q10.setText(_translate("AytekinStatv12", "Q10"))

        self.giris()
        self.pushButton_3.clicked.connect(self.get)
        self.pushButton_2.clicked.connect(self.parcala)
        self.pushButton.clicked.connect(self.add)
        self.Q062.clicked.connect(self.q062)
        self.Q061.clicked.connect(self.q061)
        self.Q083.clicked.connect(self.q083)
        self.Q085.clicked.connect(self.q085)
        self.Q04.clicked.connect(self.q04)
        self.Q071.clicked.connect(self.deyil)
        self.Q10.clicked.connect(self.deyil)
        self.Q01.clicked.connect(self.ozun)




        self.textEdit_2.setHtml(_translate("AytekinStatv12", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.menuMain.setTitle(_translate("AytekinStatv12", "Info"))
        self.actionMursudden_Sevgilerle.setText(_translate("AytekinStatv12", "Mursudden Sevgilerle :)"))

    def onChanged(self):
        return self.comboBox.currentText()
    def giris(self):
        url = 'https://www.azstat.org/evtesg/index.jsp'
        url2 = 'https://www.azstat.org/evtesg/body.jsp'
        ##url = 'https://0c2bdebdec3972a29c05bfd4cded89f3.m.pipedream.net' ##deneme url
        data = {'KODINTERVYUER': info[0], 'PASS': info[1]}
        self.s.post(url, data=data, headers=head)  # login olur
        self.s.post(url2, data=data, headers=head)


    def get(self):

        url = 'https://www.azstat.org/evtesg/load.jsp'
        ##url = 'https://0c2bdebdec3972a29c05bfd4cded89f3.m.pipedream.net' ## deneme url
        data = {'AREAL': basliq[2], 'DOVR': self.comboBox.currentText(), 'HHNUMBER': self.lineEdit_4.text(), 'IL': self.comboBox_2.currentText(), 'INTERVYUER': basliq[3], 'KODARAZI': basliq[0],
                'KODZONA': basliq[1], 'button': 'D2', 'metod': '0'}
        html = self.s.post(url, data=data, headers=head).content
        soup = BeautifulSoup(html, "html.parser")
        HHID=""
        for i in soup.find_all("div",{"class":"rc-title"}):
            HHID=i.text
        self.lineEdit_6.setText(HHID)

        #return self.s.post(url, data=data, headers=head)

    def parcala(self):
        m = self.textBrowser_2.toPlainText()
        m = m.rstrip()  # sonda bosliq qalanda eror verir deye sondakini temizlesin
        self.dica = list()
        kodlar = ""  # Proqdaki kod blokundaki info
        warning = "Parcalama prosesi alinmadi, Daxil olunacaq mehsullarin siyahisini yeniden copy/paste et  #Beceriksiz \n\n\n\nYene alinmasa yaradininan Sorus :)"
        # writing to file
        file1 = open('hk1.txt', 'w')
        file1.writelines(m)
        file1.close()
        # oxu gulum
        try:
            with open("hk1.txt", 'r') as file:
                for i in file:
                    i = i.split()
                    i[4] = float(i[4])
                    if (i[4] == 1 or i[4] == 3 or i[4] == 4):
                        data = {'LINE': i[0], 'CODE': i[1], 'WHERE1': i[2], 'QUANT': i[3], 'MEASURE': i[4],
                                'AMOUNT': i[5],
                                'FROWHOM': i[6], 'd2_8': 'Yaz'}
                        kodlar = kodlar + i[0] + "  " + i[1] + "    " + i[2] + "   " + str(i[3]) + "   " + str(
                            i[4]) + "   " + str(i[5]) + "   " + i[6] + "\n"
                        self.dica.append(data)
                    else:
                        i[5] = str(i[4])
                        i[4] = str("")
                        i[6] = '1'
                        data = {'LINE': i[0], 'CODE': i[1], 'WHERE1': i[2], 'QUANT': i[3], 'MEASURE': i[4],
                                'AMOUNT': i[5],
                                'FROWHOM': i[6], 'd2_8': 'Yaz'}
                        kodlar = kodlar + i[0] + "  " + i[1] + "    " + i[2] + "   " + str(i[3]) + "   " + str(
                            i[4]) + "   " + str(i[5]) + "   " + i[6] + "\n"
                        self.dica.append(data)
            self.textBrowser_2.setText(kodlar)

        except Exception:
            self.textBrowser_2.setText(warning) #parcalama islemi alinmadi mesaji

        return self.dica

    def add(self):
        url = 'https://www.azstat.org/evtesg/d2.jsp?metod=1'
        ##url = 'https://enmjezaa2bznd.x.pipedream.net/' ## deneme url
        i = 0
        while True:
            if  not(i > (len(self.dica) - 1)):
                self.s.post(url, data=self.dica[i], headers=head)
                self.textEdit_2.setStyleSheet("background-color: rgb(0,255,0);")
                self.textEdit_2.setText("\n {}-cu mehsul yazilir... \n    ".format(i))
                QApplication.processEvents()
                time.sleep(2)
            else:
                self.textEdit_2.setStyleSheet("background-color: rgb(255,10,10);")
                self.textEdit_2.setText("\n Umumilikde {} mehsul yazildi ".format(i))
                QApplication.processEvents()
                break
            i += 1

    def q062(self):
        q062url = 'https://www.azstat.org/evtesg/q062.jsp?metod=1'
        url = 'https://www.azstat.org/evtesg/load.jsp'
        tibb = ["", 1, 2]
        aileno = 1
        for i in self.liste:
            data = {'AREAL': basliq[2], 'DOVR': self.comboBox.currentText(), 'HHNUMBER': i,
                    'IL': self.comboBox_2.currentText(),
                    'INTERVYUER': basliq[3],
                    'KODARAZI': basliq[0], 'KODZONA': basliq[1], 'button': 'Q062', 'metod': '0'}

            self.s.post(url, data=data, headers=head)  # Q062'naa kec
            time.sleep(1)
            q062data = {'SERV01': '', 'SERV02': random.choice(tibb), 'SERV03': '', 'SERV04': '', 'SERV05': '',
                        'SERV06': random.randrange(1, 3, 1), 'SERV07': '', 'SERV08': '', 'SERV09': '', 'SERV10': '',
                        'q62_11': 'Yaz'}
            self.textEdit_2.setStyleSheet("background-color: rgb(0,255,0);")
            self.textEdit_2.setText("\n {}-cu ailenin Q062 yazilir... \n    ".format(i))
            QApplication.processEvents()
            self.s.post(q062url, data=q062data, headers=head)  # Q062 yazildi
            time.sleep(1)
            if i == 43:
              self.textEdit_2.setStyleSheet("background-color: rgb(255,10,10);")
              self.textEdit_2.setText("\n Butun Q062-ler yazildi :) \n    ")
              QApplication.processEvents()

    def q061(self):
        q061url = 'https://www.azstat.org/evtesg/q061.jsp?metod=1'
        url = 'https://www.azstat.org/evtesg/load.jsp'
        hekim = [1,1,2,2,2,6,6]
        qiymeti=['', '', '', '','',15, 15, 20, 20, 30, 35, 30, 40, 60, '' ]
        for i in self.liste:
            data = {'AREAL': basliq[2], 'DOVR': self.comboBox.currentText(), 'HHNUMBER': i,
                    'IL': self.comboBox_2.currentText(),
                    'INTERVYUER': basliq[3],
                    'KODARAZI': basliq[0], 'KODZONA': basliq[1], 'button': 'Q061', 'metod': '0'}
            self.s.post(url, data=data, headers=head)  # Q062'naa kec
            time.sleep(1)
            q061data = {'EXPENCE': random.choice(hekim), 'SUM1': random.choice(qiymeti), 'SUM2':random.choice(qiymeti), 'SUM3': random.choice(qiymeti),'q61_5': 'Yaz'}
            self.textEdit_2.setStyleSheet("background-color: rgb(0,255,0);")
            self.textEdit_2.setText("\n {}-cu ailenin Q062 yazilir... \n ".format(i))
            QApplication.processEvents()
            self.s.post(q061url, data=q061data, headers=head)  # Q062 yazildi
            time.sleep(1)
            lista = [1, 1, 1, 1, 1, 2]
            if random.choice(lista)==2:
                time.sleep(0.5)
                q061data = {'EXPENCE': 4, 'SUM1':'' ,
                            'SUM2': random.choice([35,40,55,60]), 'SUM3':'', 'q61_5': 'Yaz'}
                self.s.post(q061url, data=q061data, headers=head)  # Q062 yazildi
            if i == 43:
                self.textEdit_2.setStyleSheet("background-color: rgb(255,10,10);")
                self.textEdit_2.setText("\n Butun Q061-ler yazildi :) \n    ")
                QApplication.processEvents()
    def q083(self):
        q083url = 'https://www.azstat.org/evtesg/q083.jsp?metod=1'
        url = 'https://www.azstat.org/evtesg/load.jsp'
        for i in self.liste:
            data = {'AREAL': basliq[2], 'DOVR': self.comboBox.currentText(), 'HHNUMBER': i,
                    'IL': self.comboBox_2.currentText(),
                    'INTERVYUER': basliq[3],
                    'KODARAZI': basliq[0], 'KODZONA': basliq[1], 'button': 'Q083', 'metod': '0'}
            self.s.post(url, data=data, headers=head)  # Q083'naa kec
            time.sleep(1)
            q083data = {'INCOME': 14, 'SUM1': '', 'SUM2': '', 'SUM3': 30, 'q83_5': 'Yaz'}
            self.textEdit_2.setStyleSheet("background-color: rgb(0,255,0);")
            self.textEdit_2.setText("\n {}-cu ailenin Q083 yazilir... \n    ".format(i))
            QApplication.processEvents()
            self.s.post(q083url, data=q083data, headers=head)  # Q083 yazildi
            time.sleep(1)
            if i == 43:
                self.textEdit_2.setStyleSheet("background-color: rgb(255,10,10);")
                self.textEdit_2.setText("\n Butun Q083-ler yazildi :) \n    ")
                QApplication.processEvents()
    def q085(self):
        q085url = 'https://www.azstat.org/evtesg/q085.jsp?metod=1'
        url = 'https://www.azstat.org/evtesg/load.jsp'
        for i in self.liste:
            data = {'AREAL': basliq[2], 'DOVR': self.comboBox.currentText(), 'HHNUMBER': i,
                    'IL': self.comboBox_2.currentText(),
                    'INTERVYUER': basliq[3],
                    'KODARAZI': basliq[0], 'KODZONA': basliq[1], 'button': 'Q085', 'metod': '0'}
            self.s.post(url, data=data, headers=head)  # Q083'naa kec
            time.sleep(1)
            q085data={'HOWMANY1':random.choice([1600,1500,1200,1400]), 'HOWMANY2':random.choice([400,450,500,550]), 'INC851=':'', 'INC852=':'','INC853=':'','INC854=':'','INC855=':'','INC856=':'','INC857=':'','SATISFY=':random.choice([2,3,4]),'q85_9': 'Yaz'}
            self.textEdit_2.setStyleSheet("background-color: rgb(0,255,0);")
            self.textEdit_2.setText("\n {}-cu ailenin Q085 yazilir... \n    ".format(i))
            QApplication.processEvents()
            self.s.post(q085url, data=q085data, headers=head)  # Q085 yazildi
            time.sleep(1)
            if i == 43:
                self.textEdit_2.setStyleSheet("background-color: rgb(255,10,10);")
                self.textEdit_2.setText("\n Butun Q085-ler yazildi :) \n    ")
                QApplication.processEvents()

    def q04(self):
        q04url = 'https://www.azstat.org/evtesg/q04_list.jsp?metod=1'
        url = 'https://www.azstat.org/evtesg/load.jsp'
        for a in self.liste:
            data = {'AREAL': basliq[2], 'DOVR': self.comboBox.currentText(), 'HHNUMBER': a,
                    'IL': self.comboBox_2.currentText(),
                    'INTERVYUER': basliq[3],
                    'KODARAZI': basliq[0], 'KODZONA': basliq[1], 'button': 'Q04', 'metod': '0'}
            basliq01 = []
            q04data = {"q4_8": "Yaz", "s10_1": "", "s10_2": "", "s10_3": "", "s11_1": "", "s11_2": "", "s11_3": "",
                           "s12_1": "",
                           "s12_2": "", "s12_3": "", "s13_1": "", "s13_2": "", "s13_3": "", "s14_1": "", "s14_2": "",
                           "s14_3": "",
                           "s15_1": "", "s15_2": "", "s15_3": "", "s16_1": "", "s16_2": "", "s16_3": "", "s17_1": "",
                           "s17_2": "",
                           "s17_3": "", "s18_1": "", "s18_2": "", "s18_3": "", "s19_1": "", "s19_2": "", "s19_3": "",
                           "s1_1": "",
                           "s1_2": "", "s1_3": "", "s20_1": "", "s20_2": "", "s20_3": "", "s21_1": "", "s21_2": "",
                           "s21_3": "",
                           "s22_1": "", "s22_2": "", "s22_3": "", "s23_1": "", "s23_2": "", "s23_3": "", "s2_1":"" ,
                           "s2_2": "",
                           "s2_3": "", "s3_1": "", "s3_2": "", "s3_3": "", "s4_1": "", "s4_2": "", "s4_3": "",
                           "s5_1": "",
                           "s5_2": "",
                           "s5_3": "", "s6_1": "", "s6_2": "", "s6_3": "", "s7_1": "", "s7_2": "", "s7_3": "",
                           "s8_1": "",
                           "s8_2": "",
                           "s8_3": "", "s9_1": "", "s9_2": "", "s9_3": ""}
            data = {'AREAL': basliq[2], 'DOVR': self.comboBox.currentText(), 'HHNUMBER': a,
                        'IL': self.comboBox_2.currentText(),
                        'INTERVYUER': basliq[3],
                        'KODARAZI': basliq[0], 'KODZONA': basliq[1], 'button': 'Q04', 'metod': '0'}
            url1 = "https://www.azstat.org/evtesg/newjsp.jsp?IL=2020&DOVR=2&INTERVYUER="+str(info[0]) + "&HHNUMBER="+str(a)
            self.textEdit_2.setStyleSheet("background-color: rgb(0,255,0);")
            self.textEdit_2.setText("\n {}-cu ailenin Q04 yazilir... \n    ".format(a))
            QApplication.processEvents()
            html = self.s.post(url=url1, headers=head).content  # aa kec icini al
            time.sleep(3)
            soup = BeautifulSoup(html, "html.parser")
            table = soup.find(id="questionQ04")
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                basliq01.append([ele for ele in cols if ele])  # Get rid of empty values
            uzunluq = len(basliq01[0][1:])
            xercnov = []
            for i in basliq01[0][0:]:
                i = "s" + str(i) + "_1"
                xercnov.append(i)
            count=1
            while uzunluq > 0:
                for i in xercnov[1:]:
                    if i in q04data:
                        q04data[i] = basliq01[1][count]  # 1ci Ay
                        # print(i,a[i])
                        i = i[:-1] + "2"
                        q04data[i] = basliq01[2][count]  # 2ci Ay
                        i = i[:-1] + "3"
                        q04data[i] = basliq01[3][count]  # 3ci Ay
                        count+=1
                    uzunluq -= 1
            if "s2_1" in q04data:
                q04data["s2_1"] = float(q04data["s2_1"]) + random.choice([1, 2, -1,-2])
                q04data["s2_2"] = float(q04data["s2_2"]) + random.choice([1, 2, -1,-2])
                q04data["s2_3"] = float(q04data["s2_3"]) + random.choice([1, 2, -1,-2])

                q04data["s3_1"] = float(q04data["s3_1"])  + random.choice([1, 2, -1,-2])
                q04data["s3_2"] = float(q04data["s3_2"])  + random.choice([1, 2, -1,-2])
                q04data["s3_3"] = float(q04data["s3_3"])  + random.choice([1, 2, -1,-2])

                q04data["s4_1"] = float(q04data["s4_1"])  + random.choice([1, 2, -1,-2])
                q04data["s4_2"] = float(q04data["s4_2"])  + random.choice([1, 2, -1,-2])
                q04data["s4_3"] = float(q04data["s4_3"])  + random.choice([1, 2, -1,-2])
            self.s.post(url=url, data=data, headers=head)  # Q04a kec
            time.sleep(2)
            self.s.post(q04url, data=q04data, headers=head)  # Q04 yazildi
            time.sleep(1)
            if a == 43:
                self.textEdit_2.setStyleSheet("background-color: rgb(255,10,10);")
                self.textEdit_2.setText("\n Butun Q04-ler yazildi :) \n    ")
                QApplication.processEvents()

    def deyil(self):

        self.textEdit_2.setStyleSheet("background-color: rgb(255,10,10);")
        self.textEdit_2.setText("\n Aktiv Deyil \n    ")
    def ozun(self):

        self.textEdit_2.setStyleSheet("background-color: rgb(255,10,10);")
        self.textEdit_2.setText("\n Beke bunu da ozun yazasan :)\n    ")


class MyWin(QtWidgets.QMainWindow, Login):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self)


        self.ui = Ui_AytekinStatv12()
        self.ui.setupUi(self)


if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)
    login = Login()
    if login.exec_() == QtWidgets.QDialog.Accepted:
        window = MyWin()
        window.show()
        sys.exit(app.exec_())
#son hal
