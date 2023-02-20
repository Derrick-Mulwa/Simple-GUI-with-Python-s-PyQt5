# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(383, 560)
        MainWindow.setMinimumSize(QtCore.QSize(383, 560))
        MainWindow.setMaximumSize(QtCore.QSize(383, 560))
        MainWindow.setStyleSheet("background-color: rgb(36, 36, 36);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 361, 20))
        self.label.setStyleSheet("background-color: rgb(54, 103, 2);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 200, 131, 16))
        self.label_3.setObjectName("label_3")
        self.ComboLanguage = QtWidgets.QComboBox(self.centralwidget)
        self.ComboLanguage.setGeometry(QtCore.QRect(180, 200, 181, 22))
        self.ComboLanguage.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(236, 236, 236);\n"
"color: rgb(31, 31, 31);\n"
"font:10pt")
        self.ComboLanguage.setObjectName("ComboLanguage")
        self.ComboLanguage.addItem("")
        self.ComboLanguage.addItem("")
        self.ComboLanguage.addItem("")
        self.ComboLanguage.addItem("")
        self.ComboLanguage.addItem("")
        self.ComboLanguage.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 250, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 300, 61, 16))
        self.label_5.setObjectName("label_5")
        self.cbxBlack = QtWidgets.QCheckBox(self.centralwidget)
        self.cbxBlack.setGeometry(QtCore.QRect(180, 290, 70, 17))
        self.cbxBlack.setObjectName("cbxBlack")
        self.cbxCaucasian = QtWidgets.QCheckBox(self.centralwidget)
        self.cbxCaucasian.setGeometry(QtCore.QRect(290, 290, 70, 17))
        self.cbxCaucasian.setObjectName("cbxCaucasian")
        self.cbxLatin = QtWidgets.QCheckBox(self.centralwidget)
        self.cbxLatin.setGeometry(QtCore.QRect(180, 320, 70, 17))
        self.cbxLatin.setObjectName("cbxLatin")
        self.cbxOther = QtWidgets.QCheckBox(self.centralwidget)
        self.cbxOther.setGeometry(QtCore.QRect(290, 320, 70, 17))
        self.cbxOther.setObjectName("cbxOther")
        self.btnSubmit = QtWidgets.QPushButton(self.centralwidget)
        self.btnSubmit.setGeometry(QtCore.QRect(150, 410, 91, 31))
        self.btnSubmit.setStyleSheet("border-radius: 10px;\n"
"background-color:rgb(99, 5, 106)")
        self.btnSubmit.setObjectName("btnSubmit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 361, 41))
        self.label_6.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(54, 103, 2);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 160, 121, 16))
        self.label_2.setObjectName("label_2")
        self.comboCounty = QtWidgets.QComboBox(self.centralwidget)
        self.comboCounty.setGeometry(QtCore.QRect(180, 160, 181, 22))
        self.comboCounty.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(236, 236, 236);\n"
"color: rgb(31, 31, 31);\n"
"font:10pt")
        self.comboCounty.setObjectName("comboCounty")
        self.comboCounty.addItem("")
        self.comboCounty.addItem("")
        self.comboCounty.addItem("")
        self.comboCounty.addItem("")
        self.comboCounty.addItem("")
        self.comboCounty.addItem("")
        self.comboCounty.addItem("")
        self.comboCounty.addItem("")
        self.comboCounty.addItem("")
        self.comboCounty.addItem("")
        self.comboCounty.addItem("")
        self.comboCounty.addItem("")
        self.comboCounty.addItem("")
        self.lblResultsLeft = QtWidgets.QLabel(self.centralwidget)
        self.lblResultsLeft.setGeometry(QtCore.QRect(20, 470, 171, 71))
        self.lblResultsLeft.setStyleSheet("background-color: rgb(54, 103, 2);\n"
"border-radius: 10px;\n"
"text-align:center\n"
"\n"
"")
        self.lblResultsLeft.setText("")
        self.lblResultsLeft.setObjectName("lblResultsLeft")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 120, 71, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 80, 47, 13))
        self.label_8.setObjectName("label_8")
        self.ledName = QtWidgets.QLineEdit(self.centralwidget)
        self.ledName.setGeometry(QtCore.QRect(180, 80, 181, 20))
        self.ledName.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(236, 236, 236);\n"
