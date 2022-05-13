# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'flexible.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QLCDNumber, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_AsiadForm(object):
    def setupUi(self, AsiadForm):
        if not AsiadForm.objectName():
            AsiadForm.setObjectName(u"AsiadForm")
        AsiadForm.resize(473, 781)
        AsiadForm.setStyleSheet(u"background-color: #7b9acc;\n"
"color:#FCF6F5;")
        self.centralwidget = QWidget(AsiadForm)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_7, 4, 2, 1, 1)

        self.ito_time = QComboBox(self.centralwidget)
        self.ito_time.addItem("")
        self.ito_time.addItem("")
        self.ito_time.addItem("")
        self.ito_time.addItem("")
        self.ito_time.addItem("")
        self.ito_time.addItem("")
        self.ito_time.addItem("")
        self.ito_time.addItem("")
        self.ito_time.addItem("")
        self.ito_time.addItem("")
        self.ito_time.addItem("")
        self.ito_time.addItem("")
        self.ito_time.setObjectName(u"ito_time")
        sizePolicy.setHeightForWidth(self.ito_time.sizePolicy().hasHeightForWidth())
        self.ito_time.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.ito_time, 4, 3, 1, 1)

        self.ifm_time = QComboBox(self.centralwidget)
        self.ifm_time.addItem("")
        self.ifm_time.addItem("")
        self.ifm_time.addItem("")
        self.ifm_time.addItem("")
        self.ifm_time.addItem("")
        self.ifm_time.addItem("")
        self.ifm_time.addItem("")
        self.ifm_time.addItem("")
        self.ifm_time.addItem("")
        self.ifm_time.addItem("")
        self.ifm_time.addItem("")
        self.ifm_time.addItem("")
        self.ifm_time.setObjectName(u"ifm_time")
        sizePolicy.setHeightForWidth(self.ifm_time.sizePolicy().hasHeightForWidth())
        self.ifm_time.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.ifm_time, 4, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_10, 4, 4, 1, 1)

        self.icourse = QComboBox(self.centralwidget)
        self.icourse.addItem("")
        self.icourse.addItem("")
        self.icourse.addItem("")
        self.icourse.addItem("")
        self.icourse.setObjectName(u"icourse")
        sizePolicy.setHeightForWidth(self.icourse.sizePolicy().hasHeightForWidth())
        self.icourse.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.icourse, 5, 1, 1, 1)

        self.imember = QPushButton(self.centralwidget)
        self.imember.setObjectName(u"imember")
        sizePolicy.setHeightForWidth(self.imember.sizePolicy().hasHeightForWidth())
        self.imember.setSizePolicy(sizePolicy)
        self.imember.setCheckable(True)

        self.gridLayout.addWidget(self.imember, 1, 4, 1, 1)

        self.iid = QLineEdit(self.centralwidget)
        self.iid.setObjectName(u"iid")
        sizePolicy.setHeightForWidth(self.iid.sizePolicy().hasHeightForWidth())
        self.iid.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.iid, 1, 1, 1, 3)

        self.ipassword = QLineEdit(self.centralwidget)
        self.ipassword.setObjectName(u"ipassword")
        sizePolicy.setHeightForWidth(self.ipassword.sizePolicy().hasHeightForWidth())
        self.ipassword.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.ipassword, 2, 1, 1, 3)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Old English Text MT"])
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 5)

        self.idate = QDateEdit(self.centralwidget)
        self.idate.setObjectName(u"idate")
        sizePolicy.setHeightForWidth(self.idate.sizePolicy().hasHeightForWidth())
        self.idate.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(14)
        self.idate.setFont(font1)
        self.idate.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.idate, 3, 1, 1, 2)

        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setRowStretch(5, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.iproc = QPushButton(self.frame)
        self.iproc.setObjectName(u"iproc")
        sizePolicy.setHeightForWidth(self.iproc.sizePolicy().hasHeightForWidth())
        self.iproc.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(21)
        self.iproc.setFont(font2)

        self.horizontalLayout_3.addWidget(self.iproc)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_8)

        self.ilcdNumber = QLCDNumber(self.frame)
        self.ilcdNumber.setObjectName(u"ilcdNumber")
        sizePolicy.setHeightForWidth(self.ilcdNumber.sizePolicy().hasHeightForWidth())
        self.ilcdNumber.setSizePolicy(sizePolicy)
        self.ilcdNumber.setDigitCount(8)

        self.horizontalLayout.addWidget(self.ilcdNumber)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)

        self.horizontalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.frame)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_2.addWidget(self.label_9)

        self.iresult = QTextBrowser(self.centralwidget)
        self.iresult.setObjectName(u"iresult")

        self.horizontalLayout_2.addWidget(self.iresult)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(2, 5)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        AsiadForm.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AsiadForm)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 473, 26))
        AsiadForm.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AsiadForm)
        self.statusbar.setObjectName(u"statusbar")
        AsiadForm.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.iid, self.imember)
        QWidget.setTabOrder(self.imember, self.ipassword)
        QWidget.setTabOrder(self.ipassword, self.idate)
        QWidget.setTabOrder(self.idate, self.ifm_time)
        QWidget.setTabOrder(self.ifm_time, self.ito_time)
        QWidget.setTabOrder(self.ito_time, self.icourse)
        QWidget.setTabOrder(self.icourse, self.iproc)
        QWidget.setTabOrder(self.iproc, self.iresult)

        self.retranslateUi(AsiadForm)

        QMetaObject.connectSlotsByName(AsiadForm)
    # setupUi

    def retranslateUi(self, AsiadForm):
        AsiadForm.setWindowTitle(QCoreApplication.translate("AsiadForm", u"Asiad country club reservation", None))
        self.label_4.setText(QCoreApplication.translate("AsiadForm", u"\uc120\ud638 \uc2dc\uac04", None))
        self.label_7.setText(QCoreApplication.translate("AsiadForm", u"\ubd80\ud130", None))
        self.ito_time.setItemText(0, QCoreApplication.translate("AsiadForm", u"\uc804\uccb4", None))
        self.ito_time.setItemText(1, QCoreApplication.translate("AsiadForm", u"5\uc2dc", None))
        self.ito_time.setItemText(2, QCoreApplication.translate("AsiadForm", u"6\uc2dc", None))
        self.ito_time.setItemText(3, QCoreApplication.translate("AsiadForm", u"7\uc2dc", None))
        self.ito_time.setItemText(4, QCoreApplication.translate("AsiadForm", u"8\uc2dc", None))
        self.ito_time.setItemText(5, QCoreApplication.translate("AsiadForm", u"9\uc2dc", None))
        self.ito_time.setItemText(6, QCoreApplication.translate("AsiadForm", u"10\uc2dc", None))
        self.ito_time.setItemText(7, QCoreApplication.translate("AsiadForm", u"11\uc2dc", None))
        self.ito_time.setItemText(8, QCoreApplication.translate("AsiadForm", u"12\uc2dc", None))
        self.ito_time.setItemText(9, QCoreApplication.translate("AsiadForm", u"13\uc2dc", None))
        self.ito_time.setItemText(10, QCoreApplication.translate("AsiadForm", u"14\uc2dc", None))
        self.ito_time.setItemText(11, QCoreApplication.translate("AsiadForm", u"15\uc2dc", None))

        self.ifm_time.setItemText(0, QCoreApplication.translate("AsiadForm", u"\uc804\uccb4", None))
        self.ifm_time.setItemText(1, QCoreApplication.translate("AsiadForm", u"5\uc2dc", None))
        self.ifm_time.setItemText(2, QCoreApplication.translate("AsiadForm", u"6\uc2dc", None))
        self.ifm_time.setItemText(3, QCoreApplication.translate("AsiadForm", u"7\uc2dc", None))
        self.ifm_time.setItemText(4, QCoreApplication.translate("AsiadForm", u"8\uc2dc", None))
        self.ifm_time.setItemText(5, QCoreApplication.translate("AsiadForm", u"9\uc2dc", None))
        self.ifm_time.setItemText(6, QCoreApplication.translate("AsiadForm", u"10\uc2dc", None))
        self.ifm_time.setItemText(7, QCoreApplication.translate("AsiadForm", u"11\uc2dc", None))
        self.ifm_time.setItemText(8, QCoreApplication.translate("AsiadForm", u"12\uc2dc", None))
        self.ifm_time.setItemText(9, QCoreApplication.translate("AsiadForm", u"13\uc2dc", None))
        self.ifm_time.setItemText(10, QCoreApplication.translate("AsiadForm", u"14\uc2dc", None))
        self.ifm_time.setItemText(11, QCoreApplication.translate("AsiadForm", u"15\uc2dc", None))

        self.label_3.setText(QCoreApplication.translate("AsiadForm", u"\uc608\uc57d \uc77c\uc790", None))
        self.label_5.setText(QCoreApplication.translate("AsiadForm", u"Password", None))
        self.label_2.setText(QCoreApplication.translate("AsiadForm", u"ID", None))
        self.label_6.setText(QCoreApplication.translate("AsiadForm", u"\uc120\ud638 \ucf54\uc2a4", None))
        self.label_10.setText(QCoreApplication.translate("AsiadForm", u"\uae4c\uc9c0", None))
        self.icourse.setItemText(0, QCoreApplication.translate("AsiadForm", u"\uc804\uccb4", None))
        self.icourse.setItemText(1, QCoreApplication.translate("AsiadForm", u"Lake \ucf54\uc2a4", None))
        self.icourse.setItemText(2, QCoreApplication.translate("AsiadForm", u"Pine \ucf54\uc2a4", None))
        self.icourse.setItemText(3, QCoreApplication.translate("AsiadForm", u"Valley \ucf54\uc2a4", None))

        self.imember.setText(QCoreApplication.translate("AsiadForm", u"\uc815\ud68c\uc6d0", None))
        self.label.setText(QCoreApplication.translate("AsiadForm", u"Asiad country club reservation", None))
        self.iproc.setText(QCoreApplication.translate("AsiadForm", u"\uc608\uc57d\ud558\uae30", None))
        self.label_8.setText(QCoreApplication.translate("AsiadForm", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Count</span></p><p align=\"center\"><span style=\" font-weight:700;\">Down</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("AsiadForm", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Info</span></p></body></html>", None))
    # retranslateUi

