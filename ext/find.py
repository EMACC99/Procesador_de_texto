from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import re


class Find(QtWidgets.QDialog):
    def __init__(self, parent=None):

        QtWidgets.QDialog.__init__(self, parent)

        self.parent = parent

        self.lastMatch = None

        self.initUI()

    def initUI(self):

        # Button to search the document for something
        findButton = QtWidgets.QPushButton("Buscar", self)
        findButton.clicked.connect(self.find)

        # Button to replace the last finding
        replaceButton = QtWidgets.QPushButton("Remplazar", self)
        replaceButton.clicked.connect(self.replace)

        # Button to remove all findings
        allButton = QtWidgets.QPushButton("Remplazar todos", self)
        allButton.clicked.connect(self.replaceAll)

        # Normal mode - radio button
        self.normalRadio = QtWidgets.QRadioButton("Normal", self)
        self.normalRadio.toggled.connect(self.normalMode)

        # Regular Expression Mode - radio button
        self.regexRadio = QtWidgets.QRadioButton("Expresiones Regulares", self)
        self.regexRadio.toggled.connect(self.regexMode)

        # The field into which to type the query
        self.findField = QtWidgets.QTextEdit(self)
        self.findField.resize(250, 50)

        # The field into which to type the text to replace the
        # queried text
        self.replaceField = QtWidgets.QTextEdit(self)
        self.replaceField.resize(250, 50)

        optionsLabel = QtWidgets.QLabel("Opciones: ", self)

        # Case Sensitivity option
        self.caseSens = QtWidgets.QCheckBox("Distingue Mayúsculas", self)

        # Whole Words option
        self.wholeWords = QtWidgets.QCheckBox("Palabras enteras", self)

        # Layout the objects on the screen
        layout = QtWidgets.QGridLayout()

        layout.addWidget(self.findField, 1, 0, 1, 4)
        layout.addWidget(self.normalRadio, 2, 2)
        layout.addWidget(self.regexRadio, 2, 3)
        layout.addWidget(findButton, 2, 0, 1, 2)

        layout.addWidget(self.replaceField, 3, 0, 1, 4)
        layout.addWidget(replaceButton, 4, 0, 1, 2)
        layout.addWidget(allButton, 4, 2, 1, 2)

        # Add some spacing
        spacer = QtWidgets.QWidget(self)

        spacer.setFixedSize(0, 10)

        layout.addWidget(spacer, 5, 0)

        layout.addWidget(optionsLabel, 6, 0)
        layout.addWidget(self.caseSens, 6, 1)
        layout.addWidget(self.wholeWords, 6, 2)

        self.setGeometry(300, 300, 360, 250)
        self.setWindowTitle("Buscar y Remplazar")
        self.setLayout(layout)

        # By default the normal mode is activated
        self.normalRadio.setChecked(True)

    def find(self):

        # Grab the parent's text
        text = self.parent.textEdit.toPlainText() ###Edit

        # And the text to find
        query = self.findField.toPlainText()

        # If the 'Whole Words' checkbox is checked, we need to append
        # and prepend a non-alphanumeric character
        if self.wholeWords.isChecked():
            query = r'\W' + query + r'\W'

        # By default regexes are case sensitive but usually a search isn't
        # case sensitive by default, so we need to switch this around here
        flags = 0 if self.caseSens.isChecked() else re.I

        # Compile the pattern
        pattern = re.compile(query, flags)

        # If the last match was successful, start at position after the last
        # match's start, else at 0
        start = self.lastMatch.start() + 1 if self.lastMatch else 0

        # The actual search
        self.lastMatch = pattern.search(text, start)

        if self.lastMatch:

            start = self.lastMatch.start()
            end = self.lastMatch.end()

            # If 'Whole words' is checked, the selection would include the two
            # non-alphanumeric characters we included in the search, which need
            # to be removed before marking them.
            if self.wholeWords.isChecked():
                start += 1
                end -= 1

            self.moveCursor(start, end)

        else:

            # We set the cursor to the end if the search was unsuccessful
            self.parent.textEdit.moveCursor(QtGui.QTextCursor.End) ###Edit

    def replace(self):

        # Grab the text cursor
        cursor = self.parent.textEdit.textCursor() ###Edit

        # Security
        if self.lastMatch and cursor.hasSelection():
            # We insert the new text, which will override the selected
            # text
            cursor.insertText(self.replaceField.toPlainText())

            # And set the new cursor
            self.parent.textEdit.setTextCursor(cursor) ###Edit

    def replaceAll(self):

        # Set lastMatch to None so that the search
        # starts from the beginning of the document
        self.lastMatch = None

        # Initial find() call so that lastMatch is
        # potentially not None anymore
        self.find()

        # Replace and find until find is None again
        while self.lastMatch:
            self.replace()
            self.find()

    def regexMode(self):

        # First uncheck the checkboxes
        self.caseSens.setChecked(False)
        self.wholeWords.setChecked(False)

        # Then disable them (gray them out)
        self.caseSens.setEnabled(False)
        self.wholeWords.setEnabled(False)

    def normalMode(self):

        # Enable checkboxes (un-gray them)
        self.caseSens.setEnabled(True)
        self.wholeWords.setEnabled(True)

    def moveCursor(self, start, end):

        # We retrieve the QTextCursor object from the parent's QTextEdit
        cursor = self.parent.textEdit.textCursor()  ###Edit

        # Then we set the position to the beginning of the last match
        cursor.setPosition(start)

        # Next we move the Cursor by over the match and pass the KeepAnchor parameter
        # which will make the cursor select the the match's text
        cursor.movePosition(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor, end - start) ###Edit

        # And finally we set this new cursor as the parent's
        self.parent.textEdit.setTextCursor(cursor) ###Edit
