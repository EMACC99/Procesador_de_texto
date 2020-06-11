# -*- coding: utf-8 -*-

import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QColorDialog, QPushButton, QAction
from PyQt5.QtGui import QFont, QPainter, QColor, QTextCursor, QIcon, QPalette
import sys
import os
from interfaz.interfaz import Ui_MainWindow as text_ui
import io

class EditorWindow(QMainWindow, text_ui):
    def __init__(self, parent = None, file = None):
        super(EditorWindow, self).__init__(parent)
        self.setupUi(self)
        self.doubleSpinBox.setValue(12)
        # self.fontComboBox.setWritingSystem()

        # backColor = QAction(QIcon("icons/backcolor.png"),"Change background color",self)

        self.actionNew.triggered.connect(self.NewFile)
        self.actionOpen.triggered.connect(lambda: self.OpenFile(None))
        self.actionSave.triggered.connect(self.Save)
        self.actionExit.triggered.connect(self.Exit)
        self.actionSave_as.triggered.connect(self.Save_as)
        self.actionAcerca_de.triggered.connect(self.about)
        self.actionAbout_QT.triggered.connect(self.about_qt)
        self.actionText_Colour.triggered.connect(lambda: self.change_text_colour("Text"))
        self.actionbackground_color.triggered.connect(lambda: self.change_text_colour("Background"))
        
        self.actionBold.triggered.connect(lambda: self.text_format("Bold"))
        self.actionItalic.triggered.connect(lambda: self.text_format("Italic"))
        self.actionUnderline.triggered.connect(lambda: self.text_format("Underline"))

        self.actionCopy.triggered.connect(lambda: self.textEdit.copy())
        self.actionPaste.triggered.connect(lambda: self.textEdit.paste() if self.textEdit.canPaste() else None)

        self.textEdit.setUndoRedoEnabled(True)

        self.textEdit.textChanged.connect(lambda: self.setWindowModified(True))


        self.textEdit.cursorPositionChanged.connect(self.UpdateLineCol)
        self.textEdit.cursorPositionChanged.connect(self.updateFont)
        self.textEdit.cursorPositionChanged.connect(self.autosave)

        self.statusbar.showMessage("Ln 1, Col 1")
        self.fontComboBox.setEditable(False)

        self.toolBar.addWidget(self.fontComboBox)
        self.toolBar.addWidget(self.doubleSpinBox)
        # self.toolBar.addAction(backColor)

        self.titleTemplate = "[*]"
        self.filename = file

        self.actionCambiar_Fondo.triggered.connect(self.Backgroud_Color)


        if file is not None and not os.path.exists(self.filename):
            self.filename = None
        
        if self.filename is None:
            self.NewFile()
        else:
            self.OpenFile(self.filename)
            self._baseFile  = os.path.basename(self.filename)

        print(self.windowTitle())


    def autosave(self): # no sirve aun pero no rompe nada, si pueden moverle que chido
        import time

        print("autosave")

        time1 = time.time()
        while time.time() - time1 < 5:
            print (time.time())
            if self.textEdit.textChanged:
                return            
        
        self.Save()
        return


    def NewFile(self):
        self.filename = None
        self._baseFile = None
        self.setWindowTitle(f"Untitled {self.titleTemplate}")
        self.textEdit.clear()
        

    def OpenFile(self,file):
        if file is None:
            tmpFile, ok = QFileDialog.getOpenFileName(self, "Open File", str(os.path.abspath(os.getcwd())), filter="All Files (*.*);;Text (*.txt);;HTML (*.html);;Churuk (*.chk)", initialFilter="Churuk (*.chk)")
            if not ok:
                return
            self.filename = tmpFile

        self._baseFile = os.path.basename(self.filename)
        self.setWindowTitle(self._baseFile + self.titleTemplate)

        self.textEdit.clear()
        with io.open(self.filename, 'r', encoding='utf8') as f:
            if ".txt" in self.filename:
                self.textEdit.setPlainText(f.read())
            else:
                self.textEdit.setHtml(f.read())
        
        self.setWindowModified(False)

    def Save(self):
        if not self.isWindowModified():
            return
        
        if self.filename is None:
            
            tmpFile, ok = QFileDialog.getSaveFileName(self, "Save File", str(os.path.abspath(os.getcwd())), filter="All Files (*.*);;Text (*.txt);;HTML (*.html);;Churuk (*.chk)", initialFilter="Churuk (*.chk)")
            if not ok:
                return
            self.filename = tmpFile
            self._baseFile = os.path.basename(self.filename)
        
        self.setWindowTitle(self._baseFile + self.titleTemplate)

        with io.open(self.filename, 'w', encoding='utf8') as f:
            if ".txt" in self.filename:
                f.write(self.textEdit.toPlainText())
            else:
                
                f.write(self.textEdit.toHtml())
            
            
        self.setWindowModified(False)


    def Save_as(self):
        # QFileDialog.setDefaultSuffix(QFileDialog,".chk")
        tmpFile, ok = QFileDialog.getSaveFileName(self, "Save File", str(os.path.abspath(os.getcwd())), filter="All Files (*.*);;Text (*.txt);;HTML (*.html);;Churuk (*.chk)", initialFilter="Churuk (*.chk)")

        if not ok:
            return

        self.filename = tmpFile
        self._baseFile = os.path.basename(self.filename)
        
        self.setWindowTitle(self._baseFile + self.titleTemplate)

        with io.open(self.filename, 'w', encoding='utf8') as f:
            f.write(self.textEdit.toPlainText())
            
        self.setWindowModified(False)



    def closeEvent(self, a0):
        # print("Puchaste x")
        if self.Exit():
            a0.accept()
        else:
            a0.ignore()
            
    def Exit(self):        
        def Check(i):
            print(msg.buttonRole(i))
            #if i.text() == "Discard"
            if  msg.buttonRole(i) == 2:
                sys.exit()
            
            elif msg.buttonRole(i) == 0:
            # i.text() == "Save    
                self.Save()
                sys.exit()

            elif msg.buttonRole(i) == 1:
            #i.text() == "Save" or
                # print("cancel")
                return False

        if not self.isWindowModified():
            sys.exit()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Salir sin guardar")
            msg.setInformativeText("Todos los cambios se perderan")
            msg.setWindowTitle("Advertencia")
            
            # msg.addButton(QMessageBox.Discard)
            # msg.addButton(QMessageBox.Save )
            # msg.addButton(QMessageBox.Cancel)
            
            msg.setStandardButtons(QMessageBox.Save| QMessageBox.Discard| QMessageBox.Cancel)
            msg.setDefaultButton(QMessageBox.Save)
            msg.buttonClicked.connect(Check)
            
            buttonY = msg.button(QMessageBox.Save)
            buttonY.setText('Guardar')
            buttonN = msg.button(QMessageBox.Discard)
            buttonN.setText('Descartar')
            buttonO = msg.button(QMessageBox.Cancel)
            buttonO.setText('Cancelar')
            
            if msg.exec_() is not True:
                return False


    def UpdateLineCol(self):
        line = self.textEdit.textCursor().blockNumber() + 1
        col = self.textEdit.textCursor().columnNumber() + 1
        self.statusbar.showMessage(f"Ln {line}, Col {col}")


    def updateFont(self):
        Font = self.fontComboBox.currentFont()
        FontFam = Font.family()
        indexOf = self.fontComboBox.findText(FontFam)
        self.fontComboBox.setCurrentIndex(indexOf)
        self.textEdit.setCurrentFont(Font)
        self.textEdit.setFontPointSize(self.doubleSpinBox.value())

        
    def change_text_colour(self, value):
        ColorD = QColorDialog(self)
        if value is "Text":
            ColorD.colorSelected.connect(self.textEdit.setTextColor)
        elif value is "Background":
            ColorD.colorSelected.connect(self.textEdit.setTextBackgroundColor)
        ColorD.open()

        

    def text_format(self, value): 
        # italic
        # bold
        # underline, etc
        # print(f"Cambiar {value}")
        if value is "Italic":
            if not self.textEdit.fontItalic():
                self.textEdit.setFontItalic(True)
            else:
                self.textEdit.setFontItalic(False)
        elif value is "Underline":
            if not self.textEdit.fontUnderline():
                self.textEdit.setFontUnderline(True)
            else:
                self.textEdit.setFontUnderline(False)
    

    def search_and_replace(self, word, newWord = None, replace = False):

        self.textEdit.textCursor().beginEditBlock()
        doc = self.textEdit.document()
        cursor = QTextCursor(doc)
        while True:
            cursor = doc.find(word, cursor)
            if cursor.isNull():
                break
            if replace and newWord is not None:
                cursor.insertText(newWord)

        self.textEdit.textCursor().endEditBlock()



    def Backgroud_Color(self):
        c = self.textEdit.viewport().palette()
        ColorD = QColorDialog(self)
        # ColorD.colorSelected.connect(c.setColor(self.textEdit.viewport().backgroudRole()))
        # ColorD.exec()
        # print(ColorD.currentColor())
        c.setColor(self.textEdit.viewport().backgroundRole(), ColorD.getColor())
        self.textEdit.viewport().setPalette(c)
        print(self.textEdit.viewport().palette().color(c).name())
        # print(c.name())

        


    def about(self):
        msg = QMessageBox(self)
        msg.resize(240,110)
        msg.setWindowTitle("Chukurh")
        msg.setText("Licenciatura en Tecnologías para la Información en Ciencias\n"
        "Proyecto Final, Ingeniería de Software 2020-2\n"
        "ENES Unidad Morelia, UNAM\n"
        "\n"
        "Arcos González César\n"
        "Armas Gamiño Saúl\n"
        "Ceja Cruz Eduardo Manuel\n"
        "Fonseca Márquez Pablo Francisco\n"
        "Navarro Espindola Javier\n"
        "\n"
        "Editor de texto enfocado a la comunidad hispana\n"
        "Chukurh proviene del Purépecha, traducido al español como 'hoja'\n"
        "*Procesador de texto licenciado bajo: MIT License*")
        msg.show()


    def about_qt(self):
        msg = QMessageBox(self)
        msg.setWindowTitle( "About Qt\n")
        msg.setText("<p>Qt is a C++ toolkit for cross-platform application "
        "development.</p>"
        "<p>Qt provides single-source portability across all major desktop "
        "operating systems. It is also available for embedded Linux and other "
        "embedded and mobile operating systems.</p>"
        "<p>Qt is available under three different licensing options designed "
        "to accommodate the needs of our various users.</p>"
        "<p>Qt licensed under our commercial license agreement is appropriate "
        "for development of proprietary/commercial software where you do not "
        "want to share any source code with third parties or otherwise cannot "
        "comply with the terms of the GNU LGPL version 3 or GNU LGPL version 2.1.</p>"
        "<p>Qt licensed under the GNU LGPL version 3 is appropriate for the "
        "development of Qt&nbsp;applications provided you can comply with the terms "
        "and conditions of the GNU LGPL version 3.</p>"
        "<p>Qt licensed under the GNU LGPL version 2.1 is appropriate for the "
        "development of Qt&nbsp;applications provided you can comply with the terms "
        "and conditions of the GNU LGPL version 2.1.</p>"
        "<p>Please see <a href=http://qt.io/licensing>Licensing</a> "
        "for an overview of Qt licensing.</p>"
        "<p>Copyright (C) 2019 The Qt Company Ltd and other "
        "contributors.</p>"
        "<p>Qt and the Qt logo are trademarks of The Qt Company Ltd.</p>"
        "<p>Qt is The Qt Company Ltd product developed as an open source "
        "project. See <a href='http://qt.io'>here </a> for more information.</p>")
        msg.show()
        
