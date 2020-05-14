import os
import sys
from PyQt5.QtWidgets import QApplication
from functions.connector import EditorWindow

if __name__ == '__main__':
    APP = QApplication(sys.argv)

    openFile = None

    if len(sys.argv) > 1:
        openFile = sys.argv[1]
    
    GUI = EditorWindow(file=openFile)
    GUI.show()

    sys.exit(APP.exec_())