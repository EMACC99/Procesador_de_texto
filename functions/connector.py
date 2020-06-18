# -*- coding: utf-8 -*-

import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QColorDialog, QPushButton, QAction, QComboBox
from PyQt5.QtGui import QFont, QPainter, QColor, QTextCursor, QIcon, QPalette
import sys
import os
from interfaz.interfaz import Ui_MainWindow as text_ui
import io
import functions.about
import functions.window_color

class EditorWindow(QMainWindow, text_ui):
    def __init__(self, parent = None, file = None):
        super(EditorWindow, self).__init__(parent)
        self.setupUi(self)
        self.doubleSpinBox.setValue(12)
        # self.fontComboBox.setWritingSystem()

        # backColor = QAction(QIcon("icons/backcolor.png"),"Change background color",self)

        self.actionNew.triggered.connect(lambda: self.NewFile(existing=True))
        # self.actionNew.triggered.connect(lambda: NewFile(self, self.titleTemplate,  existing=True))
        self.actionOpen.triggered.connect(lambda: self.OpenFile(None))
        # self.actionOpen.triggered.connect(lambda: OpenFile(self, None))
        self.actionSave.triggered.connect(self.Save)
        # self.actionSave.triggered.connect(lambda: Save(self))
        self.actionExit.triggered.connect(lambda: sys.exit() if self.Exit() is 2 or self.Exit is 0 else None)
        self.actionSave_as.triggered.connect(self.Save_as)
        # self.actionSave_as.triggered.connect(lambda: Save_as(self))
        self.actionAcerca_de.triggered.connect(functions.about.about)
        self.actionAbout_QT.triggered.connect(functions.about.about_qt)
        self.actionText_Colour.triggered.connect(lambda: self.change_text_colour("Text"))
        self.actionbackground_color.triggered.connect(lambda: self.change_text_colour("Background"))
        
        self.actionBold.triggered.connect(lambda: self.text_format("Bold"))
        self.actionItalic.triggered.connect(lambda: self.text_format("Italic"))
        self.actionUnderline.triggered.connect(lambda: self.text_format("Underline"))

        self.actionCopy.triggered.connect(lambda: self.textEdit.copy())
        self.actionPaste.triggered.connect(lambda: self.textEdit.paste() if self.textEdit.canPaste() else None)
        self.actionCut.triggered.connect(lambda: self.textEdit.cut())


        self.actionNegro.triggered.connect(lambda: functions.window_color.change_window_color(self))

        self.textEdit.setUndoRedoEnabled(True)

        self.textEdit.textChanged.connect(lambda: self.setWindowModified(True))


        self.textEdit.cursorPositionChanged.connect(self.UpdateLineCol)
        #self.textEdit.cursorPositionChanged.connect(self.updateFont)
        self.fontComboBox.currentFontChanged.connect(self.updateFont)
        self.doubleSpinBox.valueChanged.connect(self.updateFont)

        # self.textEdit.cursorPositionChanged.connect(self.autosave)

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


    def NewFile(self, existing=False):
        if existing:
            choice = self.Exit()
            if choice is 0:
                self.Save()
            elif choice is 1:
                return
        self.filename = None
        self._baseFile = None
        self.setWindowTitle(f"Untitled {self.titleTemplate}")
        self.textEdit.clear()
        self.doubleSpinBox.setValue(12)
        self.textEdit.setTextColor(QColor('#000000'))
        self.textEdit.setTextBackgroundColor(QColor(255,255,255,0))
        c = self.textEdit.viewport().palette()
        c.setColor(self.textEdit.viewport().backgroundRole(), QColor(255,255,255))
        self.textEdit.viewport().setPalette(c)


    def OpenFile(self,file):
        if file is None:
            tmpFile, ok = QFileDialog.getOpenFileName(self, "Open File", str(os.path.abspath(os.getcwd())), filter="All Files (*.*);;Text (*.txt);;HTML (*.html);;Chukurh (*.chk)", initialFilter="Chukurh (*.chk)")
            if not ok:
                return
            
            if tmpFile is '':
                QMessageBox.critical(self, 'Error', "Operacion 'abrir archivo' cancelada por el usuario ")
                return
            
            self.filename = tmpFile
            
        self._baseFile = os.path.basename(self.filename)
        self.setWindowTitle(self._baseFile + self.titleTemplate)

        self.textEdit.clear()
        with io.open(self.filename, 'r', encoding='utf8') as f:
            if ".txt" in self.filename:
                self.textEdit.setPlainText(f.read())
            elif ".html" or ".chk" in self.filename:
                self.textEdit.setHtml(f.read())
            else:
                self.textEdit.setPlainText(f.read())

        self.setWindowModified(False)


    def write_file(self, ok):
        with io.open(self.filename, 'w', encoding='utf8') as f:
            if ".chk" in ok or ".html" in ok:
                color = f'background-color:{self.textEdit.viewport().palette().color(self.textEdit.viewport().backgroundRole()).name()};'
                html = self.textEdit.toHtml()
                html = html.splitlines()
                temp  = html[3]
                body_style = temp[:-2] + color + temp[-2:]
                html_final = ''
                for i in html:
                    if i == temp:
                        html_final += body_style + '\n'
                    else:
                        html_final += i + '\n'
                f.write(html_final)
            else:
                f.write(self.textEdit.toPlainText())


    def Save(self):
        if not self.isWindowModified():
            return
        
        if self.filename is None:
            tmpFile, ok = QFileDialog.getSaveFileName(self, "Save File", str(os.path.abspath(os.getcwd())), filter="All Files (*.*);;Text (*.txt);;HTML (*.html);;Chukurh (*.chk)", initialFilter="Chukurh (*.chk)")
            if not ok:
                return
            if tmpFile is '':
                QMessageBox.critical(self, 'Error', "Guardado de archivo cancelado por el usuario")
                return
                
            self.filename = tmpFile
            self._baseFile = os.path.basename(self.filename)
        
        self.setWindowTitle(self._baseFile + self.titleTemplate)

        self.write_file(ok)
            
        self.setWindowModified(False)


    def Save_as(self):
        tmpFile, ok = QFileDialog.getSaveFileName(self, "Save File", str(os.path.abspath(os.getcwd())), filter="All Files (*.*);;Text (*.txt);;HTML (*.html);;Chukurh (*.chk)", initialFilter="Chukurh (*.chk)")

        if not ok:
            return

        if tmpFile is '':
            QMessageBox.critical(self, 'Error', "Guardado de archivo cancelado por el usuario")
            return

        self.filename = tmpFile
        self._baseFile = os.path.basename(self.filename)
        
        self.setWindowTitle(self._baseFile + self.titleTemplate)

        self.write_file(ok)
            
        self.setWindowModified(False)



    def closeEvent(self, a0):
        # print("Puchaste x")
        check = self.Exit()
        if check is 2 or check is 0:
            print("Adios")
            a0.accept()
        else:
            print("Nel")
            a0.ignore()
            
    def Exit(self):        
        if not self.isWindowModified():
            return 0
            # sys.exit()
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
            # msg.buttonClicked.connect(Check)
            
            buttonY = msg.button(QMessageBox.Save)
            buttonY.setText('Guardar')
            buttonN = msg.button(QMessageBox.Discard)
            buttonN.setText('Descartar')
            buttonO = msg.button(QMessageBox.Cancel)
            buttonO.setText('Cancelar')
            
            if msg.exec():
                if msg.buttonRole(msg.clickedButton())== 2:
                    #print("Discard")
                    return 2
                elif msg.buttonRole(msg.clickedButton()) == 0:
                    # i.text() == "Save    
                    #print("Save")
                    self.Save()
                    # sys.exit()
                    return 0
                elif msg.buttonRole(msg.clickedButton()) == 1:
                    #i.text() == "cancel"
                    print("cancel")
                    print(False)
                    return 1


    def UpdateLineCol(self):
        line = self.textEdit.textCursor().blockNumber() + 1
        col = self.textEdit.textCursor().columnNumber() + 1
        self.statusbar.showMessage(f"Ln {line}, Col {col}")

    def updateFont(self):
        Font = self.fontComboBox.currentFont()
        FontFam = Font.family()
        indexOf = self.fontComboBox.findText(FontFam)
        self.fontComboBox.setCurrentIndex(indexOf)
        self.textEdit.setFont(Font)
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
        print(self.textEdit.viewport().palette().color(self.textEdit.viewport().backgroundRole()).name())
        # print(c.name())