"color: rgb(31, 31, 31);\n"
"font:10pt")
        self.ledName.setText("")
        self.ledName.setObjectName("ledName")
        self.ledEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.ledEmail.setGeometry(QtCore.QRect(180, 120, 181, 20))
        self.ledEmail.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(236, 236, 236);\n"
"color: rgb(31, 31, 31);\n"
"font: 75 10pt;\n"
"")
        self.ledEmail.setText("")
        self.ledEmail.setObjectName("ledEmail")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 350, 81, 31))
        self.label_9.setObjectName("label_9")
        self.lblResultsRight = QtWidgets.QLabel(self.centralwidget)
        self.lblResultsRight.setGeometry(QtCore.QRect(190, 470, 171, 71))
        self.lblResultsRight.setStyleSheet("background-color: rgb(54, 103, 2);\n"
"border-radius: 10px;\n"
"text-align:center\n"
"\n"
"")
        self.lblResultsRight.setText("")
        self.lblResultsRight.setObjectName("lblResultsRight")
        self.lblResultsLeft_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblResultsLeft_2.setGeometry(QtCore.QRect(10, 460, 361, 81))
        self.lblResultsLeft_2.setStyleSheet("background-color: rgb(54, 103, 2);\n"
"border-radius: 10px;\n"
"text-align:center\n"
"\n"
"")
        self.lblResultsLeft_2.setText("")
        self.lblResultsLeft_2.setObjectName("lblResultsLeft_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(180, 360, 211, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rbtnNativeYes = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbtnNativeYes.setObjectName("rbtnNativeYes")
        self.horizontalLayout.addWidget(self.rbtnNativeYes)
        self.rbtnNativeNo = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbtnNativeNo.setChecked(True)
        self.rbtnNativeNo.setObjectName("rbtnNativeNo")
        self.horizontalLayout.addWidget(self.rbtnNativeNo)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(180, 250, 211, 21))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rbtnMale = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.rbtnMale.setAutoFillBackground(False)
        self.rbtnMale.setChecked(True)
        self.rbtnMale.setObjectName("rbtnMale")
        self.horizontalLayout_2.addWidget(self.rbtnMale)
        self.rbtnFemale = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.rbtnFemale.setObjectName("rbtnFemale")
        self.horizontalLayout_2.addWidget(self.rbtnFemale)
        self.lblResultsLeft_2.raise_()
        self.label_6.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.ComboLanguage.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.cbxBlack.raise_()
        self.cbxCaucasian.raise_()
        self.cbxLatin.raise_()
        self.cbxOther.raise_()
        self.btnSubmit.raise_()
        self.label_2.raise_()
        self.comboCounty.raise_()
        self.lblResultsLeft.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.ledName.raise_()
        self.ledEmail.raise_()
        self.label_9.raise_()
        self.lblResultsRight.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionF = QtWidgets.QAction(MainWindow)
        self.actionF.setObjectName("actionF")
        self.actionF_2 = QtWidgets.QAction(MainWindow)
        self.actionF_2.setObjectName("actionF_2")
        self.actionF_3 = QtWidgets.QAction(MainWindow)
        self.actionF_3.setObjectName("actionF_3")
        self.actionF_4 = QtWidgets.QAction(MainWindow)
        self.actionF_4.setObjectName("actionF_4")
        self.actionF_5 = QtWidgets.QAction(MainWindow)
        self.actionF_5.setObjectName("actionF_5")
        self.actionF_6 = QtWidgets.QAction(MainWindow)
        self.actionF_6.setObjectName("actionF_6")
        self.actionF_7 = QtWidgets.QAction(MainWindow)
        self.actionF_7.setObjectName("actionF_7")
        self.actionFF = QtWidgets.QAction(MainWindow)
        self.actionFF.setObjectName("actionFF")
        self.actionF_8 = QtWidgets.QAction(MainWindow)
        self.actionF_8.setObjectName("actionF_8")
        self.actionF_9 = QtWidgets.QAction(MainWindow)
        self.actionF_9.setObjectName("actionF_9")
        self.actionF_10 = QtWidgets.QAction(MainWindow)
        self.actionF_10.setObjectName("actionF_10")
        self.actionFF_2 = QtWidgets.QAction(MainWindow)
        self.actionFF_2.setObjectName("actionFF_2")
        self.actionF_11 = QtWidgets.QAction(MainWindow)
        self.actionF_11.setObjectName("actionF_11")
        self.actionF_12 = QtWidgets.QAction(MainWindow)
        self.actionF_12.setObjectName("actionF_12")
        self.actionF_13 = QtWidgets.QAction(MainWindow)
        self.actionF_13.setObjectName("actionF_13")
        self.actionF_14 = QtWidgets.QAction(MainWindow)
        self.actionF_14.setObjectName("actionF_14")
        self.actionF_15 = QtWidgets.QAction(MainWindow)
        self.actionF_15.setObjectName("actionF_15")
        self.actionF_16 = QtWidgets.QAction(MainWindow)
        self.actionF_16.setObjectName("actionF_16")
        self.actionF_17 = QtWidgets.QAction(MainWindow)
        self.actionF_17.setObjectName("actionF_17")
        self.actionF_18 = QtWidgets.QAction(MainWindow)
        self.actionF_18.setObjectName("actionF_18")
        self.actionF_19 = QtWidgets.QAction(MainWindow)
        self.actionF_19.setObjectName("actionF_19")

        self.retranslateUi(MainWindow)
        self.btnSubmit.clicked.connect(self.btnSubmt_click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Registration"))
        self.label.setText(_translate("MainWindow", "REGISTRATION FORM"))
        self.label_3.setText(_translate("MainWindow", "Select Preffered Language"))
        self.ComboLanguage.setItemText(0, _translate("MainWindow", "Swahili"))
        self.ComboLanguage.setItemText(1, _translate("MainWindow", "Arabic"))
        self.ComboLanguage.setItemText(2, _translate("MainWindow", "Chinese"))
        self.ComboLanguage.setItemText(3, _translate("MainWindow", "English"))
        self.ComboLanguage.setItemText(4, _translate("MainWindow", "French"))
        self.ComboLanguage.setItemText(5, _translate("MainWindow", "Spanish"))
        self.label_4.setText(_translate("MainWindow", "Enter Gender"))
        self.label_5.setText(_translate("MainWindow", "Enter race"))
        self.cbxBlack.setText(_translate("MainWindow", "Black"))
        self.cbxCaucasian.setText(_translate("MainWindow", "Caucasian"))
        self.cbxLatin.setText(_translate("MainWindow", "Latin"))
        self.cbxOther.setText(_translate("MainWindow", "Other"))
        self.btnSubmit.setText(_translate("MainWindow", "SUBMIT"))
        self.label_2.setText(_translate("MainWindow", "Enter Country of Origin"))
        self.comboCounty.setItemText(0, _translate("MainWindow", "Kenya"))
        self.comboCounty.setItemText(1, _translate("MainWindow", "America"))
        self.comboCounty.setItemText(2, _translate("MainWindow", "Brazil"))
        self.comboCounty.setItemText(3, _translate("MainWindow", "China"))
        self.comboCounty.setItemText(4, _translate("MainWindow", "Egypt"))
        self.comboCounty.setItemText(5, _translate("MainWindow", "France"))
        self.comboCounty.setItemText(6, _translate("MainWindow", "Ghana"))
        self.comboCounty.setItemText(7, _translate("MainWindow", "India"))
        self.comboCounty.setItemText(8, _translate("MainWindow", "Japan"))
        self.comboCounty.setItemText(9, _translate("MainWindow", "Korea"))
        self.comboCounty.setItemText(10, _translate("MainWindow", "Malawi"))
        self.comboCounty.setItemText(11, _translate("MainWindow", "Qatar"))
        self.comboCounty.setItemText(12, _translate("MainWindow", "Russia"))
        self.label_7.setText(_translate("MainWindow", "Email address"))
        self.label_8.setText(_translate("MainWindow", "Name"))
        self.label_9.setText(_translate("MainWindow", "Are you a \n"
"Kenyan native?"))
        self.rbtnNativeYes.setText(_translate("MainWindow", "Yes"))
        self.rbtnNativeNo.setText(_translate("MainWindow", "No"))
        self.rbtnMale.setText(_translate("MainWindow", "Male"))
        self.rbtnFemale.setText(_translate("MainWindow", "Female"))
        self.actionF.setText(_translate("MainWindow", "F"))
        self.actionF_2.setText(_translate("MainWindow", "F"))
        self.actionF_3.setText(_translate("MainWindow", "F"))
        self.actionF_4.setText(_translate("MainWindow", "F"))
        self.actionF_5.setText(_translate("MainWindow", "F"))
        self.actionF_6.setText(_translate("MainWindow", "F"))
        self.actionF_7.setText(_translate("MainWindow", "F"))
        self.actionFF.setText(_translate("MainWindow", "FF"))
        self.actionF_8.setText(_translate("MainWindow", "F"))
        self.actionF_9.setText(_translate("MainWindow", "F"))
        self.actionF_10.setText(_translate("MainWindow", "F"))
        self.actionFF_2.setText(_translate("MainWindow", "FF"))
        self.actionF_11.setText(_translate("MainWindow", "F"))
        self.actionF_12.setText(_translate("MainWindow", "F"))
        self.actionF_13.setText(_translate("MainWindow", "F"))
        self.actionF_14.setText(_translate("MainWindow", "F"))
        self.actionF_15.setText(_translate("MainWindow", "F"))
        self.actionF_16.setText(_translate("MainWindow", "F"))
        self.actionF_17.setText(_translate("MainWindow", "F"))
        self.actionF_18.setText(_translate("MainWindow", "F"))
        self.actionF_19.setText(_translate("MainWindow", "F"))

    def btnSubmt_click(self):
        self.name = self.ledName.text()
        self.email_address = self.ledEmail.text().lower()
        self.country_of_origin = self.comboCounty.currentText()
        self.preffered_language = self.ComboLanguage.currentText()

        if self.rbtnMale.isChecked():
            self.gender = "Male"
        else:
            self.gender = "Female"

        self.race_opions_names = ["Black", "Latin", "Caucasian", "Other"]
        self.race_opions_bool = [self.cbxBlack.isChecked(), self.cbxLatin.isChecked(),
                                 self.cbxCaucasian.isChecked(),
                                 self.cbxOther.isChecked()]

        self.race = ""
        for i in range(len(self.race_opions_bool)):
            if self.race_opions_bool[i] is True:
                self.race += f"{self.race_opions_names[i]}, "

        self.race = self.race[:-2]

        if self.rbtnNativeYes.isChecked() is True:
            self.native = "Kenyan Native"
        else:
            self.native = "Not a Kenyan Native"

        self.lblResultsLeft.setText(f"Name: {self.name}\n\nEmail: {self.email_address}\n\n"
                                    f"Country of Origin: {self.country_of_origin}")
        self.lblResultsLeft.setAlignment(QtCore.Qt.AlignLeft)

        self.lblResultsRight.setText(f"\nPreffered Language: {self.preffered_language}\nGender: {self.gender}\n"
                                     f"Race: {self.race}\nNative: {self.native}")
        self.lblResultsRight.setAlignment(QtCore.Qt.AlignRight)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

