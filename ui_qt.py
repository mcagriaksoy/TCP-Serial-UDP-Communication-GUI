# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_qt(object):
    def setupUi(self, qt):
        if not qt.objectName():
            qt.setObjectName(u"qt")
        qt.resize(740, 556)
        qt.setMinimumSize(QSize(740, 556))
        qt.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        icon = QIcon()
        icon.addFile(u"index.jpeg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        qt.setWindowIcon(icon)
        qt.setWindowOpacity(0.990000000000000)
        self.actionAna_Ekran = QAction(qt)
        self.actionAna_Ekran.setObjectName(u"actionAna_Ekran")
        self.centralwidget = QWidget(qt)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(740, 556))
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 731, 511))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.gridLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setAutoFillBackground(False)
        self.verticalLayoutWidget_2 = QWidget(self.tab)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 3, 531, 361))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.textEdit_8 = QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.textEdit_8)

        self.formLayoutWidget = QWidget(self.tab)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(540, 0, 188, 141))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.comboBox_1 = QComboBox(self.formLayoutWidget)
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.setObjectName(u"comboBox_1")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.comboBox_1)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.comboBox_2 = QComboBox(self.formLayoutWidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.comboBox_2)

        self.label_11 = QLabel(self.formLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_11)

        self.pushButton_4 = QPushButton(self.formLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.pushButton_4)

        self.comboBox = QComboBox(self.formLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.comboBox)

        self.label_12 = QLabel(self.formLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_12)

        self.formLayoutWidget_2 = QWidget(self.tab)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(540, 340, 171, 21))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.label_5 = QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_5)

        self.verticalLayoutWidget = QWidget(self.tab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(540, 150, 181, 181))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout.addWidget(self.label_10)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.progressBar = QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)

        self.textEdit = QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(390, 390, 121, 31))
        self.pushButton_5 = QPushButton(self.tab)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(590, 390, 121, 31))
        self.textEdit_2 = QTextEdit(self.tab)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(0, 390, 391, 31))
        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 359, 451, 31))
        self.pushButton_14 = QPushButton(self.tab)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(510, 390, 81, 31))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.textEdit_4 = QTextEdit(self.tab_2)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(0, 40, 591, 171))
        self.pushButton_6 = QPushButton(self.tab_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(600, 40, 121, 51))
        self.pushButton_7 = QPushButton(self.tab_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(600, 100, 121, 51))
        self.label_14 = QLabel(self.tab_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(0, 20, 121, 21))
        self.textEdit_6 = QTextEdit(self.tab_2)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(0, 260, 591, 161))
        self.label_16 = QLabel(self.tab_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(0, 240, 121, 16))
        self.pushButton_8 = QPushButton(self.tab_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(600, 270, 121, 51))
        self.progressBar_2 = QProgressBar(self.tab_2)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setGeometry(QRect(600, 330, 118, 23))
        self.progressBar_2.setValue(0)
        self.horizontalLayoutWidget = QWidget(self.tab_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(403, 230, 341, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.horizontalLayoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout.addWidget(self.label_13)

        self.textEdit_5 = QTextEdit(self.horizontalLayoutWidget)
        self.textEdit_5.setObjectName(u"textEdit_5")

        self.horizontalLayout.addWidget(self.textEdit_5)

        self.horizontalLayoutWidget_3 = QWidget(self.tab_2)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(162, 0, 661, 31))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.horizontalLayoutWidget_3)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_4.addWidget(self.label_22)

        self.textEdit_11 = QTextEdit(self.horizontalLayoutWidget_3)
        self.textEdit_11.setObjectName(u"textEdit_11")

        self.horizontalLayout_4.addWidget(self.textEdit_11)

        self.label_15 = QLabel(self.horizontalLayoutWidget_3)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_4.addWidget(self.label_15)

        self.textEdit_7 = QTextEdit(self.horizontalLayoutWidget_3)
        self.textEdit_7.setObjectName(u"textEdit_7")

        self.horizontalLayout_4.addWidget(self.textEdit_7)

        self.label_20 = QLabel(self.tab_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(120, 210, 251, 51))
        self.label_20.setPixmap(QPixmap(u"Desktop/Intern/udppackets.png"))
        self.label_20.setScaledContents(True)
        self.pushButton_12 = QPushButton(self.tab_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(600, 360, 121, 41))
        self.label_19 = QLabel(self.tab_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(600, 170, 111, 29))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.textEdit_3 = QTextEdit(self.tab_3)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(0, 40, 591, 291))
        self.horizontalLayoutWidget_2 = QWidget(self.tab_3)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(220, 0, 501, 31))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.horizontalLayoutWidget_2)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_3.addWidget(self.label_17)

        self.textEdit_10 = QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit_10.setObjectName(u"textEdit_10")

        self.horizontalLayout_3.addWidget(self.textEdit_10)

        self.label_23 = QLabel(self.horizontalLayoutWidget_2)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_3.addWidget(self.label_23)

        self.textEdit_12 = QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit_12.setObjectName(u"textEdit_12")

        self.horizontalLayout_3.addWidget(self.textEdit_12)

        self.pushButton_11 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout_3.addWidget(self.pushButton_11)

        self.label_18 = QLabel(self.tab_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 20, 221, 16))
        self.label_21 = QLabel(self.tab_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(170, 340, 361, 71))
        self.label_21.setPixmap(QPixmap(u"Desktop/Intern/tcpstream.png"))
        self.label_21.setScaledContents(True)
        self.pushButton_9 = QPushButton(self.tab_3)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(600, 50, 121, 61))
        self.pushButton_10 = QPushButton(self.tab_3)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(600, 110, 121, 61))
        self.label_24 = QLabel(self.tab_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(0, 340, 221, 16))
        self.pushButton_15 = QPushButton(self.tab_3)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(0, 360, 151, 51))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.pushButton_37 = QPushButton(self.tab_4)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setGeometry(QRect(600, 150, 121, 51))
        self.pushButton_38 = QPushButton(self.tab_4)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setGeometry(QRect(600, 50, 121, 31))
        self.progressBar_10 = QProgressBar(self.tab_4)
        self.progressBar_10.setObjectName(u"progressBar_10")
        self.progressBar_10.setGeometry(QRect(600, 120, 121, 20))
        self.progressBar_10.setValue(0)
        self.textEdit_37 = QTextEdit(self.tab_4)
        self.textEdit_37.setObjectName(u"textEdit_37")
        self.textEdit_37.setGeometry(QRect(0, 40, 591, 151))
        self.pushButton_39 = QPushButton(self.tab_4)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setGeometry(QRect(600, 80, 121, 31))
        self.horizontalLayoutWidget_10 = QWidget(self.tab_4)
        self.horizontalLayoutWidget_10.setObjectName(u"horizontalLayoutWidget_10")
        self.horizontalLayoutWidget_10.setGeometry(QRect(150, 0, 571, 72))
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_72 = QLabel(self.horizontalLayoutWidget_10)
        self.label_72.setObjectName(u"label_72")

        self.horizontalLayout_13.addWidget(self.label_72)

        self.textEdit_38 = QTextEdit(self.horizontalLayoutWidget_10)
        self.textEdit_38.setObjectName(u"textEdit_38")

        self.horizontalLayout_13.addWidget(self.textEdit_38)

        self.label_73 = QLabel(self.horizontalLayoutWidget_10)
        self.label_73.setObjectName(u"label_73")

        self.horizontalLayout_13.addWidget(self.label_73)

        self.textEdit_39 = QTextEdit(self.horizontalLayoutWidget_10)
        self.textEdit_39.setObjectName(u"textEdit_39")

        self.horizontalLayout_13.addWidget(self.textEdit_39)

        self.pushButton_13 = QPushButton(self.horizontalLayoutWidget_10)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.horizontalLayout_13.addWidget(self.pushButton_13)

        self.label_74 = QLabel(self.tab_4)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(0, 10, 201, 16))
        self.label_71 = QLabel(self.tab_4)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(270, 200, 321, 61))
        self.label_71.setPixmap(QPixmap(u"Desktop/Intern/tcpstream.png"))
        self.label_71.setScaledContents(True)
        self.label_75 = QLabel(self.tab_4)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(0, 200, 231, 21))
        self.pushButton_16 = QPushButton(self.tab_4)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(200, 270, 171, 61))
        self.pushButton_17 = QPushButton(self.tab_4)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(0, 220, 201, 41))
        self.label = QLabel(self.tab_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 220, 51, 41))
        self.label.setPixmap(QPixmap(u"1.jpg"))
        self.label.setScaledContents(True)
        self.verticalLayoutWidget_3 = QWidget(self.tab_4)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(-1, 270, 201, 61))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.verticalLayoutWidget_3)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_3.addWidget(self.label_25)

        self.label_26 = QLabel(self.verticalLayoutWidget_3)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_3.addWidget(self.label_26)

        self.label_27 = QLabel(self.tab_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(600, 220, 121, 31))
        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        qt.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(qt)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 740, 21))
        self.menuAna_Ekran = QMenu(self.menubar)
        self.menuAna_Ekran.setObjectName(u"menuAna_Ekran")
        self.hakkinda = QMenu(self.menubar)
        self.hakkinda.setObjectName(u"hakkinda")
        qt.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(qt)
        self.statusbar.setObjectName(u"statusbar")
        qt.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAna_Ekran.menuAction())
        self.menubar.addAction(self.hakkinda.menuAction())

        self.retranslateUi(qt)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(qt)
    # setupUi

    def retranslateUi(self, qt):
        qt.setWindowTitle(QCoreApplication.translate("qt", u"PyQT ile TCP-UDP-Seri Haberle\u015fme Program\u0131", None))
