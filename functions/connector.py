import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QColorDialog, QPushButton
from PyQt5.QtGui import QFont, QPainter, QColor
import sys
import os
from interfaz.interfaz import Ui_MainWindow as text_ui


class EditorWindow(QMainWindow, text_ui):
    def __init__(self, parent = None, file = None):
        super(EditorWindow, self).__init__(parent)
        self.setupUi(self)

        self.actionNew.triggered.connect(self.NewFile)
        self.actionOpen.triggered.connect(lambda: self.OpenFile(None))
        self.actionSave.triggered.connect(self.Save)
        self.actionExit.triggered.connect(self.Exit)
        self.actionAcerca_de.triggered.connect(self.about)

        self.textEdit.textChanged.connect(lambda: self.setWindowModified(True))
        self.textEdit.cursorPositionChanged.connect(self.UpdateLineCol)
        self.textEdit.cursorPositionChanged.connect(self.updateFont)

        self.statusbar.showMessage("Ln 1, Col 1")
        self.fontComboBox.setEditable(False)

        self.toolBar.addWidget(self.fontComboBox)
        self.toolBar.addWidget(self.doubleSpinBox)

        self.titleTemplate = "[*]"
        self.filename = file

        if file is not None and not os.path.exists(self.filename):
            self.filename = None
        
        if self.filename is None:
            self.NewFile()
        else:
            self.OpenFile(self.filename)
            self._baseFile  = os.path.basename(self.filename)


    def NewFile(self):
        self.filename = None
        self._baseFile = None
        self.setWindowTitle(f"Untitled {self.titleTemplate}")
        self.textEdit.clear()
        

    def OpenFile(self,file):
        if file is None:
            tmpFile, ok = QFileDialog.getOpenFileName(self, "Open File", str(os.path.abspath(os.getcwd())))
            if not ok:
                return
            self.filename = tmpFile

        self._baseFile = os.path.basename(self.filename)
        self.setWindowTitle(self._baseFile + self.titleTemplate)

        self.textEdit.clear()
        with open(self.filename, "r") as f:
            self.textEdit.setPlainText(f.read())
        
        self.setWindowModified(False)

    def Save(self):
        if not self.isWindowModified():
            return
        
        if self.filename is None:
            tmpFile, ok = QFileDialog.getSaveFileName(self, "Save File", "./")

            if not ok:
                return
            self.filename = tmpFile
            self._baseFile = os.path.basename(self.filename)
        
        self.setWindowTitle(self._baseFile + self.titleTemplate)

        with open(self.filename, 'w') as f:
            f.write(self.textEdit.toPlainText())
        self.setWindowModified(False)

    def closeEvent(self, a0):
        # print("Puchaste x")
        self.Exit()
        a0.accept()
        

    def Exit(self):        
        def Check(i):
            if i.text() == "Salir":
                sys.exit()
            elif i.text() == "Guardar":
                self.Save()
                sys.exit()
        
        if not self.isWindowModified():
            sys.exit()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Salir sin guardar")
            msg.setInformativeText("Todos los cambios se perderan")
            msg.setWindowTitle("Advertencia")
            msg.addButton(QPushButton("Salir"), QMessageBox.NoRole)
            msg.addButton(QPushButton("Guardar"), QMessageBox.YesRole)
            msg.buttonClicked.connect(Check)
            msg.exec_()


    def UpdateLineCol(self):
        line = self.textEdit.textCursor().blockNumber() + 1
        col = self.textEdit.textCursor().columnNumber() + 1
        self.statusbar.showMessage(f"Ln {line}, Col {col}")

    def updateFont(self):
        FontFam = self.textEdit.currentFont().family()
        indexOf = self.fontComboBox.findText(FontFam)
        self.fontComboBox.setCurrentIndex(indexOf)

    def about(self):
        msg = QMessageBox(self)
        msg.resize(240,110)
        msg.setWindowTitle("About")
        msg.setText("Editor de texto para la materia de ingenieria de software uwu")
        msg.show()