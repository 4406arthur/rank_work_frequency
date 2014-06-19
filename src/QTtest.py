import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from PySide import *
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *

def main():
    app = QApplication(sys.argv)
    window = QtGui.QMainWindow()
    palette = QtGui.QPalette()
    gridLayout = QtGui.QGridLayout()
    centralWidget = QtGui.QWidget()
    button = QPushButton("Click")
    b = QWebView()
    URL = 'http://www.google.com'
    b.load(QUrl(URL))
    IEdit = QtGui.QLineEdit()
    Trans = QtGui.QTextEdit()

    gridLayout.addWidget(IEdit,0,0)
    gridLayout.addWidget(button,1,0)
    gridLayout.addWidget(b,2,0)
    gridLayout.addWidget(Trans,3,0)

    window.setCentralWidget(centralWidget)
    centralWidget.setLayout(gridLayout)

    window.resize(1200,700)
    window.setWindowTitle('UNIX')
    window.show()

    sys.exit(app.exec_())       



if __name__== '__main__':
    main()
