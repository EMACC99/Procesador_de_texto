# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfazv0.1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
###     NEW     ###
from ext import find
###             ###

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 731)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fontComboBox = QtWidgets.QFontComboBox(self.centralwidget)
        self.fontComboBox.setObjectName("fontComboBox")
        self.verticalLayout.addWidget(self.fontComboBox)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setDecimals(0)
        self.doubleSpinBox.setMaximum(99.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.verticalLayout.addWidget(self.doubleSpinBox)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 23))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(48, 48))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/iconos/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/iconos/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/iconos/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/iconos/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon3)
        self.actionExit.setObjectName("actionExit")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/iconos/save_as.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_as.setIcon(icon4)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionAcerca_de = QtWidgets.QAction(MainWindow)
        self.actionAcerca_de.setObjectName("actionAcerca_de")


        self.actionText_Colour = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/iconos/font_color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionText_Colour.setIcon(icon5)
        self.actionText_Colour.setObjectName("actionText_Colour")


        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/iconos/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon6)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/newPrefix/iconos/paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon7)
        self.actionPaste.setObjectName("actionPaste")
        self.actionCut = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/newPrefix/iconos/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon8)
        self.actionCut.setObjectName("actionCut")


        self.actionItalic = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/newPrefix/iconos/italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionItalic.setIcon(icon9)
        self.actionItalic.setObjectName("actionItalic")

        self.actionBold = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/newPrefix/iconos/bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBold.setIcon(icon10)
        self.actionBold.setObjectName("actionBold")

        self.actionUnderline = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/newPrefix/iconos/underline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUnderline.setIcon(icon11)
        self.actionUnderline.setObjectName("actionUnderline")

        self.actionbackground_color = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/newPrefix/iconos/status_bar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbackground_color.setIcon(icon12)
        self.actionbackground_color.setObjectName("actionbackground_color")


        ###             NEW                 ###
        self.findAction = QtWidgets.QAction(QtGui.QIcon(":/newPrefix/iconos/find.png"), "Buscar y reemplazar", self)
        self.findAction.setShortcut("Ctrl+F")
        #self.findAction.triggered.connect(lambda: self.text_format("find"))
        #self.findAction.triggered.connect(lambda: self.text_format("Underline"))
        #self.findAction.triggered.connect(find.Find(self).show)
        self.toolBar.addAction(self.findAction)
        ###         NEW         ###

        ###     NEW        ### !no sirve
        #toolBar.addAction(self.findAction)
        ###                ###

        #edit.addAction(self.findAction)

        #podría servir ----> ####self.toolBar.addSeparator()


        self.actionAbout_QT = QtWidgets.QAction(MainWindow)
        self.actionAbout_QT.setObjectName("actionAbout_QT")
        self.actionCambiar_Fondo = QtWidgets.QAction(MainWindow)


        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/newPrefix/iconos/fondo.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.actionCambiar_Fondo.setIcon(icon13)
        self.actionCambiar_Fondo.setObjectName("actionCambiar_Fondo")
        self.menufile.addSeparator()
        self.menufile.addSeparator()
        self.menufile.addAction(self.actionNew)
        self.menufile.addAction(self.actionOpen)
        self.menufile.addAction(self.actionSave_as)
        self.menufile.addAction(self.actionSave)
        self.menufile.addSeparator()
        self.menufile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionCut)
        self.menuHelp.addAction(self.actionAcerca_de)
        self.menuHelp.addAction(self.actionAbout_QT)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionText_Colour)
        self.toolBar.addAction(self.actionbackground_color)
        self.toolBar.addAction(self.actionUnderline)
        self.toolBar.addAction(self.actionItalic)
        self.toolBar.addAction(self.actionCambiar_Fondo)

        ### antes aquí estaba lo de find    ###


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menufile.setTitle(_translate("MainWindow", "Archivo"))
        self.menuEdit.setTitle(_translate("MainWindow", "Editar"))
        self.menuHelp.setTitle(_translate("MainWindow", "Ayuda"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNew.setText(_translate("MainWindow", "Nuevo"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Abrir"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Guardar"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Salir"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionSave_as.setText(_translate("MainWindow", "Guardar como"))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de"))
        self.actionText_Colour.setText(_translate("MainWindow", "Text Coulour"))
        self.actionCopy.setText(_translate("MainWindow", "Copiar"))
        self.actionCopy.setIconText(_translate("MainWindow", "Copiar"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Pegar"))
        self.actionPaste.setIconText(_translate("MainWindow", "Pegar"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionCut.setText(_translate("MainWindow", "Cortar"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionItalic.setText(_translate("MainWindow", "Italic"))
        self.actionItalic.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionBold.setText(_translate("MainWindow", "Bold"))
        self.actionBold.setShortcut(_translate("MainWindow", "Ctrl+B"))
        self.actionUnderline.setText(_translate("MainWindow", "Underline"))
        self.actionUnderline.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionbackground_color.setText(_translate("MainWindow", "background color"))
        self.actionAbout_QT.setText(_translate("MainWindow", "Acerca de QT"))
        self.actionCambiar_Fondo.setText(_translate("MainWindow", "Cambiar Fondo"))

import interfaz.iconos
