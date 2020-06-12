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

        self.actionNew.triggered.connect(lambda: self.NewFile(existing=True))
        # self.actionNew.triggered.connect(lambda: NewFile(self, self.titleTemplate,  existing=True))
        self.actionOpen.triggered.connect(lambda: self.OpenFile(None))
        # self.actionOpen.triggered.connect(lambda: OpenFile(self, None))
        self.actionSave.triggered.connect(self.Save)
        # self.actionSave.triggered.connect(lambda: Save(self))
        self.actionExit.triggered.connect(self.Exit)
        self.actionSave_as.triggered.connect(self.Save_as)
        # self.actionSave_as.triggered.connect(lambda: Save_as(self))
        self.actionAcerca_de.triggered.connect(self.about)
        self.actionAbout_QT.triggered.connect(self.about_qt)
        self.actionText_Colour.triggered.connect(lambda: self.change_text_colour("Text"))
        self.actionbackground_color.triggered.connect(lambda: self.change_text_colour("Background"))
        
        self.actionBold.triggered.connect(lambda: self.text_format("Bold"))
        self.actionItalic.triggered.connect(lambda: self.text_format("Italic"))
        self.actionUnderline.triggered.connect(lambda: self.text_format("Underline"))

        self.actionCopy.triggered.connect(lambda: self.textEdit.copy())
        self.actionPaste.triggered.connect(lambda: self.textEdit.paste() if self.textEdit.canPaste() else None)
        self.actionCut.triggered.connect(lambda: self.textEdit.cut())

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


    def NewFile(self, existing=False):
        if existing:
            if not self.Exit():
                self.Save()
            
        self.filename = None
        self._baseFile = None
        self.setWindowTitle(f"Untitled {self.titleTemplate}")
        self.textEdit.clear()
        

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

        with io.open(self.filename, 'w', encoding='utf8') as f:
            if ".txt" in self.filename:
                f.write(self.textEdit.toPlainText())
            elif ".chk" or ".html" in self.filename:
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

            
        self.setWindowModified(False)


    def Save_as(self):
        # QFileDialog.setDefaultSuffix(QFileDialog,".chk")
        tmpFile, ok = QFileDialog.getSaveFileName(self, "Save File", str(os.path.abspath(os.getcwd())), filter="All Files (*.*);;Text (*.txt);;HTML (*.html);;Chukurh (*.chk)", initialFilter="Chukurh (*.chk)")

        if not ok:
            return

        if tmpFile is '':
            QMessageBox.critical(self, 'Error', "Guardado de archivo cancelado por el usuario")
            return

        self.filename = tmpFile
        self._baseFile = os.path.basename(self.filename)
        
        self.setWindowTitle(self._baseFile + self.titleTemplate)

        with io.open(self.filename, 'w', encoding='utf8') as f:
            if ".txt" in self.filename:
                f.write(self.textEdit.toPlainText())
            elif ".chk" or ".html" in self.filename:
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
            
        self.setWindowModified(False)



    def closeEvent(self, a0):
        # print("Puchaste x")
        if self.Exit():
            # print(True)
            a0.accept()
        else:
            # print(False)
            a0.ignore()
            
    def Exit(self):        
        def Check(i):
            print(msg.buttonRole(i))
            #if i.text() == "Discard"
            if  msg.buttonRole(i) == 2:
                return True
                # sys.exit()
            
            elif msg.buttonRole(i) == 0:
            # i.text() == "Save    
                self.Save()
                # sys.exit()
                return True
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
            
            if msg.exec_() is False:
                # print(False)
                return False
            else:
                # print(True)
                return True

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
        print(self.textEdit.viewport().palette().color(self.textEdit.viewport().backgroundRole()).name())
        # print(c.name())

        


    def about(self):
        msg = QMessageBox(self)
        msg.resize(240,110)
        msg.setWindowTitle("Chukurh\n")
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
        "El instructivo está en la página del programa: https://bit.ly/2UCPvpv \n"
        "\n"
        "Editor de texto enfocado a la comunidad hispana\n"
        "Chukurh proviene del Purépecha, traducido al español como 'hoja'\n"
        "*Procesador de texto licenciado bajo: MIT License*")
        msg.show()


    def about_qt(self):
        msg = QMessageBox(self)
        msg.setWindowTitle( "Acerca de Qt\n")
        msg.setText("<p>Qt es una herramienta de desarrollo de aplicación " 
        "multiplataforma de C++.</p>"
        "<p>Qt proporciona una portabilidad de fuente única a través de todos los sistemas "
        "operativos. También se encuentra disponible para sistemas embebidos como Linux y otros; "
        "Incluso funciona con sistemas operativos de celular.</p>"
        "<p>Qt se encuentra disponible bajo tres diferentes opciones de licencia, "
        "diseñadas para encajar en las necesidades de distintos usuarios</p>"
        "<p>Debido a su acuerdo de licencia comercial, Qt es apropiado para el desarrollo "
        "de software, ya sea propio o comercial, donde no se quiere compartir ningún tipo "
        "de fuente de código con nadie externo al proyecto o si se da el caso que no cumple "
        "con los términos de GNU LGLP versión 3 o GNU LGPL versión 2.1.</p>"
        "<p>Licenciar Qt bajo GNU LGPL versión 3 es apropiado para el desarrollo de Qt&nbsp; "
        "aplicaciones proporcionadas deben cumplir con los términos y condiciones "
        "de GNU LGLP versión 3.</p>"
        "<p>Licenciar Qt bajo GNU LGPL versión 2.1 es apropiado para el desarrollo de Qt&nbsp; "
        "aplicaciones proporcionadas deben cumplir con los términos y condiciones "
        "de GNU LGLP versión 2.1.</p>"
        "<p>Por favor, visita <a href=http://qt.io/licensing>Licensing</a> para "
        "una visión general de la licencia Qt.</p>"
        "<p>Derechos de autor (C) 2019, Qt Company Ltd y otros contribuidores.</p>"
        "<p>Qt y el logo de Qt son marcas registradas de Qt Company Ltd.</p>"
        "<p>Qt es producto desarrollado por Qt Company Ltd como un proyecto de fuente abierta. "
        "Visitar: <a href='http://qt.io'>aquí </a> para más información")
        msg.show()
