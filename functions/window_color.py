from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QColorDialog

color_dict = {
    'Light Default ' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' :('#ededed', '#6b9dc2')
}

def change_window_color(window):
    window.setStyleSheet("QMainWindow{background-color:" + color_dict['Dark'][0] + ";border: 1px solid black;}")
    window.setStyleSheet("QToolButton:!hover {background-color:" + color_dict['Dark'][1] + "} QToolBar {background:" + color_dict['Dark'][1] + "}")