import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *

app = QApplication(sys.argv)
b = QWebView()
b.load(QUrl('http://www.google.com'))
b.show()
app.exec_()

