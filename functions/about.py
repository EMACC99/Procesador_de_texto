from PyQt5.QtWidgets import QMessageBox


def about():
    msg = QMessageBox(None)
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
    msg.exec()


def about_qt():
    msg = QMessageBox(None)
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
    msg.exec()