#if QT_CONFIG(statustip)
        qt.setStatusTip(QCoreApplication.translate("qt", u"Mehmet Cagri Aksoy 2018", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        qt.setWhatsThis(QCoreApplication.translate("qt", u"Serial Communication Program", None))
#endif // QT_CONFIG(whatsthis)
        self.actionAna_Ekran.setText(QCoreApplication.translate("qt", u"Ana Ekran", None))
#if QT_CONFIG(whatsthis)
        self.tabWidget.setWhatsThis(QCoreApplication.translate("qt", u"<html><head/><body><p>UDP Tab</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.tab.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.label_3.setText(QCoreApplication.translate("qt", u" Al\u0131nan / G\u00f6nderilen Veri (Rx/Tx)", None))
        self.label_2.setText(QCoreApplication.translate("qt", u"PORT Ad\u0131:", None))
        self.label_6.setText(QCoreApplication.translate("qt", u"Baud Oran\u0131:", None))
        self.comboBox_1.setItemText(0, QCoreApplication.translate("qt", u"Se\u00e7iniz...", None))
        self.comboBox_1.setItemText(1, QCoreApplication.translate("qt", u"1200", None))
        self.comboBox_1.setItemText(2, QCoreApplication.translate("qt", u"2400", None))
        self.comboBox_1.setItemText(3, QCoreApplication.translate("qt", u"4800", None))
        self.comboBox_1.setItemText(4, QCoreApplication.translate("qt", u"9600", None))
        self.comboBox_1.setItemText(5, QCoreApplication.translate("qt", u"19200", None))
        self.comboBox_1.setItemText(6, QCoreApplication.translate("qt", u"38400", None))
        self.comboBox_1.setItemText(7, QCoreApplication.translate("qt", u"57600", None))
        self.comboBox_1.setItemText(8, QCoreApplication.translate("qt", u"115200", None))

        self.label_7.setText(QCoreApplication.translate("qt", u"Boyut (B):", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("qt", u"Se\u00e7iniz...", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("qt", u"2", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("qt", u"4", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("qt", u"8", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("qt", u"16", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("qt", u"32", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("qt", u"64", None))

        self.label_11.setText(QCoreApplication.translate("qt", u"-", None))
        self.pushButton_4.setText(QCoreApplication.translate("qt", u"Kaydet", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("qt", u"Se\u00e7iniz...", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("qt", u"0", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("qt", u"2", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("qt", u"4", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("qt", u"6", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("qt", u"8", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("qt", u"10", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("qt", u"15", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("qt", u"20", None))

        self.label_12.setText(QCoreApplication.translate("qt", u"Zaman A\u015f\u0131m\u0131:", None))
        self.label_4.setText(QCoreApplication.translate("qt", u"Port Durumu:", None))
        self.label_5.setText(QCoreApplication.translate("qt", u"Ba\u011fl\u0131 De\u011fil", None))
        self.label_10.setText(QCoreApplication.translate("qt", u"Ba\u011flant\u0131 Se\u00e7enekleri:", None))
        self.pushButton_2.setText(QCoreApplication.translate("qt", u"DURDUR", None))
        self.pushButton.setText(QCoreApplication.translate("qt", u"BA\u015eLAT", None))
        self.label_8.setText(QCoreApplication.translate("qt", u"Ba\u011flant\u0131 Y\u00fczde \u00c7ubu\u011fu:", None))
        self.pushButton_3.setText(QCoreApplication.translate("qt", u"G\u00f6nder", None))
        self.pushButton_5.setText(QCoreApplication.translate("qt", u".txt Olarak Kaydet", None))
        self.label_9.setText(QCoreApplication.translate("qt", u" Veri G\u00f6nder:", None))
        self.pushButton_14.setText(QCoreApplication.translate("qt", u"HEX", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("qt", u"Seri Haberle\u015fme (COM, /USB)", None))
        self.pushButton_6.setText(QCoreApplication.translate("qt", u"Dinlemeye Ba\u015fla", None))
        self.pushButton_7.setText(QCoreApplication.translate("qt", u"Dinlemeyi Durdur!", None))
        self.label_14.setText(QCoreApplication.translate("qt", u"UDP Al\u0131c\u0131s\u0131:", None))
        self.label_16.setText(QCoreApplication.translate("qt", u"UDP Mesaj \u0130letici:", None))
        self.pushButton_8.setText(QCoreApplication.translate("qt", u"G\u00f6nder!", None))
        self.label_13.setText(QCoreApplication.translate("qt", u"Mesaj G\u00f6nderim Portunu Giriniz:", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("qt", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:10pt;\">80</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("qt", u"IP Giriniz:", None))
        self.textEdit_11.setHtml(QCoreApplication.translate("qt", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:10pt;\">255.255.255.255</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("qt", u"Dinleme Portu Giriniz", None))
        self.textEdit_7.setHtml(QCoreApplication.translate("qt", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:10pt;\">80</span></p></body></html>", None))
        self.label_20.setText("")
        self.pushButton_12.setText(QCoreApplication.translate("qt", u".TXT Olarak Kaydet!", None))
        self.label_19.setText(QCoreApplication.translate("qt", u"Ba\u011flant\u0131 YOK!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("qt", u"UDP - BROADCAST", None))
        self.label_17.setText(QCoreApplication.translate("qt", u"IP:", None))
        self.textEdit_10.setHtml(QCoreApplication.translate("qt", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Ubuntu'; font-size:10pt;\"><br /></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("qt", u"Port:", None))
        self.textEdit_12.setHtml(QCoreApplication.translate("qt", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:10pt;\">4444</span></p></body></html>", None))
        self.pushButton_11.setText(QCoreApplication.translate("qt", u"KAYDET", None))
        self.label_18.setText(QCoreApplication.translate("qt", u"SERVER'DAN GELEN VER\u0130LER\u0130 AL:", None))
        self.label_21.setText("")
        self.pushButton_9.setText(QCoreApplication.translate("qt", u"Dinle", None))
        self.pushButton_10.setText(QCoreApplication.translate("qt", u"Portu Kapat!", None))
        self.label_24.setText(QCoreApplication.translate("qt", u"Server'den Dosya Al:", None))
        self.pushButton_15.setText(QCoreApplication.translate("qt", u"Dosya Konumunu A\u00e7", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("qt", u"TCP - CLIENT", None))
        self.pushButton_37.setText(QCoreApplication.translate("qt", u"G\u00f6nder", None))
        self.pushButton_38.setText(QCoreApplication.translate("qt", u"Yay\u0131na BA\u015eLA!", None))
        self.textEdit_37.setHtml(QCoreApplication.translate("qt", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:10pt;\">deneme</span></p></body></html>", None))
        self.pushButton_39.setText(QCoreApplication.translate("qt", u"Portu Kapat!", None))
        self.label_72.setText(QCoreApplication.translate("qt", u"IP:", None))
        self.textEdit_38.setHtml(QCoreApplication.translate("qt", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:10pt;\">127.0.0.1</span></p></body></html>", None))
        self.label_73.setText(QCoreApplication.translate("qt", u"Port:", None))
        self.textEdit_39.setHtml(QCoreApplication.translate("qt", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:10pt;\">4444</span></p></body></html>", None))
        self.pushButton_13.setText(QCoreApplication.translate("qt", u"KAYDET", None))
        self.label_74.setText(QCoreApplication.translate("qt", u"G\u00f6nderici:", None))
        self.label_71.setText("")
        self.label_75.setText(QCoreApplication.translate("qt", u"Dosya G\u00f6nder:", None))
        self.pushButton_16.setText(QCoreApplication.translate("qt", u"Dosya G\u00f6nder", None))
        self.pushButton_17.setText(QCoreApplication.translate("qt", u"G\u00f6nderilecek Dosyay\u0131 Se\u00e7iniz...", None))
        self.label.setText("")
        self.label_25.setText(QCoreApplication.translate("qt", u"Se\u00e7ili Dosya:", None))
        self.label_26.setText(QCoreApplication.translate("qt", u"-", None))
        self.label_27.setText(QCoreApplication.translate("qt", u"-", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("qt", u"TCP SERVER", None))
        self.menuAna_Ekran.setTitle(QCoreApplication.translate("qt", u"Ana Ekran", None))
        self.hakkinda.setTitle(QCoreApplication.translate("qt", u"Hakk\u0131nda", None))
    # retranslateUi

