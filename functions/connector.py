import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QColorDialog
from PyQt5.QtGui import QFont
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
        
        self.textEdit.textChanged.connect(lambda: self.setWindowModified(True))
        self.textEdit.cursorPositionChanged.connect(self.UpdateLineCol)
        self.textEdit.cursorPositionChanged.connect(self.UpdateFont)
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

    def UpdateLineCol(self):
        pass

    def UpdateFont(self):
        pass